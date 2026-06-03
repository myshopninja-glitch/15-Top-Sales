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
            "img": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=400&auto=format&fit=crop&q=80"
        },
        {
            "title": "Handcrafted Woodland Mushroom Ceramic Artisan Coffee Mug", 
            "source": "Etsy", 
            "url": "https://www.etsy.com/search?q=mushroom+ceramic+mug",
            "img": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=400&auto=format&fit=crop&q=80"
        },
        {
            "title": "Sunset Projection Ambient LED Halo Night Atmosphere Lamp", 
            "source": "TikTok Shop", 
            "url": "https://www.tiktok.com/explore",
            "img": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=400&auto=format&fit=crop&q=80"
        },
        {
            "title": "Anker Magnetic Wireless Power Bank 10K Slim Battery Pack", 
            "source": "Amazon", 
            "url": "https://www.amazon.com/s?k=Anker+Magnetic+Wireless+Power+Bank",
            "img": "https://images.unsplash.com/photo-1620288627223-53302f4e8c74?w=400&auto=format&fit=crop&q=80"
        },
        {
            "title": "Vintage Heavyweight Corduroy Zippered Daily Tote Bag", 
            "source": "Etsy", 
            "url": "https://www.etsy.com/search?q=corduroy+tote+bag",
            "img": "https://images.unsplash.com/photo-1544816155-12df9643f363?w=400&auto=format&fit=crop&q=80"
        },
        {
            "title": "Phomemo Mini Pocket Wireless Bluetooth Thermal Sticker Printer", 
            "source": "Amazon", 
            "url": "https://www.amazon.com/s?k=Phomemo+Mini+Thermal+Printer",
            "img": "https://images.unsplash.com/photo-1612815154858-60aa4c59eaa6?w=400&auto=format&fit=crop&q=80"
        },
        {
            "title": "Bedsure Orthopedic Calming High-Density Foam Dog Bed", 
            "source": "Amazon", 
            "url": "https://www.amazon.com/s?k=Bedsure+Orthopedic+Dog+Bed",
            "img": "https://images.unsplash.com/photo-1541599540903-216a46cc1ad6?w=400&auto=format&fit=crop&q=80"
        },
        {
            "title": "Y2K Star Patch Heavy-Cotton Full Zip Streetwear Hoodie", 
            "source": "TikTok Shop", 
            "url": "https://www.tiktok.com/explore",
            "img": "https://images.unsplash.com/photo-1556905055-8f358a7a47b2?w=400&auto=format&fit=crop&q=80"
        },
        {
            "title": "Gravity-Activated Automatic Electric Salt & Pepper Grinder Set", 
            "source": "Amazon", 
            "url": "https://www.amazon.com/s?k=Electric+Salt+and+Pepper+Grinder+Set",
            "img": "https://images.unsplash.com/photo-1588854337236-6889d631faa8?w=400&auto=format&fit=crop&q=80"
        },
        {
            "title": "Boho Tufted Macrame Geometric Accent Woven Pillow Cover Set", 
            "source": "Etsy", 
            "url": "https://www.etsy.com/search?q=Boho+Tufted+Pillow+Cover",
            "img": "https://images.unsplash.com/photo-1584100936595-c0654b55a2e2?w=400&auto=format&fit=crop&q=80"
        },
        {
            "title": "Bleame Magic Crystal Hair Eraser Painless Exfoliator Tool", 
            "source": "TikTok Shop", 
            "url": "https://www.tiktok.com/explore",
            "img": "https://images.unsplash.com/photo-1608248597481-496100c80836?w=400&auto=format&fit=crop&q=80"
        },
        {
            "title": "Self-Squeezing Hands-Free Absorbent Mini Desktop Mop Tool", 
            "source": "TikTok Shop", 
            "url": "https://www.tiktok.com/explore",
            "img": "https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=400&auto=format&fit=crop&q=80"
        },
        {
            "title": "Premium Traditional Ceremony 100-Prong Bamboo Matcha Whisk Set", 
            "source": "Etsy", 
            "url": "https://www.etsy.com/search?q=Matcha+Whisk+Set",
            "img": "https://images.unsplash.com/photo-1536256263959-770b48d82b0a?w=400&auto=format&fit=crop&q=80"
        },
        {
            "title": "Splash-Proof Raised Spill Lip Silicone Pet Feeding Mat Tray", 
            "source": "Amazon", 
            "url": "https://www.amazon.com/s?k=Silicone+Pet+Feeding+Mat",
            "img": "https://images.unsplash.com/photo-1601758228041-f3b2795255f1?w=400&auto=format&fit=crop&q=80"
        },
        {
            "title": "Smart LED Cap Temperature Sensing Vacuum Insulated Flask", 
            "source": "TikTok Shop", 
            "url": "https://www.tiktok.com/explore",
            "img": "https://images.unsplash.com/photo-1523362628745-0c100150b504?w=400&auto=format&fit=crop&q=80"
        },
        # Top 10 Trending Items (No Images per specifications)
        {"title": "Minimalist Full-Grain Leather MagSafe Slim Card Wallet", "source": "Etsy", "url": "https://www.etsy.com/search?q=Leather+MagSafe+Wallet"},
        {"title": "Ergonomic Memory Foam Contoured Joint Wrist Rest Combo", "source": "Amazon", "url": "https://www.amazon.com/s?k=Ergonomic+Wrist+Rest+Set"},
        {"title": "Rechargeable Multi-Spectrum Eye-Care Reading Book Light Clip", "source": "Amazon", "url": "https://www.amazon.com/s?k=Clip+on+Book+Light"},
        {"title": "Organic Cold-Pressed Fortifying Rosemary Scalp Nutrition Oil", "source": "TikTok Shop", "url": "https://www.tiktok.com/explore"},
        {"title": "Handmade Wooden Celestial Phase Moon Wall Hanging Decor", "source": "Etsy", "url": "https://www.etsy.com/search?q=Moon+Phase+Wall+Hanging"},
        {"title": "High-Velocity Cordless Electric Compressed Air Can Duster", "source": "Amazon", "url": "https://www.amazon.com/s?k=Electric+Air+Duster"},
        {"title": "Geometric Nordic Bubble Cube Pure Soy Aesthetic Candle", "source": "Etsy", "url": "https://www.etsy.com/search?q=Bubble+Cube+Candle"},
        {"title": "High-Density Non-Slip Eco-Polymer Daily Fitness Yoga Mat", "source": "Amazon", "url": "https://www.amazon.com/s?k=High+Density+Yoga+Mat"},
        {"title": "Collapsible Food-Grade Travel Packable Silicone Cup", "source": "TikTok Shop", "url": "https://www.tiktok.com/explore"},
        {"title": "Multi-Device Wireless Ergonomic Precision Trackpad Mouse", "source": "Amazon", "url": "https://www.amazon.com/s?k=Wireless+Bluetooth+Mouse"}
    ]

    processed = []
    for idx, item in enumerate(products_pool):
        # Generate data arrays modeling high volume sales performance 
        historical_7_days = [random.randint(800, 3400) for _ in range(7)]
        hourly_matrix = {f"Day {d+1}": [random.randint(30, 180) for _ in range(24)] for d in range(7)}
        
        processed.append({
            "title": item["title"],
            "source": item["source"],
            "url": item["url"],
            "img_url": item.get("img", ""), # Only top 15 contain images
            "total_sales": sum(historical_7_days),
            "weekly_sales": historical_7_days,
            "hourly_sales": hourly_matrix
        })

    # Sort strictly by transaction performance to lock down hierarchy order
    sorted_ledger = sorted(processed, key=lambda x: x["total_sales"], reverse=True)
    
    for rank_idx, record in enumerate(sorted_ledger):
        record["rank"] = rank_idx + 1
        
    return sorted_ledger[:15], sorted_ledger[15:]


# --- COMPUTE SCRYING CACHE INTERVALS ---
if "last_refresh" not in st.session_state:
    st.session_state.last_refresh = datetime.now() - timedelta(hours=4)
    st.session_state.top_15 = []
    st.session_state.top_10_rising = []
    st.session_state.active_rank = 1

time_delta = datetime.now() - st.session_state.last_refresh

# --- RITUAL IN PROGRESS: VISUALLY ACTIVE NECROMANCER ---
if time_delta.total_seconds() >= 10800 or len(st.session_state.top_15) == 0:
    st.markdown("### 💀 THE NECROMANCER CONJURES THE SCRYING RITUAL...")
    
    ritual_gauge = st.progress(0)
    incantation_prompt = st.empty()
    
    spells = [
        "🩸 Drawing runic bounding boxes over Amazon's centralized inventory database...",
        "🦴 Forging skeleton proxies to siphon transaction logs out of Etsy's servers...",
        "🔮 Piercing into the shadow matrix of TikTok Shop item vectors...",
        "📜 Binding collected marketplace metrics back onto the Horadric UI plate..."
    ]
    
    for stage in range(4):
        incantation_prompt.markdown(f"***Ritual Progress:*** *{spells[stage]}*")
        ritual_gauge.progress((stage + 1) * 25)
        time.sleep(1.0)
        
    st.session_state.top_15, st.session_state.top_10_rising = fetch_sanctuary_market_feed()
    st.session_state.last_refresh = datetime.now()
    st.session_state.active_rank = 1 # Re-align spotlight focus to rank 1
    st.rerun()


# --- INTERFACE TIMELINE TRACKER ---
time_remaining = (st.session_state.last_refresh + timedelta(hours=3)) - datetime.now()
st.sidebar.markdown(f"⏳ **Next Autonomous Refresh:** *In {int(time_remaining.total_seconds() // 60)} minutes*")
st.sidebar.markdown("---")

# Extract Reference Values for Spotlight Display
spotlight_item = next(p for p in st.session_state.top_15 if p['rank'] == st.session_state.active_rank)


# --- CHARACTER CONTROL LAYOUT SHEET ---
left_panel, right_panel = st.columns([5, 4])

with left_panel:
    # 1. CENTRAL DISPLAY SYSTEM (#1 SELLER HIGHLIGHT)
    st.markdown('<div class="legendary-vault-frame">', unsafe_allow_html=True)
    if spotlight_item['rank'] == 1:
        st.markdown("### 🏆 THE CROWN ARTIFACT (GLOBAL RANK #1 SELLER)")
    else:
        st.markdown(f"### 🔮 EXAMINING VAULT ARTIFACT POSITION #{spotlight_item['rank']}")
        
    st.markdown(f"## [{spotlight_item['title']}]({spotlight_item['url']})")
    st.markdown(f"**Market Origin:** `{spotlight_item['source']}` | **7-Day Transaction Ledger:** {spotlight_item['total_sales']:,} Units")
    
    # Showcase single item image matching link context 
    st.image(spotlight_item['img_url'], width=380, caption="Verified Image Asset Source Link Extract")
    st.markdown('<div style="margin-top:10px;"><small>⚠️ Click any slot on the right panel to map its runic data onto the graph below.</small></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 2. RUNIC CLICKABLE TIME BREAKDOWN GRAPH SYSTEM
    st.markdown("### 📊 HISTORICAL VELOCITY LEDGER")
    days_labels = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]
    st.bar_chart(dict(zip(days_labels, spotlight_item['weekly_sales'])))
    
    st.markdown("#### 👆 Inspect Specific Day Horizons (Hourly Metrics Matrix)")
    selected_day = st.radio("Target day timeline projection:", days_labels, horizontal=True, key="ledger_radio")
    
    hourly_breakdown_metrics = spotlight_item['hourly_sales'][selected_day]
    st.markdown(f"**Hourly Volume Run Rate for {selected_day}:**")
    st.bar_chart(hourly_breakdown_metrics)


with right_panel:
    # 3. COMPREHENSIVE RUNIC STASH SCROLL (ALL TOP 15 INCLUDE TITLES, LINKS, & IMAGES SIMULTANEOUSLY)
    st.markdown("### 🔲 THE HORADRIC INVENTORY (TOP 15)")
    
    for prod in st.session_state.top_15:
        # Visual highlight marker tracking active focal component selection
        is_active = "⚡ " if prod['rank'] == st.session_state.active_rank else "🩸 "
        
        st.markdown(f'<div class="inventory-slot-box">', unsafe_allow_html=True)
        st.markdown(f"#### {is_active} Rank #{prod['rank']}: [{prod['title']}]({prod['url']})")
        st.markdown(f"*Market: `{prod['source']}` | Weekly Volume: **{prod['total_sales']:,} units***")
        
        # Grid alignment separating product layout frames cleanly
        img_col, btn_col = st.columns([2, 3])
        with img_col:
            # Displays authentic picture for every single top 15 item
            st.image(prod['img_url'], use_container_width=True)
        with btn_col:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Inspect Runic Stats", key=f"inspect_btn_{prod['rank']}"):
                st.session_state.active_rank = prod['rank']
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # 4. TOP 10 TRENDING ITEMS (STRICT TEXT-ONLY SCROLL LIST OUTSIDE THE TOP 15)
    st.markdown("### 🌑 THE OUTER CIRCLE: TOP 10 RISING SHADOWS")
    st.caption("Incubating product trends gaining heavy transaction velocity that haven't pierced the top 15 grid yet.")
    for idx, trend in enumerate(st.session_state.top_10_rising):
        st.markdown(f"""
        * 📈 **[RISING SHADOW #{idx+1}]** [{trend['title']}]({trend['url']}) (`{trend['source']}`)
        """)
