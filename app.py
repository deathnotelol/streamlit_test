import streamlit as st
import streamlit.components.v1 as components

# --- CONFIG ---
st.set_page_config(page_title="My Multi-Page App", page_icon="🚀", layout="centered")

# --- INIT SESSION ---
if "page" not in st.session_state:
    st.session_state.page = "Home"

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("📌 Navigation")
if st.sidebar.button("🏠 Home"):
    st.session_state.page = "Home"
if st.sidebar.button("🧮 Calculator"):
    st.session_state.page = "Calculator"
if st.sidebar.button("✅ Todo List"):
    st.session_state.page = "Todo"

# --- PAGE ROUTER ---
if st.session_state.page == "Home":
    st.title("🏠 Home Page")
    st.write("Welcome to your multi-page Streamlit app! Use the sidebar to switch between pages.")

elif st.session_state.page == "Calculator":
    st.title("🧮 Advanced Calculator")
    calculator_html = """
    <div class="calculator" style="width: 300px; background: #222; padding: 20px; border-radius: 12px; margin: auto;">
      <div id="display" style="width:100%;height:60px;background:#000;color:#0f0;font-size:2em;text-align:right;padding:10px;border-radius:8px;margin-bottom:10px;box-sizing:border-box;">0</div>
      <div class="keys" style="display:grid;grid-template-columns:repeat(4,1fr);grid-gap:10px;">
        <button onclick="press('7')">7</button>
        <button onclick="press('8')">8</button>
        <button onclick="press('9')">9</button>
        <button style='background:#ff9500;' onclick="press('/')">/</button>
        <button onclick="press('4')">4</button>
        <button onclick="press('5')">5</button>
        <button onclick="press('6')">6</button>
        <button style='background:#ff9500;' onclick="press('*')">*</button>
        <button onclick="press('1')">1</button>
        <button onclick="press('2')">2</button>
        <button onclick="press('3')">3</button>
        <button style='background:#ff9500;' onclick="press('-')">-</button>
        <button onclick="press('0')">0</button>
        <button onclick="press('.')">.</button>
        <button onclick="clearDisplay()">C</button>
        <button style='background:#ff9500;' onclick="press('+')">+</button>
        <button style='grid-column:span 4;background:#ff9500;' onclick="calculate()">=</button>
      </div>
      <script>
        let display = document.getElementById('display');
        function press(num) {
          if (display.innerText === "0" || display.innerText === "Error") { display.innerText = num; }
          else { display.innerText += num; }
        }
        function clearDisplay() { display.innerText = "0"; }
        function calculate() {
          try { display.innerText = eval(display.innerText); }
          catch { display.innerText = "Error"; }
        }
      </script>
    </div>
    """
    components.html(calculator_html, height=500)

elif st.session_state.page == "Todo":
    st.title("✅ Todo List")

    # Initialize todo list
    if "todos" not in st.session_state:
        st.session_state.todos = []

    # Add todo
    new_todo = st.text_input("Add new task:")
    if st.button("Add Task"):
        if new_todo:
            st.session_state.todos.append(new_todo)

    # Show todos
    st.write("### Your Tasks:")
    for i, todo in enumerate(st.session_state.todos):
        if st.checkbox(todo, key=f"todo_{i}"):
            st.session_state.todos.pop(i)
            st.experimental_rerun()
