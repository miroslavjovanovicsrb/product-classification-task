import pandas as pd
import os

# AUTOMATSKO PRONALAŽENJE PUTANJE
# Skripta gleda folder u kojem se i sama nalazi
base_dir = os.path.dirname(os.path.abspath(__file__))

# Formiranje putanja do fajlova bez otkrivanja tvog korisničkog imena
input_file = os.path.join(base_dir, 'products.csv')
output_file = os.path.join(base_dir, 'products_clean.csv')

def fix_data():
    print(f"📂 Pokrećem čišćenje podataka u folderu: {base_dir}")
    
    try:
        # Učitavanje originalnog CSV-a
        df = pd.read_csv(input_file)
        
        # Čišćenje: Uklanjamo redove gde nedostaje naslov ili kategorija
        initial_count = len(df)
        df_clean = df.dropna(subset=['Product Title', 'Category Label'])
        
        # Čuvanje očišćenog fajla u isti folder
        df_clean.to_csv(output_file, index=False)
        
        print("-" * 50)
        print(f"✅ USPEH: Podaci su očišćeni.")
        print(f"📊 Broj redova pre: {initial_count}")
        print(f"📊 Broj redova posle: {len(df_clean)}")
        print(f"📁 Novi fajl sačuvan kao: products_clean.csv")
        print("-" * 50)
        
    except FileNotFoundError:
        print(f"❌ GREŠKA: Originalni fajl 'products.csv' nije pronađen na lokaciji: {input_file}")
    except Exception as e:
        print(f"❌ Došlo je do neočekivane greške: {e}")

if __name__ == "__main__":
    fix_data()