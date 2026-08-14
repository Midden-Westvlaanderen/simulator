import streamlit as st


PHOTO_CHALLENGES = [
    {
        "title": "Verwarming",
        "image": "assets/training_photos/fout_verwarming_kraan.png",
        "question": "Wat is hier niet goed?",
        "options": [
            "De radiatorkraan in de thermostaatruimte staat niet volledig open",
            "De thermostaat hangt te laag",
            "De radiator is te groot",
        ],
        "answer": "De radiatorkraan in de thermostaatruimte staat niet volledig open",
        "feedback": "De thermostaat vraagt warmte, maar de radiator wordt begrensd. Daardoor blijft de ketel werken.",
    },
    {
        "title": "Elektriciteit",
        "image": "assets/training_photos/fout_elektriciteit_standby.png",
        "question": "Welke fout zie je?",
        "options": [
            "Het toestel blijft op stand-by staan",
            "Het toestel staat te dicht bij de muur",
            "Het scherm is te klein",
        ],
        "answer": "Het toestel blijft op stand-by staan",
        "feedback": "Stand-by kan sluipverbruik veroorzaken. Volledig uitschakelen is zuiniger.",
    },
    {
        "title": "Water",
        "image": "assets/training_photos/fout_water_lek.png",
        "question": "Wat moet hier opgelost worden?",
        "options": [
            "Een lekkende kraan of leiding",
            "Een te kleine lavabo",
            "Te weinig licht in de badkamer",
        ],
        "answer": "Een lekkende kraan of leiding",
        "feedback": "Een klein lek kan op jaarbasis veel water verspillen.",
    },
    {
        "title": "Warmteverlies",
        "image": "assets/training_photos/fout_open_raam.png",
        "question": "Waarom is dit geen goede instelling?",
        "options": [
            "Het raam staat open terwijl de radiator verwarmt",
            "De radiator staat te laag tegen de muur",
            "Er hangt geen gordijn",
        ],
        "answer": "Het raam staat open terwijl de radiator verwarmt",
        "feedback": "Warmte verdwijnt naar buiten, waardoor de ketel langer blijft werken.",
    },
    {
        "title": "Koelkast",
        "image": "assets/training_photos/fout_koelkast_open.png",
        "question": "Wat zorgt hier voor extra elektriciteitsverbruik?",
        "options": [
            "De koelkastdeur blijft open",
            "De koelkast is wit",
            "Er ligt te weinig eten in de koelkast",
        ],
        "answer": "De koelkastdeur blijft open",
        "feedback": "Als koude lucht ontsnapt, moet de koelkast harder werken.",
    },
    {
        "title": "Warm water",
        "image": "assets/training_photos/fout_warm_water_lopen.png",
        "question": "Welke fout zie je?",
        "options": [
            "De warme kraan blijft lopen tijdens het tandenpoetsen",
            "De tandenborstel is te groot",
            "De lavabo is leeg",
        ],
        "answer": "De warme kraan blijft lopen tijdens het tandenpoetsen",
        "feedback": "Je verspilt water en energie om dat water te verwarmen.",
    },
    {
        "title": "Grootverbruiker elektriciteit",
        "image": "assets/training_photos/fout_grootverbruiker_droogkast.png",
        "question": "Wat is hier niet zuinig?",
        "options": [
            "De droogkast gebruiken voor weinig was",
            "De was eerst sorteren",
            "De droogkast na gebruik uitschakelen",
        ],
        "answer": "De droogkast gebruiken voor weinig was",
        "feedback": "Een droogkast maakt warmte en verbruikt veel elektriciteit. Gebruik ze liefst voor een volle lading of droog aan de lucht.",
    },
]


BIG_ELECTRICITY_CONSUMERS = [
    {
        "name": "Droogkast",
        "image": "assets/training_photos/grootverbruiker_droogkast.png",
        "tip": "Maakt warmte en verbruikt veel stroom. Gebruik liefst een volle lading.",
    },
    {
        "name": "Oven en kookplaat",
        "image": "assets/training_photos/grootverbruiker_oven.png",
        "tip": "Alles wat elektrisch verwarmt, vraagt veel energie.",
    },
    {
        "name": "Elektrische boiler",
        "image": "assets/training_photos/grootverbruiker_elektrische_boiler.png",
        "tip": "Warm water elektrisch maken kan zwaar doorwegen op de factuur.",
    },
    {
        "name": "Koelkast",
        "image": "assets/training_photos/grootverbruiker_koelkast.png",
        "tip": "Staat altijd aan. Sluit de deur snel en kies een goede stand.",
    },
    {
        "name": "Wasmachine",
        "image": "assets/training_photos/grootverbruiker_wasmachine.png",
        "tip": "Draai volle machines en gebruik een zuinig programma.",
    },
    {
        "name": "Vaatwasser",
        "image": "assets/training_photos/grootverbruiker_vaatwasser.png",
        "tip": "Gebruik ze vol en kies eco waar mogelijk.",
    },
]


PRACTICE_SECTIONS = {
    "Verwarming": [
        {
            "key": "training_practice_heating_1",
            "question": "1. Welke instelling is het meest energiezuinig?",
            "options": [
                "Thermostaat in Woonkamer, woonkamerkraan op 5, slaapkamer op 2",
                "Thermostaat in Woonkamer, woonkamerkraan op 3, slaapkamer op 5",
                "Thermostaat in slaapkamer, slaapkamerkraan op 2, Woonkamer op 5",
            ],
            "answer": "Thermostaat in Woonkamer, woonkamerkraan op 5, slaapkamer op 2",
            "feedback": "De thermostaatruimte kan de gewenste temperatuur bereiken en de slaapkamer staat lager.",
        },
        {
            "key": "training_practice_heating_2",
            "question": "2. De ketel blijft actief omdat de thermostaatruimte niet warm genoeg wordt. Wat doe je eerst?",
            "options": [
                "Radiatorkraan in de thermostaatruimte op 5 zetten",
                "Alle andere radiatoren hoger zetten",
                "De thermostaat nog hoger zetten",
            ],
            "answer": "Radiatorkraan in de thermostaatruimte op 5 zetten",
            "feedback": "De radiator in de thermostaatruimte moet volledig open staan.",
        },
        {
            "key": "training_practice_heating_3",
            "question": "3. Welke instelling past het best voor een slaapkamer die weinig gebruikt wordt?",
            "options": [
                "Radiatorkraan lager zetten, bijvoorbeeld op 2",
                "Radiatorkraan altijd op 5 laten",
                "Thermostaat verplaatsen zonder reden",
            ],
            "answer": "Radiatorkraan lager zetten, bijvoorbeeld op 2",
            "feedback": "Minder gebruikte kamers hoeven niet even warm te zijn.",
        },
    ],
    "Elektriciteit": [
        {
            "key": "training_practice_electricity_1",
            "question": "1. Welke gewoonte bespaart het meeste elektriciteit?",
            "options": [
                "Toestellen volledig uitschakelen wanneer ze niet nodig zijn",
                "Alle toestellen op stand-by laten staan",
                "De koelkast vaak lang open laten",
            ],
            "answer": "Toestellen volledig uitschakelen wanneer ze niet nodig zijn",
            "feedback": "Volledig uitschakelen voorkomt sluipverbruik.",
        },
        {
            "key": "training_practice_electricity_2",
            "question": "2. Hoe gebruik je wasmachine of vaatwasser zuiniger?",
            "options": [
                "Volle machines draaien met een zuinig programma",
                "Elke dag halflege machines draaien",
                "Altijd het heetste programma kiezen",
            ],
            "answer": "Volle machines draaien met een zuinig programma",
            "feedback": "Volle machines en zuinige programma's beperken het verbruik.",
        },
        {
            "key": "training_practice_electricity_3",
            "question": "3. Wat is een goede keuze voor verlichting?",
            "options": [
                "Ledlampen gebruiken en lichten uitdoen waar niemand is",
                "Alle lichten laten branden voor comfort",
                "Oude gloeilampen blijven gebruiken",
            ],
            "answer": "Ledlampen gebruiken en lichten uitdoen waar niemand is",
            "feedback": "Ledlampen en lichten uitdoen besparen elektriciteit.",
        },
    ],
    "Water": [
        {
            "key": "training_practice_water_1",
            "question": "1. Welke keuze bespaart water en energie?",
            "options": [
                "Korter douchen met een spaardouchekop",
                "De warme kraan laten lopen tijdens het tandenpoetsen",
                "Een lekkende kraan pas later herstellen",
            ],
            "answer": "Korter douchen met een spaardouchekop",
            "feedback": "Korter douchen bespaart water en energie voor warm water.",
        },
        {
            "key": "training_practice_water_2",
            "question": "2. Wat doe je met een lekkende kraan of toilet?",
            "options": [
                "Zo snel mogelijk herstellen of melden",
                "Wachten tot het erger wordt",
                "Alleen de kraan harder dichtdraaien",
            ],
            "answer": "Zo snel mogelijk herstellen of melden",
            "feedback": "Een lek kan ongemerkt veel water verspillen.",
        },
        {
            "key": "training_practice_water_3",
            "question": "3. Wat is zuinig wassen?",
            "options": [
                "Een volle wasmachine gebruiken",
                "Veel kleine wasjes apart draaien",
                "Altijd extra spoelen",
            ],
            "answer": "Een volle wasmachine gebruiken",
            "feedback": "Volle wasmachines gebruiken water efficienter.",
        },
    ],
}


QUIZ_SECTIONS = {
    "Verwarming": [
        {
            "key": "quiz_q1",
            "question": "1. Wat gebeurt er als de thermostaat 21 graden vraagt, maar de kraan in die kamer op 3 staat?",
            "options": [
                "De ketel blijft actief",
                "De ketel stopt meteen",
                "Alle andere radiatoren sluiten automatisch",
            ],
            "answer": "De ketel blijft actief",
        },
        {
            "key": "quiz_q2",
            "question": "2. Welke radiatorkraan moet volledig open staan?",
            "options": [
                "De kraan in de ruimte waar de thermostaat hangt",
                "Altijd alleen de woonkamerkraan",
                "Alle kranen in de woning",
            ],
            "answer": "De kraan in de ruimte waar de thermostaat hangt",
        },
        {
            "key": "quiz_q3",
            "question": "3. Wat doet elke graad boven 20 graden met het gasverbruik in deze simulatie?",
            "options": [
                "Ongeveer 7% meer verbruik",
                "Ongeveer 6% minder verbruik",
                "Geen verschil",
            ],
            "answer": "Ongeveer 7% meer verbruik",
        },
    ],
    "Elektriciteit": [
        {
            "key": "quiz_q4",
            "question": "1. Wat is sluipverbruik?",
            "options": [
                "Elektriciteit die toestellen verbruiken terwijl ze niet echt gebruikt worden",
                "Water dat door de radiator stroomt",
                "Gasverbruik bij een open raam",
            ],
            "answer": "Elektriciteit die toestellen verbruiken terwijl ze niet echt gebruikt worden",
        },
        {
            "key": "quiz_q5",
            "question": "2. Welke toestellen zijn vaak grote elektriciteitsverbruikers?",
            "options": [
                "Toestellen die warmte of koude maken",
                "Een uitgeschakelde lamp",
                "Een lege stekkerdoos zonder toestellen",
            ],
            "answer": "Toestellen die warmte of koude maken",
        },
        {
            "key": "quiz_q6",
            "question": "3. Welke verlichting is meestal het zuinigst?",
            "options": [
                "Ledverlichting",
                "Gloeilampen",
                "Lampen laten branden in lege kamers",
            ],
            "answer": "Ledverlichting",
        },
    ],
    "Water": [
        {
            "key": "quiz_q7",
            "question": "1. Waarom kost warm water extra?",
            "options": [
                "Je betaalt voor water en voor de energie om het water te verwarmen",
                "Warm water telt dubbel op de watermeter",
                "Warm water gebruikt altijd elektriciteit, nooit gas",
            ],
            "answer": "Je betaalt voor water en voor de energie om het water te verwarmen",
        },
        {
            "key": "quiz_q8",
            "question": "2. Welke situatie verspilt vaak ongemerkt veel water?",
            "options": [
                "Een lekkende kraan of lekkend toilet",
                "Een gesloten kraan",
                "Een volle wasmachine",
            ],
            "answer": "Een lekkende kraan of lekkend toilet",
        },
        {
            "key": "quiz_q9",
            "question": "3. Welke gewoonte bespaart water in de badkamer?",
            "options": [
                "Korter douchen",
                "De kraan laten lopen tijdens tandenpoetsen",
                "Een bad nemen in plaats van kort douchen",
            ],
            "answer": "Korter douchen",
        },
    ],
}


PRACTICE_KEYS = [question["key"] for questions in PRACTICE_SECTIONS.values() for question in questions]
QUIZ_KEYS = [question["key"] for questions in QUIZ_SECTIONS.values() for question in questions]
PHOTO_FAULT_KEYS = [f"photo_fault_{index}" for index in range(1, len(PHOTO_CHALLENGES) + 1)]

def render_central_heating_diagram():

    st.subheader("🔄 Gesloten circuit - Centrale verwarming")

    col1, col2 = st.columns(2)

    with col1:

        st.error("""
🔥 KETEL

Verwarmt water tot 60-80°C
""")

        st.markdown("### ⬇️ Hete water aanvoer")
        st.caption("Warm water stroomt via de leidingen")

        st.info("""
🌡️ THERMOSTAAT

Gemeten temperatuur: 19°C

Gewenste temperatuur: 20°C

Status: KETEL AAN
""")

    with col2:

        st.info("""
⬅️ RETOURLEIDING

Koeler water (ongeveer 30-40°C)
stroomt terug naar de ketel.
""")

        st.success("🏠 Woonkamer - Kraan 5 (open)")
        st.success("🍳 Keuken - Kraan 3 (half)")
        st.success("🛏️ Slaapkamer - Kraan 2 (laag)")
        st.success("🚿 Badkamer - Kraan 4 (hoog)")

    st.divider()

    st.markdown("""
### Hoe werkt het gesloten circuit?

1. De ketel verwarmt water.
2. Warm water stroomt naar de radiatoren.
3. De radiatorkranen regelen de warmteafgifte.
4. De kamers warmen op.
5. Het afgekoelde water stroomt terug naar de ketel.
6. Het systeem vormt een gesloten circuit.
""")

def reset_session_keys(keys):
    for key in keys:
        st.session_state.pop(key, None)


def render_training_module():
    st.subheader("Opleidingsmodule")

    with st.container(border=True):
        lesson_tab, practice_tab, quiz_tab, photo_tab = st.tabs(
            ["Leren", "Oefenen", "Quiz", "Zoek de fout"]
        )

        with lesson_tab:
            render_lessons()

        with practice_tab:
            render_practice()

        with quiz_tab:
            render_quiz()

        with photo_tab:
            render_photo_challenges()


def render_lessons():
    topic_tabs = st.tabs(["Verwarming", "Elektriciteit", "Water"])

    with topic_tabs[0]:
        
        st.markdown("### Centrale verwarming — basisprincipe")
        st.write(
            "Centrale verwarming werkt zo: een ketel verwarmt water tot hoge temperatuur. "
            "Dit hete water circuleert door buizen naar radiatoren in alle kamers. "
            "De radiatoren geven warmte af aan de lucht in elke kamer."
        )
        st.write(
            "De thermostaat meet de temperatuur in één kamer (de 'thermostaatruimte'). "
            "Als die kamer kouder wordt dan de gewenste temperatuur, geeft het signaal aan de ketel om warmte te produceren."
        )
        st.markdown("**Hoe centrale verwarming zuinig instellen:**")
        st.write(
            "1. **Radiatorkranen begrenzen de warmtestroom** — Elke radiator heeft een kraan met stand 0–5. "
            "Stand 5 = helemaal open, stand 0 = dicht."
        )
        st.write(
            "2. **Thermostaat bepaalt wanneer de ketel aan- en uitgaat** — In de thermostaatruimte "
            "moet de radiatorkraan op stand 5 staan, zodat de thermostaat goed kan werken."
        )
        st.write(
            "3. **Andere kamers kun je apart regelen** — Kamers die minder gebruikt worden, kunnen lager staan."
        )
        
        st.markdown("### Interactief schema centrale verwarming")
        render_central_heating_diagram()
        st.divider()
        st.markdown("**1. De thermostaat meet in een ruimte**")
        st.write(
            "De ketel reageert op de temperatuur in de ruimte waar de thermostaat hangt. "
            "Als die kamer de gevraagde temperatuur niet haalt, blijft de ketel verwarmen."
        )
        st.markdown("**2. De radiatorkraan in de thermostaatruimte moet op 5 staan**")
        st.write(
            "Een lagere stand knijpt de radiator dicht. De thermostaat blijft dan warmte vragen, "
            "maar de kamer warmt onvoldoende op."
        )
        st.markdown("**3. Andere kamers regel je apart**")
        st.write(
            "Kamers zonder thermostaat mogen lager staan als ze minder gebruikt worden. "
            "Zo vermijd je onnodig verbruik."
        )
        st.markdown("### Thermostaat = doeltemperatuur")
        st.markdown("### 🔥 Thermostaatkraan = hoeveel warmte de radiator mag geven")
        st.write("Thermostaat = doeltemperatuur. De radiatorkraan regelt hoeveel warmte de radiator mag afgeven.")
        render_heating_table()
    with topic_tabs[1]:
        st.write(
            "Grote verbruikers zijn toestellen die warmte of koude maken: droogkast, oven, "
            "elektrische boiler, vaatwasser, wasmachine en koelkast."
        )
        st.write(
            "Besparen kan door toestellen volledig uit te schakelen, ledlampen te gebruiken, "
            "volle machines te draaien en energiezuinige programma's te kiezen."
        )
        st.markdown("**Grootverbruikers elektriciteit**")
        consumer_columns = st.columns(3)
        for index, consumer in enumerate(BIG_ELECTRICITY_CONSUMERS):
            with consumer_columns[index % 3]:
                with st.container(border=True):
                    st.image(consumer["image"], width="stretch")
                    st.markdown(f"**{consumer['name']}**")
                    st.caption(consumer["tip"])

    with topic_tabs[2]:
        st.write(
            "Warm water kost dubbel: je verbruikt water en energie om dat water te verwarmen. "
            "Korter douchen, lekken herstellen en spaarkoppen gebruiken helpt meteen."
        )
        st.write(
            "Een lopende kraan of lekkend toilet lijkt klein, maar kan op jaarbasis veel water verspillen."
        )


def render_heating_table():
    st.subheader("Radiatorkraaninstellingen")
    st.table(
        [
            {"Kraan": 5, "Warmte": "██████████", "Percentage": "100%"},
            {"Kraan": 4, "Warmte": "████████░░", "Percentage": "80%"},
            {"Kraan": 3, "Warmte": "██████░░░░", "Percentage": "60%"},
            {"Kraan": 2, "Warmte": "████░░░░░░", "Percentage": "40%"},
            {"Kraan": 1, "Warmte": "██░░░░░░░░", "Percentage": "20%"},
        ]
    )


def render_practice():
    st.button(
        "Reset oefening",
        key="reset_practice",
        on_click=reset_session_keys,
        args=(PRACTICE_KEYS,),
    )

    render_question_sections(PRACTICE_SECTIONS)

    if st.button("Controleer oefening", key="check_practice"):
        results = collect_results(PRACTICE_SECTIONS)
        st.metric("Oefenscore", f"{results['score']}/{results['total']}")

        for result in results["items"]:
            if result["is_correct"]:
                st.success(f"{result['section']}: correct. {result['feedback']}")
            else:
                st.warning(f"{result['section']}: kijk dit nog eens na. {result['feedback']}")


def render_quiz():
    st.button(
        "Reset quiz",
        key="reset_quiz",
        on_click=reset_session_keys,
        args=(QUIZ_KEYS,),
    )

    render_question_sections(QUIZ_SECTIONS)

    if st.button("Controleer quiz", key="check_quiz"):
        results = collect_results(QUIZ_SECTIONS)
        st.metric("Score", f"{results['score']}/{results['total']}")

        if results["score"] == results["total"]:
            st.success("Prima. Je hebt de basis goed beet.")
        elif results["score"] >= 6:
            st.info("Goed bezig. Kijk nog eens naar de onderdelen waar je twijfelde.")
        else:
            st.warning("Bekijk de leerblokjes nog eens en probeer opnieuw.")


def render_question_sections(sections):
    topic_tabs = st.tabs(list(sections.keys()))

    for tab, (section_name, questions) in zip(topic_tabs, sections.items()):
        with tab:
            st.markdown(f"**{section_name}**")
            for question in questions:
                st.radio(
                    question["question"],
                    question["options"],
                    index=None,
                    key=question["key"],
                )


def collect_results(sections):
    items = []
    score = 0

    for section_name, questions in sections.items():
        for question in questions:
            selected = st.session_state.get(question["key"])
            is_correct = selected == question["answer"]
            score += 1 if is_correct else 0
            items.append(
                {
                    "section": section_name,
                    "is_correct": is_correct,
                    "feedback": question.get("feedback", f"Juiste antwoord: {question['answer']}."),
                }
            )

    return {
        "score": score,
        "total": len(items),
        "items": items,
    }


def render_photo_challenges():
    st.write("Bekijk elke foto en duid aan wat er niet goed is.")
    st.button(
        "Reset zoek de fout",
        key="reset_photo_faults",
        on_click=reset_session_keys,
        args=(PHOTO_FAULT_KEYS,),
    )
    photo_score = 0

    for index, challenge in enumerate(PHOTO_CHALLENGES, start=1):
        with st.container(border=True):
            left, right = st.columns([1, 1], gap="medium")

            with left:
                st.markdown(f"**{index}. {challenge['title']}**")
                st.image(challenge["image"], width="stretch")

            with right:
                answer = st.radio(
                    challenge["question"],
                    challenge["options"],
                    index=None,
                    key=f"photo_fault_{index}",
                )
                if answer == challenge["answer"]:
                    photo_score += 1

    if st.button("Controleer foto's", key="check_photo_faults"):
        st.metric("Fotoscore", f"{photo_score}/{len(PHOTO_CHALLENGES)}")

        for index, challenge in enumerate(PHOTO_CHALLENGES, start=1):
            selected = st.session_state.get(f"photo_fault_{index}")
            if selected == challenge["answer"]:
                st.success(f"{index}. Correct. {challenge['feedback']}")
            else:
                st.warning(
                    f"{index}. Niet helemaal. Juiste antwoord: {challenge['answer']}. "
                    f"{challenge['feedback']}"
                )
