from data import GAS_PRICE_PER_KWH, HOUSE_TYPES, VALVE_TEMPERATURES


def calculate_room_temperature(valve_setting):
    return VALVE_TEMPERATURES[valve_setting]


def calculate_effective_room_temperature(room, valve_setting, thermostat_room, thermostat_temperature):
    if room == thermostat_room and valve_setting == 5:
        return thermostat_temperature

    return calculate_room_temperature(valve_setting)


def calculate_thermostat_factor(thermostat_temperature):
    degrees_from_reference = thermostat_temperature - 20

    if degrees_from_reference > 0:
        return 1 + (degrees_from_reference * 0.07)

    if degrees_from_reference < 0:
        return 1 + (degrees_from_reference * 0.06)

    return 1


def calculate_boiler_penalty(thermostat_temperature, thermostat_room_valve_setting):
    closed_thermostat_room_valve_penalty = 0

    if thermostat_room_valve_setting < 5:
        closed_thermostat_room_valve_penalty = (5 - thermostat_room_valve_setting) * 0.08

    max_thermostat_room_temperature = (
        thermostat_temperature
        if thermostat_room_valve_setting == 5
        else calculate_room_temperature(thermostat_room_valve_setting)
    )
    unreachable_degrees = max(0, thermostat_temperature - max_thermostat_room_temperature)
    unreachable_temperature_penalty = unreachable_degrees * 0.10

    return 1 + closed_thermostat_room_valve_penalty + unreachable_temperature_penalty


def calculate_usage(house_type, thermostat_temperature, thermostat_room_valve_setting):
    base_usage = HOUSE_TYPES[house_type]["base_usage_kwh"]
    thermostat_factor = calculate_thermostat_factor(thermostat_temperature)
    boiler_penalty = calculate_boiler_penalty(
        thermostat_temperature,
        thermostat_room_valve_setting,
    )

    return base_usage * thermostat_factor * boiler_penalty


def estimate_cost(usage_kwh):
    return usage_kwh * GAS_PRICE_PER_KWH


def boiler_status(thermostat_temperature, thermostat_room_valve_setting, thermostat_room):
    if thermostat_room_valve_setting < 5:
        return {
            "is_active": True,
            "label": "Actief",
            "explanation": (
                f"De thermostaat staat in de {thermostat_room}. De radiatorkraan in die ruimte moet op stand 5 staan om de gevraagde temperatuur te kunnen bereiken."
            ),
        }

    return {
        "is_active": False,
        "label": "In rust",
        "explanation": f"De {thermostat_room} kan de gevraagde temperatuur bereiken.",
    }


def get_energy_tips(
    house_type,
    thermostat_temperature,
    valve_settings,
    boiler_is_active,
    thermostat_room,
):
    tips = []

    if thermostat_temperature > 20:
        tips.append("Zet de thermostaat lager: elke graad boven 20°C verhoogt het verbruik met ongeveer 7%.")

    if thermostat_temperature < 20:
        tips.append("Goed bezig: elke graad onder 20°C verlaagt het verbruik met ongeveer 6%.")

    if boiler_is_active:
        if valve_settings[thermostat_room] < 5:
            tips.append(
                f"Zet de radiatorkraan in de {thermostat_room} op 5: daar hangt de thermostaat, dus die kraan moet volledig open staan."
            )
        else:
            tips.append("Verlaag de thermostaat zodat de ketel niet blijft draaien.")

    rooms_with_high_valves = [
        room for room, setting in valve_settings.items() if room != thermostat_room and setting >= 4
    ]
    if rooms_with_high_valves:
        tips.append("Zet radiatorkranen in minder gebruikte kamers lager, bijvoorbeeld in slaapkamer of keuken.")

    if house_type in {"halfopen", "vrijstaand"}:
        tips.append("Bij dit woningtype loont extra isolatie vaak sterk door het grotere warmteverlies.")

    if not tips:
        tips.append(
            f"Je instellingen zijn evenwichtig: thermostaat en radiatorkraan in de {thermostat_room} werken goed samen."
        )

    return tips
