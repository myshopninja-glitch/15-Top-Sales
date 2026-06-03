import streamlit as st
import pandas as pd
import plotly.express as px
import random

# Page config for high-end cinematic dashboard aspect ratio
st.set_page_config(page_title="Global Retail Scavenger", layout="wide", initial_sidebar_state="collapsed")

# Sleek Premium Dark UI Style Architecture (Neo-Brutalist Glassmorphism)
st.markdown('''
<style>
    /* Global Page Overrides */
    .stApp {
        background-color: #080b11;
        color: #e2e8f0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        background-image: 
            radial-gradient(at 0% 0%, rgba(31, 38, 135, 0.15) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(127, 0, 255, 0.1) 0px, transparent 50%);
    }
    
    /* Elegant Modern Typography */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff;
        font-weight: 700;
        letter-spacing: -0.025em;
    }

    /* Premium Glass Panels */
    .premium-card {
        background: rgba(17, 24, 39, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        margin-bottom: 20px;
    }
    
    .card-title {
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #94a3b8;
        font-weight: 600;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* Item Tile Grid Matrix */
    .tile-container {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 8px;
        padding: 10px;
        text-align: center;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .tile-container:hover {
        transform: translateY(-2px);
        border-color: #00f2fe;
        box-shadow: 0 0 15px rgba(0, 242, 254, 0.2);
    }
    
    /* Source Platform Tags */
    .platform-tag {
        font-size: 0.75rem;
        font-weight: 600;
        padding: 2px 8px;
        border-radius: 4px;
        display: inline-block;
        margin-top: 6px;
        text-transform: uppercase;
        letter-spacing: 0.02em;
    }
    .tag-amazon { background-color: rgba(255, 153, 0, 0.15); color: #ff9900; border: 1px solid rgba(255, 153, 0, 0.3); }
    .tag-etsy { background-color: rgba(241, 100, 30, 0.15); color: #f1641e; border: 1px solid rgba(241, 100, 30, 0.3); }
    .tag-tiktok { background-color: rgba(0, 242, 254, 0.15); color: #00f2fe; border: 1px solid rgba(0, 242, 254, 0.3); }
    .tag-aliexpress { background-color: rgba(230, 0, 51, 0.15); color: #e60033; border: 1px solid rgba(230, 0, 51, 0.3); }

    /* Clean Image Handling */
    .tile-img {
        width: 100%;
        height: 100px;
        object-fit: cover;
        border-radius: 6px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Native Clean Navigation Links */
    a.clean-anchor {
        text-decoration: none;
        color: inherit;
    }
    a.clean-anchor:hover {
        color: #00f2fe;
    }

    /* Selection Trigger Buttons */
    .stButton>button {
        background: rgba(255, 255, 255, 0.05);
        color: #e2e8f0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 6px;
        padding: 4px 10px;
        font-size: 0.8rem;
        transition: all 0.2s;
    }
    .stButton>button:hover {
        background: #00f2fe;
        color: #080b11;
        border-color: #00f2fe;
    }
</style>
''', unsafe_allow_html=True)

# Generate Mock Dataset with live retail single-click anchors and authentic imagery
@st.cache_data
def load_scavenger_intelligence():
    items = [
        {"rank": 1, "name": "Minimalist Mechanical Keyboard", "source": "Amazon", "price": "$119.00", "url": "https://www.amazon.com/s?k=Mechanical+Keyboard", "img": "https://images.unsplash.com/photo-1618384887929-16ec33fab9ef?w=500&auto=format&fit=crop&q=80"},
        {"rank": 2, "name": "Matte Black Travel Tumbler", "source": "Amazon", "price": "$38.00", "url": "https://www.amazon.com/s?k=Travel+Tumbler", "img": "https://images.unsplash.com/photo-1577937927133-66ef06acdf18?w=500&auto=format&fit=crop&q=80"},
        {"rank": 3, "name": "Ergonomic Office Chair", "source": "Amazon", "price": "$289.50", "url": "https://www.amazon.com/s?k=Ergonomic+Office+Chair", "img": "https://images.unsplash.com/photo-1505797149-43b0069ec26b?w=500&auto=format&fit=crop&q=80"},
        {"rank": 4, "name": "Leather Desk Mat (Large)", "source": "Etsy", "price": "$45.00", "url": "https://www.etsy.com/search?q=Leather+Desk+Mat", "img": "https://images.unsplash.com/photo-1632292224971-0d45778bd364?w=500&auto=format&fit=crop&q=80"},
        {"rank": 5, "name": "Concrete Succulent Planter", "source": "Etsy", "price": "$22.00", "url": "https://www.etsy.com/search?q=Concrete+Planter", "img": "https://images.unsplash.com/photo-1485955900006-10f4d324d411?w=500&auto=format&fit=crop&q=80"},
        {"rank": 6, "name": "Handcrafted Leather Wallet", "source": "Etsy", "price": "$54.00", "url": "https://www.etsy.com/search?q=Leather+Wallet", "img": "https://images.unsplash.com/photo-1627123424574-724758594e93?w=500&auto=format&fit=crop&q=80"},
        {"rank": 7, "name": "Smart Ambient RGB Strip", "source": "TikTok Shop", "price": "$15.99", "url": "https://www.tiktok.com/market", "img": "https://images.unsplash.com/photo-1565814636199-ae8133055c1c?w=500&auto=format&fit=crop&q=80"},
        {"rank": 8, "name": "Viral Portable Blender", "source": "TikTok Shop", "price": "$29.95", "url": "https://www.tiktok.com/market", "img": "https://images.unsplash.com/photo-1578643463396-0997cb5328c1?w=500&auto=format&fit=crop&q=80"},
        {"rank": 9, "name": "Premium Snail Mucin Serum", "source": "TikTok Shop", "price": "$19.00", "url": "https://www.tiktok.com/market", "img": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=500&auto=format&fit=crop&q=80"},
        {"rank": 10, "name": "MagSafe Wireless Power Bank", "source": "AliExpress", "price": "$14.20", "url": "https://www.aliexpress.com", "img": "https://images.unsplash.com/photo-1609592424109-dd9892f1b17c?w=500&auto=format&fit=crop&q=80"},
        {"rank": 11, "name": "Ultra-thin GaN Charger 65W", "source": "AliExpress", "price": "$11.50", "url": "https://www.aliexpress.com", "img": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?w=500&auto=format&fit=crop&q=80"},
        {"rank": 12, "name": "RGB LED Pocket Video Light", "source": "AliExpress", "price": "$18.90", "url": "https://www.aliexpress.com", "img": "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=500&auto=format&fit=crop&q=80"},
        {"rank": 13, "name": "Active Noise Cancelling Buds", "source": "Amazon", "price": "$89.99", "url": "https://www.amazon.com/s?k=Wireless+Earbuds", "img": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=500&auto=format&fit=crop&q=80"},
        {"rank": 14, "name": "Minimalist Titanium Key Loop", "source": "Etsy", "price": "$31.00", "url": "https://www.etsy.com/search?q=Titanium+Key+Loop", "img": "https://images.unsplash.com/photo-1582139329536-e7284fece509?w=500&auto=format&fit=crop&q=80"},
        {"rank": 15, "name": "High Velocity Desk Fan", "source": "Amazon", "price": "$34.99", "url": "https://www.amazon.com/s?k=Desk+Fan", "img": "https://images.unsplash.com/photo-1618944847828-82e943c3beb5?w=500&auto=format&fit=crop&q=80"}
    ]
    
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    for item in items:
        random.seed(item['rank'])
        base_sales = random.randint(500, 2500)
        item['sales_days'] = pd.DataFrame({'Day': days, 'Units Sold': [int(base_sales * random.uniform(0.8, 1.3)) for _ in days]})
        
        item['sales_hours'] = {}
        for day in days:
            hourly_data = [int((base_sales / 24) * (1 + 0.5 * random.uniform(-0.6, 1.0))) for _ in range(24)]
            item['sales_hours'][day] = pd.DataFrame({'Hour': [f"{h:02d}:00" for h in range(24)], 'Units Sold': hourly_data})
            
    return items

retrieved_items = load_scavenger_intelligence()

# Initialize Navigation / Click Drill-Down Session States
if 'selected_idx' not in st.session_state:
    st.session_state.selected_idx = 0
if 'selected_day' not in st.session_state:
    st.session_state.selected_day = 'Wed'

selected_item = retrieved_items[st.session_state.selected_idx]

# --- PREMIUM DASHBOARD APP BAR ---
st.markdown('''
<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 0; margin-bottom: 10px;">
    <div>
        <h2 style="margin: 0; font-size: 1.5rem; font-weight: 800; letter-spacing: -0.04em; background: linear-gradient(90deg, #ffffff, #94a3b8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">DATA SCAVENGER ENGINE</h2>
        <p style="margin: 0; font-size: 0.75rem; color: #4caf50; font-family: monospace; letter-spacing: 0.05em;">● TELEMETRY ONLINE // CROSS-RETAILER ENDPOINTS SYNCED</p>
    </div>
    <div style="font-size:0.8rem; color: #64748b; font-family: monospace; border: 1px solid rgba(255,255,255,0.05); padding: 6px 12px; border-radius: 6px; background: rgba(255,255,255,0.01);">
        METRIC CYCLE: <span style="color: #00f2fe; font-weight: bold;">LIVE SESSION</span>
    </div>
</div>
''', unsafe_allow_html=True)

# --- THREE ASYMMETRICAL COLUMN STRUCTURE ---
col_left, col_center, col_right = st.columns([1.3, 1.7, 1])

# ==================== LEFT COLUMN ====================
with col_left:
    # Top Left Widget: High-Tech Node Ingestion Animation
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">📡 NETWORK INGESTION FLOW</div>', unsafe_allow_html=True)
    
    st.components.v1.html('''
    <div style="position:relative; width:100%; height:140px; background:#0b0f17; border-radius:8px; border:1px solid rgba(255,255,255,0.05); overflow:hidden;">
        <canvas id="neuralCanvas" style="position:absolute; top:0; left:0; width:100%; height:100%;"></canvas>
    </div>
    <script>
        const canvas = document.getElementById('neuralCanvas');
        const ctx = canvas.getContext('2d');
        function initSize() {
            canvas.width = canvas.parentElement.clientWidth;
            canvas.height = canvas.parentElement.clientHeight;
        }
        initSize();
        
        const nodes = [
            {name:"Amazon", x: 30, y: 30, color:"#ff9900"},
            {name:"Etsy", x: 30, y: 110, color:"#f1641e"},
            {name:"TikTok", x: 110, y: 70, color:"#00f2fe"},
            {name:"AliExpress", x: 190, y: 30, color:"#e60033"},
            {name:"HUB", x: 190, y: 110, color:"#7f00ff"}
        ];
        
        let pulses = [];
        setInterval(() => {
            let src = nodes[Math.floor(Math.random() * 4)];
            pulses.push({src: src, dest: nodes[4], t: 0, speed: 0.02});
        }, 400);

        function drawMatrix() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // Grid background lines
            ctx.strokeStyle = 'rgba(255,255,255,0.02)';
            ctx.lineWidth = 1;
            for(let i=0; i<canvas.width; i+=20) { ctx.beginPath(); ctx.moveTo(i,0); ctx.lineTo(i,canvas.height); ctx.stroke(); }
            for(let i=0; i<canvas.height; i+=20) { ctx.beginPath(); ctx.moveTo(0,i); ctx.lineTo(canvas.width,i); ctx.stroke(); }
            
            // Connections
            ctx.strokeStyle = 'rgba(255,255,255,0.04)';
            for(let i=0; i<4; i++) {
                ctx.beginPath(); ctx.moveTo(nodes[i].x, nodes[i].y); ctx.lineTo(nodes[4].x, nodes[4].y); ctx.stroke();
            }
            
            // Nodes
            nodes.forEach(n => {
                ctx.fillStyle = n.color;
                ctx.beginPath(); ctx.arc(n.x, n.y, 4, 0, Math.PI*2); ctx.fill();
                ctx.font = "9px system-ui, sans-serif";
                ctx.fillStyle = "#64748b";
                ctx.fillText(n.name, n.x + 8, n.y + 3);
            });
            
            // Pulses
            pulses.forEach((p, idx) => {
                p.t += p.speed;
                if(p.t >= 1) { pulses.splice(idx, 1); return; }
                let cx = p.src.x + (p.dest.x - p.src.x) * p.t;
                let cy = p.src.y + (p.dest.y - p.src.y) * p.t;
                ctx.fillStyle = '#ffffff';
                ctx.beginPath(); ctx.arc(cx, cy, 3, 0, Math.PI*2); ctx.fill();
            });
            requestAnimationFrame(drawMatrix);
        }
        drawMatrix();
    </script>
    ''', height=142)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Middle Left Widget: 14 Item Tiles Grid
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">📦 RETAIL MATRIX MARKET (RANKS 2-15)</div>', unsafe_allow_html=True)
    
    tile_grid = st.columns(2)
    for idx in range(1, 15):
        item_node = retrieved_items[idx]
        grid_col = tile_grid[idx % 2]
        
        with grid_col:
            tag_class = f"tag-{item_node['source'].lower().replace('.','').replace(' shop','')}"
            st.markdown(f'''
            <div class="tile-container">
                <span style="font-size:0.7rem; color:#64748b; font-weight:700; display:block; margin-bottom:4px;">RANK #{item_node['rank']}</span>
                <a href="{item_node['url']}" target="_blank">
                    <img src="{item_node['img']}" class="tile-img" />
                </a>
                <div class="platform-tag {tag_class}">{item_node['source']}</div>
            ''', unsafe_allow_html=True)
            
            if st.button(f"Analyze #{item_node['rank']}", key=f"select_btn_{idx}"):
                st.session_state.selected_idx = idx
                st.rerun()
                
            st.markdown('</div><div style="margin-bottom:12px;"></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== CENTER COLUMN ====================
with col_center:
    # Prominent Element Display (#1 spot or currently highlighted index node)
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    is_rank_1 = "✨ HIGHLIGHTED PRODUCT ALTAR" if selected_item['rank'] != 1 else "👑 PROMINENT POSITION #1 RANKING"
    st.markdown(f'<div class="card-title">{is_rank_1}</div>', unsafe_allow_html=True)
    
    show_col1, show_col2 = st.columns([1.1, 1])
    with show_col1:
        st.markdown(f'''
        <a href="{selected_item['url']}" target="_blank">
            <img src="{selected_item['img']}" style="width:100%; height:230px; object-fit:cover; border-radius:10px; border:1px solid rgba(255,255,255,0.12);" />
        </a>
        ''', unsafe_allow_html=True)
    with show_col2:
        tag_class = f"tag-{selected_item['source'].lower().replace('.','').replace(' shop','')}"
        st.markdown(f'''
        <h3 style="margin-top:0; margin-bottom:6px; font-size:1.2rem; line-height:1.2;">
            <a href="{selected_item['url']}" target="_blank" class="clean-anchor">{selected_item['name']}</a>
        </h3>
        <div class="platform-tag {tag_class}" style="margin-bottom:12px;">{selected_item['source']} Marketplace</div>
        <p style="margin:0; font-size:0.85rem; color:#64748b;">Estimated Retail Value</p>
        <h2 style="margin:0; color:#00f2fe; font-size:1.8rem; font-weight:800;">{selected_item['price']}</h2>
        <div style="margin-top:15px;">
            <a href="{selected_item['url']}" target="_blank" style="text-decoration:none;">
                <button style="width:100%; background:#7f00ff; color:white; border:none; padding:8px 12px; border-radius:6px; font-weight:600; cursor:pointer;">🔗 Direct One-Click Storefront</button>
            </a>
        </div>
        ''', unsafe_allow_html=True)

    st.markdown('<hr style="border:1px solid rgba(255,255,255,0.06); margin:20px 0;">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">📊 METRIC ANALYSIS TOME (7-DAY DRILLDOWN)</div>', unsafe_allow_html=True)
    
    # Pill selectors mapping directly to drill down state actions
    choice_day = st.radio("Select Bar Variable to Map Hourly Delivery Curves:", ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], index=['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].index(st.session_state.selected_day), horizontal=True)
    if choice_day != st.session_state.selected_day:
        st.session_state.selected_day = choice_day
        st.rerun()

    view_tab1, view_tab2 = st.tabs(["7-Day Cumulative Run", f"Hourly Velocity Details ({st.session_state.selected_day})"])
    
    with view_tab1:
        fig_7d = px.bar(selected_item['sales_days'], x='Day', y='Units Sold', color='Units Sold', color_continuous_scale='Purples')
        fig_7d.update_layout(
            plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='#94a3b8',
            margin=dict(l=10, r=10, t=10, b=10), coloraxis_showscale=False, height=240
        )
        st.plotly_chart(fig_7d, use_container_width=True)
        
    with view_tab2:
        fig_24h = px.line(selected_item['sales_hours'][st.session_state.selected_day], x='Hour', y='Units Sold', markers=True)
        fig_24h.update_traces(line_color='#00f2fe', marker=dict(size=6, color='#ffffff'))
        fig_24h.update_layout(
            plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='#94a3b8',
            margin=dict(l=10, r=10, t=10, b=10), height=240
        )
        st.plotly_chart(fig_24h, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== RIGHT COLUMN ====================
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
        <div style="margin-bottom: 14px; font-size: 0.85rem; line-height: 1.4;">
            <div style="font-weight: 700; color: #ffffff;">
                {i}. <a href="{t_url}" target="_blank" class="clean-anchor">{t_name}</a>
            </div>
            <span style="font-size: 0.7rem; font-weight: bold; color: #64748b; text-transform: uppercase;">[{t_src}]</span>
        </div>
        ''', unsafe_allow_html=True)
        if i < 10:
            st.markdown('<hr style="margin: 6px 0; border: none; border-top: 1px solid rgba(255,255,255,0.04);">', unsafe_allow_html=True)
            
    st.markdown('</div>', unsafe_allow_html=True)
