# 🛒 Klasifikacija Proizvoda (Machine Learning Task)

Ovaj repozitorijum sadrži kompletno rešenje za automatizovanu klasifikaciju naziva proizvoda u odgovarajuće kategorije (npr. frižideri, mašine za sudove, telefoni).

## 🚀 Ključne Karakteristike
- **Visoka Preciznost:** Model ostvaruje **95.7%** tačnosti na testnom skupu podataka.
- **Hibridni Model:** Kombinacija mašinskog učenja i "rule-based" logike za rešavanje kritičnih grešaka kod brendova kao što je Bosch.
- **Napredna Analiza:** Korišćenje TF-IDF vektorizacije sa trigramima (ngram 1-3) za prepoznavanje specifičnih kodova modela.

## 📁 Struktura Projekta
- `product_classification.ipynb` - Jupyter sveska sa detaljnom vizuelizacijom podataka i poređenjem modela (Linear SVC vs Naive Bayes vs Logistic Regression).
- `train_model.py` - Skripta za treniranje modela i čuvanje `.pkl` fajla.
- `predict_category.py` - Interaktivna konzolna aplikacija za testiranje predikcija.
- `products_clean.csv` - Očišćen i pripremljen skup podataka.

## 🛠️ Instalacija i Pokretanje
1. Klonirajte repozitorijum.
2. Instalirajte biblioteke:
   ```bash
   pip install pandas scikit-learn matplotlib seaborn joblib
