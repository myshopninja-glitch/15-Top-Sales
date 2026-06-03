import streamlit as st
import pandas as pd
import plotly.express as px
import random

# Force wide layout and dark-gothic style settings
st.set_page_config(page_title="Internet Scavenger", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS styling to perfectly match the high-fidelity Diablo 2 LOD UI image
st.markdown('''
<style>
    /* Global Background and Typography */
    .stApp {
        background-color: #0d0d0d;
        color: #d4c4a8;
        font-family: "Courier New", Courier, monospace;
        background-image: radial-gradient(circle at center, #1a1510 0%, #050505 100%);
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #dfc89f;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.9);
        font-family: "Georgia", serif;
        letter-spacing: 1px;
    }

    /* Gothic UI Panel Frames */
    .gothic-panel {
        background-color: rgba(14, 14, 14, 0.95);
        border: 2px solid #3a3225;
        border-radius: 4px;
        padding: 16px;
        box-shadow: inset 0 0 15px #000000, 0 6px 12px rgba(0,0,0,0.9);
        margin-bottom: 15px;
        height: 100%;
    }
    
    .panel-title {
        border-bottom: 2px solid #4a3f2e;
        padding-bottom: 6px;
        margin-bottom: 12px;
        text-align: center;
        text-transform: uppercase;
        font-weight: bold;
        font-family: "Georgia", serif;
        color: #dfc89f;
        font-size: 1.05rem;
    }

    /* Inventory Items Grid Styling */
    .inventory-card {
        border: 2px solid #3a3225;
        background-color: rgba(10, 10, 10, 0.85);
        padding: 8px;
        border-radius: 4px;
        text-align: center;
        margin-bottom: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.8);
        transition: border-color 0.2s ease;
    }
    .inventory-card.equipped {
        border-color: #dfc89f;
        background-color: rgba(45, 35, 25, 0.5);
    }

    /* Real Hyperlinks */
    .product-link {
        color: #dfc89f !important;
        text-decoration: none;
        font-weight: bold;
    }
    .product-link:hover {
        color: #ffffff !important;
        text-decoration: underline !important;
    }

    /* Custom HTML Clickable Bar Chart Layout */
    .bar-chart-container {
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        height: 140px;
        padding: 10px 20px;
        background: #050505;
        border: 1px solid #262118;
        border-radius: 4px;
    }
    
    /* Live Ticker Styling */
    .live-ticker {
        background-color: #030303;
        padding: 10px 15px;
        border: 2px solid #262118;
        font-family: monospace;
        color: #4caf50;
        font-size: 0.85rem;
        margin-top: 15px;
    }
</style>
''', unsafe_allow_html=True)

# Dataset Initialization
@st.cache_data
def get_scavenged_data():
    top_15 = [
        {"rank": 1, "name": "Kindle Paperwhite", "source": "Amazon", "price": "$139.99", "url": "https://www.amazon.com/s?k=Kindle+Paperwhite", "img": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=500&auto=format&fit=crop&q=80"},
        {"rank": 2, "name": "Yeti Rambler Tumbler", "source": "Amazon", "price": "$35.00", "url": "https://www.amazon.com/s?k=Yeti+Rambler+20+oz", "img": "https://images.unsplash.com/photo-1577937927133-66ef06acdf18?w=500&auto=format&fit=crop&q=80"},
        {"rank": 3, "name": "Dyson V8 Vacuum", "source": "Amazon", "price": "$399.99", "url": "https://www.amazon.com/s?k=Dyson+V8", "img": "https://images.unsplash.com/photo-1558317374-067fb5f30001?w=500&auto=format&fit=crop&q=80"},
        {"rank": 4, "name": "Apple AirPods Pro", "source": "Amazon", "price": "$249.00", "url": "https://www.amazon.com/s?k=AirPods+Pro", "img": "https://images.unsplash.com/photo-1588449668365-d15e397f6787?w=500&auto=format&fit=crop&q=80"},
        {"rank": 5, "name": "Echo Dot 5th Gen", "source": "Amazon", "price": "$49.99", "url": "https://www.amazon.com/s?k=Echo+Dot+5th+Gen", "img": "https://images.unsplash.com/photo-1543512214-318c7553f230?w=500&auto=format&fit=crop&q=80"},
        {"rank": 6, "name": "Apple Watch Series 9", "source": "Amazon", "price": "$399.00", "url": "https://www.amazon.com/s?k=Apple+Watch+Series+9", "img": "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=500&auto=format&fit=crop&q=80"},
        {"rank": 7, "name": "Stanley Quencher 40oz", "source": "TikTok Shop", "price": "$45.00", "url": "https://www.tiktok.com/t/ZT887eX7V/", "img": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=500&auto=format&fit=crop&q=80"},
        {"rank": 8, "name": "Gothic Heavy Hoodie", "source": "TikTok Shop", "price": "$49.99", "url": "https://www.tiktok.com/t/ZT887eX7V/", "img": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=500&auto=format&fit=crop&q=80"},
        {"rank": 9, "name": "Mielle Rosemary Oil", "source": "TikTok Shop", "price": "$10.20", "url": "https://www.tiktok.com/t/ZT887eX7V/", "img": "https://images.unsplash.com/photo-1608248597481-496100c80836?w=500&auto=format&fit=crop&q=80"},
        {"rank": 10, "name": "Custom Name Necklace", "source": "Etsy", "price": "$28.00", "url": "https://www.etsy.com/search?q=name+necklace", "img": "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500&auto=format&fit=crop&q=80"},
        {"rank": 11, "name": "Handmade Soy Candles", "source": "Etsy", "price": "$18.50", "url": "https://www.etsy.com/search?q=soy+candles", "img": "https://images.unsplash.com/photo-1603006905003-be475563bc59?w=500&auto=format&fit=crop&q=80"},
        {"rank": 12, "name": "Minimalist Leather Wallet", "source": "Etsy", "price": "$42.00", "url": "https://www.etsy.com/search?q=leather+wallet", "img": "https://images.unsplash.com/photo-1627123424574-724758594e93?w=500&auto=format&fit=crop&q=80"},
        {"rank": 13, "name": "Cosrx Snail Mucin", "source": "Amazon", "price": "$14.50", "url": "https://www.amazon.com/s?k=Cosrx+Snail+Mucin", "img": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=500&auto=format&fit=crop&q=80"},
        {"rank": 14, "name": "Ninja Creami Maker", "source": "Amazon", "price": "$229.00", "url": "https://www.amazon.com/s?k=Ninja+Creami", "img": "https://images.unsplash.com/photo-1584269600464-37b1b58a9fe7?w=500&auto=format&fit=crop&q=80"},
        {"rank": 15, "name": "CeraVe Moisturizer", "source": "Amazon", "price": "$16.22", "url": "https://www.amazon.com/s?k=CeraVe+Moisturizer", "img": "https://images.unsplash.com/photo-1611080501637-285b7f522b17?w=500&auto=format&fit=crop&q=80"},
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

# Manage Navigation & Layout States
if 'selected_idx' not in st.session_state:
    st.session_state.selected_idx = 0
if 'drill_day' not in st.session_state:
    st.session_state.drill_day = 'Wed'

curr_item = top_items[st.session_state.selected_idx]

# --- HEADER ASSEMBLY ---
st.markdown('''
<div style="display: flex; justify-content: space-between; align-items: flex-end; padding: 5px 0;">
    <h2 style="margin: 0; font-size: 1.6rem;">(💀) INTERNET SCAVENGER <span style="font-size:0.6em; color:#4caf50;">[LIVE METRIC SESSION]</span></h2>
    <div style="font-size:0.85rem; color:#888; font-family: monospace;">NEXT REFRESH CYCLE IN: <span style="color:#dfc89f; font-weight:bold;">1h 25m</span></div>
</div>
<hr style="border: 1px solid #4a3f2e; margin-top: 5px; margin-bottom: 15px;">
''', unsafe_allow_html=True)

# --- PANEL COLUMN GRID ---
col_left, col_center, col_right = st.columns([1.3, 1.7, 1])

# 1. LEFT PANEL: SEARCHING (Isometric Artwork Grid Canvas)
with col_left:
    st.markdown('<div class="gothic-panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">SEARCHING</div>', unsafe_allow_html=True)
    
    # High-fidelity isometric visualizer built directly inside Canvas HTML5 environment
    st.components.v1.html('''
    <div style="position:relative; width:100%; height:275px; background:#040404; border:1px solid #3a3225; overflow:hidden;">
        <canvas id="isometricCanvas" style="position:absolute; top:0; left:0; width:100%; height:100%;"></canvas>
        <div style="position:absolute; top:12px; left:12px; font-family:monospace; font-size:11px; color:#4caf50; background:rgba(0,0,0,0.8); padding:5px; border:1px solid #221a12;">
            Active Scrying: Processing top sellers...
        </div>
    </div>
    <script>
        const canvas = document.getElementById('isometricCanvas');
        const ctx = canvas.getContext('2d');
        
        function resize() {
            canvas.width = canvas.parentElement.clientWidth;
            canvas.height = canvas.parentElement.clientHeight;
        }
        window.onresize = resize;
        resize();

        // High-Fidelity Isometric Projector Coordinate Transforms
        function isoProject(x, y, z=0) {
            const centerX = canvas.width / 2;
            const centerY = canvas.height / 2 - 20;
            return {
                x: centerX + (x - y) * 0.85,
                y: centerY + (x + y) * 0.45 - z
            };
        }

        const nodes = [
            {name: "amazon.com", x: -70, y: -70, color: "#ff9900"},
            {name: "etsy.com", x: -70, y: 70, color: "#f1641e"},
            {name: "tiktok.com", x: 70, y: -70, color: "#00f2fe"},
            {name: "CORE PORTAL", x: 0, y: 0, color: "#dfc89f"}
        ];

        const wanderers = [];
        for(let i=0; i<5; i++) {
            wanderers.push({
                target: Math.floor(Math.random() * 3),
                prog: Math.random(),
                speed: 0.008 + Math.random() * 0.012,
                dir: 1
            });
        }

        function runLoop() {
            ctx.clearRect(0,0,canvas.width,canvas.height);
            
            // Draw Isometric Isometric Energy Paths
            ctx.lineWidth = 2;
            for(let i=0; i<3; i++) {
                const pStart = isoProject(nodes[3].x, nodes[3].y);
                const pEnd = isoProject(nodes[i].x, nodes[i].y);
                let grad = ctx.createLinearGradient(pStart.x, pStart.y, pEnd.x, pEnd.y);
                grad.addColorStop(0, "rgba(223, 200, 159, 0.4)");
                grad.addColorStop(1, "rgba(58, 50, 37, 0.1)");
                ctx.strokeStyle = grad;
                ctx.beginPath();
                ctx.moveTo(pStart.x, pStart.y);
                ctx.lineTo(pEnd.x, pEnd.y);
                ctx.stroke();
            }

            // Draw Structures & Hub Points
            nodes.forEach(n => {
                const pt = isoProject(n.x, n.y);
                ctx.fillStyle = n.color;
                ctx.shadowColor = n.color;
                ctx.shadowBlur = 10;
                ctx.beginPath();
                ctx.arc(pt.x, pt.y, 7, 0, Math.PI*2);
                ctx.fill();
                ctx.shadowBlur = 0;
                
                ctx.font = "bold 10px Courier New";
                ctx.fillStyle = "#dfc89f";
                ctx.fillText(n.name, pt.x - 35, pt.y + 18);
            });

            // Animate Traveling Scavenger Sparks
            wanderers.forEach(w => {
                w.prog += w.speed * w.dir;
                if(w.prog > 1 || w.prog < 0) w.dir *= -1;

                const start = nodes[3];
                const end = nodes[w.target];
                const cx = start.x + (end.x - start.x) * w.prog;
                const cy = start.y + (end.y - start.y) * w.prog;
                const pt = isoProject(cx, cy, 4);

                ctx.fillStyle = "#4caf50";
                ctx.shadowColor = "#4caf50";
                ctx.shadowBlur = 12;
                ctx.beginPath();
                ctx.arc(pt.x, pt.y, 5, 0, Math.PI*2);
                ctx.fill();
                ctx.shadowBlur = 0;
            });

            requestAnimationFrame(runLoop);
        }
        runLoop();
    </script>
    ''', height=280)
    st.markdown('</div>', unsafe_allow_html=True)

# 2. CENTER PANEL: MAIN ALTAR & INTERACTIVE SALES METRIC GRAPH
with col_center:
    st.markdown('<div class="gothic-panel">', unsafe_allow_html=True)
    st.markdown(f'<div class="panel-title">🏆 RANK #{curr_item["rank"]} DISPLAY</div>', unsafe_allow_html=True)
    
    img_col, info_col = st.columns([1, 1.2])
    with img_col:
        # Wrap item display in direct verified href architecture to bypass inner application click traps
        st.markdown(f'''
            <a href="{curr_item["url"]}" target="_blank" style="text-decoration:none;">
                <img src="{curr_item["img"]}" style="width:100%; border-radius:4px; border:2px solid #5a4a35; box-shadow:0 0 10px #000;" />
            </a>
        ''', unsafe_allow_html=True)
    with info_col:
        st.markdown(f'### <a href="{curr_item["url"]}" class="product-link" target="_blank">{curr_item["name"]}</a>', unsafe_allow_html=True)
        st.markdown(f"**Source Marketplace:** {curr_item['source']}")
        st.markdown(f"**Current Listed Price:** <span style='color:#4caf50; font-weight:bold; font-size:1.2rem;'>{curr_item['price']}</span>", unsafe_allow_html=True)
        
        # Raw standalone absolute HTML anchor link for flawless TikTok routing setup
        st.markdown(f'''
            <a href="{curr_item["url"]}" target="_blank" style="text-decoration: none;">
                <div style="background: linear-gradient(to bottom, #4a3f2e, #2b2318); color: #dfc89f; text-align: center; padding: 8px; border: 1px solid #5a4a35; border-radius: 3px; font-weight: bold; cursor: pointer; margin-top: 15px; font-family: Georgia, serif; font-size: 0.9rem;">
                    🔗 Open Live Verified Storefront Link
                </div>
            </a>
        ''', unsafe_allow_html=True)

    st.markdown('<hr style="border:1px dashed #3a3225; margin:15px 0;">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title" style="font-size:0.95rem;">📊 SALES METRIC GRAPH</div>', unsafe_allow_html=True)
    
    # 7-Day Interactive Custom Component Drilldown Setup
    days_list = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    max_units = curr_item['sales_days']['Units Sold'].max()
    
    # Renders responsive bar triggers that alter application session states seamlessly
    cols_bars = st.columns(7)
    for idx, day_lbl in enumerate(days_list):
        with cols_bars[idx]:
            day_data = curr_item['sales_days'][curr_item['sales_days']['Day'] == day_lbl].iloc[0]
            units = day_data['Units Sold']
            pct_height = int((units / max_units) * 100)
            
            is_active = (day_lbl == st.session_state.drill_day)
            bar_color = "#f1641e" if is_active else "#4caf50"
            text_weight = "bold" if is_active else "normal"
            
            if st.button(f"{day_lbl}\n({units})", key=f"bar_trigger_{day_lbl}"):
                st.session_state.drill_day = day_lbl
                st.rerun()

    # Renders the corresponding hourly distribution profile below
    st.markdown(f"<div style='text-align:center; margin-top:10px; font-size:0.85rem; color:#888;'>Showing Hourly Profile Breakdown for: <span style='color:#dfc89f; font-weight:bold;'>{st.session_state.drill_day}</span></div>", unsafe_allow_html=True)
    fig_hours = px.line(curr_item['sales_hours'][st.session_state.drill_day], x='Hour', y='Units Sold', markers=True)
    fig_hours.update_traces(line_color='#f1641e', marker=dict(size=6, color='#dfc89f'))
    fig_hours.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='#c4b59d', height=140, margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig_hours, use_container_width=True, config={'displayModeBar': False})

    st.markdown('</div>', unsafe_allow_html=True)

# 3. RIGHT PANEL: TOP 10 TRENDING ITEMS
with col_right:
    st.markdown('<div class="gothic-panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">⚡ TOP 10 TRENDING (OFF-RANKING)</div>', unsafe_allow_html=True)
    
    trending_sheet = [
        ("Custom Engraved Moon Phase Lamp", "Etsy", "https://www.etsy.com/search?q=moon+lamp"),
        ("Smart Reusable Notebook", "Amazon", "https://www.amazon.com/s?k=Smart+Reusable+Notebook"),
        ("Mushroom Coffee Starter Kit", "TikTok Shop", "https://www.tiktok.com/t/ZT887eX7V/"),
        ("Portable Fabric Shaver", "Amazon", "https://www.amazon.com/s?k=Portable+Fabric+Shaver"),
        ("Silicone Wine Glass Holder", "Etsy", "https://www.etsy.com/search?q=wine+holder"),
        ("Cold Brew Coffee Maker", "TikTok Shop", "https://www.tiktok.com/t/ZT887eX7V/"),
        ("Grant Pevetle Loop Short", "Amazon", "https://www.amazon.com/s?k=Loop+Short"),
        ("Portable Winie Shoer", "Amazon", "https://www.amazon.com/s?k=Portable+Shoer"),
        ("Pilicone Coffee Maker", "TikTok Shop", "https://www.tiktok.com/t/ZT887eX7V/"),
        ("Mushroom Coffee Maker", "TikTok Shop", "https://www.tiktok.com/t/ZT887eX7V/")
    ]
    
    for idx, (t_name, t_src, t_url) in enumerate(trending_sheet, 1):
        st.markdown(f"""
        <div style="margin-bottom: 7px; font-size: 0.82rem;">
            {idx}. <a href="{t_url}" class="product-link" target="_blank">{t_name}</a> <br>
            <span style="color: #666; font-size: 0.72rem;">[{t_src.upper()}]</span>
        </div>
        """, unsafe_allow_html=True)
        if idx < 10:
            st.markdown('<hr style="margin: 4px 0; border: 0.5px solid #221a12;">', unsafe_allow_html=True)
            
    st.markdown('</div>', unsafe_allow_html=True)

# --- LOWER HORIZONTAL RUNNER-UP INVENTORY GRID (RANKS 1-15) ---
st.markdown('<div style="margin-top: 20px; margin-bottom: 10px; font-family:\'Georgia\'; color:#dfc89f; font-size:1.1rem; text-align:center; font-weight:bold; text-transform:uppercase;">Inventory Retail Grid (Select Item to Equip Display)</div>', unsafe_allow_html=True)

grid_cols = st.columns(5)
for i in range(15):
    col_slot = i % 5
    item_node = top_items[i]
    is_equipped = (i == st.session_state.selected_idx)
    
    with grid_cols[col_slot]:
        card_border = "#dfc89f" if is_equipped else "#3a3225"
        card_bg = "rgba(45, 35, 25, 0.45)" if is_equipped else "rgba(10, 10, 10, 0.85)"
        
        st.markdown(f"""
        <div style="border: 2px solid {card_border}; background-color: {card_bg}; padding: 8px; border-radius: 4px; text-align: center; margin-bottom: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.6);">
            <span style="font-size: 0.75rem; color:#dfc89f; font-weight:bold; display:block; margin-bottom:4px;">RANK #{item_node['rank']}</span>
            <img src="{item_node['img']}" style="width:100%; height:110px; object-fit:cover; border-radius:2px; margin-bottom:6px; border:1px solid #2a2218;" />
        """, unsafe_allow_html=True)
        
        # Equip target button
        if st.button(f"Equip {item_node['name'][:14]}...", key=f"equip_btn_{i}"):
            st.session_state.selected_idx = i
            st.rerun()
            
        st.markdown('</div>', unsafe_allow_html=True)

# --- BOT-LEVEL LIVE MONITORING TICKER ---
st.markdown('''
<div class="live-ticker">
    <strong>[ LIVE MONITORING TICKER ]</strong> &nbsp;&nbsp; Spiking Now: Oversized Hoodies (TikTok Shop) &nbsp;&nbsp;•&nbsp;&nbsp; <span style="color:#dfc89f;">🚀 Hot Lead: Magnetic Wireless Car Mount (AliExpress)</span> &nbsp;&nbsp;•&nbsp;&nbsp; Rising Interest: Retro Gaming Consoles (Etsy)...
</div>
''', unsafe_allow_html=True)
