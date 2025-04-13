import streamlit as st

# Page Configuration
st.set_page_config(page_title="Unit Converter", page_icon="🔁", layout="centered")

# Custom Styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f4f4f4;
    }
    .block-container {
        padding: 2rem 2rem 2rem 2rem;
        background-color: white;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🔁 Simple Unit Converter")
st.markdown("Convert between common units of **length** and **weight** easily.")

# Conversion logic
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000,
    }
    key = f"{unit_from}_{unit_to}"
    if key in conversions:
        factor = conversions[key]
        return value * factor
    elif unit_from == unit_to:
        return value
    else:
        return "🚫 Conversion not supported!"

# Input section
st.subheader("Enter your values:")
col1, col2 = st.columns(2)

with col1:
    unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"])

with col2:
    unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

value = st.number_input("Enter the value to convert:", min_value=0.0, step=0.5)

# Convert button
if st.button("Convert Now"):
    result = convert_units(value, unit_from, unit_to)
    st.success(f"✅ **Converted Value:** {result}")
