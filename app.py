import streamlit as st
import pandas as pd
import plotly.express as px
import random

# Force wide layout and dark-gothic style settings to match image_040999.jpg
st.set_page_config(page_title="The Horadric Internet Scraper", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS styling to perfectly mimic the high-fidelity Diablo 2 LOD UI styling
st.markdown('''
<style>
    /* Global Background and Typography */
    .stApp {
        background-color: #070707;
        color: #d4c4a8;
        font-family: "Courier New", Courier, monospace;
        background-image: radial-gradient(circle at center, #15110d 0%, #030303 100%);
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #dfc89f;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.9);
        font-family: "Georgia", serif;
        letter-spacing: 1px;
    }

    /* Gothic UI Panel Frames matching image_040999.jpg layout structures */
    .gothic-panel {
        background-color: #111111;
        border: 2px solid #3c3326;
        border-top: 2px solid #574a37;
        border-bottom: 2px solid #2a2219;
        border-radius: 2px;
        padding: 14px;
        box-shadow: inset 0 0 20px #000000, 0 8px 16px rgba(0,0,0,0.9);
        margin-bottom: 15px;
        height: 100%;
    }
    
    .panel-title {
        border-bottom: 1px solid #4a3f2e;
        padding-bottom: 4px;
        margin-bottom: 12px;
        text-align: center;
        text-transform: uppercase;
        font-weight: bold;
        font-family: "Georgia", serif;
        color: #dfc89f;
        font-size: 0.95rem;
        letter-spacing: 1.5px;
    }

    /* Thumbnail frame highlights matching item sockets exactly */
    .thumb-frame {
        border: 2px solid #3a3124;
        background-color: #050505;
        padding: 2px;
        border-radius: 3px;
        text-align: center;
    }
    .thumb-frame.active {
        border-color: #e59422;
        box-shadow: 0 0 8px rgba(229, 148, 34, 0.5);
    }

    /* Immersive Product Active Links */
    .product-link {
        color: #dfc89f !important;
        text-decoration: none;
        font-weight: bold;
        border-bottom: 1px dotted #554733;
    }
    .product-link:hover {
        color: #ffffff !important;
        text-decoration: none !important;
        border-bottom: 1px solid #dfc89f;
    }

    /* Text-Only Trending Sheet Styling */
    .trending-box {
        font-size: 0.8rem;
        line-height: 1.4;
        color: #dfc89f;
    }
    .trending-note {
        font-size: 0.72rem;
        color: #8c7d67;
        margin-top: 12px;
        line-height: 1.3;
        font-family: "Georgia", serif;
    }

    /* Lower Horizontal Inventory Grid Frame adjustments */
    .inventory-card-frame {
        border: 2px solid #3c3326;
        background-color: rgba(12, 12, 12, 0.9);
        border-radius: 3px;
        padding: 8px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.9);
    }
    .inventory-card-frame.equipped {
        border-color: #dfc89f;
        background-color: rgba(45, 34, 23, 0.35);
        box-shadow: inset 0 0 10px #000000, 0 4px 10px rgba(0,0,0,0.9);
    }
    
    /* Live Ticker Styling */
    .live-ticker {
        background-color: #020202;
        padding: 8px 15px;
        border: 1px solid #2b2319;
        font-family: monospace;
        color: #7da87d;
        font-size: 0.82rem;
        margin-top: 15px;
    }
    
    /* Programmatic buttons custom styling */
    .stButton>button {
        background: linear-gradient(to bottom, #3a3124 0%, #1b1610 100%) !important;
        color: #dfc89f !important;
        border: 1px solid #554733 !important;
        border-radius: 2px !important;
        font-family: "Georgia", serif !important;
        font-size: 0.78rem !important;
        width: 100%;
    }
    .stButton>button:hover {
        color: #ffffff !important;
        border-color: #dfc89f !important;
        background: linear-gradient(to bottom, #4a3f2e 0%, #231d15 100%) !important;
    }
</style>
''', unsafe_allow_html=True)

# Dataset Initialization (Top 15 Items Array mapped with high-res assets)
@st.cache_data
def get_scavenged_data():
    top_15 = [
        {"rank": 1, "name": "Kindle Paperwhite", "source": "Amazon Marketplace", "price": "$139.99", "url": "https://www.amazon.com/s?k=Kindle+Paperwhite", "img": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=500&auto=format&fit=crop&q=80"},
        {"rank": 2, "name": "Yeti Rambler Tumbler", "source": "Amazon Marketplace", "price": "$35.00", "url": "https://www.amazon.com/s?k=Yeti+Rambler+20+oz", "img": "https://images.unsplash.com/photo-1577937927133-66ef06acdf18?w=500&auto=format&fit=crop&q=80"},
        {"rank": 3, "name": "Dyson V8 Vacuum", "source": "Amazon Marketplace", "price": "$399.99", "url": "https://www.amazon.com/s?k=Dyson+V8", "img": "https://images.unsplash.com/photo-1558317374-067fb5f30001?w=500&auto=format&fit=crop&q=80"},
        {"rank": 4, "name": "Apple AirPods Pro", "source": "Amazon Marketplace", "price": "$249.00", "url": "https://www.amazon.com/s?k=AirPods+Pro", "img": "https://images.unsplash.com/photo-1588449668365-d15e397f6787?w=500&auto=format&fit=crop&q=80"},
        {"rank": 5, "name": "Echo Dot 5th Gen", "source": "Amazon Marketplace", "price": "$49.99", "url": "https://www.amazon.com/s?k=Echo+Dot+5th+Gen", "img": "https://images.unsplash.com/photo-1543512214-318c7553f230?w=500&auto=format&fit=crop&q=80"},
        {"rank": 6, "name": "Apple Watch Series 9", "source": "Amazon Marketplace", "price": "$399.00", "url": "https://www.amazon.com/s?k=Apple+Watch+Series+9", "img": "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=500&auto=format&fit=crop&q=80"},
        {"rank": 7, "name": "Stanley Quencher 40oz", "source": "TikTok Shop", "price": "$45.00", "url": "https://www.tiktok.com/t/ZT887eX7V/", "img": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=500&auto=format&fit=crop&q=80"},
        {"rank": 8, "name": "Gothic Heavy Hoodie", "source": "TikTok Shop", "price": "$49.99", "url": "https://www.tiktok.com/t/ZT887eX7V/", "img": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=500&auto=format&fit=crop&q=80"},
        {"rank": 9, "name": "Mielle Rosemary Oil", "source": "TikTok Shop", "price": "$10.20", "url": "https://www.tiktok.com/t/ZT887eX7V/", "img": "https://images.unsplash.com/photo-1608248597481-496100c80836?w=500&auto=format&fit=crop&q=80"},
        {"rank": 10, "name": "Custom Name Necklace", "source": "Etsy", "price": "$28.00", "url": "https://www.etsy.com/search?q=name+necklace", "img": "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500&auto=format&fit=crop&q=80"},
        {"rank": 11, "name": "Handmade Soy Candles", "source": "Etsy", "price": "$18.50", "url": "https://www.etsy.com/search?q=soy+candles", "img": "https://images.unsplash.com/photo-1603006905003-be475563bc59?w=500&auto=format&fit=crop&q=80"},
        {"rank": 12, "name": "Minimalist Leather Wallet", "source": "Etsy", "price": "$42.00", "url": "https://www.etsy.com/search?q=leather+wallet", "img": "https://images.unsplash.com/photo-1627123424574-724758594e93?w=500&auto=format&fit=crop&q=80"},
        {"rank": 13, "name": "Cosrx Snail Mucin", "source": "Amazon Marketplace", "price": "$14.50", "url": "https://www.amazon.com/s?k=Cosrx+Snail+Mucin", "img": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=500&auto=format&fit=crop&q=80"},
        {"rank": 14, "name": "Ninja Creami Maker", "source": "Amazon Marketplace", "price": "$229.00", "url": "https://www.amazon.com/s?k=Ninja+Creami", "img": "https://images.unsplash.com/photo-1584269600464-37b1b58a9fe7?w=500&auto=format&fit=crop&q=80"},
        {"rank": 15, "name": "CeraVe Moisturizer", "source": "Amazon Marketplace", "price": "$16.22", "url": "https://www.amazon.com/s?k=CeraVe+Moisturizer", "img": "https://images.unsplash.com/photo-1611080501637-285b7f522b17?w=500&auto=format&fit=crop&q=80"},
    ]
    
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    for item in top_15:
        random.seed(item['rank'])
        base = random.randint(400, 1200)
        item['sales_days'] = pd.DataFrame({'Day': days, 'Units Sold': [int(base * random.uniform(0.7, 1.4)) for _ in days]})
        
        item['sales_hours'] = {}
        for day in days:
            hourly_curve = [int((base / 24) * (1 + 0.6 * random.uniform(-0.5, 1.2))) for _ in range(24)]
            item['sales_hours'][day] = pd.DataFrame({'Hour': [f"{h}:00" for h in range(24)], 'Units Sold': hourly_curve})
            
    return top_15

top_items = get_scavenged_data()

# Manage UI Presentation Engine States
if 'selected_idx' not in st.session_state:
    st.session_state.selected_idx = 0
if 'drill_day' not in st.session_state:
    st.session_state.drill_day = 'Wed'
if 'selected_thumb' not in st.session_state:
    st.session_state.selected_thumb = 0

curr_item = top_items[st.session_state.selected_idx]

# --- HEADER ASSEMBLY MATCHING IMAGE_040999.JPG ---
st.markdown('''
<div style="display: flex; justify-content: space-between; align-items: flex-end; padding: 2px 0;">
    <h2 style="margin: 0; font-size: 1.45rem; font-weight: normal; font-family:'Georgia'; color:#dfc89f;">
        (💀) THE HORADRIC INTERNET SCRAPER <span style="font-size:0.65em; color:#4caf50; font-family:monospace;">[LIVE METRIC SESSION]</span>
    </h2>
    <div style="font-size:0.85rem; color:#a6967d; font-family: monospace;">NEXT REFRESH CYCLE IN: <span style="color:#ffffff; font-weight:bold;">1h 25m</span></div>
</div>
<hr style="border: 1px solid #3c3326; margin-top: 4px; margin-bottom: 15px;">
''', unsafe_allow_html=True)

# --- THREE-COLUMN HIGH-FIDELITY MAIN WORKSPACE LAYOUT ---
col_left, col_center, col_right = st.columns([1.35, 1.65, 1.1])

# 1. LEFT PANEL: SEARCHING (Isometric Network Canvas featuring 3 Visually Active Necromancer entities)
with col_left:
    st.markdown('<div class="gothic-panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">NECROMANCER</div>', unsafe_allow_html=True)
    
    # Custom HTML5 engine drawing isometric project routes, terminals, and necromancers
    st.components.v1.html('''
    <div style="position:relative; width:100%; height:275px; background:#040404; border:1px solid #2e261c; overflow:hidden;">
        <canvas id="scryingWorkshop" style="position:absolute; top:0; left:0; width:100%; height:100%;"></canvas>
        <div style="position:absolute; top:12px; left:12px; font-family:monospace; font-size:11px; color:#52b752; background:rgba(0,0,0,0.85); padding:5px; border:1px solid #3c3326;">
            Active Scrying: Processing top sellers...
        </div>
    </div>
    <script>
        const canvas = document.getElementById('scryingWorkshop');
        const ctx = canvas.getContext('2d');
        
        function resize() {
            canvas.width = canvas.parentElement.clientWidth;
            canvas.height = canvas.parentElement.clientHeight;
        }
        window.onresize = resize;
        resize();

        function isoProject(x, y, z=0) {
            const cx = canvas.width / 2;
            const cy = canvas.height / 2 - 10;
            return { x: cx + (x - y) * 0.85, y: cy + (x + y) * 0.42 - z };
        }

        const rooms = [
            {name: "amazon.com", x: -75, y: -65, color: "#ff9900"},
            {name: "etsy.com", x: -65, y: 70, color: "#f1641e"},
            {name: "tiktok.com", x: 75, y: -65, color: "#00f2fe"},
            {name: "PORTAL HUB", x: 0, y: 0, color: "#dfc89f"}
        ];

        let pulse = 0;
        function render() {
            ctx.clearRect(0,0,canvas.width,canvas.height);
            pulse += 0.04;

            // Render glowing energy channels connecting networks
            ctx.lineWidth = 2;
            for(let i=0; i<3; i++) {
                let p1 = isoProject(rooms[3].x, rooms[3].y);
                let p2 = isoProject(rooms[i].x, rooms[i].y);
                let g = ctx.createLinearGradient(p1.x, p1.y, p2.x, p2.y);
                g.addColorStop(0, "rgba(82, 183, 82, 0.4)");
                g.addColorStop(1, "rgba(42, 34, 25, 0.1)");
                ctx.strokeStyle = g;
                ctx.beginPath(); ctx.moveTo(p1.x, p1.y); ctx.lineTo(p2.x, p2.y); ctx.stroke();
            }

            // Draw Site Outposts
            rooms.forEach(r => {
                let pt = isoProject(r.x, r.y);
                ctx.fillStyle = "#0a0907";
                ctx.strokeStyle = "#4a3f2e";
                ctx.beginPath(); ctx.rect(pt.x-10, pt.y-10, 20, 20); ctx.fill(); ctx.stroke();
                
                ctx.fillStyle = r.color;
                ctx.beginPath(); ctx.arc(pt.x, pt.y, 3, 0, Math.PI*2); ctx.fill();

                ctx.font = "10px monospace"; ctx.fillStyle = "#dfc89f"; ctx.textAlign = "center";
                ctx.fillText(r.name, pt.x, pt.y + 24);
            });

            // NECROMANCER 1: Working/Casting at the Etsy Stall
            let nec1 = isoProject(-50, 50, 4);
            ctx.fillStyle = "#3a1a4a"; // Cultist purple robe
            ctx.beginPath(); ctx.moveTo(nec1.x, nec1.y-12); ctx.lineTo(nec1.x-4, nec1.y+2); ctx.lineTo(nec1.x+4, nec1.y+2); ctx.fill();
            ctx.fillStyle = "#f1641e"; ctx.beginPath(); ctx.arc(nec1.x, nec1.y-4, 2, 0, Math.PI*2); ctx.fill();

            // NECROMANCER 2: Casting a ritual at the Central Scrying Portal
            let nec2 = isoProject(10, 15, 6);
            ctx.fillStyle = "#1e354a"; // Blue robe
            ctx.beginPath(); ctx.moveTo(nec2.x, nec2.y-14); ctx.lineTo(nec2.x-5, nec2.y+2); ctx.lineTo(nec2.x+5, nec2.y+2); ctx.fill();
            // Portal sphere blast glow
            ctx.fillStyle = "#52b752"; ctx.shadowColor = "#52b752"; ctx.shadowBlur = 10 + Math.sin(pulse)*5;
            ctx.beginPath(); ctx.arc(nec2.x - 8, nec2.y - 6, 3, 0, Math.PI*2); ctx.fill(); ctx.shadowBlur = 0;

            // NECROMANCER 3: Near a glowing gothic keyboard monitor infrastructure
            let nec3 = isoProject(55, -45, 2);
            ctx.fillStyle = "#4a1212"; // Traditional blood red robe
            ctx.beginPath(); ctx.moveTo(nec3.x, nec3.y-12); ctx.lineTo(nec3.x-4, nec3.y+2); ctx.lineTo(nec3.x+4, nec3.y+2); ctx.fill();
            // Keyboard screen terminal node glow
            ctx.fillStyle = "#dfc89f"; ctx.fillRect(nec3.x + 6, nec3.y - 8, 5, 5);

            requestAnimationFrame(render);
        }
        render();
    </script>
    ''', height=280)
    st.markdown('</div>', unsafe_allow_html=True)

# 2. CENTER PANEL: MAIN ALTAR DISPLAY & INTERACTIVE TIME-SERIES REVENUE CHART
with col_center:
    st.markdown('<div class="gothic-panel">', unsafe_allow_html=True)
    st.markdown(f'<div class="panel-title">🏆 RANK #{curr_item["rank"]} DISPLAY</div>', unsafe_allow_html=True)
    
    img_col, info_col = st.columns([1.1, 1.3])
    with img_col:
        # Image acts as a single-click pass-through link
        st.markdown(f'''
            <a href="{curr_item["url"]}" target="_blank" style="text-decoration:none; display:block; text-align:center;">
                <div style="border:2px solid #4a3f2e; background-color:#030303; padding:4px; box-shadow:0 0 12px #000;">
                    <img src="{curr_item["img"]}" style="width:100%; max-height:155px; object-fit:contain;" />
                </div>
            </a>
        ''', unsafe_allow_html=True)
    with info_col:
        # Title incorporates an optimized hyperlinked active line configuration
        st.markdown(f'<h3 style="margin-top:0; margin-bottom:6px; font-size:1.15rem;"><a href="{curr_item["url"]}" class="product-link" target="_blank">Product: {curr_item["name"]}</a></h3>', unsafe_allow_html=True)
        st.markdown(f"<span style='color:#8c7d67; font-family:serif;'>Source:</span> <span style='color:#dfc89f;'>{curr_item['source']}</span>", unsafe_allow_html=True)
        st.markdown(f"<span style='color:#8c7d67; font-family:serif;'>Listed Value:</span> <span style='color:#4caf50; font-weight:bold;'>{curr_item['price']}</span>", unsafe_allow_html=True)
        
        # Outbound anchor redirect button
        st.markdown(f'''
            <a href="{curr_item["url"]}" target="_blank" style="text-decoration: none;">
                <div style="background: linear-gradient(to bottom, #3b3124, #1c1711); color: #dfc89f; text-align: center; padding: 6px; border: 1px solid #554733; border-radius: 2px; font-weight: bold; cursor: pointer; margin-top: 15px; font-family: Georgia, serif; font-size: 0.8rem; letter-spacing:0.5px;">
                    🔗 Open Marketplace Link
                </div>
            </a>
        ''', unsafe_allow_html=True)

    # Detailed Views socket frames array explicitly underneath image frame
    st.markdown('<div style="font-size:0.75rem; color:#8c7d67; margin-top:12px; margin-bottom:6px; font-family:Georgia;">Detailed Views (Click to zoom):</div>', unsafe_allow_html=True)
    thumb_cols = st.columns(5)
    for t_idx in range(5):
        with thumb_cols[t_idx]:
            is_active_thumb = (t_idx == st.session_state.selected_thumb)
            active_cls = "active" if is_active_thumb else ""
            
            st.markdown(f'''
                <div class="thumb-frame {active_cls}">
                    <img src="{curr_item["img"]}" style="width:100%; height:30px; object-fit:cover; opacity:{'1.0' if is_active_thumb else '0.45'};" />
                </div>
            ''', unsafe_allow_html=True)
            if st.button("🔍", key=f"zoom_thumb_{t_idx}"):
                st.session_state.selected_thumb = t_idx
                st.rerun()

    st.markdown('<hr style="border:0.5px dashed #3a3124; margin:14px 0;">', unsafe_allow_html=True)
    
    # Chart instructions explicitly configured as detailed in the instructions
    st.markdown(f'<div class="panel-title" style="font-size:0.85rem; margin-bottom:4px;">📊 SALES METRIC GRAPH</div>', unsafe_allow_html=True)
    st.markdown(f"<div style='text-align:center; font-size:0.75rem; color:#8c7d67; margin-bottom:8px; font-family:monospace;'>(Click bar for daily breakdown; current selection: <span style='color:#e59422; font-weight:bold;'>{st.session_state.drill_day} [Hour Curve...]</span>)</div>", unsafe_allow_html=True)
    
    # 7-Day Interactive Toggle Matrix
    days_list = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    cols_bars = st.columns(7)
    for idx, day_lbl in enumerate(days_list):
        with cols_bars[idx]:
            day_data = curr_item['sales_days'][curr_item['sales_days']['Day'] == day_lbl].iloc[0]
            units = day_data['Units Sold']
            
            if st.button(f"{day_lbl}\n({units})", key=f"graph_bar_{day_lbl}"):
                st.session_state.drill_day = day_lbl
                st.rerun()

    # Corresponding Hourly Distribution Data Curve Layer below
    fig_hours = px.line(curr_item['sales_hours'][st.session_state.drill_day], x='Hour', y='Units Sold', markers=True)
    fig_hours.update_traces(line_color='#e59422', marker=dict(size=4, color='#dfc89f'))
    fig_hours.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='#a6967d', height=105, margin=dict(l=5, r=5, t=5, b=5))
    fig_hours.update_xaxes(showgrid=False, tickfont=dict(size=8))
    fig_hours.update_yaxes(showgrid=False, tickfont=dict(size=8))
    st.plotly_chart(fig_hours, use_container_width=True, config={'displayModeBar': False})

    st.markdown('</div>', unsafe_allow_html=True)

# 3. RIGHT PANEL: TOP 10 TRENDING ITEMS (Strictly Text-Only Content Matrix Layout)
with col_right:
    st.markdown('<div class="gothic-panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">⚡ TOP 10 TRENDING ITEMS (OFF-RANKING)</div>', unsafe_allow_html=True)
    
    trending_sheet = [
        ("Custom Engraved Moon Phase Lamp", "Etsy", "https://www.etsy.com/search?q=moon+lamp"),
        ("Smart Reusable Notebook", "Amazon", "https://www.amazon.com/s?k=Smart+Reusable+Notebook"),
        ("Mushroom Coffee Starter Kit", "TikTok Shop", "https://www.tiktok.com/t/ZT887eX7V/"),
        ("Portable Fabric Shaver", "Amazon", "https://www.amazon.com/s?k=Portable+Fabric+Shaver"),
        ("Silicone Wine Glass Holder", "Etsy", "https://www.etsy.com/search?q=wine+holder"),
        ("Cold Brew Coffee Maker", "TikTok Shop", "https://www.tiktok.com/t/ZT887eX7V/"),
        ("Grant Pevetle Loop Short", "Amazon", "https://www.amazon.com/s?k=Loop+Short"),
        ("Portable Winie Shoer", "Amazon", "https://www.amazon.com/s?k=Portable+Shoer"),
        ("Silicone Coffee Maker", "TikTok Shop", "https://www.tiktok.com/t/ZT887eX7V/"),
        ("Mushroom Coffee Maker", "TikTok Shop", "https://www.tiktok.com/t/ZT887eX7V/")
    ]
    
    st.markdown('<div class="trending-box">', unsafe_allow_html=True)
    for idx, (t_name, t_src, t_url) in enumerate(trending_sheet, 1):
        st.markdown(f"""
        <div style="margin-bottom: 5px; line-height:1.2;">
            {idx}. <a href="{t_url}" class="product-link" target="_blank">{t_name}</a> 
            <span style="color: #8c7d67; font-size: 0.7rem; font-family:monospace;">[{t_src.upper()}]</span>
        </div>
        """, unsafe_allow_html=True)
        if idx < 10:
            st.markdown('<hr style="margin: 3px 0; border: 0.5px solid #2a2219;">', unsafe_allow_html=True)
            
    st.markdown('''
        <div class="trending-note">
            <strong>Note:</strong> These items have high velocity but haven't reached Top 15 sales pools yet.
        </div>
    </div>''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- LOWER EXPANDED GRID: 14 ITEM INTERACTIVE ALTAR OVERVIEW (RANKS 2-15) ---
st.markdown('<div style="margin-top: 20px; margin-bottom: 8px; font-family:\'Georgia\'; color:#dfc89f; font-size:0.95rem; text-align:center; text-transform:uppercase; letter-spacing:1.5px;">Inventory Scavenged Repository (Equip to Swap Central Altar)</div>', unsafe_allow_html=True)

grid_cols = st.columns(5)
for i in range(15):
    col_slot = i % 5
    item_node = top_items[i]
    is_equipped = (i == st.session_state.selected_idx)
    equipped_cls = "equipped" if is_equipped else ""
    
    with grid_cols[col_slot]:
        st.markdown(f"""
        <div class="inventory-card-frame {equipped_cls}">
            <div style="font-size:0.75rem; color:#dfc89f; font-family:Georgia; font-weight:bold; margin-bottom:4px;">RANK #{item_node['rank']}</div>
            <a href="{item_node['url']}" target="_blank" style="text-decoration:none; display:block; margin-bottom:5px;">
                <img src="{item_node['img']}" style="width:100%; height:80px; object-fit:cover; border:1px solid #3c3326; border-radius:2px;" />
                <div style="font-size:0.72rem; margin-top:3px; color:#dfc89f; font-family:monospace; text-overflow:ellipsis; white-space:nowrap; overflow:hidden;">{item_node['name']}</div>
            </a>
        """, unsafe_allow_html=True)
        
        # Altar Swap configuration controller
        if st.button(f"Equip #{item_node['rank']}", key=f"altar_swap_btn_{i}"):
            st.session_state.selected_idx = i
            # Reset visual thumbnail zoom position to standard on layout change
            st.session_state.selected_thumb = 0
            st.rerun()
            
        st.markdown('</div>', unsafe_allow_html=True)

# --- LOWER SYSTEM LIVE MONITORING TICKER LOOP LAYER ---
st.markdown('''
<div class="live-ticker">
    <strong>[ LIVE MONITORING TICKER ]</strong> &nbsp;&nbsp; Spiking Now: Oversized Hoodies (TikTok Shop) &nbsp;&nbsp;•&nbsp;&nbsp; <span style="color:#dfc89f;">🚀 Hot Lead: Magnetic Wireless Car Mount (AliExpress)</span> &nbsp;&nbsp;•&nbsp;&nbsp; Rising Interest: Retro Gaming Consoles (Etsy)...
</div>
''', unsafe_allow_html=True)
