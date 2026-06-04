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
        padding: 16px;
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
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    /* Micro-Sized Item Tile Grid Matrix Styling (Half Size) */
    .tile-container {
        background: rgba(255, 255, 255, 0.015);
        border: 1px solid rgba(255, 255, 255, 0.04);
        border-radius: 6px;
        padding: 6px;
        text-align: center;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .tile-container:hover {
        transform: translateY(-2px);
        border-color: #00f2fe;
        box-shadow: 0 0 10px rgba(0, 242, 254, 0.15);
    }
    
    /* Highly Compact Product Placement underneath picture */
    .tile-product-title {
        font-size: 0.7rem;
        font-weight: 600;
        color: #ffffff;
        margin-top: 4px;
        margin-bottom: 2px;
        line-height: 1.2;
        height: 2.4em;
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
    }
    
    /* Source Platform Badges */
    .platform-tag {
        font-size: 0.6rem;
        font-weight: 700;
        padding: 0px 4px;
        border-radius: 3px;
        display: inline-block;
        margin-bottom: 4px;
        text-transform: uppercase;
        letter-spacing: 0.02em;
    }
    .tag-amazon { background-color: rgba(255, 153, 0, 0.12); color: #ff9900; border: 1px solid rgba(255, 153, 0, 0.25); }
    .tag-etsy { background-color: rgba(241, 100, 30, 0.12); color: #f1641e; border: 1px solid rgba(241, 100, 30, 0.25); }
    .tag-tiktok { background-color: rgba(0, 242, 254, 0.12); color: #00f2fe; border: 1px solid rgba(0, 242, 254, 0.25); }
    .tag-aliexpress { background-color: rgba(230, 0, 51, 0.12); color: #e60033; border: 1px solid rgba(230, 0, 51, 0.25); }

    /* Downscaled Tile Image Configuration */
    .tile-img {
        width: 100%;
        height: 60px;
        object-fit: cover;
        border-radius: 4px;
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

    /* Micro Action Triggers */
    .reduced-btn-wrapper .stButton>button {
        background: rgba(255, 255, 255, 0.04) !important;
        color: #94a3b8 !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 3px !important;
        padding: 0px 4px !important;
        font-size: 0.65rem !important;
        min-height: unset !important;
        height: 18px !important;
        width: 90% !important;
        margin: 0 auto !important;
        display: block !important;
        line-height: 1.1 !important;
        transition: all 0.2s ease;
    }
    .reduced-btn-wrapper .stButton>button:hover {
        background: #00f2fe !important;
        color: #07090e !important;
        border-color: #00f2fe !important;
        box-shadow: 0 0 6px rgba(0, 242, 254, 0.3) !important;
    }

    /* Infinite Scrolling Marquee Styles */
    .marquee-wrapper {
        width: 100%;
        overflow: hidden;
        white-space: nowrap;
        box-sizing: border-box;
        mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent);
        -webkit-mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent);
    }
    .marquee-content {
        display: inline-block;
        animation: marquee 25s linear infinite;
        font-family: monospace;
        font-size: 0.75rem;
        color: #00f2fe;
    }
    .marquee-content span {
        margin-right: 30px;
    }
    @keyframes marquee {
        0%   { transform: translate(0, 0); }
        100% { transform: translate(-50%, 0); }
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
        <h2 style="margin: 0; font-size: 1.55rem; font-weight: 800; letter-spacing: -0.03em; background: linear-gradient(90deg, #ffffff, #94a3b8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">INTERNET SCAVENGER</h2>
        <p style="margin: 0; font-size: 0.72rem; color: #4caf50; font-family: monospace; letter-spacing: 0.05em;">● TELEMETRY STATUS ONLINE // PERSONAL RESEARCH USE ONLY</p>
    </div>
</div>
''', unsafe_allow_html=True)


# ==================== UPPER LAYOUT: ASYMMETRICAL 3-COLUMN REORGANIZATION ====================
col_left, col_center, col_right = st.columns([1.4, 1.7, 1.1])

with col_left:
    # --- Expanded Photorealistic Earth & Scrolling Marquee ---
    st.markdown('<div class="premium-card" style="height: 485px; display: flex; flex-direction: column;">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">📡 LIVE PLANETARY RECONNAISSANCE &nbsp;<span style="color:#00f2fe;">[STATUS: SEARCHING...]</span></div>', unsafe_allow_html=True)
    
    st.components.v1.html('''
    <div style="position:relative; width:100%; flex-grow: 1; height: 350px; background:#04060a; border-radius:8px; border:1px solid rgba(255,255,255,0.04); overflow:hidden; display:flex; justify-content:center; align-items:center;">
        
        <div style="position:absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 170px; height: 170px; border-radius: 50%; background: url('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Solarsystemscope_texture_8k_earth_daymap.jpg/1024px-Solarsystemscope_texture_8k_earth_daymap.jpg') repeat-x; background-size: auto 100%; animation: rotateEarth 25s linear infinite; box-shadow: inset -30px -15px 40px rgba(0,0,0,0.9), inset 5px 0px 15px rgba(255,255,255,0.2), 0 0 25px rgba(0, 180, 255, 0.3);"></div>
        
        <canvas id="satCanvas" style="position:absolute; top:0; left:0; width:100%; height:100%; z-index:10; pointer-events:none;"></canvas>
        
        <style>
        @keyframes rotateEarth {
            from { background-position: 0 0; }
            to { background-position: 200% 0; }
        }
        </style>

        <script>
            const canvas = document.getElementById('satCanvas');
            const ctx = canvas.getContext('2d');
            function resize() {
                canvas.width = canvas.parentElement.clientWidth;
                canvas.height = canvas.parentElement.clientHeight;
            }
            window.addEventListener('resize', resize);
            resize();

            let orbitAngle = 0;
            let signalPulses = [];

            function render() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                const cx = canvas.width / 2;
                const cy = canvas.height / 2;
                const r = 85; // Matches the 170px Earth CSS diameter

                orbitAngle += 0.012; // Satellite Speed

                // Faint orbital ring trajectory
                ctx.beginPath();
                ctx.ellipse(cx, cy, r + 50, 30, 0, 0, Math.PI * 2);
                ctx.strokeStyle = 'rgba(0, 242, 254, 0.1)';
                ctx.lineWidth = 1;
                ctx.stroke();

                // Compute exact 3D elliptical coordinates
                let satX = cx + Math.sin(orbitAngle) * (r + 50);
                let satY = cy + Math.cos(orbitAngle) * 30;
                let satelliteIsBehind = Math.cos(orbitAngle) > 0;

                // Fire Telemetry Laser Pings onto Earth Surface
                if (!satelliteIsBehind && Math.random() < 0.08) {
                    signalPulses.push({ x: satX, y: satY, tx: cx + (Math.random() - 0.5) * (r-10), ty: cy + (Math.random() - 0.5) * (r-10), life: 1.0 });
                }

                signalPulses.forEach((pulse, idx) => {
                    pulse.life -= 0.03;
                    if (pulse.life <= 0) { signalPulses.splice(idx, 1); return; }
                    ctx.strokeStyle = `rgba(0, 242, 254, ${pulse.life})`;
                    ctx.lineWidth = 1.5;
                    ctx.beginPath(); ctx.moveTo(pulse.x, pulse.y); ctx.lineTo(pulse.tx, pulse.ty); ctx.stroke();
                });

                // Render Satellite only when traversing the front hemisphere (creates 3D depth)
                if (!satelliteIsBehind) {
                    ctx.fillStyle = "#00f2fe";
                    ctx.fillRect(satX - 14, satY - 2, 8, 4);
                    ctx.fillRect(satX + 6, satY - 2, 8, 4);
                    ctx.fillStyle = "#7f00ff";
                    ctx.fillRect(satX - 4, satY - 4, 8, 8);
                    ctx.fillStyle = "#ffffff";
                    ctx.beginPath(); ctx.arc(satX, satY, 1.5, 0, Math.PI*2); ctx.fill();
                }
                requestAnimationFrame(render);
            }
            render();
        </script>
    </div>
    
    <div style="margin-top: 16px; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 12px;">
        <div style="font-size: 0.65rem; color: #94a3b8; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.05em; font-weight: 700;">📡 Live Intercept Stream</div>
        <div class="marquee-wrapper">
            <div class="marquee-content">
                <span>• Graphene Power Bank [Amazon]</span>
                <span>• Holographic Keyboard [TikTok Shop]</span>
                <span>• Levitating Desk Lamp [Etsy]</span>
                <span>• Bone Conduction Glasses [Amazon]</span>
                <span>• AI Posture Corrector [TikTok Shop]</span>
                <span>• Pocket Retro Handheld [AliExpress]</span>
                <span>• Heated Mouse Pad [Amazon]</span>
                <span>• UV Phone Sanitizer [Amazon]</span>
                <span>• Graphene Power Bank [Amazon]</span>
                <span>• Holographic Keyboard [TikTok Shop]</span>
                <span>• Levitating Desk Lamp [Etsy]</span>
                <span>• Bone Conduction Glasses [Amazon]</span>
                <span>• AI Posture Corrector [TikTok Shop]</span>
                <span>• Pocket Retro Handheld [AliExpress]</span>
                <span>• Heated Mouse Pad [Amazon]</span>
                <span>• UV Phone Sanitizer [Amazon]</span>
            </div>
        </div>
    </div>
    ''', height=435)
    st.markdown('</div>', unsafe_allow_html=True)


with col_center:
    # --- Prominently Displayed Item (Moved Up) ---
    st.markdown('<div class="premium-card" style="height: 220px;">', unsafe_allow_html=True)
    
    show_col1, show_col2 = st.columns([1, 1.1])
    with show_col1:
        st.markdown(f'''
        <a href="{selected_item['url']}" target="_blank">
            <img src="{selected_item['img']}" style="width:100%; height:185px; object-fit:cover; border-radius:8px; border:1px solid rgba(255,255,255,0.1);" />
        </a>
        ''', unsafe_allow_html=True)
    with show_col2:
        tag_class = f"tag-{selected_item['source'].lower().replace('.','').replace(' shop','')}"
        st.markdown(f'''
        <div class="card-title" style="margin-bottom:6px;">✨ SELECTION ANALYSIS</div>
        <h3 style="margin-top:0; margin-bottom:4px; font-size:1.05rem; line-height:1.2; height: 2.4em; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">
            <a href="{selected_item['url']}" target="_blank" class="clean-anchor">{selected_item['name']}</a>
        </h3>
        <div class="platform-tag {tag_class}" style="margin-bottom:6px;">{selected_item['source']}</div>
        <p style="margin:0; font-size:0.75rem; color:#64748b;">Est. Marketplace Value</p>
        <h2 style="margin:0; color:#00f2fe; font-size:1.4rem; font-weight:800; line-height:1.1;">{selected_item['price']}</h2>
        <div style="margin-top:12px;">
            <a href="{selected_item['url']}" target="_blank" style="text-decoration:none;">
                <button style="width:100%; background:#7f00ff; color:white; border:none; padding:6px 10px; border-radius:4px; font-size:0.75rem; font-weight:600; cursor:pointer;">🔗 Direct Store Access</button>
            </a>
        </div>
        ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- Bar Graph / Metrics (Moved Directly Underneath Prominent Item) ---
    st.markdown('<div class="premium-card" style="height: 245px; padding: 12px;">', unsafe_allow_html=True)
    
    choice_day = st.radio("Drilldown Chrono Vector:", ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], index=['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].index(st.session_state.selected_day), horizontal=True)
    if choice_day != st.session_state.selected_day:
        st.session_state.selected_day = choice_day
        st.rerun()

    view_tab1, view_tab2 = st.tabs(["7-Day Cumulative", f"Hourly Velocity ({st.session_state.selected_day})"])
    
    with view_tab1:
        fig_7d = px.bar(selected_item['sales_days'], x='Day', y='Units Sold', color='Units Sold', color_continuous_scale='Purples')
        fig_7d.update_layout(
            plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='#94a3b8',
            margin=dict(l=5, r=5, t=5, b=5), coloraxis_showscale=False, height=120,
            xaxis_title=None, yaxis_title=None
        )
        st.plotly_chart(fig_7d, use_container_width=True, config={'displayModeBar': False})
        
    with view_tab2:
        fig_24h = px.line(selected_item['sales_hours'][st.session_state.selected_day], x='Hour', y='Units Sold')
        fig_24h.update_traces(line_color='#00f2fe')
        fig_24h.update_layout(
            plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='#94a3b8',
            margin=dict(l=5, r=5, t=5, b=5), height=120, xaxis_title=None, yaxis_title=None
        )
        st.plotly_chart(fig_24h, use_container_width=True, config={'displayModeBar': False})
    st.markdown('</div>', unsafe_allow_html=True)


with col_right:
    # --- Micro-Trending Velocities (List of 10 items moved to the Right Column) ---
    st.markdown('<div class="premium-card" style="height: 485px;">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">⚡ NEXT 10 MICRO-TRENDS</div>', unsafe_allow_html=True)
    
    micro_trends = [
        ("Collapsible Silicone Kettle", "Amazon", "https://www.amazon.com/s?k=Collapsible+Silicone+Travel+Kettle"),
        ("Smart Self-Stirring Mug", "TikTok Shop", "https://www.tiktok.com/market"),
        ("Celestial Birth Chart Print", "Amazon", "https://www.amazon.com/s?k=Custom+Celestial+Birth+Chart+Print"),
        ("Mini Pocket Thermal Printer", "Amazon", "https://www.amazon.com/s?k=Mini+Pocket+Label+Thermal+Printer"),
        ("Jar Vacuum Sealer Machine", "TikTok Shop", "https://www.tiktok.com/market"),
        ("Titanium EDC Multi-Tool", "AliExpress", "https://www.aliexpress.com"),
        ("Ceramic Mushroom Desk Lamp", "Etsy", "https://www.etsy.com/search?q=mushroom+lamp"),
        ("Abstract Ceramic Vases", "Etsy", "https://www.etsy.com/search?q=ceramic+vase"),
        ("Memory Foam Wrist Rest", "Amazon", "https://www.amazon.com/s?k=Wrist+Rest"),
        ("Flame Ultrasonic Diffuser", "TikTok Shop", "https://www.tiktok.com/market")
    ]
    
    for i, (t_name, t_src, t_url) in enumerate(micro_trends, 1):
        st.markdown(f'''
        <div style="margin-bottom: 12px; font-size: 0.8rem; line-height: 1.3;">
            <div style="font-weight: 700; color: #ffffff;">
                {i}. <a href="{t_url}" target="_blank" class="clean-anchor">{t_name}</a>
            </div>
            <span style="font-size: 0.65rem; font-weight: bold; color: #64748b; text-transform: uppercase;">[{t_src}]</span>
        </div>
        ''', unsafe_allow_html=True)
        if i < 10:
            st.markdown('<hr style="margin: 6px 0; border: none; border-top: 1px solid rgba(255,255,25
