WATER_PRICE_PER_M3 = 5.3
HOT_WATER_ENERGY_KWH_PER_M3 = 46
HOT_WATER_ENERGY_PRICE_PER_KWH = 0.11


def calculate_water_usage(inputs):
    shower_liters = inputs["showers_week"] * inputs["shower_minutes"] * inputs["shower_liters_minute"] * 52
    bath_liters = inputs["baths_week"] * 120 * 52
    washing_liters = inputs["washer_cycles_week"] * 50 * 52
    dishwasher_liters = inputs["dishwasher_cycles_week"] * 12 * 52
    leak_liters = 0

    if inputs["leak_present"]:
        leak_liters = 15 * 365

    total_liters = shower_liters + bath_liters + washing_liters + dishwasher_liters + leak_liters
    hot_liters = shower_liters + bath_liters

    return {
        "total_liters": total_liters,
        "total_m3": total_liters / 1000,
        "hot_m3": hot_liters / 1000,
        "leak_liters": leak_liters,
    }


def estimate_water_cost(usage):
    water_cost = usage["total_m3"] * WATER_PRICE_PER_M3
    hot_water_energy_cost = usage["hot_m3"] * HOT_WATER_ENERGY_KWH_PER_M3 * HOT_WATER_ENERGY_PRICE_PER_KWH
    return {
        "water_cost": water_cost,
        "hot_water_energy_cost": hot_water_energy_cost,
        "total_cost": water_cost + hot_water_energy_cost,
    }


def get_water_tips(inputs, usage):
    tips = []

    if inputs["shower_minutes"] > 7:
        tips.append("Korter douchen bespaart water en energie voor warm water.")

    if inputs["shower_liters_minute"] > 8:
        tips.append("Een spaardouchekop verlaagt het waterverbruik per minuut.")

    if inputs["leak_present"]:
        tips.append("Herstel lekken snel: een klein lek kan duizenden liters per jaar verspillen.")

    if inputs["baths_week"] > 1:
        tips.append("Een bad verbruikt vaak veel meer water dan een korte douche.")

    if not tips:
        tips.append("Je waterinstellingen zijn vrij zuinig.")

    return tips
