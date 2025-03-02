import streamlit as st


st.set_page_config(page_title="Unit Converter", page_icon="📏")
st.title("Unit Converter")
st.markdown("### Convert Length, Mass, and Time with Ease")
st.write("##### Select a category and units to get started!")


with st.sidebar:
    st.markdown("#### Conversion Options")
    category = st.selectbox("Select Category", ["Length", "Mass", "Time"])


conversion_factors = {
    "Length": {
        "Kilometers to Miles": 0.621371,
        "Miles to Kilometers": 1 / 0.621371,
        "Meters to Feet": 3.28084,
        "Feet to Meters": 1 / 3.28084,
        "Centimeters to Inches": 0.393701,
        "Inches to Centimeters": 1 / 0.393701
    },
    "Mass": {
        "Kilograms to Pounds": 2.20462,
        "Pounds to Kilograms": 1 / 2.20462,
        "Grams to Ounces": 0.035274,
        "Ounces to Grams": 1 / 0.035274,
        "Kilograms to Tons": 0.001,
        "Tons to Kilograms": 1000
    },
    "Time": {
        "Seconds to Minutes": 1 / 60,
        "Minutes to Seconds": 60,
        "Minutes to Hours": 1 / 60,
        "Hours to Minutes": 60,
        "Hours to Days": 1 / 24,
        "Days to Hours": 24,
        "Days to Weeks": 1 / 7,
        "Weeks to Days": 7
    }
}


result_units = {
    "Kilometers to Miles": "miles",
    "Miles to Kilometers": "kilometers",
    "Meters to Feet": "feet",
    "Feet to Meters": "meters",
    "Centimeters to Inches": "inches",
    "Inches to Centimeters": "centimeters",
    "Kilograms to Pounds": "pounds",
    "Pounds to Kilograms": "kilograms",
    "Grams to Ounces": "ounces",
    "Ounces to Grams": "grams",
    "Kilograms to Tons": "tons",
    "Tons to Kilograms": "kilograms",
    "Seconds to Minutes": "minutes",
    "Minutes to Seconds": "seconds",
    "Minutes to Hours": "hours",
    "Hours to Minutes": "minutes",
    "Hours to Days": "days",
    "Days to Hours": "hours",
    "Days to Weeks": "weeks",
    "Weeks to Days": "days"
}


def convert_units(category, value, unit):
    return value * conversion_factors[category][unit]


unit_options = list(conversion_factors[category].keys())
unit = st.selectbox("Select Conversion", unit_options)


col1, col2 = st.columns(2)
with col1:
    value = st.number_input("Enter value to convert", min_value=0.0, step=0.01)
with col2:
    convert_btn = st.button("Convert")
    reset_btn = st.button("Reset")

# Conversion Logic
if convert_btn:
    if value < 0 and category == "Time":
        st.error("Time cannot be negative!")
    else:
        result = convert_units(category, value, unit)
        st.success(f"The result is {result:.2f} {result_units[unit]}")

if reset_btn:
    st.session_state.value = 0
    st.rerun()

