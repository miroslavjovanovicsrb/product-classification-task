🛒 Product Categorization System
Ovaj repozitorijum sadrži kompletno rešenje za automatizovanu klasifikaciju naziva proizvoda u kategorije bele tehnike i elektronike. Sistem je razvijen korišćenjem Machine Learning algoritama i NLP (Natural Language Processing) tehnika.

📊 Analiza i Razvoj
U okviru projekta urađena je detaljna analiza u product_classification.ipynb koja obuhvata:

Čišćenje podataka: Identifikacija i uklanjanje nevalidnih unosa.

EDA (Exploratory Data Analysis): Vizuelni prikaz distribucije kategorija.

Uporedni trening: Testiranje tri modela (Linear SVC, Naive Bayes, Logistic Regression) uz podelu podataka 80/20 (trening/test).

Evaluacija: Detaljan prikaz performansi putem Matrice konfuzije i Classification Report-a.

🧠 Tehničko Rešenje
Najbolje rezultate pokazao je Linear SVC model sa 95.7% tačnosti. Za potrebe stabilnosti u realnom radu, implementiran je Hibridni pristup:

ML Model: Primarna klasifikacija zasnovana na TF-IDF vektorizaciji (unigrami, bigrami, trigrami).

Rule-based Logic: Specifične korekcije za brendove kao što su Bosch, Smeg i Samsung kako bi se osigurala preciznost na kritičnim artiklima.

📂 Struktura fajlova
train_model.py - Skripta za trening i selekciju najboljeg modela.

predict_category.py - Interaktivna konzolna aplikacija za testiranje.

product_model.pkl - Sačuvan (istreniran) model spreman za upotrebu.

products_clean.csv - Očišćen dataset korišćen za razvoj.

product_classification.html - Izveštaj analize u HTML formatu.

## 🛠️ Instalacija i Pokretanje
1. Klonirajte repozitorijum.
2. Instalirajte biblioteke:
   ```bash
   pip install pandas scikit-learn matplotlib seaborn joblib
