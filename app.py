import streamlit as st
import random
import time
from datetime import datetime, timedelta

# --- DIABLO IV ADVANCED INTERFACE STYLING ---
st.set_page_config(layout="wide", page_title="The Horadric Archive", page_icon="💀")

st.markdown("""
    <style>
    /* Dark Sanctuary Core Theme */
    .stApp {
        background-color: #0b0705;
        color: #d1c4b2;
        font-family: 'Cinzel', 'Georgia', serif;
    }
    
    /* Gothic Titles with Crimson Under-Glow */
    h1, h2, h3, h4 {
        color: #b39256 !important;
        text-shadow: 2px 2px 4px #000000, 0 0 10px #800000;
        font-family: 'Cinzel', 'Georgia', serif;
        letter-spacing: 1px;
    }
    
    /* Central Focus Item Frame (Diablo Legendary Border Accent) */
    .legendary-vault-frame {
        background: linear-gradient(180deg, #17100b 0%, #080504 100%);
        border: 2px dashed #b39256;
        box-shadow: 0px 0px 25px rgba(184, 134, 11, 0.4);
        padding: 25px;
        border-radius: 4px;
        text-align: center;
        margin-bottom: 25px;
    }
    
    /* Diablo IV Style Inventory Item Slot Tile */
    .inventory-slot-box {
        background: linear-gradient(135deg, #140e0a 0%, #0b0705 100%);
        border: 2px solid #36281c;
        padding: 15px;
        border-radius: 3px;
        margin-bottom: 15px;
        box-shadow: inset 0 0 15px #000000;
        transition: all 0.2s ease-in-out;
    }
    .inventory-slot-box:hover {
        border-color: #9e2216;
        box-shadow: 0 0 12px #9e2216;
    }
    
    /* Core Content Action Buttons styled as Runes */
    .stButton>button {
        background-color: #1c130c;
        color: #b39256;
        border: 1px solid #543f2b;
        font-weight: bold;
        width: 100%;
        border-radius: 2px;
        transition: all 0.2s;
    }
    .stButton>button:hover {
        background-color: #8a0000;
        color: #ffffff;
        border-color: #ff0000;
        box-shadow: 0px 0px 8px #8a0000;
    }
    
    /* Real Product Hyperlinks */
    a {
        color: #e63929 !important;
        text-decoration: none;
        font-weight: bold;
    }
    a:hover {
        color: #ff857a !important;
        text-shadow: 0 0 6px #ff0000;
    }
    </style>
""", unsafe_allow_html=True)


# --- LIVE SELLING MATRIX GENERATOR ---
def fetch_sanctuary_market_feed():
    # Strict dictionary pairing verified selling items, matching URLs, and clean authentic image links
    products_pool = [
        {
            "title": "Owala FreeSip Insulated Stainless Steel Triple-Layer Water Bottle", 
            "source": "Amazon", 
            "url": "https://www.amazon.com/s?k=Owala+FreeSip+Water+Bottle",
            "img": "
