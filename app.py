import streamlit as st

st.set_page_config(page_title="Beautiful Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Simple & Beautiful Calculator")

# Input fields
num1 = st.number_input("Enter first number", format="%.2f")
num2 = st.number_input("Enter second number", format="%.2f")

operation = st.selectbox(
    "Select Operation",
    ("Add ➕", "Subtract ➖", "Multiply ✖️", "Divide ➗")
)

if st.button("Calculate"):
    if operation == "Add ➕":
        result = num1 + num2
        st.success(f"✅ Result: {result:.2f}")

    elif operation == "Subtract ➖":
        result = num1 - num2
        st.success(f"✅ Result: {result:.2f}")

    elif operation == "Multiply ✖️":
        result = num1 * num2
        st.success(f"✅ Result: {result:.2f}")

    elif operation == "Divide ➗":
        if num2 != 0:
            result = num1 / num2
            st.success(f"✅ Result: {result:.2f}")
        else:
            st.error("❌ Cannot divide by zero!")

