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

    /* Gothic UI Panel Frames matching the golden-brown borders of D2 LOD */
    .gothic-panel {
        background-color: #121212;
        border: 2px solid #3a3124;
        border-top: 2px solid #554733;
        border-bottom: 2px solid #282118;
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

    /* Thumbnail frame highlights exactly like item sockets */
    .thumb-frame {
        border: 2px solid #3a3124;
        background-color: #090909;
        padding: 2px;
        border-radius: 4px;
        display: inline-block;
        transition: border-color 0.2s ease;
    }
    .thumb-frame.active {
        border-color: #e5a93c;
        box-shadow: 0 0 8px rgba(229, 169, 60, 0.4);
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

    /* Lower Inventory Item Cards */
    .inventory-card-frame {
        border: 2px solid #3a3124;
        background-color: rgba(14, 14, 14, 0.85);
        border-radius: 3px;
        padding: 6px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.9);
    }
    .inventory-card-frame.equipped {
        border-color: #dfc89f;
        background-color: rgba(45, 34, 23, 0.4);
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
    
    /* Override standard streamlit button layouts to keep them immersive */
    .stButton>button {
        background: linear-gradient(to bottom, #3a3124 0%, #1b1610 100%) !important;
        color: #dfc89f !important;
        border: 1px solid #554733 !important;
        border-radius: 2px !important;
        font-family: "Georgia", serif !important;
        font-size: 0.8rem !important;
        transition: all 0.1s ease-in-out;
    }
    .stButton>button:hover {
        color: #ffffff !important;
        border-color: #dfc89f !important;
        background: linear-gradient(to bottom, #4a3f2e 0%, #231d15 100%) !important;
    }
</style>
''', unsafe_allow_html=True)

# Dataset Initialization
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

# Manage UI Presentation State Engine
if 'selected_idx' not in st.session_state:
    st.session_state.selected_idx = 0
if 'drill_day' not in st.session_state:
    st.session_state.drill_day = 'Wed'
if 'selected_thumb' not in st.session_state:
    st.session_state.selected_thumb = 0

curr_item = top_items[st.session_state.selected_idx]

# --- HEADER ASSEMBLY ---
st.markdown('''
<div style="display: flex; justify-content: space-between; align-items: flex-end; padding: 2px 0;">
    <h2 style="margin: 0; font-size: 1.45rem; font-weight: normal; font-family:'Georgia';">(💀) INTERNET SCAVENGER <span style="font-size:0.65em; color:#4caf50; font-family:monospace;">[LIVE METRIC SESSION]</span></h2>
    <div style="font-size:0.82rem; color:#858585; font-family: monospace;">NEXT REFRESH CYCLE IN: <span style="color:#dfc89f; font-weight:bold;">1h 25m</span></div>
</div>
<hr style="border: 1px solid #3a3124; margin-top: 4px; margin-bottom: 15px;">
''', unsafe_allow_html=True)

# --- PANEL COLUMN GRID ---
col_left, col_center, col_right = st.columns([1.35, 1.65, 1.1])

# 1. LEFT PANEL: SEARCHING (Isometric Canvas with Traveling Necromancer Character Sprite)
with col_left:
    st.markdown('<div class="gothic-panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">SEARCHING</div>', unsafe_allow_html=True)
    
    # HTML5 Canvas Injector running real-time scrying loops tracking market outposts
    st.components.v1.html('''
    <div style="position:relative; width:100%; height:275px; background:#040404; border:1px solid #2e261c; overflow:hidden;">
        <canvas id="isometricCanvas" style="position:absolute; top:0; left:0; width:100%; height:100%;"></canvas>
        <div style="position:absolute; top:12px; left:12px; font-family:monospace; font-size:11px; color:#68a368; background:rgba(0,0,0,0.85); padding:6px; border:1px solid #3a3124;">
            ✨ Active Scrying: Necromancer crawling realms...
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

        function isoProject(x, y, z=0) {
            const centerX = canvas.width / 2;
            const centerY = canvas.height / 2 - 15;
            return {
                x: centerX + (x - y) * 0.82,
                y: centerY + (x + y) * 0.42 - z
            };
        }

        const nodes = [
            {name: "amazon.com", x: -75, y: -65, color: "#e59422"},
            {name: "etsy.com", x: -65, y: 70, color: "#d9531e"},
            {name: "tiktok.com", x: 75, y: -65, color: "#17c2cc"},
            {name: "SCAVENGER ALTAR", x: 0, y: 0, color: "#dfc89f"}
        ];

        // Necromancer configuration wandering between marketplace nodes
        const necro = {
            currentPath: 0,
            prog: 0.0,
            speed: 0.006,
            forward: true,
            pulse: 0
        };

        function runLoop() {
            ctx.clearRect(0,0,canvas.width,canvas.height);
            necro.pulse += 0.05;
            
            // Draw runic paths
            ctx.lineWidth = 1.5;
            for(let i=0; i<3; i++) {
                const pStart = isoProject(nodes[3].x, nodes[3].y);
                const pEnd = isoProject(nodes[i].x, nodes[i].y);
                let grad = ctx.createLinearGradient(pStart.x, pStart.y, pEnd.x, pEnd.y);
                grad.addColorStop(0, "rgba(141, 113, 80, 0.4)");
                grad.addColorStop(1, "rgba(40, 30, 20, 0.05)");
                ctx.strokeStyle = grad;
                ctx.beginPath();
                ctx.moveTo(pStart.x, pStart.y);
                ctx.lineTo(pEnd.x, pEnd.y);
                ctx.stroke();
            }

            // Draw Outposts
            nodes.forEach(n => {
                const pt = isoProject(n.x, n.y);
                ctx.fillStyle = "#0c0a08";
                ctx.strokeStyle = "#4a3f2e";
                ctx.lineWidth = 2;
                ctx.beginPath();
                ctx.rect(pt.x - 8, pt.y - 8, 16, 16);
                ctx.fill();
                ctx.stroke();
                
                ctx.fillStyle = n.color;
                ctx.beginPath();
                ctx.arc(pt.x, pt.y, 3, 0, Math.PI*2);
                ctx.fill();

                ctx.font = "10px monospace";
                ctx.fillStyle = "#dfc89f";
                ctx.textAlign = "center";
                ctx.fillText(n.name, pt.x, pt.y + 22);
            });

            // Update & Animate Necromancer Sprite representation
            if(necro.forward) {
                necro.prog += necro.speed;
                if(necro.prog >= 1.0) { necro.forward = false; }
            } else {
                necro.prog -= necro.speed;
                if(necro.prog <= 0.0) {
                    necro.forward = true;
                    necro.currentPath = (necro.currentPath + 1) % 3;
                }
            }

            const startNode = nodes[3];
            const endNode = nodes[necro.currentPath];
            const nx = startNode.x + (endNode.x - startNode.x) * necro.prog;
            const ny = startNode.y + (endNode.y - startNode.y) * necro.prog;
            const nPt = isoProject(nx, ny, 6);

            // Draw Cloaked Necromancer Model
            ctx.fillStyle = "#4a1212"; // Deep dark red robe
            ctx.beginPath();
            ctx.moveTo(nPt.x, nPt.y - 12); // Hood peak
            ctx.lineTo(nPt.x - 5, nPt.y + 2);
            ctx.lineTo(nPt.x + 5, nPt.y + 2);
            ctx.closePath();
            ctx.fill();

            // Scrying Orb Energy Glow
            ctx.fillStyle = "#52b752";
            ctx.shadowColor = "#52b752";
            ctx.shadowBlur = 8 + Math.sin(necro.pulse) * 4;
            ctx.beginPath();
            ctx.arc(nPt.x, nPt.y - 4, 2.5, 0, Math.PI*2);
            ctx.fill();
            ctx.shadowBlur = 0;

            requestAnimationFrame(runLoop);
        }
        runLoop();
    </script>
    ''', height=280)
    st.markdown('</div>', unsafe_allow_html=True)

# 2. CENTER PANEL: MAIN ALTAR WITH DETAILED VIEWS CAROUSEL GRID
with col_center:
    st.markdown('<div class="gothic-panel">', unsafe_allow_html=True)
    st.markdown(f'<div class="panel-title">🏆 RANK #{curr_item["rank"]} DISPLAY</div>', unsafe_allow_html=True)
    
    img_col, info_col = st.columns([1.1, 1.3])
    with img_col:
        # Single-click direct hyperlink mapping over the product artwork frame
        st.markdown(f'''
            <a href="{curr_item["url"]}" target="_blank" style="text-decoration:none; display:block; text-align:center;">
                <div style="border:3px solid #4a3f2e; background-color:#050505; padding:4px; box-shadow:0 0 15px #000; display:inline-block; width:100%;">
                    <img src="{curr_item["img"]}" style="width:100%; max-height:165px; object-fit:contain;" />
                </div>
            </a>
        ''', unsafe_allow_html=True)
    with info_col:
        # Title acts as a direct standalone anchor bypass 
        st.markdown(f'<h3 style="margin-top:0; margin-bottom:6px; font-size:1.15rem;"><a href="{curr_item["url"]}" class="product-link" target="_blank">{curr_item["name"]}</a></h3>', unsafe_allow_html=True)
        st.markdown(f"<span style='color:#8c7d67;'>Source:</span> <span style='color:#dfc89f;'>{curr_item['source']}</span>", unsafe_allow_html=True)
        st.markdown(f"<span style='color:#8c7d67;'>Price:</span> <span style='color:#4caf50; font-weight:bold; font-size:1.1rem;'>{curr_item['price']}</span>", unsafe_allow_html=True)
        
        # Immediate outbound gateway option
        st.markdown(f'''
            <a href="{curr_item["url"]}" target="_blank" style="text-decoration: none;">
                <div style="background: linear-gradient(to bottom, #3b3124, #1c1711); color: #dfc89f; text-align: center; padding: 6px; border: 1px solid #554733; border-radius: 2px; font-weight: bold; cursor: pointer; margin-top: 12px; font-family: Georgia, serif; font-size: 0.8rem; letter-spacing:0.5px;">
                    🔗 Direct Link to Storefront
                </div>
            </a>
        ''', unsafe_allow_html=True)

    # Detailed Views Carousel Selectors Grid matching item socket lookups
    st.markdown('<div style="font-size:0.75rem; color:#8c7d67; margin-top:12px; margin-bottom:4px; font-family:Georgia;">Detailed Views (Click to zoom):</div>', unsafe_allow_html=True)
    thumb_cols = st.columns(5)
    for t_idx in range(5):
        with thumb_cols[t_idx]:
            is_thumb_active = (t_idx == st.session_state.selected_thumb)
            border_cls = "active" if is_thumb_active else ""
            
            # Encapsulate thumbnail layout inside safe programmatic rerun state triggers
            st.markdown(f'''
                <div class="thumb-frame {border_cls}" style="width:100%; text-align:center;">
                    <img src="{curr_item["img"]}" style="width:100%; height:32px; object-fit:cover; opacity:{'1.0' if is_thumb_active else '0.55'};" />
                </div>
            ''', unsafe_allow_html=True)
            if st.button("🔍", key=f"thumb_trigger_{t_idx}"):
                st.session_state.selected_thumb = t_idx
                st.rerun()

    st.markdown('<hr style="border:0.5px dashed #3a3124; margin:12px 0;">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title" style="font-size:0.85rem; margin-bottom:8px;">📊 SALES METRIC GRAPH</div>', unsafe_allow_html=True)
    
    # 7-Day Interactive Custom Component Drilldown Setup
    days_list = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    max_units = curr_item['sales_days']['Units Sold'].max()
    
    cols_bars = st.columns(7)
    for idx, day_lbl in enumerate(days_list):
        with cols_bars[idx]:
            day_data = curr_item['sales_days'][curr_item['sales_days']['Day'] == day_lbl].iloc[0]
            units = day_data['Units Sold']
            
            is_active = (day_lbl == st.session_state.drill_day)
            lbl_color = "#e5a93c" if is_active else "#dfc89f"
            
            if st.button(f"{day_lbl}\n({units})", key=f"bar_trigger_{day_lbl}"):
                st.session_state.drill_day = day_lbl
                st.rerun()

    # Dynamic line layer parsing hourly distributions safely underneath
    fig_hours = px.line(curr_item['sales_hours'][st.session_state.drill_day], x='Hour', y='Units Sold', markers=True)
    fig_hours.update_traces(line_color='#e59422', marker=dict(size=4, color='#dfc89f'))
    fig_hours.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='#a6967d', height=105, margin=dict(l=5, r=5, t=5, b=5))
    fig_hours.update_xaxes(showgrid=False, tickfont=dict(size=8))
    fig_hours.update_yaxes(showgrid=False, tickfont=dict(size=8))
    st.plotly_chart(fig_hours, use_container_width=True, config={'displayModeBar': False})

    st.markdown('</div>', unsafe_allow_html=True)

# 3. RIGHT PANEL: TOP 10 TRENDING ITEMS (With direct functional outbound hyperlinks)
with col_right:
    st.markdown('<div class="gothic-panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">⚡ TOP 10 TRENDING</div>', unsafe_allow_html=True)
    
    trending_sheet = [
        ("Custom Engraved Moon Lamp", "Etsy", "https://www.etsy.com/search?q=moon+lamp"),
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
        <div style="margin-bottom: 5px; font-size: 0.78rem; line-height:1.2;">
            {idx}. <a href="{t_url}" class="product-link" target="_blank">{t_name}</a> <br>
            <span style="color: #615647; font-size: 0.68rem; font-family:monospace;">[{t_src.upper()}]</span>
        </div>
        """, unsafe_allow_html=True)
        if idx < 10:
            st.markdown('<hr style="margin: 3px 0; border: 0.5px solid #282118;">', unsafe_allow_html=True)
            
    st.markdown('</div>', unsafe_allow_html=True)

# --- LOWER HORIZONTAL RUNNER-UP INVENTORY GRID (RANKS 1-15) ---
st.markdown('<div style="margin-top: 15px; margin-bottom: 8px; font-family:\'Georgia\'; color:#dfc89f; font-size:1.0rem; text-align:center; text-transform:uppercase; letter-spacing:1px;">Inventory Retail Grid (Equip Item to Altar)</div>', unsafe_allow_html=True)

grid_cols = st.columns(5)
for i in range(15):
    col_slot = i % 5
    item_node = top_items[i]
    is_equipped = (i == st.session_state.selected_idx)
    
    with grid_cols[col_slot]:
        equipped_cls = "equipped" if is_equipped else ""
        
        st.markdown(f"""
        <div class="inventory-card-frame {equipped_cls}">
            <div style="font-size: 0.72rem; color:#dfc89f; font-family:Georgia; margin-bottom:3px; font-weight:bold;">RANK #{item_node['rank']}</div>
            <a href="{item_node['url']}" target="_blank" style="text-decoration:none; display:block; margin-bottom:4px;">
                <img src="{item_node['img']}" style="width:100%; height:75px; object-fit:cover; border:1px solid #3a3124; border-radius:2px;" />
            </a>
        """, unsafe_allow_html=True)
        
        if st.button(f"Equip #{item_node['rank']}", key=f"equip_btn_{i}"):
            st.session_state.selected_idx = i
            st.rerun()
            
        st.markdown('</div>', unsafe_allow_html=True)

# --- BOT-LEVEL LIVE MONITORING TICKER ---
st.markdown('''
<div class="live-ticker">
    <strong>[ LIVE MONITORING TICKER ]</strong> &nbsp;&nbsp; Spiking Now: Oversized Hoodies (TikTok Shop) &nbsp;&nbsp;•&nbsp;&nbsp; <span style="color:#dfc89f;">🚀 Hot Lead: Magnetic Wireless Car Mount (AliExpress)</span> &nbsp;&nbsp;•&nbsp;&nbsp; Rising Interest: Retro Gaming Consoles (Etsy)...
</div>
''', unsafe_allow_html=True)
