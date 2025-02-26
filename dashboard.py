import streamlit as st
import pandas as pd
import requests
import time
from bs4 import BeautifulSoup

# Custom CSS for Styling
st.markdown("""
    <style>
        .main {
            background-color: #0f0f0f;
            color: #ffffff;
        }
        .stButton>button {
            background-color: #ff4b4b;
            color: white;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
        }
        .stSidebar {
            background-color: #1c1c1c;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar for Navigation
st.sidebar.title("🔍 Legion AI Dashboard")
st.sidebar.subheader("⚡ Real-Time Intelligence")
page = st.sidebar.radio("Select a Category", ["Financial Markets", "AI & Tech", "Geopolitics"])

# Title & Refresh Button
st.title("🚀 Legion AI Command Center")
if st.button("🔄 Refresh Data"):
    st.experimental_rerun()

# Functions to Fetch Real-Time Data
def fetch_financial_data():
    return {"Stock Market": "Up 1.8%", "Crypto": "BTC +2.7%", "Private Equity": "Massive Capital Inflows"}

def fetch_aitech_news():
    return ["🚀 OpenAI drops GPT-5", "🔬 Quantum AI investment skyrockets", "🤖 Tesla unveils AGI research lab"]

def fetch_geopolitical_data():
    return {"🛢️ Oil Prices": "Rising due to conflict", "📉 US-China Relations": "Trade War Intensifies", "💰 EU AI Regulation": "Stricter Policies Passed"}

# Fetch Data
financial_data = fetch_financial_data()
aitech_news = fetch_aitech_news()
geopolitical_data = fetch_geopolitical_data()

# Display Data Based on Selection
if page == "Financial Markets":
    st.subheader("📊 Financial Market Trends")
    st.json(financial_data)
elif page == "AI & Tech":
    st.subheader("🤖 AI & Tech Developments")
    for news in aitech_news:
        st.write(f"🔹 {news}")
elif page == "Geopolitics":
    st.subheader("🌍 Geopolitical Risk Alerts")
    st.json(geopolitical_data)

# Live Data Update (Auto Refresh Every 30s)
st.sidebar.write("⏳ Updating every 30 seconds...")
time.sleep(30)
st.experimental_rerun()

