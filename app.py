import streamlit as st
import pandas as pd
import plotly.express as px
import random

# Page config for modern dashboard layout
st.set_page_config(page_title="Global Retail Scavenger", layout="wide", initial_sidebar_state="collapsed")

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

    /* Premium Translucent Cards */
    .premium-card {
        background: rgba(13, 18, 28, 0.75);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 12px;
        padding: 20px;
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
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    /* Item Tile Grid Matrix Styling */
    .tile-container {
        background: rgba(255, 255, 255, 0.015);
        border: 1px solid rgba(255, 255, 255, 0.04);
        border-radius: 8px;
        padding: 10px;
        text-align: center;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .tile-container:hover {
        transform: translateY(-2px);
        border-color: #00f2fe;
        box-shadow: 0 0 12px rgba(0, 242, 254, 0.15);
    }
    
    /* Clean Product Title and Shop Placement underneath picture */
    .tile-product-title {
        font-size: 0.8rem;
        font-weight: 600;
        color: #ffffff;
        margin-top: 8px;
        margin-bottom: 2px;
        line-height: 1.25;
        height: 2.5em;
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
    }
    
    /* Source Platform Badges */
    .platform-tag {
        font-size: 0.7rem;
        font-weight: 700;
        padding: 1px 6px;
        border-radius: 4px;
        display: inline-block;
        margin-bottom: 8px;
        text-transform: uppercase;
        letter-spacing: 0.02em;
    }
    .tag-amazon { background-color: rgba(255, 153, 0, 0.12); color: #ff9900; border: 1px solid rgba(255, 153, 0, 0.25); }
    .tag-etsy { background-color: rgba(241, 100, 30, 0.12); color: #f1641e; border: 1px solid rgba(241, 100, 30, 0.25); }
    .tag-tiktok { background-color: rgba(0, 242, 254, 0.12); color: #00f2fe; border: 1px solid rgba(0, 242, 254, 0.25); }
    .tag-aliexpress { background-color: rgba(230, 0, 51, 0.12); color: #e60033; border: 1px solid rgba(230, 0, 51, 0.25); }

    /* Compact Tile Image Matrix configuration */
    .tile-img {
        width: 100%;
        height: 100px;
        object-fit: cover;
        border-radius: 6px;
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

    /* 50% Reduced Micro Button Wrapper Override */
    .reduced-btn-wrapper .stButton>button {
        background: rgba(255, 255, 255, 0.04) !important;
        color: #94a3b8 !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 4px !important;
        padding: 2px 6px !important;
        font-size: 0.7rem !important;
        min-height: unset !important;
        height: 22px !important;
        width: 75% !important;
        margin: 0 auto !important;
        display: block !important;
        line-height: 1.2 !important;
        transition: all 0.2s ease;
    }
    .reduced-btn-wrapper .stButton>button:hover {
        background: #00f2fe !important;
        color: #07090e !important;
        border-color: #00f2fe !important;
        box-shadow: 0 0 8px rgba(0, 242, 254, 0.3) !important;
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
        {"id": 5, "name": "Concrete Succulent Planter", "source": "Etsy", "price": "$22.00", "url": "https://www.etsy.com/search?q=Concrete+Planter", "img": "https://images.unsplash.com/photo-1485955900006-10f4d324d411?w=500&auto=format&fit=crop&q=80"},
        {"id": 6, "name": "Handcrafted Leather Wallet", "source": "Etsy", "price": "$54.00", "url": "https://www.etsy.com/search?q=Leather+Wallet", "img": "https://images.unsplash.com/photo-1627123424574-724758594e93?w=500&auto=format&fit=crop&q=80"},
        {"id": 7, "name": "Smart Ambient RGB Strip", "source": "TikTok Shop", "price": "$15.99", "url": "https://www.tiktok.com/market", "img": "https://images.unsplash.com/photo-1565814636199-ae8133055c1c?w=500&auto=format&fit=crop&q=80"},
        {"id": 8, "name": "Viral Portable Blender", "source": "TikTok Shop", "price": "$29.95", "url": "https://www.tiktok.com/market", "img": "https://images.unsplash.com/photo-1578643463396-0997cb5328c1?w=500&auto=format&fit=crop&q=80"},
        {"id": 9, "name": "Premium Snail Mucin Serum", "source": "TikTok Shop", "price": "$19.00", "url": "https://www.tiktok.com/market", "img": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=500&auto=format&fit=crop&q=80"},
        {"id": 10, "name": "MagSafe Wireless Power Bank", "source": "AliExpress", "price": "$14.20", "url": "https://www.aliexpress.com", "img": "https://images.unsplash.com/photo-1609592424109-dd9892f1b17c?w=500&auto=format&fit=crop&q=80"},
        {"id": 11, "name": "Ultra-thin GaN Charger 65W", "source": "AliExpress", "price": "$11.50", "url": "https://www.aliexpress.com", "img": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=500&auto=format&fit=crop&q=80"},
        {"id": 12, "name": "RGB LED Pocket Video Light", "source": "AliExpress", "price": "$18.90", "url": "https://www.aliexpress.com", "img": "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=500&auto=format&fit=crop&q=80"},
        {"id": 13, "name": "Active Noise Cancelling Buds", "source": "Amazon", "price": "$89.99", "url": "https://www.amazon.com/s?k=Wireless+Earbuds", "img": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=500&auto=format&fit=crop&q=80"},
        {"id": 14, "name": "Minimalist Titanium Key Loop", "source": "Etsy", "price": "$31.00", "url": "https://www.etsy.com/search?q=Titanium+Key+Loop", "img": "https://images.unsplash.com/photo-1582139329536-e7284fece509?w=500&auto=format&fit=crop&q=80"},
        {"id": 15, "name": "High Velocity Desk Fan", "source": "Amazon", "price": "$34.99", "url": "https://www.amazon.com/s?k=Desk+Fan", "img": "https://images.unsplash.com/photo-1618944847828-82e943c3beb5?w=500&auto=format&fit=crop&q=80"}
    ]
    
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    for idx, item in enumerate(items):
        random.seed(idx + 1)
        base_sales = random.randint(500, 2500)
        item['sales_days'] = pd.DataFrame({'Day': days, 'Units Sold': [int(base_sales * random.uniform(0.8, 1.3)) for _ in days]})
        
        item['sales_hours'] = {}
        for day in days:
            hourly_data = [int((base_sales / 24) * (1 + 0.5 * random.uniform(-0.6, 1.0))) for _ in range(24)]
            item['sales_hours'][day] = pd.DataFrame({'Hour': [f"{h:02d}:00" for h in range(24)], 'Units Sold': hourly_data})
            
    return items

retrieved_items = load_scavenger_intelligence()

# Manage Interactive Drilldown Session States
if 'selected_idx' not in st.session_state:
    st.session_state.selected_idx = 0
if 'selected_day' not in st.session_state:
    st.session_state.selected_day = 'Wed'

selected_item = retrieved_items[st.session_state.selected_idx]

# --- APP SYSTEM TITLE BAR ---
st.markdown('''
<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 0; margin-bottom: 10px;">
    <div>
        <h2 style="margin: 0; font-size: 1.45rem; font-weight: 800; letter-spacing: -0.03em; background: linear-gradient(90deg, #ffffff, #94a3b8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">DATA SCAVENGER ENGINE</h2>
        <p style="margin: 0; font-size: 0.72rem; color: #4caf50; font-family: monospace; letter-spacing: 0.05em;">● TELEMETRY STATUS ONLINE // ALL GLOBAL ENDPOINTS CONVERGED</p>
    </div>
</div>
''', unsafe_allow_html=True)

# --- THREE COLUMN ASYMMETRICAL INTERFACE ---
col_left, col_center, col_right = st.columns([1.3, 1.7, 1])

# ==================== LEFT COLUMN: RADAR INGESTION & 14 TILES ====================
with col_left:
    # 1. New Style Network Ingestor: Centralized Orbital Constellation
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">📡 RADAR INGESTION LOOP</div>', unsafe_allow_html=True)
    
    st.components.v1.html('''
    <div style="position:relative; width:100%; height:140px; background:#0a0d14; border-radius:8px; border:1px solid rgba(255,255,255,0.04); overflow:hidden;">
        <canvas id="radarCanvas" style="position:absolute; top:0; left:0; width:100%; height:100%;"></canvas>
    </div>
    <script>
        const canvas = document.getElementById('radarCanvas');
        const ctx = canvas.getContext('2d');
        function resize() {
            canvas.width = canvas.parentElement.clientWidth;
            canvas.height = canvas.parentElement.clientHeight;
        }
        resize();
        
        let angle = 0;
        let pulses = [];

        function renderRadar() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            const hx = canvas.width / 2;
            const hy = canvas.height / 2;
            const orbitRadius = 42;

            // Draw radar concentric telemetry tracks
            ctx.strokeStyle = 'rgba(0, 242, 254, 0.05)';
            ctx.lineWidth = 1;
            ctx.beginPath(); ctx.arc(hx, hy, orbitRadius, 0, Math.PI * 2); ctx.stroke();
            ctx.beginPath(); ctx.arc(hx, hy, orbitRadius + 22, 0, Math.PI * 2); ctx.stroke();
            
            // Constellation outer platform coordinates
            const nodes = [
                {name: "Amazon", color: "#ff9900", baseAngle: 0},
                {name: "Etsy", color: "#f1641e", baseAngle: Math.PI / 2},
                {name: "TikTok", color: "#00f2fe", baseAngle: Math.PI},
                {name: "AliExpress", color: "#e60033", baseAngle: Math.PI * 1.5}
            ];

            angle += 0.006; // Rotate the orbit array constellation over time

            nodes.forEach(n => {
                const currentAngle = n.baseAngle + angle;
                const nx = hx + Math.cos(currentAngle) * orbitRadius;
                const ny = hy + Math.sin(currentAngle) * orbitRadius;

                // Telemetry radial connection lines
                ctx.strokeStyle = 'rgba(255, 255, 255, 0.03)';
                ctx.beginPath(); ctx.moveTo(nx, ny); ctx.lineTo(hx, hy); ctx.stroke();

                // Draw endpoint node
                ctx.fillStyle = n.color;
                ctx.beginPath(); ctx.arc(nx, ny, 4, 0, Math.PI * 2); ctx.fill();

                // Dynamic variable string labels
                ctx.font = "9px system-ui, sans-serif";
                ctx.fillStyle = "#64748b";
                ctx.fillText(n.name, nx + 7, ny + 3);

                // Probability spark loop to feed items inside the hub
                if (Math.random() < 0.012) {
                    pulses.push({sx: nx, sy: ny, t: 0});
                }
            });

            // Process data ingestion packet streams converging to the center
            pulses.forEach((p, index) => {
                p.t += 0.03;
                if (p.t >= 1) { pulses.splice(index, 1); return; }
                
                let px = p.sx + (hx - p.sx) * p.t;
                let py = p.sy + (hy - p.sy) * p.t;
                
                ctx.fillStyle = '#ffffff';
                ctx.shadowColor = '#00f2fe';
                ctx.shadowBlur = 4;
                ctx.beginPath(); ctx.arc(px, py, 2.5, 0, Math.PI * 2); ctx.fill();
                ctx.shadowBlur = 0;
            });

            // Prominent Master Central Hub Node Placement
            ctx.fillStyle = "#7f00ff";
            ctx.shadowColor = "#7f00ff";
            ctx.shadowBlur = 12;
            ctx.beginPath(); ctx.arc(hx, hy, 6, 0, Math.PI * 2); ctx.fill();
            ctx.shadowBlur = 0;

            ctx.font = "bold 9px monospace";
            ctx.fillStyle = "#ffffff";
            ctx.fillText("HUB", hx - 9, hy - 11);
            
            requestAnimationFrame(renderRadar);
        }
        renderRadar();
    </script>
    ''', height=142)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 2. 14 Item Tile Grid (Names and shops cleanly stacked directly under graphics)
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">📦 RETAIL MATRIX MARKET</div>', unsafe_allow_html=True)
    
    tile_grid = st.columns(2)
    for idx in range(1, 15):
        item_node = retrieved_items[idx]
        grid_col = tile_grid[idx % 2]
        
        with grid_col:
            tag_class = f"tag-{item_node['source'].lower().replace('.','').replace(' shop','')}"
            st.markdown(f'''
            <div class="tile-container">
                <a href="{item_node['url']}" target="_blank">
                    <img src="{item_node['img']}" class="tile-img" />
                </a>
                <div class="tile-product-title">
                    <a href="{item_node['url']}" target="_blank" class="clean-anchor">{item_node['name']}</a>
                </div>
                <div class="platform-tag {tag_class}">{item_node['source']}</div>
            ''', unsafe_allow_html=True)
            
            # Wrap the action layout inside the 50% downscaled custom CSS wrapper class
            st.markdown('<div class="reduced-btn-wrapper">', unsafe_allow_html=True)
            if st.button("Analyze", key=f"select_btn_{idx}"):
                st.session_state.selected_idx = idx
                st.rerun()
            st.markdown('</div></div><div style="margin-bottom:12px;"></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== CENTER COLUMN: PROMINENT HIGHLIGHT & INTERACTIVE GRAPH ====================
with col_center:
    # Top Prominent Display Spot (#1 Item by default, changes cleanly when other tile buttons are clicked)
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">✨ HIGHLIGHTED PRODUCT SPECIFICATION</div>', unsafe_allow_html=True)
    
    show_col1, show_col2 = st.columns([1.1, 1])
    with show_col1:
        st.markdown(f'''
        <a href="{selected_item['url']}" target="_blank">
            <img src="{selected_item['img']}" style="width:100%; height:210px; object-fit:cover; border-radius:10px; border:1px solid rgba(255,255,255,0.1);" />
        </a>
        ''', unsafe_allow_html=True)
    with show_col2:
        tag_class = f"tag-{selected_item['source'].lower().replace('.','').replace(' shop','')}"
        st.markdown(f'''
        <h3 style="margin-top:0; margin-bottom:6px; font-size:1.15rem; line-height:1.25;">
            <a href="{selected_item['url']}" target="_blank" class="clean-anchor">{selected_item['name']}</a>
        </h3>
        <div class="platform-tag {tag_class}" style="margin-bottom:10px;">{selected_item['source']}</div>
        <p style="margin:0; font-size:0.8rem; color:#64748b;">Estimated Retail Value</p>
        <h2 style="margin:0; color:#00f2fe; font-size:1.7rem; font-weight:800;">{selected_item['price']}</h2>
        <div style="margin-top:14px;">
            <a href="{selected_item['url']}" target="_blank" style="text-decoration:none;">
                <button style="width:100%; background:#7f00ff; color:white; border:none; padding:8px 12px; border-radius:6px; font-weight:600; cursor:pointer;">🔗 Direct One-Click Storefront</button>
            </a>
        </div>
        ''', unsafe_allow_html=True)

    st.markdown('<hr style="border:1px solid rgba(255,255,255,0.05); margin:20px 0;">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">📊 METRIC ANALYSIS METADATA (7-DAY DRILLDOWN)</div>', unsafe_allow_html=True)
    
    # Target pill row to execute instant interactive graph variable transitions
    choice_day = st.radio("Select Calendar Variable below to update the Hourly Line Profile curve directly:", ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], index=['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].index(st.session_state.selected_day), horizontal=True)
    if choice_day != st.session_state.selected_day:
        st.session_state.selected_day = choice_day
        st.rerun()

    view_tab1, view_tab2 = st.tabs(["7-Day Cumulative Volume Run", f"Hourly Velocity Spread ({st.session_state.selected_day})"])
    
    with view_tab1:
        fig_7d = px.bar(selected_item['sales_days'], x='Day', y='Units Sold', color='Units Sold', color_continuous_scale='Purples')
        fig_7d.update_layout(
            plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='#94a3b8',
            margin=dict(l=10, r=10, t=10, b=10), coloraxis_showscale=False, height=230
        )
        st.plotly_chart(fig_7d, use_container_width=True)
        
    with view_tab2:
        fig_24h = px.line(selected_item['sales_hours'][st.session_state.selected_day], x='Hour', y='Units Sold', markers=True)
        fig_24h.update_traces(line_color='#00f2fe', marker=dict(size=5, color='#ffffff'))
        fig_24h.update_layout(
            plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='#94a3b8',
            margin=dict(l=10, r=10, t=10, b=10), height=230
        )
        st.plotly_chart(fig_24h, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== RIGHT COLUMN: TEXT-ONLY MICRO-TREND SHEET ====================
with col_right:
    st.markdown('<div class="premium-card" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">⚡ NEXT 10 MICRO-TRENDING VELOCITIES</div>', unsafe_allow_html=True)
    
    micro_trends = [
        ("Collapsible Silicone Travel Kettle", "Amazon", "https://www.amazon.com/s?k=Collapsible+Silicone+Travel+Kettle"),
        ("Automatic Smart Self-Stirring Mug", "TikTok Shop", "https://www.tiktok.com/market"),
        ("Custom Celestial Birth Chart Print", "Amazon", "https://www.amazon.com/s?k=Custom+Celestial+Birth+Chart+Print"),
        ("Mini Pocket Label Thermal Printer", "Amazon", "https://www.amazon.com/s?k=Mini+Pocket+Label+Thermal+Printer"),
        ("Electric Jar Vacuum Sealer Machine", "TikTok Shop", "https://www.tiktok.com/market"),
        ("Premium Titanium EDC Multi-Tool", "AliExpress", "https://www.aliexpress.com"),
        ("Vintage Ceramic Mushroom Desk Lamp", "Etsy", "https://www.etsy.com/search?q=mushroom+lamp"),
        ("Aesthetic Abstract Ceramic Vases", "Etsy", "https://www.etsy.com/search?q=ceramic+vase"),
        ("Ergonomic Memory Foam Wrist Rest", "Amazon", "https://www.amazon.com/s?k=Wrist+Rest"),
        ("Flame Effect Ultrasonic Air Diffuser", "TikTok Shop", "https://www.tiktok.com/market")
    ]
    
    for i, (t_name, t_src, t_url) in enumerate(micro_trends, 1):
        st.markdown(f'''
        <div style="margin-bottom: 12px; font-size: 0.85rem; line-height: 1.4;">
            <div style="font-weight: 700; color: #ffffff;">
                {i}. <a href="{t_url}" target="_blank" class="clean-anchor">{t_name}</a>
            </div>
            <span style="font-size: 0.7rem; font-weight: bold; color: #64748b; text-transform: uppercase;">[{t_src}]</span>
        </div>
        ''', unsafe_allow_html=True)
        if i < 10:
            st.markdown('<hr style="margin: 6px 0; border: none; border-top: 1px solid rgba(255,255,255,0.03);">', unsafe_allow_html=True)
            
    st.markdown('</div>', unsafe_allow_html=True)
