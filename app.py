import streamlit as st

st.set_page_config(page_title="Styled Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Beautiful Calculator")

# Initialize session state
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Styling with CSS
st.markdown("""
    <style>
    .calculator {
        display: grid;
        grid-template-columns: repeat(4, 80px);
        grid-gap: 10px;
        justify-content: center;
    }
    .calculator button {
        height: 60px;
        font-size: 20px;
        border: none;
        background: #f1f1f1;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.2s;
    }
    .calculator button:hover {
        background: #ddd;
    }
    .calculator button:active {
        background: #ccc;
    }
    .result {
        text-align: right;
        font-size: 32px;
        padding: 10px;
        border: 2px solid #ccc;
        border-radius: 8px;
        margin-bottom: 20px;
        background: #f9f9f9;
    }
    </style>
""", unsafe_allow_html=True)

# Display the current expression
st.markdown(f'<div class="result">{st.session_state.expression}</div>', unsafe_allow_html=True)

# Handle button click
def click(item):
    st.session_state.expression += str(item)

def clear():
    st.session_state.expression = ""

def calculate():
    try:
        st.session_state.expression = str(eval(st.session_state.expression))
    except:
        st.session_state.expression = "Error"

# Layout buttons in HTML
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "C", "+"),
]

# Render buttons
st.markdown('<div class="calculator">', unsafe_allow_html=True)
for row in buttons:
    for btn in row:
        if btn == "C":
            st.button(btn, on_click=clear, key=btn)
        else:
            st.button(btn, on_click=click, args=(btn,), key=btn)
# Equals button (spanning full row)
st.button("=", on_click=calculate, key="=")
st.markdown('</div>', unsafe_allow_html=True)
