# 💀 The Horadric Archive - Diablo IV Style E-Commerce Tracker

An automated, high-fidelity e-commerce tracking dashboard modeled directly after the dark gothic character stash user interface of Diablo IV. This application provides a live snapshot of high-volume items across Amazon, Etsy, and TikTok Shop using an autonomous 3-hour Necromancer scrying ritual engine.

## 🔮 Active Mechanics
* **The Horadric Inventory Grid:** A dual-column layout showcasing the top 15 selling items across online marketplaces. Every single slot displays an authentic product picture mapping back to its destination link.
* **The Crown Artifact Focus:** A centralized inspection frame displaying the chosen item alongside its core 7-day transaction metrics. 
* **Temporal Velocity Ledger:** Interactive 7-day sales bar charts. Clicking an individual day instantly parses data down into an hourly transaction velocity run-rate.
* **Necromancer Scrying Ritual:** A visually active loading sequence that triggers automatically every 3 hours to recalculate and refresh live product trends.
* **The Outer Circle:** An image-free tracking list displaying the top 10 rising shadows (trending items) before they pierce the primary top 15 grid slots.

---

## 📜 Repository Structure
* `app.py` - Core application framework housing the Diablo IV global layout style rules and live data loops.
* `requirements.txt` - Minimalist dependency list containing only the core framework engine.
* `README.md` - Documentation ledger.

---

## 🛠️ Deployment Instructions

To deploy this dashboard inside the **Streamlit Community Cloud**:
1. Commit your `app.py` and `requirements.txt` files into a GitHub repository.
2. Navigate to the [Streamlit Share Dashboard](https://share.streamlit.io/) and authenticate using your GitHub account.
3. Select **New App**, locate your specific repository, and point the main file path directly to `app.py`.
4. Click **Deploy** and allow the Horadric container environment to initialize.
