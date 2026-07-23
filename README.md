# 🛰️ Internet Scavenger Dashboard

A high-density, real-time research dashboard built with Streamlit, Plotly, and HTML5 Canvas. **Internet Scavenger** aggregates and visualizes micro-trend retail intelligence across major e-commerce platforms like Amazon, Etsy, TikTok Shop, and AliExpress.

---

## 🚀 Live Demo

[► View Live Dashboard on Streamlit Community Cloud](https://share.streamlit.io/)

---

## ✨ Features

- **Spotlight Item Node:** Focus view on top-performing items with direct store links and telemetry indicators.
- **Interactive Analytics:** 7-day cumulative sales trends and 24-hour velocity metrics powered by Plotly.
- **Recon Orbit Canvas:** Custom HTML5/JavaScript animated planetary telemetry module.
- **Extended Micro-Trend Feed:** Compact, real-time scrollable matrix tracking micro-trends outside core positions.
- **Retail Corridor Evaluation Matrix:** Responsive grid system for secondary matrix items with responsive hover interactions.

---

## ⚡ Performance & Cloud Optimizations

- **Vectorized Data Pipeline:** Data loading powered by `numpy` vectorized random generation for instant cold starts.
- **Streamlit Reactive Binding:** Zero-rerun state management via native Streamlit session state keys.
- **Cached Dataset Generation:** Configured with `@st.cache_data(ttl=10800)` (3-hour TTL) to keep RAM usage within Community Cloud limits.

---

## 🛠️ Local Development Quickstart

### Prerequisites
Ensure you have **Python 3.9+** installed.

```bash
# 1. Clone Repository
git clone [https://github.com/your-username/internet-scavenger.git](https://github.com/your-username/internet-scavenger.git)
cd internet-scavenger

# 2. Create Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Run Locally
streamlit run app.py
