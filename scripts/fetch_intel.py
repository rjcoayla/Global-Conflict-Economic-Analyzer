import requests
import json
import datetime
import random

def get_intel():
    # Simulación de extracción de datos reales de mercado
    # En un entorno real, aquí conectarías con Alpha Vantage o Yahoo Finance
    brent_base = 90.00
    current_price = brent_base + random.uniform(-2, 5)
    
    # Generación de incidentes dinámicos (Simulando feed de ACLED/Noticias)
    incidentes = [
        {
            "id": f"OP-{random.randint(1000, 9999)}",
            "fecha": datetime.datetime.now().isoformat(),
            "lat": random.uniform(25.0, 35.0),
            "lng": random.uniform(45.0, 60.0),
            "tipo": random.choice(["Dron Detectado", "Intercepción Naval", "Ciberataque"]),
            "intensidad": random.choice(["Alta", "Media", "Crítica"]),
            "actor": random.choice(["EE.UU.", "Irán", "Hezbollah", "Hutíes"])
        } for _ in range(5)
    ]

    data = {
        "last_update": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "brent_price": round(current_price, 2),
        "defcon": random.choice([2, 3, 3, 3]),
        "incidentes": incidentes
    }

    with open('data/intel_report.json', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    get_intel()