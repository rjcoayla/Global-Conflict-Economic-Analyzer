import requests
import json
import datetime
import random

def get_intel():
    # Simulación de mercado real (Brent y Oro)
    brent_base = 85.00
    gold_base = 2300.00
    current_price = brent_base + random.uniform(-1, 8)
    current_gold = gold_base + random.uniform(10, 150)
    
    # Nuevos actores para un análisis global
    actores = ["EE.UU.", "Irán", "Hezbollah (Líbano)", "Hutíes (Yemen)", "Fuerzas de Israel", "Milicias Pro-Irán (Irak)"]
    tipos_ataque = ["Ataque con Drones", "Intercepción Naval", "Misil Balístico", "Sabotaje a Refinería", "Ciberataque a Infraestructura"]
    impactos = ["ALTO: Cierre de rutas marítimas", "MEDIO: Volatilidad de precios", "CRÍTICO: Interrupción de suministro energético"]

    incidentes = [
        {
            "id": f"EVT-{random.randint(1000, 9999)}",
            "fecha": datetime.datetime.now().strftime("%H:%M UTC"),
            "lat": random.uniform(12.0, 35.0), # Cubre desde Yemen hasta Líbano
            "lng": random.uniform(35.0, 60.0), # Cubre desde Israel hasta Irán
            "tipo": random.choice(tipos_ataque),
            "intensidad": random.choice(["Alta", "Crítica", "Media"]),
            "actor": random.choice(actores),
            "efecto": random.choice(impactos)
        } for _ in range(6) # Más incidentes para el mapa
    ]

    data = {
        "last_update": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "brent_price": round(current_price, 2),
        "gold_price": round(current_gold, 2),
        "incidentes": incidentes
    }

    with open('data/intel_report.json', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    get_intel()