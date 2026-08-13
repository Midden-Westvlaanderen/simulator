import streamlit as st
import training

from data import ROOMS, DEFAULT_THERMOSTAT_ROOM, HOUSE_TYPES, ROOM_DEVICES, DEVICE_SYMBOLS
from electricity_simulation import (
    calculate_electricity_usage,
    estimate_electricity_cost,
    get_electricity_tips,
)
from gas_simulation import (
    calculate_effective_room_temperature,
    calculate_room_temperature,
    calculate_usage,
    boiler_status,
    estimate_cost,
    get_energy_tips,
)
from water_simulation import calculate_water_usage, estimate_water_cost, get_water_tips

st.set_page_config(
    page_title="Virtuele woning",
    page_icon="ðŸ ",
    layout="wide",
)


ROOM_LABELS = {
    "living": "Woonkamer",
    "keuken": "Keuken",
    "badkamer": "Badkamer",
    "slaapkamer": "Slaapkamer",
}


def room_label(value):
    if value is None:
        return ""
    key = str(value)
    return ROOM_LABELS.get(key, key.replace("_", " ").capitalize())


def render_room_card(room_name, valve_setting, thermostat_room, thermostat):
    room_temperature = calculate_effective_room_temperature(
        room_name,
        valve_setting,
        thermostat_room,
        thermostat,
    )

    with st.container():
        st.markdown(f"**{room_label(room_name)}**")
        if room_name == thermostat_room:
            st.caption(f"Thermostaat: {thermostat:.1f}°C")
        st.metric(label="Temperatuur", value=f"{room_temperature:.1f}°C")


def render_boiler_visual(boiler, thermostat_room, thermostat_room_valve_setting, thermostat):
    is_active = boiler["is_active"]
    boiler_class = "boiler-active" if is_active else "boiler-idle"
    flame_class = "flame-active" if is_active else "flame-idle"
    flow_class = "gas-flow-active" if is_active else "gas-flow-idle"
    status_text = "Gasverbruik loopt door" if is_active else "Gasverbruik gestopt"
    meter_text = "Gewenste temperatuur niet bereikt" if is_active else "Temperatuur bereikt"

    st.markdown(
        (
            f'<div class="boiler-panel {boiler_class}">'
            '<div class="boiler-header">'
            '<div>'
            '<div class="metric-label">Ketelvisualisatie</div>'
            f'<div class="boiler-title">{status_text}</div>'
            '</div>'
            f'<div class="boiler-flame {flame_class}"></div>'
            '</div>'
            '<div class="boiler-body">'
            '<div class="boiler-unit">'
            '<div class="boiler-screen">KETEL</div>'
            '<div class="boiler-lines"><span></span><span></span><span></span></div>'
            '</div>'
            '<div class="gas-pipe">'
            f'<div class="gas-flow {flow_class}"></div>'
            '</div>'
            '</div>'
            '<div class="gas-meter">'
            f'<div class="gas-meter-fill {flow_class}"></div>'
            '</div>'
            f'<div class="boiler-note">{meter_text}</div>'
            f'<div class="boiler-detail">Thermostaat in {room_label(thermostat_room)}: {thermostat:.1f}°C</div>'
            f'<div class="boiler-detail">Radiatorkraan daar: stand {thermostat_room_valve_setting}</div>'
            '</div>'
        ),
        unsafe_allow_html=True,
    )


def render_styles():
    st.markdown(
        """
        <style>
            .main .block-container {
                padding-top: 1.5rem;
                padding-bottom: 2rem;
            }

            .app-title {
                font-size: 2.1rem;
                font-weight: 700;
                margin-bottom: .25rem;
            }

            .app-subtitle {
                color: #5c6670;
                margin-bottom: 1.5rem;
            }

            .house-grid {
                display: grid;
                grid-template-columns: repeat(2, minmax(0, 1fr));
                gap: 1rem;
            }

            .room-card {
                min-height: 150px;
                border: 1px solid #d9dee5;
                border-radius: 8px;
                padding: 1rem;
                background: #ffffff;
                box-shadow: 0 1px 4px rgba(20, 32, 44, .06);
                margin-bottom: 1rem;
            }

            .room-title {
                font-size: 1.15rem;
                font-weight: 700;
                text-transform: capitalize;
                margin-bottom: .75rem;
            }

            .room-temp {
                font-size: 2rem;
                font-weight: 700;
                color: #1f6f78;
                margin-top: .35rem;
            }

            .room-meta {
                color: #58636f;
                margin-top: .35rem;
            }

            .thermostat {
                display: inline-block;
                border-radius: 999px;
                padding: .25rem .6rem;
                background: #fff2cc;
                color: #604700;
                font-weight: 650;
                font-size: .9rem;
            }

            .metric-panel {
                border: 1px solid #d9dee5;
                border-radius: 8px;
                padding: 1rem;
                background: #fbfcfd;
                margin-bottom: 1rem;
            }

            .metric-label {
                color: #5c6670;
                font-size: .9rem;
            }

            .metric-value {
                font-size: 1.65rem;
                font-weight: 750;
                margin-top: .15rem;
            }

            .status-active {
                color: #b42318;
                font-weight: 750;
            }

            .status-resting {
                color: #067647;
                font-weight: 750;
            }

            .boiler-panel {
                border: 1px solid #d9dee5;
                border-radius: 8px;
                padding: 1rem;
                background: #fbfcfd;
                margin-bottom: 1rem;
                overflow: hidden;
            }

            .boiler-active {
                border-color: #f04438;
                background: #fff7f5;
            }

            .boiler-idle {
                border-color: #cfd6df;
                background: #f8fafc;
            }

            .boiler-header {
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 1rem;
                margin-bottom: .85rem;
            }

            .boiler-title {
                font-size: 1.15rem;
                font-weight: 750;
            }

            .boiler-body {
                display: grid;
                grid-template-columns: 92px 1fr;
                align-items: center;
                gap: .75rem;
                margin-bottom: .75rem;
            }

            .boiler-unit {
                height: 112px;
                border-radius: 8px;
                border: 2px solid #65717d;
                background: linear-gradient(180deg, #ffffff 0%, #e9edf2 100%);
                padding: .6rem;
            }

            .boiler-screen {
                border-radius: 5px;
                background: #263238;
                color: #e7f8ef;
                font-size: .78rem;
                font-weight: 750;
                text-align: center;
                padding: .35rem .25rem;
                margin-bottom: .7rem;
            }

            .boiler-lines {
                display: grid;
                gap: .35rem;
            }

            .boiler-lines span {
                display: block;
                height: 8px;
                border-radius: 999px;
                background: #9aa4af;
            }

            .gas-pipe {
                position: relative;
                height: 18px;
                border-radius: 999px;
                background: #d0d7de;
                overflow: hidden;
            }

            .gas-flow {
                position: absolute;
                inset: 0;
            }

            .gas-flow-active {
                background: repeating-linear-gradient(
                    90deg,
                    #f04438 0,
                    #f04438 14px,
                    #ffb4a9 14px,
                    #ffb4a9 28px
                );
                animation: gas-flow 850ms linear infinite;
            }

            .gas-flow-idle {
                background: #9aa4af;
                opacity: .45;
            }

            .boiler-flame {
                width: 36px;
                height: 45px;
                border-radius: 55% 55% 55% 55%;
                transform: rotate(45deg);
            }

            .flame-active {
                background: #f04438;
                box-shadow: 0 0 20px rgba(240, 68, 56, .55);
                animation: flame-flicker .75s ease-in-out infinite alternate;
            }

            .flame-idle {
                background: #b8c0c9;
                box-shadow: none;
            }

            .gas-meter {
                height: 18px;
                border-radius: 999px;
                border: 1px solid #cfd6df;
                background: #edf1f5;
                overflow: hidden;
                margin-top: .35rem;
            }

            .gas-meter-fill {
                height: 100%;
                width: 100%;
            }

            .boiler-note {
                font-weight: 750;
                margin-top: .6rem;
            }

            .boiler-detail {
                color: #58636f;
                font-size: .92rem;
                margin-top: .15rem;
            }

            @keyframes gas-flow {
                from {
                    background-position: 0 0;
                }
                to {
                    background-position: 56px 0;
                }
            }

            @keyframes flame-flicker {
                from {
                    transform: rotate(45deg) scale(.92);
                    opacity: .78;
                }
                to {
                    transform: rotate(45deg) scale(1.04);
                    opacity: 1;
                }
            }

            .plan-room {
                position: relative;
                min-height: 155px;
                padding: .35rem .15rem .25rem;
            }

            .plan-room-content {
                position: relative;
                z-index: 1;
            }

            .selected-room {
                border-left: 5px solid #1f6f78;
                padding-left: .65rem;
            }

            .plan-room-name {
                font-size: 1.2rem;
                font-weight: 750;
            }

            .plan-room-temp {
                color: #1f6f78;
                font-size: 2rem;
                font-weight: 800;
                margin-top: .3rem;
            }

            .plan-room-valve {
                color: #58636f;
                margin-top: .2rem;
            }

            .floorplan {
                position: relative;
                margin-top: 1rem;
                padding: 1rem;
                border: 2px solid #d7dde5;
                border-radius: 18px;
                background: linear-gradient(180deg, #ebf5fb 0%, #f6fafb 100%);
                min-height: 470px;
                overflow: hidden;
            }

            .house-shell {
                position: relative;
                display: grid;
                grid-template-columns: 1.5fr 1fr 1.1fr;
                grid-template-rows: 1.25fr 1fr;
                gap: 14px;
                background: rgba(255,255,255,0.25);
                border: 2px solid #b0bec8;
                border-radius: 16px;
                padding: 0.9rem;
                min-height: 430px;
            }

            .floorplan::before {
                content: "";
                position: absolute;
                inset: 22px 18px 18px 18px;
                border: 2px solid #aebac5;
                border-radius: 12px;
                pointer-events: none;
            }

            .room-block {
                position: relative;
                z-index: 1;
                border: 2px solid #cbd5e1;
                border-radius: 14px;
                padding: 0.7rem 0.8rem;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                min-height: 170px;
                box-shadow: inset 0 0 0 1px rgba(255,255,255,0.55);
                transition: transform .2s ease, border-color .2s ease;
            }

            .room-block:hover {
                transform: translateY(-1px);
            }

            .room-block-thermostat {
                border-color: #1f6f78;
                box-shadow: 0 0 0 2px rgba(31,111,120,0.12), inset 0 0 0 1px rgba(255,255,255,0.6);
            }

            .room-living {
                grid-column: 1 / span 2;
                grid-row: 1;
                margin-right: 12px;
            }

            .room-keuken {
                grid-column: 3;
                grid-row: 1;
            }

            .room-slaapkamer {
                grid-column: 1;
                grid-row: 2;
                margin-right: 12px;
            }

            .room-badkamer {
                grid-column: 2 / span 2;
                grid-row: 2;
            }

            .room-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: .75rem;
            }

            .room-name {
                font-size: 1.2rem;
                font-weight: 800;
                text-transform: capitalize;
            }

            .room-tag {
                display: inline-flex;
                align-items: center;
                border-radius: 999px;
                padding: .15rem .55rem;
                font-size: .72rem;
                font-weight: 700;
                background: #fff2cc;
                color: #604700;
            }

            .room-temp {
                font-size: 2.2rem;
                font-weight: 900;
                color: #1f6f78;
                margin: .4rem 0 .2rem;
                line-height: 1;
            }

            .room-meta {
                color: #58636f;
                margin-top: .15rem;
                font-size: .92rem;
            }

            .hall {
                position: absolute;
                left: 45%;
                top: 18%;
                width: 10%;
                height: 62%;
                border: 2px dashed #9aa4af;
                border-radius: 12px;
                background: rgba(255,255,255,0.2);
                z-index: 0;
            }

            .door {
                position: absolute;
                z-index: 2;
                background: #d9e2ea;
                border: 2px solid #8ea0ad;
                border-radius: 8px;
            }

            .door-horizontal {
                height: 18px;
                width: 46px;
            }

            .door-vertical {
                width: 18px;
                height: 46px;
            }

            .door-living {
                left: 42%;
                top: 64%;
            }

            .door-kitchen {
                right: 14%;
                top: 38%;
            }

            .door-bedroom {
                left: 30%;
                bottom: 10%;
            }

            .door-bathroom {
                right: 36%;
                bottom: 12%;
            }

            .radiator {
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: .25rem;
                width: min(170px, 100%);
                height: 34px;
                margin-top: .85rem;
                padding: .25rem;
                border-radius: 8px;
                border: 1px solid #cfd6df;
                background: #f8fafc;
            }

            .radiator span {
                border-radius: 5px;
                background: #aeb7c2;
            }

            .radiator-active {
                border-color: #f04438;
                background: #fff1f0;
                box-shadow: 0 0 0 rgba(240, 68, 56, 0);
                animation: radiator-glow 1.35s ease-in-out infinite;
            }

            .radiator-active span {
                background: #e02d20;
                animation: radiator-heat 1.35s ease-in-out infinite;
            }

            .radiator-active span:nth-child(2) {
                animation-delay: .12s;
            }

            .radiator-active span:nth-child(3) {
                animation-delay: .24s;
            }

            .radiator-active span:nth-child(4) {
                animation-delay: .36s;
            }

            .radiator-idle {
                border-color: #cfd6df;
                background: #f1f4f7;
            }

            .radiator-idle span {
                background: #9aa4af;
            }

            @keyframes radiator-glow {
                0%, 100% {
                    box-shadow: 0 0 0 rgba(240, 68, 56, 0);
                }
                50% {
                    box-shadow: 0 0 18px rgba(240, 68, 56, .34);
                }
            }

            @keyframes radiator-heat {
                0%, 100% {
                    opacity: .72;
                    transform: scaleY(.92);
                }
                50% {
                    opacity: 1;
                    transform: scaleY(1);
                }
            }

            .plan-thermostat {
                display: inline-block;
                margin-top: .3rem;
                border-radius: 999px;
                padding: .2rem .55rem;
                background: #fff2cc;
                color: #604700;
                font-weight: 650;
                font-size: .85rem;
            }

            @media (max-width: 780px) {
                .house-grid {
                    grid-template-columns: 1fr;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def get_selected_room_devices():
    selections = {}
    room_device_selections = st.session_state.get("room_device_selections", {})
    for room in ROOMS:
        selections[room] = list(room_device_selections.get(room, []))
    return selections


def summarize_selected_room_devices(device_selection):
    totals = {
        "fridge_count": 0,
        "freezer_count": 0,
        "dryer_cycles_week": 0,
        "washer_cycles_week": 0,
        "dishwasher_cycles_week": 0,
        "oven_uses_week": 0,
        "lighting_hours_day": 0.0,
        "standby_devices": False,
    }

    for room_devices in device_selection.values():
        for device in room_devices:
            normalized = str(device).lower().strip()

            if normalized == "koelkast":
                totals["fridge_count"] += 1
            elif normalized == "diepvries":
                totals["freezer_count"] += 1
            elif normalized in {"droger", "droogkast"}:
                totals["dryer_cycles_week"] += 2
            elif normalized == "wasmachine":
                totals["washer_cycles_week"] += 2
            elif normalized == "vaatwasser":
                totals["dishwasher_cycles_week"] += 2
            elif normalized == "oven":
                totals["oven_uses_week"] += 2
            elif normalized == "lamp":
                totals["lighting_hours_day"] += 1.5
            elif normalized in {"televisie", "soundbar", "gameconsole", "laptop", "router", "airco", "waterverwarmer", "nachtlamp", "verwarming", "komfoor", "microgolf", "koffiezetapparaat", "oplader", "haarstijltang", "ventilator"}:
                totals["standby_devices"] = True

    return totals


def render_house_plan():
    st.subheader("Gebouwvisualisatie")

    if "selected_room" not in st.session_state:
        st.session_state.selected_room = DEFAULT_THERMOSTAT_ROOM

    room_layout = {
        "living": {"row": 0, "col": 0, "w": 2, "color": "#dfeefb"},
        "keuken": {"row": 0, "col": 1, "w": 1, "color": "#f2e7d5"},
        "slaapkamer": {"row": 1, "col": 0, "w": 1, "color": "#e8f3df"},
        "badkamer": {"row": 1, "col": 1, "w": 1, "color": "#f5e3ea"},
    }

    st.markdown(
        """
        <style>
        div[data-testid="stButton"] > button {
            width: 100%;
            min-height: 130px;
            border-radius: 12px;
            border: 2px solid #8897a4;
            background: #f5f7fa;
            font-size: 1.05rem;
            font-weight: 600;
            color: #243b53;
            margin-bottom: 0.5rem;
        }
        div[data-testid="stButton"] > button:hover {
            border-color: #1f6f78;
            filter: brightness(0.98);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    room_columns = st.columns(2)
    room_button_order = ["living", "keuken", "slaapkamer", "badkamer"]

    for index, room_name in enumerate(room_button_order):
        column = room_columns[index % 2]
        with column:
            if st.button(
                room_label(room_name),
                key=f"room_button_{room_name}",
                width="stretch",
            ):
                st.session_state.selected_room = room_name

    current_room = st.session_state.get("selected_room", DEFAULT_THERMOSTAT_ROOM)
    if current_room not in room_layout:
        current_room = DEFAULT_THERMOSTAT_ROOM

    selected_style = (
        "<div style='margin-top: 1rem; padding: 0.75rem 1rem; border-radius: 10px; "
        "background: #edf8f9; border: 1px solid #cfe6ea; color: #1f6f78; font-weight: 600;'>"
        f"Geselecteerde ruimte: {room_label(current_room)}</div>"
    )
    st.markdown(selected_style, unsafe_allow_html=True)

    room_devices = ROOM_DEVICES.get(current_room, [])
    device_key = f"room_devices_{current_room}"
    if "room_device_selections" not in st.session_state:
        st.session_state["room_device_selections"] = {}

    st.subheader(f"Toestellen in {room_label(current_room)}")
    room_device_selections = st.session_state["room_device_selections"]
    selected_labels = room_device_selections.get(current_room, [])
    device_options = [f"{DEVICE_SYMBOLS.get(device, '🔧')} {device}" for device in room_devices]

    selected_devices = st.multiselect(
        "Kies alle toestellen die in deze ruimte staan",
        options=device_options,
        default=[f"{DEVICE_SYMBOLS.get(device, '🔧')} {device}" for device in selected_labels if device in room_devices],
        key=device_key,
    )

    cleaned_selection = [label.split(" ", 1)[1] for label in selected_devices]
    room_device_selections[current_room] = cleaned_selection

    if selected_devices:
        st.caption(f"{len(selected_devices)} toestel(len) geselecteerd")
        st.write(", ".join(selected_devices))
    else:
        st.caption("Geen toestellen geselecteerd in deze ruimte.")


def render_gas_simulation():
    controls_col, results_col = st.columns([1.7, 1], gap="large")

    with controls_col:
        st.subheader("Gas simuleren")
        house_type = st.selectbox("Woningtype", list(HOUSE_TYPES.keys()))
        thermostat_room = st.selectbox(
            "Ruimte waar de thermostaat hangt",
            ROOMS,
            index=ROOMS.index(DEFAULT_THERMOSTAT_ROOM),
            format_func=room_label,
        )
        thermostat = st.slider(
            f"Thermostaat in de {thermostat_room}",
            14.0,
            25.0,
            20.0,
            0.5,
        )

        st.write("Radiatorkranen")
        valve_settings = {}
        valve_columns = st.columns(2)
        for index, room in enumerate(ROOMS):
            with valve_columns[index % 2]:
                valve_settings[room] = st.slider(
                    room_label(room),
                    min_value=0,
                    max_value=5,
                    value=5 if room == thermostat_room else 2,
                    step=1,
                    key=f"valve_{room}",
                )

        thermostat_room_valve_setting = valve_settings[thermostat_room]
        usage = calculate_usage(house_type, thermostat, thermostat_room_valve_setting)
        cost = estimate_cost(usage)
        boiler = boiler_status(thermostat, thermostat_room_valve_setting, thermostat_room)
        tips = get_energy_tips(
            house_type,
            thermostat,
            valve_settings,
            boiler["is_active"],
            thermostat_room,
        )

        st.subheader("Kamertemperaturen")
        temp_columns = st.columns(2)
        for index, room in enumerate(ROOMS):
            with temp_columns[index % 2]:
                render_room_card(
                    room,
                    valve_settings[room],
                    thermostat_room,
                    thermostat,
                )

    with results_col:
        st.subheader("Resultaat")
        st.markdown(
            f"""
            <div class="metric-panel">
                <div class="metric-label">Jaarlijks gasverbruik</div>
                <div class="metric-value">{usage:,.0f} kWh</div>
            </div>
            <div class="metric-panel">
                <div class="metric-label">Geschatte kost</div>
                <div class="metric-value">&#8364; {cost:,.0f} / jaar</div>
            </div>
            """.replace(",", "."),
            unsafe_allow_html=True,
        )

        status_class = "status-active" if boiler["is_active"] else "status-resting"
        st.markdown(
            f"""
            <div class="metric-panel">
                <div class="metric-label">Status ketel</div>
                <div class="metric-value {status_class}">{boiler["label"]}</div>
                <div><strong>Thermostaatruimte:</strong> {thermostat_room}</div>
                <div><strong>Radiatorkraan daar:</strong> stand {thermostat_room_valve_setting}</div>
                <div>{boiler["explanation"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        render_boiler_visual(
            boiler,
            thermostat_room,
            thermostat_room_valve_setting,
            thermostat,
        )

        st.subheader("Tips")
        for tip in tips:
            st.info(tip)


def render_electricity_simulation():
    controls_col, results_col = st.columns([1.35, 1], gap="large")

    selected_room_devices = get_selected_room_devices()
    selected_device_totals = summarize_selected_room_devices(selected_room_devices)

    with controls_col:
        st.subheader("Elektriciteit simuleren")
        st.caption("Deze waarden volgen de gekozen toestellen per ruimte.")
        selected_device_summary = []
        for room, devices in selected_room_devices.items():
            if devices:
                selected_device_summary.append(f"{room_label(room)}: {', '.join(devices)}")
        if selected_device_summary:
            st.write("• " + "\n• ".join(selected_device_summary))
        else:
            st.info("💡 Selecteer toestellen in het Gebouw-tabblad om relevante vragen hier te zien.")

        inputs = {}

        # Only ask about appliances if they are selected
        all_devices = [device for devices in selected_room_devices.values() for device in devices]

        if "koelkast" in all_devices:
            inputs["fridge_count"] = st.number_input("Aantal koelkasten", 0, 5, selected_device_totals["fridge_count"], key="electricity_fridge")
        else:
            inputs["fridge_count"] = 0

        if "diepvries" in all_devices:
            inputs["freezer_count"] = st.number_input("Aantal diepvriezers", 0, 5, selected_device_totals["freezer_count"], key="electricity_freezer")
        else:
            inputs["freezer_count"] = 0

        if "droger" in all_devices or "droogkast" in all_devices:
            inputs["dryer_cycles_week"] = st.slider("Droogkastbeurten per week", 0, 14, selected_device_totals["dryer_cycles_week"], key="electricity_dryer")
        else:
            inputs["dryer_cycles_week"] = 0

        if "wasmachine" in all_devices:
            inputs["washer_cycles_week"] = st.slider("Wasmachinebeurten per week", 0, 14, selected_device_totals["washer_cycles_week"], key="electricity_washer")
        else:
            inputs["washer_cycles_week"] = 0

        if "vaatwasser" in all_devices:
            inputs["dishwasher_cycles_week"] = st.slider("Vaatwasserbeurten per week", 0, 14, selected_device_totals["dishwasher_cycles_week"], key="electricity_dishwasher")
        else:
            inputs["dishwasher_cycles_week"] = 0

        if "oven" in all_devices:
            inputs["oven_uses_week"] = st.slider("Ovengebruik per week", 0, 14, selected_device_totals["oven_uses_week"], key="electricity_oven")
        else:
            inputs["oven_uses_week"] = 0

        if "lamp" in all_devices:
            inputs["lighting_hours_day"] = st.slider("Uren verlichting per dag", 0.0, 12.0, selected_device_totals["lighting_hours_day"], 0.5, key="electricity_lighting")
        else:
            inputs["lighting_hours_day"] = 0.0

        if any(device in all_devices for device in ["televisie", "soundbar", "gameconsole", "laptop", "router", "airco", "waterverwarmer", "nachtlamp", "verwarming", "komfoor", "microgolf", "koffiezetapparaat", "oplader", "haarstijltang", "ventilator"]):
            inputs["standby_devices"] = st.checkbox("Meerdere toestellen blijven op stand-by", value=selected_device_totals["standby_devices"], key="electricity_standby")
        else:
            inputs["standby_devices"] = False

    usage = calculate_electricity_usage(inputs)
    cost = estimate_electricity_cost(usage)
    tips = get_electricity_tips(inputs)

    with results_col:
        st.subheader("Resultaat")
        st.metric("Jaarlijks elektriciteitsverbruik", f"{usage:,.0f} kWh".replace(",", "."))
        st.metric("Geschatte kost", f"\u20AC {cost:,.0f} / jaar".replace(",", "."))

        st.subheader("Tips")
        for tip in tips:
            st.info(tip)


def render_water_simulation():
    controls_col, results_col = st.columns([1.35, 1], gap="large")

    selected_room_devices = get_selected_room_devices()
    bathroom_devices = selected_room_devices.get("badkamer", [])
    kitchen_devices = selected_room_devices.get("keuken", [])
    
    has_shower = "douche" in bathroom_devices
    has_bath = "bad" in bathroom_devices
    has_washer = "wasmachine" in bathroom_devices
    has_dishwasher = "vaatwasser" in kitchen_devices

    with controls_col:
        st.subheader("Water simuleren")
        inputs = {}

        if has_shower:
            inputs["showers_week"] = st.slider("Douches per week", 0, 35, 7, key="water_showers")
            inputs["shower_minutes"] = st.slider("Minuten per douche", 1, 20, 8, key="water_minutes")
            inputs["shower_liters_minute"] = st.slider("Liter per minuut", 5, 15, 9, key="water_flow")
        else:
            inputs["showers_week"] = 0
            inputs["shower_minutes"] = 0
            inputs["shower_liters_minute"] = 0
            if not has_bath:
                st.info("🚿 Selecteer 'douche' of 'bad' in de badkamer om waterverbruik in te stellen.")

        if has_bath:
            inputs["baths_week"] = st.slider("Baden per week", 0, 10, 0, key="water_baths")
        else:
            inputs["baths_week"] = 0

        if has_washer:
            inputs["washer_cycles_week"] = st.slider("Wasmachinebeurten per week", 0, 14, 4, key="water_washer")
        else:
            inputs["washer_cycles_week"] = 0

        if has_dishwasher:
            inputs["dishwasher_cycles_week"] = st.slider("Vaatwasserbeurten per week", 0, 14, 4, key="water_dishwasher")
        else:
            inputs["dishwasher_cycles_week"] = 0

        inputs["leak_present"] = st.checkbox("Er is een lekkende kraan of toilet", value=False)

    usage = calculate_water_usage(inputs)
    costs = estimate_water_cost(usage)
    tips = get_water_tips(inputs, usage)

    with results_col:
        st.subheader("Resultaat")
        st.metric("Jaarlijks waterverbruik", f"{usage['total_m3']:,.1f} m³".replace(",", "."))
        st.metric("Geschatte kost", f"\u20AC {costs['total_cost']:,.0f} / jaar".replace(",", "."))
        st.caption(
            f"Waarvan ongeveer \u20AC {costs['hot_water_energy_cost']:,.0f} voor energie om warm water te maken.".replace(",", ".")
        )

        if usage["leak_liters"]:
            st.warning(f"Lekverlies: ongeveer {usage['leak_liters']:,.0f} liter per jaar.".replace(",", "."))

        st.subheader("Tips")
        for tip in tips:
            st.info(tip)


def main():
    render_styles()

    st.markdown("<div class='app-title'>Interactieve virtuele woning</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='app-subtitle'>Simuleer gas, elektriciteit en water en oefen met de opleidingsmodule.</div>",
        unsafe_allow_html=True,
    )

    house_tab, gas_tab, electricity_tab, water_tab, training_tab = st.tabs(
        ["Gebouw", "Gas", "Elektriciteit", "Water", "Opleiding"]
    )

    with house_tab:
        render_house_plan()

    with gas_tab:
        render_gas_simulation()

    with electricity_tab:
        render_electricity_simulation()

    with water_tab:
        render_water_simulation()

    with training_tab:
        training.render_training_module()


if __name__ == "__main__":
    main()
