import json

equipos = [
    {
        "Nombre": "Real Madrid",
        "país": "España",
        "nivelAtaque": 95,
        "nivelDefensa": 88
    },
    {
        "Nombre": "Manchester City",
        "país": "Inglaterra",
        "nivelAtaque": 93,
        "nivelDefensa": 90
    },
    {
        "Nombre": "Bayern Munich",
        "país": "Alemania",
        "nivelAtaque": 91,
        "nivelDefensa": 87
    },
    {
        "Nombre": "PSG",
        "país": "Francia",
        "nivelAtaque": 94,
        "nivelDefensa": 82
    },
    {
        "Nombre": "Barcelona",
        "país": "España",
        "nivelAtaque": 89,
        "nivelDefensa": 85
    }
]

json_equipos = json.dumps(equipos, indent=4, ensure_ascii=False)

print("--- EQUIPOS DE FÚTBOL EN FORMATO JSON ---\n")
print(json_equipos)

print("\n--- INFORMACIÓN RESUMIDA ---")
print(f"Total de equipos: {len(equipos)}")
for equipo in equipos:
    print(f"- {equipo["Nombre"]} ({equipo["país"]}): Ataque {equipo["nivelAtaque"]}, Defensa {equipo["nivelDefensa"]}")