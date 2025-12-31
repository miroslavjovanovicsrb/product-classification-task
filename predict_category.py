import joblib
import os

# Putanja do modela
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, 'product_model.pkl')

def run_predictor():
    if not os.path.exists(model_path):
        print("\n❌ GREŠKA: Model nije pronađen! Prvo pokreni 'train_model.py' da generišeš 'product_model.pkl'.")
        return

    # Učitavanje istreniranog modela
    model = joblib.load(model_path)

    print("\n" + "*"*60)
    print("✨  AI SISTEM ZA AUTOMATSKU KATEGORIZACIJU PROIZVODA  ✨")
    print("*"*60)
    print("Uputstvo: Unesite pun naziv proizvoda za predikciju.")
    print("Za prekid rada programa, unesite 'exit'.")
    print("-"*60)

    while True:
        user_input = input("\n📝 Unesite naziv proizvoda: ").strip()
        
        if user_input.lower() == 'exit':
            print("\n👋 Hvala na korišćenju sistema. Gasim program...")
            break
        
        if not user_input:
            print("⚠️ Molimo unesite validan naziv.")
            continue

        # Hibridni pristup: Rule-based korekcije za specifične brendove
        txt = user_input.lower()
        if any(x in txt for x in ['kgv', 'kgn', 'serie 4', 'serie 6', 'kgn36']):
            prediction = "Fridge Freezers"
        elif any(x in txt for x in ['wan', 'wak', 'wga', 'wgg']):
            prediction = "Washing Machines"
        elif any(x in txt for x in ['sms', 'smv', 'smi']):
            prediction = "Dishwashers"
        else:
            # Ako nije specijalan slučaj, koristi se ML model
            prediction = model.predict([user_input])[0]

        print(f"🔍 REZULTAT ANALIZE:")
        print(f"👉 Predviđena kategorija: 【 {prediction.upper()} 】")
        print("-" * 30)

if __name__ == "__main__":
    run_predictor()