import streamlit as st
import pandas as pd
import plotly.express as px
import random

# Page config for modern high-density dark dashboard layout
st.set_page_config(page_title="Internet Scavenger", layout="wide", initial_sidebar_state="collapsed")

# Premium Minimal Dark UI Stylesheets
st.markdown('''
<style>
    /* Global Page Body and Theme Overrides */
    .stApp {
        background-color: #07090e;
        color: #e2e8f0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        background-image: 
            radial-gradient(at 0% 0%, rgba(31, 38, 135, 0.12) 0px, transparent 45%),
            radial-gradient(at 100% 100%, rgba(127, 0, 255, 0.08) 0px, transparent 45%);
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff;
        font-weight: 700;
        letter-spacing: -0.02em;
    }

    /* Premium Translucent Glassmorphism Cards */
    .premium-card {
        background: rgba(13, 18, 28, 0.75);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        margin-bottom: 20px;
    }
    
    .card-title {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: #94a3b8;
        font-weight: 600;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    /* Micro-Sized Item Tile Grid Matrix Styling (Half Size) */
    .tile-container {
        background: rgba(255, 255, 255, 0.015);
        border: 1px solid rgba(255, 255, 255, 0.04);
        border-radius: 6px;
        padding: 6px;
        text-align: center;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .tile-container:hover {
        transform: translateY(-2px);
        border-color: #00f2fe;
        box-shadow: 0 0 10px rgba(0, 242, 254, 0.15);
    }
    
    /* Highly Compact Product Placement underneath picture */
    .tile-product-title {
        font-size: 0.7rem;
        font-weight: 600;
        color: #ffffff;
        margin-top: 4px;
        margin-bottom: 2px;
        line-height: 1.2;
        height: 2.4em;
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
    }
    
    /* Source Platform Badges */
    .platform-tag {
        font-size: 0.6rem;
        font-weight: 700;
        padding: 0px 4px;
        border-radius: 3px;
        display: inline-block;
        margin-bottom: 4px;
        text-transform: uppercase;
        letter-spacing: 0.02em;
    }
    .tag-amazon { background-color: rgba(255, 153, 0, 0.12); color: #ff9900; border: 1px solid rgba(255, 153, 0, 0.25); }
    .tag-etsy { background-color: rgba(241, 100, 30, 0.12); color: #f1641e; border: 1px solid rgba(241, 100, 30, 0.25); }
    .tag-tiktok { background-color: rgba(0, 242, 254, 0.12); color: #00f2fe; border: 1px solid rgba(0, 242, 254, 0.25); }
    .tag-aliexpress { background-color: rgba(230, 0, 51, 0.12); color: #e60033; border: 1px solid rgba(230, 0, 51, 0.25); }

    /* Downscaled Tile Image Configuration */
    .tile-img {
        width: 100%;
        height: 60px;
        object-fit: cover;
        border-radius: 4px;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }

    /* Clean Native Click Anchors */
    a.clean-anchor {
        text-decoration: none;
        color: inherit;
    }
    a.clean-anchor:hover {
        color: #00f2fe !important;
    }

    /* Micro Action Triggers */
    .reduced-btn-wrapper .stButton>button {
        background: rgba(255, 255, 255, 0.04) !important;
        color: #94a3b8 !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 3px !important;
        padding: 0px 4px !important;
        font-size: 0.65rem !important;
        min-height: unset !important;
        height: 18px !important;
        width: 90% !important;
        margin: 0 auto !important;
        display: block !important;
        line-height: 1.1 !important;
        transition: all 0.2s ease;
    }
    .reduced-btn-wrapper .stButton>button:hover {
        background: #00f2fe !important;
        color: #07090e !important;
        border-color: #00f2fe !important;
        box-shadow: 0 0 6px rgba(0, 242, 254, 0.3) !important;
    }

    /* Infinite Scrolling Marquee Styles */
    .marquee-wrapper {
        width: 100%;
        overflow: hidden;
        white-space: nowrap;
        box-sizing: border-box;
        mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent);
        -webkit-mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent);
    }
    .marquee-content {
        display: inline-block;
        animation: marquee 25s linear infinite;
        font-family: monospace;
        font-size: 0.75rem;
        color: #00f2fe;
    }
    .marquee-content span {
        margin-right: 30px;
    }
    @keyframes marquee {
        0%   { transform: translate(0, 0); }
        100% { transform: translate(-50%, 0); }
    }
</style>
''', unsafe_allow_html=True)

# Generate Mock Dataset with live retail single-click anchors and authentic imagery
@st.cache_data
def load_scavenger_intelligence():
    items = [
        {"id": 1, "name": "Minimalist Mechanical Keyboard", "source": "Amazon", "price": "$119.00", "url": "https://www.amazon.com/s?k=Mechanical+Keyboard", "img": "https://images.unsplash.com/photo-1618384887929-16ec33fab9ef?w=500&auto=format&fit=crop&q=80"},
        {"id": 2, "name": "Matte Black Travel Tumbler", "source": "Amazon", "price": "$38.00", "url": "https://www.amazon.com/s?k=Travel+Tumbler", "img": "https://images.unsplash.com/photo-1577937927133-66ef06acdf18?w=500&auto=format&fit=crop&q=80"},
        {"id": 3, "name": "Ergonomic Office Chair", "source": "Amazon", "price": "$289.50", "url": "https://www.amazon.com/s?k=Ergonomic+Office+Chair", "img": "https://images.unsplash.com/photo-1505797149-43b0069ec26b?w=500&auto=format&fit=crop&q=80"},
        {"id": 4, "name": "Leather Desk Mat (Large)", "source": "Etsy", "price": "$45.00", "url": "https://www.etsy.com/search?q=Leather+Desk+Mat", "img": "https://images.unsplash.com/photo-1632292224971-0d45778bd364?w=500&auto=format&fit=crop&q=80"},
        {"id": 5, "name": "Concrete Succulent Planter", "source": "Etsy", "price": "$2
