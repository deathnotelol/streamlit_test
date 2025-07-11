import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Advanced Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Advanced Beautiful Calculator")

calculator_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <style>
    .calculator {
      width: 300px;
      background: #222;
      padding: 20px;
      border-radius: 12px;
      box-shadow: 0 8px 30px rgba(0,0,0,0.2);
      margin: auto;
    }
    .display {
      width: 100%;
      height: 60px;
      background: #000;
      color: #0f0;
      font-size: 2em;
      text-align: right;
      padding: 10px;
      border-radius: 8px;
      margin-bottom: 10px;
      box-sizing: border-box;
    }
    .keys {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      grid-gap: 10px;
    }
    .keys button {
      height: 60px;
      font-size: 1.5em;
      border: none;
      border-radius: 8px;
      background: #333;
      color: #fff;
      cursor: pointer;
      transition: 0.2s;
    }
    .keys button:hover {
      background: #444;
    }
    .keys button:active {
      background: #555;
    }
    .operator {
      background: #ff9500;
    }
    .operator:hover {
      background: #e58c00;
    }
  </style>
</head>
<body>
  <div class="calculator">
    <div id="display" class="display">0</div>
    <div class="keys">
      <button onclick="press('7')">7</button>
      <button onclick="press('8')">8</button>
      <button onclick="press('9')">9</button>
      <button class="operator" onclick="press('/')">/</button>
      <button onclick="press('4')">4</button>
      <button onclick="press('5')">5</button>
      <button onclick="press('6')">6</button>
      <button class="operator" onclick="press('*')">*</button>
      <button onclick="press('1')">1</button>
      <button onclick="press('2')">2</button>
      <button onclick="press('3')">3</button>
      <button class="operator" onclick="press('-')">-</button>
      <button onclick="press('0')">0</button>
      <button onclick="press('.')">.</button>
      <button onclick="clearDisplay()">C</button>
      <button class="operator" onclick="press('+')">+</button>
      <button class="operator" style="grid-column: span 4;" onclick="calculate()">=</button>
    </div>
  </div>

  <script>
    let display = document.getElementById('display');

    function press(num) {
      if (display.innerText === "0" || display.innerText === "Error") {
        display.innerText = num;
      } else {
        display.innerText += num;
      }
    }

    function clearDisplay() {
      display.innerText = "0";
    }

    function calculate() {
      try {
        display.innerText = eval(display.innerText);
      } catch {
        display.innerText = "Error";
      }
    }
  </script>
</body>
</html>
"""

# Embed the HTML
components.html(calculator_html, height=500)
