import streamlit as st

st.title("⚖️ BMI Calculator")

unit = st.radio("Choose Unit System", ["Metric (kg, m)", "Imperial (lb, inches)"])

if unit == "Metric (kg, m)":
    weight = st.number_input("Enter your weight (kg):", min_value=1.0)
    height = st.number_input("Enter your height (m):", min_value=0.1)
    if height and weight:
        bmi = weight / (height ** 2)
else:
    weight = st.number_input("Enter your weight (lb):", min_value=1.0)
    height = st.number_input("Enter your height (inches):", min_value=1.0)
    if height and weight:
        bmi = (weight / (height ** 2)) * 703

if st.button("Calculate BMI"):
    if height and weight:
        st.success(f"Your BMI is: {bmi:.2f}")
        if bmi < 18.5:
            st.warning("You are Underweight.")
        elif 18.5 <= bmi < 24.9:
            st.info("You are Normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are Overweight.")
        else:
            st.error("You are Obese.")
            
# Footer
st.markdown("---")
st.write("Made by Hamza Syed~")