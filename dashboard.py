import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Title of Dashboard
st.title("Legion AI Dashboard 🚀")

# Function to fetch financial data
def fetch_financial_data():
    return {"Stock Market": "Up 1.2%", "Crypto": "BTC +3.5%", "Private Equity": "Capital inflows increasing"}

# Function to fetch AI Tech News
def fetch_aitech_news():
    return ["OpenAI announces GPT-5", "Quantum computing startup raises $500M", "Tesla AI event reveals new robotics tech"]

# Function to fetch Geopolitical Data
def fetch_geopolitical_data():
    return {"US-China Relations": "Tense", "EU AI Regulation": "Passed", "Middle East Oil Supply": "Stable"}

# Fetching data
financial_data = fetch_financial_data()
aitech_news = fetch_aitech_news()
geopolitical_data = fetch_geopolitical_data()

# Displaying data
st.subheader("📊 Financial Market Trends")
st.json(financial_data)

st.subheader("🤖 AI & Tech Developments")
for news in aitech_news:
    st.write(f"- {news}")

st.subheader("🌍 Geopolitical Risk Alerts")
st.json(geopolitical_data)
