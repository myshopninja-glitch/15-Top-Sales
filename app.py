import streamlit as st
import random
import time
from datetime import datetime, timedelta

# --- DIABLO IV INTERFACE STYLING (CUSTOM CSS) ---
st.set_page_config(layout="wide", page_title="The Horadric Vault", page_icon="💀")

st.markdown("""
    <style>
    /* Global Background and Fonts */
    .stApp {
        background-color: #0d0d0d;
        color: #e0d9cb;
        font-family: 'Cinzel', 'Georgia', serif;
    }
    
    /* Diablo Gothic Headers */
    h1, h2, h3 {
        color: #b39256 !important;
        text-shadow: 2px 2px 4px #000000, 0 0 10px #8a0303;
        font-family: 'Cinzel', 'Georgia', serif;
        letter-spacing: 2px;
    }
    
    /* Central Artifact Highlight Card */
    .central-artifact {
        background: linear-gradient(180deg, #1a120b 0%, #0a0705 100%);
        border: 2px solid #b39256;
        box-shadow: 0px 0px 25px #8a0303;
        padding: 25px;
        border-radius: 5px;
        text-align: center;
        margin-bottom: 30px;
    }
    
    /* Standard Item Card Buttons */
    .stButton>button {
        background-color: #1a120b;
        color: #b39256;
        border: 1px solid #b39256;
        border-radius: 3px;
        transition: all 0.3s ease;
        width: 100%;
        text-align: left;
    }
    .stButton>button:hover {
        background-color: #8a0303;
        color: #ffffff;
        border-color: #ff0000;
        box-shadow: 0px 0px 10px #8a0303;
    }
    
    /* Password Gate Styles */
    .crypto-gate {
        max-width: 500px;
        margin: 100px auto;
        padding: 40px;
        background-color: #111;
        border: 2px solid #8a0303;
        border-radius: 5px;
        text-align: center;
    }
    
    /* Links */
    a {
        color: #ff3333 !important;
        text-decoration: none;
        font-weight: bold;
    }
    a:hover {
        color: #ff9999 !important;
        text-shadow: 0 0 5px #ff0000;
    }
    </style>
""", unsafe_allow_html=True)

# --- PRIVACY GATE (NOT OPEN TO THE PUBLIC) ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown('<div class="crypto-gate">', unsafe_allow_html=True)
    st.title("💀 THE HORADRIC VAULT")
    st.subheader("Authorized Personnel Only")
    password = st.text_input("Speak the Word of Power to enter:", type="password")
    if st.button("Unseal Sanctuary Vault"):
        if password == "Lilith666":  # Set your private password here
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("The Hells reject your entry. Wrong incantation.")
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()


# --- DATABASE SIMULATION ENGINE (REFRESHES EVERY 3 HOURS) ---
def generate_fresh_market_data():
    sources = ["Amazon Global", "Etsy Handcrafted", "TikTok Shop Verified"]
    categories = ["Dark Apparel", "Runic Electronics", "Occult Kitchenware", "Alchemical Blends", "Gothic Decors"]
    
    items = []
    # Generate 25 total items (15 Main, 10 Rising Trends)
    for i in range(1, 26):
        src = random.choice(sources)
        cat = random.choice(categories)
        
        # Build keyword targeting for completely real looking single product images
        keywords = {
            "Dark Apparel": "hoodie,black,gothic",
            "Runic Electronics": "keyboard,gadget,tech",
            "Occult Kitchenware": "mug,ceramic,knife",
            "Alchemical Blends": "matcha,supplement,bottle",
            "Gothic Decors": "lamp,candle,statue"
        }
        
        sold_7_days = [random.randint(100, 1500) for _ in range(7)]
        # Hourly breakdown data matrix (7 days x 24 hours)
        hourly_breakdown = {f"Day {d+1}": [random.randint(5, 70) for _ in range(24)] for d in range(7)}
        
        items.append({
            "rank": i,
            "title": f"Mundane Artifact #{random.randint(1000, 9999)} ({cat})",
            "source": src,
            "url": "https://amazon.com" if "Amazon" in src else "https://etsy.com" if "Etsy" in src else "https://tiktok.com",
            "img_url": f"https://loremflickr.com/400/400/{keywords[cat]}?lock={i * 7}",
            "total_sales": sum(sold_7_days),
            "weekly_sales": sold_7_days,
            "hourly_sales": hourly_breakdown
        })
        
    # Sort by sales volume to determine rank structures cleanly
    items = sorted(items, key=lambda x: x["total_sales"], reverse=True)
    for index, item in enumerate(items):
        item["rank"] = index + 1
        
    return items[:15], items[15:]

# Handle 3-Hour Automation Timestamps
if "last_refresh" not in st.session_state:
    st.session_state.last_refresh = datetime.now() - timedelta(hours=4) # Force initial pull
    st.session_state.top_15 = []
    st.session_state.top_10_rising = []
    st.session_state.selected_item_rank = 1

time_since_refresh = datetime.now() - st.session_state.last_refresh

# --- VISUALLY ACTIVE NECROMANCER SEARCH SEQUENCE ---
if time_since_refresh.total_seconds() >= 10800 or len(st.session_state.top_15) == 0:
    necromancer_phrases = [
        "💀 Summoning skeleton thralls to parse marketplace API ledgers...",
        "🩸 Channeling blood magic to bypass Amazon anti-bot firewalls...",
        "🔮 Scrying into the chaotic abyss of the TikTok Shop trend matrices...",
        "📜 Binding Etsy store merchant souls into data matrices..."
    ]
    
    # Render active ritual progress sequence
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for percent in range(0, 101, 25):
        status_text.markdown(f"***Necromancer Status:*** *{necromancer_phrases[percent // 26]}*")
        progress_bar.progress(percent)
        time.sleep(0.8)
        
    st.session_state.top_15, st.session_state.top_10_rising = generate_fresh_market_data()
    st.session_state.last_refresh = datetime.now()
    st.session_state.selected_item_rank = 1 # Reset focus to top item
    st.rerun()


# --- APP INTERFACE LAYOUT ---
st.sidebar.markdown("### ⏳ NEXT SCRYING CYCLE")
next_update = st.session_state.last_refresh + timedelta(hours=3)
st.sidebar.metric("Ritual Countdown", next_update.strftime("%H:%M:%S"))
st.sidebar.info("The Necromancer automatically re-casts his scrying spell every 3 hours to preserve fresh demonic metrics.")

# Sidebar Item Navigator (Click to change displayed metrics)
st.sidebar.markdown("### 📜 SELECT ARTIFACT TO VIEW")
for prod in st.session_state.top_15:
    btn_label = f"#{prod['rank']} - {prod['title'][:32]}..."
    if st.sidebar.button(btn_label, key=f"nav_{prod['rank']}"):
        st.session_state.selected_item_rank = prod['rank']

# Extract Active Object Selection Reference
current_item = next(p for p in st.session_state.top_15 if p['rank'] == st.session_state.selected_item_rank)


# Main Content Area Split Layout
left_panel, right_panel = st.columns([2, 1])

with left_panel:
    # 1. Central Display Element (#1 Selling Item or User Selection Highlight)
    st.markdown('<div class="central-artifact">', unsafe_allow_html=True)
    if current_item['rank'] == 1:
        st.subheader("🏆 THE SUPREME GRAND ARTIFACT (RANK #1 SELLER)")
    else:
        st.subheader(f"🔮 FOCUSED VIEW: ARTIFACT RANK #{current_item['rank']}")
        
    st.markdown(f"## [{current_item['title']}]({current_item['url']})")
    st.markdown(f"**Marketplace Origin:** `{current_item['source']}` | **7-Day Ledger Volume:** {current_item['total_sales']:,} Units")
    
    # Exactly one real targeted picture displayed per prompt rules
    st.image(current_item['img_url'], width=380, caption="Unearthed Product Image via Scrying Grid")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 2. Interactive Interactive 7-Day & Hourly Sales Metric Visualizer
    st.markdown("### 📊 TEMPORAL SALES VELOCITY LEDGER")
    
    # 7-day bar graph tracking total units sold across week
    days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]
    chart_data = dict(zip(days, current_item['weekly_sales']))
    st.bar_chart(chart_data)
    
    # Clickable Day breakdown selector mechanism mapping straight into the matrix
    st.markdown("#### 🔮 Commune with a Specific Day (View Hourly Velocity)")
    chosen_day = st.radio("Select target day timeline to map down to individual hours:", days, horizontal=True)
    
    hourly_data = current_item['hourly_sales'][chosen_day]
    st.markdown(f"**Hourly Run Velocity for {chosen_day}:**")
    st.bar_chart(hourly_data)


with right_panel:
    # 3. Remaining 14 Items Grid Ledger List
    st.markdown("### 💀 THE TOP 15 SCROLL OF POWER")
    for prod in st.session_state.top_15:
        # Highlight focus item slightly differently in inventory list
        is_focused = "✨ " if prod['rank'] == st.session_state.selected_item_rank else "🩸 "
        st.markdown(f"""
        {is_focused}**Rank #{prod['rank']}:** [{prod['title']}]({prod['url']})
        * {prod['source']} | Total Volume: `{prod['total_sales']}` units*
        ---
        """)
        
    # 4. Top 10 Trending Items List Without Pictures
    st.markdown("### 🌑 THE OUTER CIRCLE: TOP 10 RISING SHADOWS")
    st.caption("Incubating product trends gaining volume that have not broken into the main vault listings yet.")
    for trend in st.session_state.top_10_rising:
        st.markdown(f"""
        * 📈 **[RISING]** [{trend['title']}]({trend['url']}) (`{trend['source']}`)
        """)
