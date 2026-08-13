ELECTRICITY_PRICE_PER_KWH = 0.38

ELECTRICITY_APPLIANCES = {
    "koelkast": {"kwh_per_year": 180, "tip": "Sluit de deur snel en kies een middelmatige koelstand."},
    "diepvriezer": {"kwh_per_year": 250, "tip": "Ontdooi regelmatig en zet niet kouder dan nodig."},
    "droogkast": {"kwh_per_cycle": 2.5, "tip": "Droog aan de lucht wanneer dat kan."},
    "wasmachine": {"kwh_per_cycle": 0.8, "tip": "Gebruik volle machines en eco-programma's."},
    "vaatwasser": {"kwh_per_cycle": 1.0, "tip": "Laat ze vol draaien en kies eco."},
    "oven": {"kwh_per_use": 1.4, "tip": "Gebruik restwarmte en vermijd lang voorverwarmen."},
    "verlichting": {"kwh_per_hour": 0.06, "tip": "Gebruik ledlampen en doe lichten uit."},
    "stand-by": {"kwh_per_year": 120, "tip": "Schakel toestellen volledig uit."},
}


def calculate_electricity_usage(inputs):
    usage = 0
    usage += inputs["fridge_count"] * ELECTRICITY_APPLIANCES["koelkast"]["kwh_per_year"]
    usage += inputs["freezer_count"] * ELECTRICITY_APPLIANCES["diepvriezer"]["kwh_per_year"]
    usage += inputs["dryer_cycles_week"] * 52 * ELECTRICITY_APPLIANCES["droogkast"]["kwh_per_cycle"]
    usage += inputs["washer_cycles_week"] * 52 * ELECTRICITY_APPLIANCES["wasmachine"]["kwh_per_cycle"]
    usage += inputs["dishwasher_cycles_week"] * 52 * ELECTRICITY_APPLIANCES["vaatwasser"]["kwh_per_cycle"]
    usage += inputs["oven_uses_week"] * 52 * ELECTRICITY_APPLIANCES["oven"]["kwh_per_use"]
    usage += inputs["lighting_hours_day"] * 365 * ELECTRICITY_APPLIANCES["verlichting"]["kwh_per_hour"]

    if inputs["standby_devices"]:
        usage += ELECTRICITY_APPLIANCES["stand-by"]["kwh_per_year"]

    return usage


def estimate_electricity_cost(usage_kwh):
    return usage_kwh * ELECTRICITY_PRICE_PER_KWH


def get_electricity_tips(inputs):
    tips = []

    if inputs["dryer_cycles_week"] >= 3:
        tips.append("De droogkast is een grootverbruiker. Minder droogbeurten leveren snel winst op.")

    if inputs["standby_devices"]:
        tips.append("Vermijd sluipverbruik door toestellen volledig uit te schakelen.")

    if inputs["lighting_hours_day"] > 5:
        tips.append("Beperk branduren van verlichting en gebruik ledlampen.")

    if inputs["washer_cycles_week"] > 5 or inputs["dishwasher_cycles_week"] > 5:
        tips.append("Draai wasmachine en vaatwasser pas wanneer ze goed gevuld zijn.")

    if not tips:
        tips.append("Je elektriciteitsinstellingen zijn vrij zuinig.")

    return tips
