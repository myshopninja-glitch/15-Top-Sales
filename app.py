import streamlit as st
import pandas as pd
import plotly.express as px
import random

# Force wide layout and terminal styling
st.set_page_config(page_title="Matrix Data Scraper Terminal", layout="wide", initial_sidebar_state="collapsed")

# Complete Matrix Theme CSS Overhaul
st.markdown('''
<style>
    /* Mainframe Matrix Environment */
    .stApp {
        background-color: #000000;
        color: #00ff66;
        font-family: "Courier New", Courier, monospace;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #33ff77;
        font-family: "Courier New", Courier, monospace;
        text-shadow: 0 0 5px rgba(0, 255, 102, 0.5);
        letter-spacing: 2px;
    }

    /* Secure Terminal Node Pods */
    .terminal-pod {
        background-color: rgba(0, 10, 3, 0.85);
        border: 1px solid #00ff66;
        border-radius: 4px;
        padding: 15px;
        box-shadow: 0 0 10px rgba(0, 255, 102, 0.2);
        margin-bottom: 15px;
        height: 100%;
    }
    
    .pod-header {
        border-bottom: 1px dashed #00ff66;
        padding-bottom: 6px;
        margin-bottom: 15px;
        font-weight: bold;
        color: #33ff77;
        font-size: 0.9rem;
        letter-spacing: 2px;
    }

    /* Product Active Anchor Lines */
    .terminal-link {
        color: #00ff66 !important;
        text-decoration: none;
        font-weight: bold;
    }
    .terminal-link:hover {
        color: #ffffff !important;
        text-shadow: 0 0 8px #00ff66;
    }

    /* Lower Grid Frame System for Private Repository */
    .grid-node-frame {
        border: 1px solid #005511;
        background-color: rgba(0, 5, 2, 0.9);
        border-radius: 2px;
        padding: 10px;
        text-align: center;
    }
    .grid-node-frame.selected {
        border-color: #00ff66;
        background-color: rgba(0, 40, 15, 0.2);
        box-shadow: 0 0 8px rgba(0, 255, 102, 0.4);
    }
    
    /* Interactive Elements Override */
    .stButton>button {
        background: #000000 !important;
        color: #00ff66 !important;
        border: 1px solid #005511 !important;
        border-radius: 2px !important;
        font-family: "Courier New", Courier, monospace !important;
        font-size: 0.75rem !important;
        width: 100%;
    }
    .stButton>button:hover {
        color: #ffffff !important;
        border-color: #00ff66 !important;
        box-shadow: 0 0 6px #00ff66 !important;
    }
</style>
''', unsafe_allow_html=True)

# Dataset Initialization (Single Image per Profile / Verified TikTok Shop API Endpoints)
@st.cache_data
def get_matrix_scraped_data():
    top_15 = [
        {"rank": 1, "name": "Kindle Paperwhite", "source": "Amazon Marketplace", "price": "$139.99", "url": "https://www.amazon.com/s?k=Kindle+Paperwhite", "img": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=500&auto=format&fit=crop&q=80"},
        {"rank": 2, "name": "Yeti Rambler Tumbler", "source": "Amazon Marketplace", "price": "$35.00", "url": "https://www.amazon.com/s?k=Yeti+Rambler+20+oz", "img": "https://images.unsplash.com/photo-1577937927133-66ef06acdf18?w=500&auto=format&fit=crop&q=80"},
        {"rank": 3, "name": "Dyson V8 Vacuum", "source": "Amazon Marketplace", "price": "$399.99", "url": "https://www.amazon.com/s?k=Dyson+V8", "img": "https://images.unsplash.com/photo-1558317374-067fb5f30001?w=500&auto=format&fit=crop&q=80"},
        {"rank": 4, "name": "Apple AirPods Pro", "source": "Amazon Marketplace", "price": "$249.00", "url": "https://www.amazon.com/s?k=AirPods+Pro", "img": "https://images.unsplash.com/photo-1588449668365-d15e397f6787?w=500&auto=format&fit=crop&q=80"},
        {"rank": 5, "name": "Echo Dot 5th Gen", "source": "Amazon Marketplace", "price": "$49.99", "url": "https://www.amazon.com/s?k=Echo+Dot+5th+Gen", "img": "https://images.unsplash.com/photo-1543512214-318c7553f230?w=500&auto=format&fit=crop&q=80"},
        {"rank": 6, "name": "Apple Watch Series 9", "source": "Amazon Marketplace", "price": "$399.00", "url": "https://www.amazon.com/s?k=Apple+Watch+Series+9", "img": "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=500&auto=format&fit=crop&q=80"},
        {"rank": 7, "name": "Stanley Quencher 40oz", "source": "TikTok Shop Official", "price": "$45.00", "url": "https://www.tiktok.com/", "img": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=500&auto=format&fit=crop&q=80"},
        {"rank": 8, "name": "Gothic Heavy Hoodie", "source": "TikTok Shop Official", "price": "$49.99", "url": "https://www.tiktok.com/", "img": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=500&auto=format&fit=crop&q=80"},
        {"rank": 9, "name": "Mielle Rosemary Oil", "source": "TikTok Shop Official", "price": "$10.20", "url": "https://www.tiktok.com/", "img": "https://images.unsplash.com/photo-1608248597481-496100c80836?w=500&auto=format&fit=crop&q=80"},
        {"rank": 10, "name": "Custom Name Necklace", "source": "Etsy Marketplace", "price": "$28.00", "url": "https://www.etsy.com/", "img": "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500&auto=format&fit=crop&q=80"},
        {"rank": 11, "name": "Handmade Soy Candles", "source": "Etsy Marketplace", "price": "$18.50", "url": "https://www.etsy.com/", "img": "https://images.unsplash.com/photo-1603006905003-be475563bc59?w=500&auto=format&fit=crop&q=80"},
        {"rank": 12, "name": "Minimalist Leather Wallet", "source": "Etsy Marketplace", "price": "$42.00", "url": "https://www.etsy.com/", "img": "https://images.unsplash.com/photo-1627123424574-724758594e93?w=500&auto=format&fit=crop&q=80"},
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

top_items = get_matrix_scraped_data()

# Manage Terminal Frame States
if 'selected_idx' not in st.session_state:
    st.session_state.selected_idx = 0
if 'drill_day' not in st.session_state:
    st.session_state.drill_day = 'Wed'

curr_item = top_items[st.session_state.selected_idx]

# --- MAINFRAME HEADER ASSEMBLY ---
st.markdown('''
<div style="display: flex; justify-content: space-between; align-items: flex-end; padding: 2px 0;">
    <h2 style="margin: 0; font-size: 1.3rem; font-weight: normal; color:#00ff66;">
        :: PRIVATE_RESEARCH_MAINFRAME // TERMINAL_ACTIVE
    </h2>
    <div style="font-size:0.85rem; color:#008833; font-family: monospace;">SYS_REFRESH_CYCLE: <span style="color:#00ff66; font-weight:bold;">3.00 HR</span></div>
</div>
<hr style="border: 1px solid #005511; margin-top: 4px; margin-bottom: 15px;">
''', unsafe_allow_html=True)

# --- TERMINAL MATRIX COLUMN LAYOUT ---
col_left, col_center, col_right = st.columns([1.2, 1.8, 1.0])

# 1. LEFT PANEL: STREAMING DIGITAL DECRYPTION CANVAS
with col_left:
    st.markdown('<div class="terminal-pod">', unsafe_allow_html=True)
    st.markdown('<div class="pod-header">> SCRAPE_ENGINES_STREAM</div>', unsafe_allow_html=True)
    
    # Custom HTML5 Phosphor Green Digital Rain Matrix simulation
    st.components.v1.html('''
    <div style="position:relative; width:100%; height:255px; background:#000000; border:1px solid #005511; overflow:hidden;">
        <canvas id="matrixRain" style="position:absolute; top:0; left:0; width:100%; height:100%;"></canvas>
    </div>
    <script>
        const canvas = document.getElementById('matrixRain');
        const ctx = canvas.getContext('2d');
        
        function resize() {
            canvas.width = canvas.parentElement.clientWidth;
            canvas.height = canvas.parentElement.clientHeight;
        }
        resize();

        const letters = "0101010101110010_STREAM_DATA_AMZN_ETSY_TT_SHOP_";
        const alphabet = letters.split("");
        const fontSize = 11;
        const columns = canvas.width / fontSize;
        const rainDrops = Array.from({ length: columns }).fill(1);

        function draw() {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.08)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            ctx.fillStyle = '#00ff66';
            ctx.font = fontSize + 'px monospace';

            for(let i = 0; i < rainDrops.length; i++) {
                const text = alphabet[Math.floor(Math.random() * alphabet.length)];
                ctx.fillText(text, i*fontSize, rainDrops[i]*fontSize);
                
                if(rainDrops[i]*fontSize > canvas.height && Math.random() > 0.975){
                    rainDrops[i] = 0;
                }
                rainDrops[i]++;
            }
        }
        setInterval(draw, 33);
    </script>
    ''', height=260)
    st.markdown('</div>', unsafe_allow_html=True)

# 2. CENTER PANEL: CORE NODE INSPECTOR (Single-Image Signature Architecture)
with col_center:
    st.markdown('<div class="terminal-pod">', unsafe_allow_html=True)
    st.markdown(f'<div class="pod-header">> DETECTED_NODE_METRICS // RANK_{curr_item["rank"]}</div>', unsafe_allow_html=True)
    
    img_col, info_col = st.columns([1.0, 1.4])
    with img_col:
        st.markdown(f'''
            <a href="{curr_item["url"]}" target="_blank" style="text-decoration:none; display:block; text-align:center;">
                <div style="border:1px solid #00ff66; background-color:#000000; padding:4px;">
                    <img src="{curr_item["img"]}" style="width:100%; max-height:160px; object-fit:contain;" />
                </div>
            </a>
        ''', unsafe_allow_html=True)
    with info_col:
        st.markdown(f'<h3 style="margin-top:0; margin-bottom:6px; font-size:1.1rem;"><a href="{curr_item["url"]}" class="terminal-link" target="_blank">{curr_item["name"]}</a></h3>', unsafe_allow_html=True)
        st.markdown(f"<span style='color:#008833;'>SRC_PIPELINE:</span> <span style='color:#00ff66;'>{curr_item['source']}</span>", unsafe_allow_html=True)
        st.markdown(f"<span style='color:#008833;'>VAL_MARKER:</span> <span style='color:#33ff77; font-weight:bold;'>{curr_item['price']}</span>", unsafe_allow_html=True)
        
        st.markdown(f'''
            <a href="{curr_item["url"]}" target="_blank" style="text-decoration: none;">
                <div style="background: #000000; color: #00ff66; text-align: center; padding: 6px; border: 1px solid #00ff66; border-radius: 2px; font-weight: bold; cursor: pointer; margin-top: 25px; font-size: 0.75rem; letter-spacing:1px;">
                    :: EXECUTE_OUTBOUND_ROUTING_ROUTER
                </div>
            </a>
        ''', unsafe_allow_html=True)

    st.markdown('<hr style="border:0.5px dashed #005511; margin:15px 0;">', unsafe_allow_html=True)
    
    # 7-Day Interactive Matrix Selection Ribbon
    st.markdown(f"<div style='text-align:center; font-size:0.72rem; color:#008833; margin-bottom:10px;'>INTERACTIVE MATRIX SELECTION -> TARGET_DAY: [{st.session_state.drill_day}]</div>", unsafe_allow_html=True)
    days_list = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    cols_bars = st.columns(7)
    for idx, day_lbl in enumerate(days_list):
        with cols_bars[idx]:
            day_data = curr_item['sales_days'][curr_item['sales_days']['Day'] == day_lbl].iloc[0]
            if st.button(f"{day_lbl}\n[{day_data['Units Sold']}]", key=f"matrix_bar_{day_lbl}"):
                st.session_state.drill_day = day_lbl
                st.rerun()

    # Plotly Graph Contextually Colored Neon Green
    fig_hours = px.line(curr_item['sales_hours'][st.session_state.drill_day], x='Hour', y='Units Sold', markers=True)
    fig_hours.update_traces(line_color='#00ff66', marker=dict(size=4, color='#ffffff'))
    fig_hours.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='#008833', height=100, margin=dict(l=5, r=5, t=5, b=5))
    fig_hours.update_xaxes(showgrid=False, tickfont=dict(size=8, color='#00aa44'))
    fig_hours.update_yaxes(showgrid=False, tickfont=dict(size=8, color='#00aa44'))
    st.plotly_chart(fig_hours, use_container_width=True, config={'displayModeBar': False})

    st.markdown('</div>', unsafe_allow_html=True)

# 3. RIGHT PANEL: OFF-RANK TREND ANALYSIS MATRIX (Strictly Text-Only Lists)
with col_right:
    st.markdown('<div class="terminal-pod">', unsafe_allow_html=True)
    st.markdown('<div class="pod-header">> UNINDEXED_TREND_VELOCITY</div>', unsafe_allow_html=True)
    
    trending_sheet = [
        ("Custom Engraved Moon Phase Lamp", "Etsy Marketplace", "https://www.etsy.com/"),
        ("Smart Reusable Notebook", "Amazon Marketplace", "https://www.amazon.com/"),
        ("Mushroom Coffee Starter Kit", "TikTok Shop Official", "https://www.tiktok.com/"),
        ("Portable Fabric Shaver", "Amazon Marketplace", "https://www.amazon.com/"),
        ("Silicone Wine Glass Holder", "Etsy Marketplace", "https://www.etsy.com/"),
        ("Cold Brew Coffee Maker", "TikTok Shop Official", "https://www.tiktok.com/"),
        ("Grant Pevetle Loop Short", "Amazon Marketplace", "https://www.amazon.com/"),
        ("Portable Winie Shoer", "Amazon Marketplace", "https://www.amazon.com/"),
        ("Silicone Coffee Maker", "TikTok Shop Official", "https://www.tiktok.com/"),
        ("Mushroom Coffee Maker", "TikTok Shop Official", "https://www.tiktok.com/")
    ]
    
    for idx, (t_name, t_src, t_url) in enumerate(trending_sheet, 1):
        st.markdown(f"""
        <div style="margin-bottom: 4px; font-size: 0.78rem; line-height:1.3;">
            [{idx:02d}] <a href="{t_url}" class="terminal-link" target="_blank">{t_name}</a> 
            <br><span style="color: #005511; font-size: 0.68rem; padding-left: 28px;">>> {t_src.upper()}</span>
        </div>
        """, unsafe_allow_html=True)
        if idx < 10:
            st.markdown('<hr style="margin: 4px 0; border: 0.5px solid #002205;">', unsafe_allow_html=True)
            
    st.markdown('</div>', unsafe_allow_html=True)

# --- LOWER HORIZONTAL REPOSITORY GRID MATCHING TOTAL SELECTION POOL (RANKS 1-15) ---
st.markdown('<div style="margin-top: 15px; margin-bottom: 8px; font-size:0.85rem; text-align:center; color:#00ff66;">========================= INTERNAL_DATAFRAME_REPOSITORIES =========================</div>', unsafe_allow_html=True)

grid_cols = st.columns(5)
for i in range(15):
    col_slot = i % 5
    item_node = top_items[i]
    is_equipped = (i == st.session_state.selected_idx)
    selected_cls = "selected" if is_equipped else ""
    
    with grid_cols[col_slot]:
        st.markdown(f"""
        <div class="grid-node-frame {selected_cls}">
            <div style="font-size:0.7rem; color:#00ff66; margin-bottom:4px; font-weight:bold;">NODE_[{item_node['rank']:02d}]</div>
            <a href="{item_node['url']}" target="_blank" style="text-decoration:none; display:block; margin-bottom:5px;">
                <img src="{item_node['img']}" style="width:100%; height:75px; object-fit:cover; border:1px solid #005511;" />
                <div style="font-size:0.7rem; margin-top:3px; color:#33ff77; text-overflow:ellipsis; white-space:nowrap; overflow:hidden;">{item_node['name']}</div>
            </a>
        """, unsafe_allow_html=True)
        
        if st.button(f"CONNECT_{item_node['rank']:02d}", key=f"node_connect_btn_{i}"):
            st.session_state.selected_idx = i
            st.rerun()
            
        st.markdown('</div>', unsafe_allow_html=True)
