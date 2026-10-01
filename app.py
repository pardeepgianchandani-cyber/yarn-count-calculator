import streamlit as st

# ---------------------------------------------------------
# YARN COUNT CALCULATOR
# For 2nd Year Textile Engineering Students
# ---------------------------------------------------------

st.set_page_config(
    page_title="Yarn Count Calculator",
    page_icon="🧵",
    layout="centered"
)

# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.title("🧵 Yarn Count Calculator")
st.write(
    "Calculate yarn count using Length and Weight parameters."
)

st.info(
    "Select a yarn count system, enter the length and weight, "
    "and click **Calculate Count**."
)

# ---------------------------------------------------------
# Count System Selection
# ---------------------------------------------------------

system = st.selectbox(
    "Select Yarn Count System",
    [
        "English Cotton Count (Ne)",
        "Metric Count (Nm)",
        "Tex",
        "Denier"
    ]
)

st.divider()

# ---------------------------------------------------------
# Explanation of Systems
# ---------------------------------------------------------

if system == "English Cotton Count (Ne)":

    st.subheader("English Cotton Count (Ne)")

    st.caption(
        "Indirect count system: higher count means finer yarn."
    )

    length_unit = st.selectbox(
        "Length Unit",
        ["yards", "meters"],
        key="ne_length_unit"
    )

    weight_unit = st.selectbox(
        "Weight Unit",
        ["grains", "grams"],
        key="ne_weight_unit"
    )

    length = st.number_input(
        f"Enter Length ({length_unit})",
        min_value=0.000001,
        value=840.0,
        step=1.0
    )

    weight = st.number_input(
        f"Enter Weight ({weight_unit})",
        min_value=0.000001,
        value=1.0,
        step=0.1
    )

    st.markdown(
        "**Formula:**  Ne = Length (yards) ÷ [840 × Weight (lb)]"
    )

    if st.button("Calculate Count", type="primary"):

        # Convert length to yards
        if length_unit == "meters":
            length_yards = length * 1.0936133
        else:
            length_yards = length

        # Convert weight to pounds
        if weight_unit == "grams":
            weight_lb = weight * 0.00220462262
        else:
            # grains to pounds
            weight_lb = weight / 7000

        count = length_yards / (840 * weight_lb)

        st.success(f"Yarn Count = **{count:.2f} Ne**")

        st.write(
            "This is an **indirect count system**: "
            "a higher Ne indicates a finer yarn."
        )


elif system == "Metric Count (Nm)":

    st.subheader("Metric Count (Nm)")

    st.caption(
        "Indirect count system: higher count means finer yarn."
    )

    length_unit = st.selectbox(
        "Length Unit",
        ["meters", "yards"],
        key="nm_length_unit"
    )

    weight_unit = st.selectbox(
        "Weight Unit",
        ["kilograms", "grams"],
        key="nm_weight_unit"
    )

    length = st.number_input(
        f"Enter Length ({length_unit})",
        min_value=0.000001,
        value=1000.0,
        step=1.0
    )

    weight = st.number_input(
        f"Enter Weight ({weight_unit})",
        min_value=0.000001,
        value=1.0,
        step=0.1
    )

    st.markdown(
        "**Formula:**  Nm = Length (meters) ÷ Weight (kg)"
    )

    if st.button("Calculate Count", type="primary"):

        # Convert length to meters
        if length_unit == "yards":
            length_m = length * 0.9144
        else:
            length_m = length

        # Convert weight to kg
        if weight_unit == "grams":
            weight_kg = weight / 1000
        else:
            weight_kg = weight

        count = length_m / weight_kg

        st.success(f"Yarn Count = **{count:.2f} Nm**")

        st.write(
            "This is an **indirect count system**: "
            "a higher Nm indicates a finer yarn."
        )


elif system == "Tex":

    st.subheader("Tex")

    st.caption(
        "Direct count system: higher count means coarser/heavier yarn."
    )

    length_unit = st.selectbox(
        "Length Unit",
        ["kilometers", "meters"],
        key="tex_length_unit"
    )

    weight_unit = st.selectbox(
        "Weight Unit",
        ["grams", "kilograms"],
        key="tex_weight_unit"
    )

    length = st.number_input(
        f"Enter Length ({length_unit})",
        min_value=0.000001,
        value=1.0,
        step=0.1
    )

    weight = st.number_input(
        f"Enter Weight ({weight_unit})",
        min_value=0.000001,
        value=1.0,
        step=0.1
    )

    st.markdown(
        "**Formula:**  Tex = Weight (grams) ÷ Length (km)"
    )

    if st.button("Calculate Count", type="primary"):

        # Convert length to km
        if length_unit == "meters":
            length_km = length / 1000
        else:
            length_km = length

        # Convert weight to grams
        if weight_unit == "kilograms":
            weight_g = weight * 1000
        else:
            weight_g = weight

        count = weight_g / length_km

        st.success(f"Yarn Count = **{count:.2f} Tex**")

        st.write(
            "This is a **direct count system**: "
            "a higher Tex indicates a coarser/heavier yarn."
        )


elif system == "Denier":

    st.subheader("Denier")

    st.caption(
        "Direct count system: higher count means coarser/heavier yarn."
    )

    length_unit = st.selectbox(
        "Length Unit",
        ["9000 meters", "meters", "kilometers"],
        key="denier_length_unit"
    )

    weight_unit = st.selectbox(
        "Weight Unit",
        ["grams", "kilograms"],
        key="denier_weight_unit"
    )

    length = st.number_input(
        f"Enter Length ({length_unit})",
        min_value=0.000001,
        value=9000.0,
        step=1.0
    )

    weight = st.number_input(
        f"Enter Weight ({weight_unit})",
        min_value=0.000001,
        value=1.0,
        step=0.1
    )

    st.markdown(
        "**Formula:**  Denier = Weight (grams) × 9000 ÷ Length (meters)"
    )

    if st.button("Calculate Count", type="primary"):

        # Convert length to meters
        if length_unit == "kilometers":
            length_m = length * 1000
        else:
            length_m = length

        # Convert weight to grams
        if weight_unit == "kilograms":
            weight_g = weight * 1000
        else:
            weight_g = weight

        count = (weight_g * 9000) / length_m

        st.success(f"Yarn Count = **{count:.2f} Denier**")

        st.write(
            "This is a **direct count system**: "
            "a higher Denier indicates a coarser/heavier yarn."
        )

# ---------------------------------------------------------
# Educational Reference
# ---------------------------------------------------------

st.divider()

st.subheader("Quick Reference")

st.markdown("""
| Count System | Type | Basic Relationship |
|---|---|---|
| **Ne** | Indirect | Length ÷ Weight |
| **Nm** | Indirect | Length ÷ Weight |
| **Tex** | Direct | Weight ÷ Length |
| **Denier** | Direct | Weight ÷ Length |
""")

st.caption(
    "Developed as an educational tool for Textile Engineering students."
)
