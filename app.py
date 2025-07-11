import streamlit as st

st.set_page_config(page_title="Calculator with Buttons", page_icon="🧮")

st.title("🧮 Clickable Button Calculator")

# Initialize session state
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Function to handle button click
def button_click(item):
    st.session_state.expression += str(item)

def clear():
    st.session_state.expression = ""

def calculate():
    try:
        result = eval(st.session_state.expression)
        st.session_state.expression = str(result)
    except:
        st.session_state.expression = "Error"

# Display current expression
st.text_input("Expression", st.session_state.expression, key="input", disabled=True)

# Layout for buttons
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("7", on_click=button_click, args=("7",))
    st.button("4", on_click=button_click, args=("4",))
    st.button("1", on_click=button_click, args=("1",))
    st.button("0", on_click=button_click, args=("0",))

with col2:
    st.button("8", on_click=button_click, args=("8",))
    st.button("5", on_click=button_click, args=("5",))
    st.button("2", on_click=button_click, args=("2",))
    st.button(".", on_click=button_click, args=(".",))

with col3:
    st.button("9", on_click=button_click, args=("9",))
    st.button("6", on_click=button_click, args=("6",))
    st.button("3", on_click=button_click, args=("3",))
    st.button("C", on_click=clear)

with col4:
    st.button("+", on_click=button_click, args=("+",))
    st.button("-", on_click=button_click, args=("-",))
    st.button("*", on_click=button_click, args=("*",))
    st.button("/", on_click=button_click, args=("/",))

# Equals button
st.button("=", on_click=calculate)
