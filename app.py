import streamlit as st

# Sample data
country_data = {
    "pakistan": {
        "Capital": "Islamabad",
        "Population": "241 million",
        "Region": "Asia",
        "Flag": "🇵🇰"
    },
    "canada": {
        "Capital": "Ottawa",
        "Population": "39 million",
        "Region": "North America",
        "Flag": "🇨🇦"
    },
    "japan": {
        "Capital": "Tokyo",
        "Population": "125 million",
        "Region": "Asia",
        "Flag": "🇯🇵"
    },
    "france": {
        "Capital": "Paris",
        "Population": "68 million",
        "Region": "Europe",
        "Flag": "🇫🇷"
    },
    "korea": {
        "Capital": "Seoul",
        "Population": "52 million",
        "Region": "Asia",
        "Flag": "🇰🇷"
    },
    "india": {
        "Capital": "New Delhi",
        "Population": "1.4 billion",
        "Region": "Asia",
        "Flag": "🇮🇳"
    },
    "china": {
        "Capital": "Beijing",
        "Population": "1.4 billion",
        "Region": "Asia",
        "Flag": "🇨🇳"
    },
    "usa": {
        "Capital": "Washington, D.C.",
        "Population": "333 million",
        "Region": "North America",
        "Flag": "🇺🇸"
    },
    "uk": {
        "Capital": "London",
        "Population": "67 million",
        "Region": "Europe",
        "Flag": "🇬🇧"
    },
    "germany": {
        "Capital": "Berlin",
        "Population": "83 million",
        "Region": "Europe",
        "Flag": "🇩🇪"
    },
    "saudi arabia": {
        "Capital": "Riyadh",
        "Population": "36 million",
        "Region": "Asia",
        "Flag": "🇸🇦"
    },
    "uae": {
        "Capital": "Abu Dhabi",
        "Population": "10 million",
        "Region": "Asia",
        "Flag": "🇦🇪"
    },
    "turkey": {
        "Capital": "Ankara",
        "Population": "85 million",
        "Region": "Asia/Europe",
        "Flag": "🇹🇷"
    },
    "brazil": {
        "Capital": "Brasília",
        "Population": "215 million",
        "Region": "South America",
        "Flag": "🇧🇷"
    },
    "egypt": {
        "Capital": "Cairo",
        "Population": "111 million",
        "Region": "Africa",
        "Flag": "🇪🇬"
    }
}




st.title("🌍 Country Info Cards")

user_input = st.text_input("Enter a country name:").lower()

if user_input:
    info = country_data.get(user_input)

    if info:
        st.markdown(f"""
        ### {user_input.title()} {info['Flag']}
        - **Capital:** {info['Capital']}
        - **Population:** {info['Population']}
        - **Region:** {info['Region']}
        """)
    else:
        st.error("Country not found in database. Try another one.")
