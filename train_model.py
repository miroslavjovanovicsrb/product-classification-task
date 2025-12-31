import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

# AUTOMATSKO PRONALAŽENJE PUTANJE
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, 'products_clean.csv')
model_path = os.path.join(base_dir, 'product_model.pkl')

print("="*50)
print("📂 PROCES TRENIRANJA I EVALUACIJE MODELA")
print("="*50)

try:
    # Učitavanje i čišćenje NaN vrednosti
    df = pd.read_csv(csv_path)
    df = df.dropna(subset=['Product Title', 'Category Label'])
    
    X = df['Product Title'].astype(str).str.lower()
    y = df['Category Label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Definisanje modela za poređenje
    models = {
        'Linear SVC': LinearSVC(random_state=42),
        'Naive Bayes': MultinomialNB(),
        'Logistic Regression': LogisticRegression(max_iter=1000)
    }

    results = {}
    best_acc = 0
    best_model = None

    print("\n🚀 Pokrećem poređenje performansi algoritama...\n")

    for name, clf in models.items():
        pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(stop_words='english', ngram_range=(1, 3))),
            ('clf', clf)
        ])
        
        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        results[name] = acc
        
        print(f"📊 {name:>20} -> Tačnost: {acc:.4f}")
        
        if acc > best_acc:
            best_acc = acc
            best_model = pipeline

    # Čuvanje najboljeg modela
    joblib.dump(best_model, model_path)
    print("\n" + "-"*50)
    print(f"🏆 POBEDNIK: {max(results, key=results.get)} sa {best_acc:.4f} tačnosti.")
    print(f"📁 Model je uspešno arhiviran u: {model_path}")
    print("-"*50)

except Exception as e:
    print(f"❌ Došlo je do greške: {e}")