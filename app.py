import streamlit as st
import pandas as pd
import plotly.express as px
import random

# Page config for modern high-density dark dashboard layout
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
        <p style="margin: 0; font-size: 0.72rem; color: #4caf50; font-family: monospace; letter-spacing: 0.05em;">● TELEMETRY STATUS ONLINE // ORBITAL GEOLOCATION LOCKED</p>
    </div>
</div>
''', unsafe_allow_html=True)


# ==================== UPPER LAYOUT: ASYMMETRICAL METRIC BLOCK ====================
col_left, col_center, col_right = st.columns([1.2, 1.8, 1])

with col_left:
    # Interactive Realistic Earth Satellite Telemetry Engine
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">📡 LIVE PLANETARY RECONNAISSANCE</div>', unsafe_allow_html=True)
    
    st.components.v1.html('''
    <div style="position:relative; width:100%; height:230px; background:#04060a; border-radius:8px; border:1px solid rgba(255,255,255,0.04); overflow:hidden;">
        <canvas id="globeCanvas" style="position:absolute; top:0; left:0; width:100%; height:100%;"></canvas>
    </div>
    <script>
        const canvas = document.getElementById('globeCanvas');
        const ctx = canvas.getContext('2d');
        function resize() {
            canvas.width = canvas.parentElement.clientWidth;
            canvas.height = canvas.parentElement.clientHeight;
        }
        resize();
        
        let orbitAngle = 0;
        let earthRotation = 0;
        let signalPulses = [];

        // Simple generated vector terrain loops representing global landmass definitions
        const continents = [
            [[-20,25], [-10,35], [10,30], [15,10], [5,-10], [-5,-5], [-15,5]],
            [[-60,-10], [-45,-5], [-35,-20], [-40,-40], [-60,-25]],
            [[40,45], [60,50], [80,40], [70,20], [50,25]],
            [[-100,50], [-80,45], [-70,30], [-95,20], [-115,35]]
        ];

        function project(lon, lat, r, cx, cy) {
            let radLon = (lon + earthRotation) * Math.PI / 180;
            let radLat = lat * Math.PI / 180;
            return {
                x: cx + r * Math.cos(radLat) * Math.sin(radLon),
                y: cy - r * Math.sin(radLat),
                visible: Math.cos(radLat) * Math.cos(radLon) > -0.2
            };
        }

        function renderGlobeScene() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            const cx = canvas.width / 2;
            const cy = canvas.height / 2;
            const r = 55; // Earth radius
            
            orbitAngle += 0.015;     // Speed of satellite orbit
            earthRotation += 0.25;   // Speed of Earth rotation

            // 1. Draw Background Space Atmosphere Glow
            let glow = ctx.createRadialGradient(cx, cy, r - 5, cx, cy, r + 25);
            glow.addColorStop(0, 'rgba(0, 110, 255, 0.05)');
            glow.addColorStop(0.6, 'rgba(0, 242, 254, 0.02)');
            glow.addColorStop(1, 'rgba(0,0,0,0)');
            ctx.fillStyle = glow;
            ctx.beginPath(); ctx.arc(cx, cy, r + 25, 0, Math.PI*2); ctx.fill();

            // Calculate Satellite position (3D Elliptical Ring Projection)
            let satX = cx + Math.sin(orbitAngle) * (r + 30);
            let satY = cy + Math.cos(orbitAngle) * 20 + Math.sin(orbitAngle) * 5;
            let satelliteIsBehind = Math.cos(orbitAngle) > 0;

            // 2. Render Satellite ONLY if Behind Earth
            if (satelliteIsBehind) {
                drawSatellite(satX, satY);
            }

            // 3. Draw Real Earth Body (Deep Oceanic Gradient Base)
            let oceanGrd = ctx.createRadialGradient(cx - r/3, cy - r/3, r/5, cx, cy, r);
            oceanGrd.addColorStop(0, '#102a45');
            oceanGrd.addColorStop(0.7, '#071626');
            oceanGrd.addColorStop(1, '#02070d');
            ctx.fillStyle = oceanGrd;
            ctx.beginPath();
            ctx.arc(cx, cy, r, 0, Math.PI * 2);
            ctx.fill();

            // 4. Project and Draw Moving Real Earth Continental Landmass Geometries
            ctx.fillStyle = 'rgba(34, 197, 94, 0.45)'; // Organic Deep Green Coastlines
            continents.forEach(poly => {
                ctx.beginPath();
                let first = true;
                let pathVisible = false;
                poly.forEach(pt => {
                    let proj = project(pt[0], pt[1], r, cx, cy);
                    if (proj.visible) pathVisible = true;
                    if (first) {
                        ctx.moveTo(proj.x, proj.y);
                        first = false;
                    } else {
                        ctx.lineTo(proj.x, proj.y);
                    }
                });
                ctx.closePath();
                if (pathVisible) {
                    ctx.save();
                    ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI * 2); ctx.clip(); // Mask within Sphere Edge
                    ctx.fill();
                    ctx.restore();
                }
            });

            // 5. Draw Atmosphere Limbal Edge Ring
            let atmosphere = ctx.createRadialGradient(cx, cy, r - 3, cx, cy, r + 2);
            atmosphere.addColorStop(0, 'rgba(0, 0, 0, 0)');
            atmosphere.addColorStop(0.8, 'rgba(0, 180, 255, 0.35)');
            atmosphere.addColorStop(1, 'rgba(0, 242, 254, 0)');
            ctx.fillStyle = atmosphere;
            ctx.beginPath(); ctx.arc(cx, cy, r + 2, 0, Math.PI * 2); ctx.fill();

            // 6. Spawn and Draw Active Uplink Ping Lasers 
            if (!satelliteIsBehind && Math.random() < 0.15) {
                signalPulses.push({ x: satX, y: satY, tx: cx + (Math.random() - 0.5) * r, ty: cy + (Math.random() - 0.5) * r, life: 1.0 });
            }

            signalPulses.forEach((pulse, idx) => {
                pulse.life -= 0.04;
                if (pulse.life <= 0) { signalPulses.splice(idx, 1); return; }
                ctx.strokeStyle = `rgba(0, 242, 254, ${pulse.life})`;
                ctx.lineWidth = 1.5;
                ctx.beginPath();
                ctx.moveTo(pulse.x, pulse.y);
                ctx.lineTo(pulse.tx, pulse.ty);
                ctx.stroke();
            });

            // 7. Render Satellite ONLY if Front of Earth
            if (!satelliteIsBehind) {
                drawSatellite(satX, satY);
            }

            requestAnimationFrame(renderGlobeScene);
        }

        function drawSatellite(x, y) {
            // Solar Panels
            ctx.fillStyle = "#00f2fe";
            ctx.fillRect(x - 14, y - 2, 8, 3);
            ctx.fillRect(x + 6, y - 2, 8, 3);
            // Chassis Main Module
            ctx.fillStyle = "#7f00ff";
            ctx.fillRect(x - 3, y - 4, 6, 7);
            // Core Diode Node Glow
            ctx.fillStyle = "#ffffff";
            ctx.beginPath(); ctx.arc(x, y-0.5, 1.5, 0, Math.PI*2); ctx.fill();
        }

        renderGlobeScene();
    </script>
    ''', height=232)
    st.markdown('</div>', unsafe_allow_html=True)

with col_center:
    # Highlighted Display Card Focus Spot 
    st.markdown('<div class="premium-card" style="height: 264px;">', unsafe_allow_html=True)
    
    show_col1, show_col2 = st.columns([1, 1.1])
    with show_col1:
        st.markdown(f'''
        <a href="{selected_item['url']}" target="_blank">
            <img src="{selected_item['img']}" style="width:100%; height:230px; object-fit:cover; border-radius:8px; border:1px solid rgba(255,255,255,0.1);" />
        </a>
        ''', unsafe_allow_html=True)
    with show_col2:
        tag_class = f"tag-{selected_item['source'].lower().replace('.','').replace(' shop','')}"
        st.markdown(f'''
        <div class="card-title" style="margin-bottom:6px;">✨ SELECTION ANALYSIS</div>
        <h3 style="margin-top:0; margin-bottom:4px; font-size:1.05rem; line-height:1.2; height: 2.4em; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">
            <a href="{selected_item['url']}" target="_blank" class="clean-anchor">{selected_item['name']}</a>
        </h3>
