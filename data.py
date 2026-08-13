ROOMS = ["living", "keuken", "badkamer", "slaapkamer"]

DEFAULT_THERMOSTAT_ROOM = "living"

DEVICE_SYMBOLS = {
    "lamp": "💡",
    "televisie": "📺",
    "gameconsole": "🎮",
    "laptop": "💻",
    "airco": "❄️",
    "koelkast": "🧊",
    "diepvries": "🥶",
    "oven": "🔥",
    "komfoor": "🍳",
    "vaatwasser": "🫙",
    "microgolf": "🛒",
    "koffiezetapparaat": "☕",
    "keukenboiler": "⚡",
    "waterkoker": "♨️",
    "verwarming": "🔥",
    "waterverwarmer": "🚿",
    "haarstijltang": "💇",
    "droger": "🌀",
    "ventilator": "💨",
    "nachtlamp": "🌙",
    "oplader": "🔌",
    "hout/pelletkachel": "🔥",
    "radiatoren": "♨️",
    "elektrische accumulatoren": "🔋",
    "elektrische boiler": "⚡",
    "doorstromer": "💧",
    "elektrisch vuurtje": "🔥",
    "bad": "🛁",
    "douche": "🚿",
    "wasmachine": "🧺",
    "droogkast": "🌀",
}

ROOM_DEVICES = {
    "living": [
        "lamp",
        "televisie",
        "gameconsole",
        "laptop",
        "airco",
        "hout/pelletkachel",
        "radiatoren",
        "elektrische accumulatoren",
    ],
    "keuken": [
        "koelkast",
        "diepvries",
        "oven",
        "vaatwasser",
        "microgolf",
        "koffiezetapparaat",
        "keukenboiler",
        "waterkoker",
    ],
    "badkamer": [
        "lamp",
        "verwarming",
        "elektrische boiler",
        "doorstromer",
        "elektrisch vuurtje",
        "bad",
        "douche",
        "wasmachine",
        "droogkast",
    ],
    "slaapkamer": [
        "lamp",
        "nachtlamp",
        "televisie",
        "laptop",
        "oplader",
        "airco",
        "elektrisch vuurtje",
    ],
}

HOUSE_TYPES = {
    "appartement": {
        "base_usage_kwh": 9000,
        "description": "Compact volume met weinig buitenmuren.",
    },
    "rijwoning": {
        "base_usage_kwh": 12000,
        "description": "Gedeelde muren beperken warmteverlies.",
    },
    "halfopen": {
        "base_usage_kwh": 16000,
        "description": "Meer buitenoppervlak vraagt meer verwarming.",
    },
    "vrijstaand": {
        "base_usage_kwh": 22000,
        "description": "Veel buitenmuren en dakoppervlak zorgen voor meer verlies.",
    },
}

GAS_PRICE_PER_KWH = 0.11

VALVE_TEMPERATURES = {
    0: 8.0,
    1: 12.0,
    2: 16.0,
    3: 20.0,
    4: 22.0,
    5: 24.0,
}
