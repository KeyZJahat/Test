import streamlit as st
import streamlit.components.v1 as components

# Buka file index.html anda
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Paparkan web HTML/JS/CSS anda
components.html(html_code, height=800, scrolling=True)
