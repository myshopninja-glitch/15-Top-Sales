import streamlit as st
import pandas as pd
import plotly.express as px
import random

# Page config for modern high-density dark dashboard layout
st.set_page_config(page_title="Internet Scavenger", layout="wide", initial_sidebar_state="collapsed")

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

    /* Premium Translucent Glassmorphism Cards */
    .premium-card {
        background: rgba(13, 18, 28, 0.75);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 12px;
        padding: 14px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        margin-bottom: 15px;
    }
    
    .card-title {
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: #94a3b8;
        font-weight: 600;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    /* Micro-Sized Item Tile Grid Matrix Styling */
    .tile-container {
        background: rgba(255, 255, 255, 0.015);
        border: 1px solid rgba(255, 255, 255, 0.04);
        border-radius: 6px;
        padding: 8px;
        text-align: center;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .tile-container:hover {
        transform: translateY(-2px);
        border-color: #00f2fe;
        box-shadow: 0 0 10px rgba(0, 242, 254, 0.15);
    }
    
    .tile-product-title {
        font-size: 0.72rem;
        font-weight: 600;
        color: #ffffff;
        margin-top: 5px;
        margin-bottom: 2px;
        line-height: 1.2;
        height: 2.4em;
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
    }
    
    /* Micro-Trend List Layout Styling */
    .micro-trend-row {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 6px 0;
        border-bottom: 1px solid rgba(255,255,255,0.04);
    }
    .micro-trend-rank {
        font-family: monospace;
        font-weight: 800;
        color: #64748b;
        font-size: 0.8rem;
        width: 24px;
    }
    .micro-trend-title {
        font-size: 0.75rem;
        color: #e2e8f0;
        flex-grow: 1;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    /* Source Platform Badges */
    .platform-tag {
        font-size: 0.58rem;
        font-weight: 700;
        padding: 0px 4px;
        border-radius: 3px;
        display: inline-block;
        margin-bottom: 3px;
        text-transform: uppercase;
        letter-spacing: 0.02em;
    }
    .tag-amazon { background-color: rgba(255, 153, 0, 0.1); color: #ff9900; border: 1px solid rgba(255, 153, 0, 0.2); }
    .tag-etsy { background-color: rgba(241, 100, 30, 0.1); color: #f1641e; border: 1px solid rgba(241, 100, 30, 0.2); }
    .tag-tiktok { background-color: rgba(0, 242, 254, 0.1); color: #00f2fe; border: 1px solid rgba(0, 242, 254, 0.2); }
    .tag-aliexpress { background-color: rgba(230, 0, 51, 0.1); color: #e60033; border: 1px solid rgba(230, 0, 51, 0.2); }

    .tile-img {
        width: 100%;
        height: 85px;
        object-fit: cover;
        border-radius: 4px;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }

    a.clean-anchor {
        text-decoration: none;
        color: inherit;
    }
    a.clean-anchor:hover {
        color: #00f2fe !important;
    }
</style>
''', unsafe_allow_html=True)

# Generate Live Intel Dataset spanning core matrix items and extended macro trending items
@st.cache_data(ttl=10800)
def load_scavenger_intelligence():
    items = [
        # Positions 1 - 15 (Core Grid Matrix)
        {"id": 1, "name": "Minimalist Mechanical Keyboard", "source": "Amazon", "price": "$119.00", "url": "https://www.amazon.com/s?k=Mechanical+Keyboard", "img": "https://images.unsplash.com/photo-1618384887929-16ec33fab9ef?w=600&auto=format&fit=crop&q=80"},
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
        {"id": 15, "name": "High Velocity Desk Fan", "source": "Amazon", "price": "$34.99", "url": "https://www.amazon.com/s?k=Desk+Fan", "img": "https://images.unsplash.com/photo-1618944847828-82e943c3beb5?w=500&auto=format&fit=crop&q=80"},
        
        # Positions 16 - 25 (Top 10 Micro-Trends Widget)
        {"id": 16, "name": "Magnetic Cable Management Blocks", "source": "Amazon", "price": "$19.99"},
        {"id": 17, "name": "Retro Wooden Desk Digital Clock", "source": "Etsy", "price": "$42.50"},
        {"id": 18, "name": "Sunset Projector Atmosphere Night Lamp", "source": "TikTok Shop", "price": "$12.40"},
        {"id": 19, "name": "Foldable Bluetooth Travel Trackpad", "source": "AliExpress", "price": "$24.15"},
        {"id": 20, "name": "Self-Cleaning Insulated Smart Bottle", "source": "Amazon", "price": "$79.00"},
        {"id": 21, "name": "Hand-Poured Soy Wax Aesthetic Candles", "source": "Etsy", "price": "$18.00"},
        {"id": 22, "name": "Viral Volcanic Roller Oil Absorber", "source": "TikTok Shop", "price": "$9.99"},
        {"id": 23, "name": "Miniature Desktop Vacuum Cleaner", "source": "AliExpress", "price": "$7.80"},
        {"id": 24, "name": "Aramids Fiber Ultra-Thin Phone Case", "source": "Amazon", "price": "$49.99"},
        {"id": 25, "name": "Custom Tufted Accent Mug Coasters", "source": "Etsy", "price": "$26.00"}
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

all_retrieved_items = load_scavenger_intelligence()
retrieved_items = all_retrieved_items[0:15]   # Core Top 15
micro_trends_items = all_retrieved_items[15:25] # Extended Top 10 List

if 'selected_day' not in st.session_state:
    st.session_state.selected_day = 'Wed'

prominent_item = retrieved_items[0]

# --- APP SYSTEM TITLE BAR ---
st.markdown('''
<div style="padding: 5px 0; margin-bottom: 5px;">
    <h2 style="margin: 0; font-size: 1.55rem; font-weight: 800; letter-spacing: -0.03em; background: linear-gradient(90deg, #ffffff, #94a3b8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">INTERNET SCAVENGER</h2>
    <p style="margin: 0; font-size: 0.72rem; color: #4caf50; font-family: monospace; letter-spacing: 0.05em;">● TELEMETRY STATUS ONLINE // PERSONAL RESEARCH USE ONLY</p>
</div>
''', unsafe_allow_html=True)


# ==================== HIGH DENSITY TRIPLE COLUMN SYMMETRY ====================
col_left, col_center, col_right = st.columns([0.8, 1.8, 1.1])

with col_left:
    # --- Upper-Most Left: Shrunken 50% Planetary Telemetry ---
    st.markdown('<div class="premium-card" style="height: 250px; display: flex; flex-direction: column; justify-content: center;">', unsafe_allow_html=True)
    st.markdown('<div class="card-title" style="font-size:0.7rem; margin-bottom: 4px;">📡 RECON [SEARCHING]</div>', unsafe_allow_html=True)
    
    st.components.v1.html('''
    <div style="position:relative; width:100%; height: 195px; background:#04060a; border-radius:6px; overflow:hidden; display:flex; justify-content:center; align-items:center;">
        <div style="position:absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 105px; height: 105px; border-radius: 50%; background: url('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Solarsystemscope_texture_8k_earth_daymap.jpg/1024px-Solarsystemscope_texture_8k_earth_daymap.jpg') repeat-x; background-size: auto 100%; animation: rotateEarth 25s linear infinite; box-shadow: inset -22px -12px 30px rgba(0,0,0,0.95), inset 5px 0px 12px rgba(255,255,255,0.2), 0 0 20px rgba(0, 150, 255, 0.4);"></div>
        <canvas id="miniSatCanvas" style="position:absolute; top:0; left:0; width:100%; height:100%; z-index:10; pointer-events:none;"></canvas>
        <script>
            const canvas = document.getElementById('miniSatCanvas'); const ctx = canvas.getContext('2d');
            function res() { canvas.width = canvas.parentElement.clientWidth; canvas.height = canvas.parentElement.clientHeight; }
            window.addEventListener('resize', res); res();
            let ang = 0;
            function run() {
                ctx.clearRect(0,0,canvas.width,canvas.height); const cx=canvas.width/2; const cy=canvas.height/2; ang+=0.015;
                ctx.beginPath(); ctx.ellipse(cx,cy,85,18,0,0,Math.PI*2); ctx.strokeStyle='rgba(0,242,254,0.12)'; ctx.stroke();
                let sx=cx+Math.sin(ang)*85; let sy=cy+Math.cos(ang)*18;
                if(Math.cos(ang)<=0){ ctx.fillStyle="#00f2fe"; ctx.fillRect(sx-2,sy-2,4,4); }
                requestAnimationFrame(run);
            }
            run();
        </script>
    </div>
    <style>@keyframes rotateEarth { from{background-position:0 0;} to{background-position:200% 0;} }</style>
    ''', height=210)
    st.markdown('</div>', unsafe_allow_html=True)


with col_center:
    # --- Top Center: Spotlight #1 Selling Item Box ---
    st.markdown('<div class="premium-card" style="min-height: 250px; text-align: center;">', unsafe_allow_html=True)
    
    # Large Display Picture
    st.markdown(f'''
    <a href="{prominent_item['url']}" target="_blank">
        <img src="{prominent_item['img']}" style="width:100%; height:230px; object-fit:cover; border-radius:8px; border:2px solid #00f2fe; box-shadow: 0 0 15px rgba(0, 242, 254, 0.15);" />
    </a>
    ''', unsafe_allow_html=True)
    
    # Description Placed Directly Below Item Block
    tag_class = f"tag-{prominent_item['source'].lower().replace('.','').replace(' shop','')}"
    st.markdown(f'''
    <div style="padding-top: 12px; border-top: 1px solid rgba(255,255,255,0.04); margin-top:12px; text-align:left;">
        <div class="card-title" style="color: #00f2fe; font-weight:800; margin-bottom:4px;">🥇 ITEM SPOTLIGHT PRIORITY NODE #1</div>
        <h2 style="margin: 0 0 4px 0; font-size:1.35rem; font-weight:800;">
            <a href="{prominent_item['url']}" target="_blank" class="clean-anchor">{prominent_item['name']}</a>
        </h2>
        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:6px;">
            <div>
                <span class="platform-tag {tag_class}" style="font-size:0.65rem; padding:2px 6px;">{prominent_item['source']}</span>
                <span style="font-size:0.75rem; color:#64748b; margin-left:8px;">Estimated Global Value:</span>
                <span style="color:#4caf50; font-size:1.4rem; font-weight:800; margin-left:4px;">{prominent_item['price']}</span>
            </div>
            <a href="{prominent_item['url']}" target="_blank" style="text-decoration:none;">
                <button style="background:linear-gradient(90deg, #7f00ff, #00f2fe); color:white; border:none; padding:5px 12px; border-radius:4px; font-size:0.75rem; font-weight:700; cursor:pointer;">🔗 Store Link</button>
            </a>
        </div>
    </div>
    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


with col_right:
    # --- Top Right & Down: Extended Top 10 Macro-Trends (Outside Top 15 Matrix) ---
    st.markdown('<div class="premium-card" style="height: 515px; overflow-y:auto; padding-right:8px;">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">🔥 TOP 10 EXTENDED MICRO-TRENDS</div>', unsafe_allow_html=True)
    
    for trend in micro_trends_items:
        tag_t = f"tag-{trend['source'].lower().replace('.','').replace(' shop','')}"
        st.markdown(f'''
        <div class="micro-trend-row">
            <span class="micro-trend-rank">#{trend['id']}</span>
            <div class="micro-trend-title">
                <b>{trend['name']}</b><br/>
                <span class="platform-tag {tag_t}" style="font-size:0.5rem; padding:0 3px;">{trend['source']}</span>
                <span style="color:#4caf50; font-weight:600; font-size:0.7rem; margin-left:4px;">{trend['price']}</span>
            </div>
        </div>
        ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ==================== HIGH DENSITY ANALYTICS EXPANSION LAYER ====================
with col_center:
    st.markdown('<div class="premium-card" style="padding: 12px; height: 180px; margin-top:-5px;">', unsafe_allow_html=True)
    
    c_day_col, c_tab_col = st.columns([1.1, 2])
    with c_day_col:
        choice_day = st.radio("Chrono Vector Target:", ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], index=['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].index(st.session_state.selected_day), horizontal=True)
        if choice_day != st.session_state.selected_day:
            st.session_state.selected_day = choice_day
            st.rerun()
            
    with c_tab_col:
        view_tab1, view_tab2 = st.tabs(["7-Day Cumulative Trends", f"Hourly Velocity ({st.session_state.selected_day})"])
    
    with view_tab1:
        fig_7d = px.bar(prominent_item['sales_days'], x='Day', y='Units Sold', color='Units Sold', color_continuous_scale='Purples')
        fig_7d.update_layout(
            plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='#94a3b8',
            margin=dict(l=5, r=5, t=5, b=5), coloraxis_showscale=False, height=100, xaxis_title=None, yaxis_title=None
        )
        st.plotly_chart(fig_7d, use_container_width=True, config={'displayModeBar': False})
        
    with view_tab2:
        fig_24h = px.line(prominent_item['sales_hours'][st.session_state.selected_day], x='Hour', y='Units Sold')
        fig_24h.update_traces(line_color='#00f2fe')
        fig_24h.update_layout(
            plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='#94a3b8',
            margin=dict(l=5, r=5, t=5, b=5), height=100, xaxis_title=None, yaxis_title=None
        )
        st.plotly_chart(fig_24h, use_container_width=True, config={'displayModeBar': False})
    st.markdown('</div>', unsafe_allow_html=True)


# ==================== LOWER MATRIX GRID SYSTEM (ITEMS 2 - 15) ====================
# Fills directly beneath the live radar component on the screen real estate
st.markdown('<hr style="margin: 5px 0 15px 0; border: none; border-top: 1px solid rgba(255,255,255,0.06);"/>', unsafe_allow_html=True)
st.markdown('<h3 style="margin-bottom:12px; font-size:1.0rem; letter-spacing:-0.01em;">📊 RETAIL CORRIDOR EVALUATION MATRIX (POSITIONS 2 - 15)</h3>', unsafe_allow_html=True)

cols_per_row = 5
for i in range(1, len(retrieved_items), cols_per_row):
    row_items = retrieved_items[i:i+cols_per_row]
    grid_cols = st.columns(cols_per_row)
    
    for idx, item in enumerate(row_items):
        with grid_cols[idx]:
            tag_class = f"tag-{item['source'].lower().replace('.','').replace(' shop','')}"
            st.markdown(f'''
            <div class="tile-container">
                <div class="platform-tag {tag_class}">{item['source']}</div>
                <a href="{item['url']}" target="_blank">
                    <img src="{item['img']}" class="tile-img" />
                </a>
                <div class="tile-product-title">
                    <a href="{item['url']}" target="_blank" class="clean-anchor">#{item['id']} {item['name']}</a>
                </div>
                <div style="color:#00f2fe; font-size:0.85rem; font-weight:700; margin-top:2px;">{item['price']}</div>
            </div>
            <div style="margin-bottom: 15px;"></div>
            ''', unsafe_allow_html=True)

```
