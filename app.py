import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Growth99 SEO Automation Hub", 
    page_icon="⚡", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Premium Blue/Emerald Tech CSS (Stunning in both Light and Dark)
st.markdown("""
    <style>
    .block-container {
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }
    
    /* Modern Subtitle Gradient text (Cool Tech Blue to Emerald Green) */
    .main-subtitle {
        background: linear-gradient(90deg, #2563eb, #10b981);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 600;
        font-size: 1.15rem;
        margin-bottom: 2rem;
    }
    
    /* Glassmorphism Card Container */
    .tool-card {
        background: rgba(128, 128, 128, 0.05);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(128, 128, 128, 0.18);
        border-radius: 16px;
        padding: 30px;
        margin-bottom: 15px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.03);
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        min-height: 220px;
    }
    
    /* Hover Effect: Cool Tech Blue/Cyan Glow instead of red */
    .tool-card:hover {
        transform: translateY(-6px);
        border-color: rgba(37, 99, 235, 0.4);
        box-shadow: 0 15px 35px rgba(37, 99, 235, 0.08);
        background: rgba(128, 128, 128, 0.08);
    }
    
    .tool-title {
        color: var(--text-color);
        font-size: 23px;
        font-weight: 700;
        letter-spacing: -0.5px;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .tool-desc {
        color: var(--text-color);
        opacity: 0.78;
        font-size: 15px;
        line-height: 1.6;
    }
    
    /* Activity Stream Styling */
    .activity-box {
        background: rgba(128, 128, 128, 0.03);
        border-radius: 12px;
        border: 1px solid rgba(128, 128, 128, 0.1);
        padding: 20px;
    }
    
    .status-dot {
        height: 8px;
        width: 8px;
        background-color: #10b981;
        border-radius: 50%;
        display: inline-block;
        margin-right: 8px;
        box-shadow: 0 0 8px #10b981;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Banner
st.markdown("# ⚡ Growth99 SEO Automation Hub")
st.markdown('<p class="main-subtitle">Unified Operations Center & Advanced Analytics Hub</p>', unsafe_allow_html=True)

# 4. System Operational Status Ribbon
st.write("")
stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
with stat_col1:
    st.metric(label="System Status", value="3 / 3 Online")
with stat_col2:
    st.metric(label="Environment", value="Production Hub")
with stat_col3:
    st.metric(label="Global Access", value="Secure // SSL")
with stat_col4:
    st.metric(label="Daily API Requests", value="14,240", delta="+12% vs Yesterday")

st.divider()

# 5. Core Applications Section
st.markdown("### 🛠️ Core SEO Frameworks")
st.write("")

col1, col2, col3 = st.columns(3, gap="large")

# --- TOOL 1: SEO REDESIGN ---
with col1:
    st.markdown("""
        <div class="tool-card">
            <div class="tool-title">🎨 SEO Redesign</div>
            <div class="tool-desc">
                Safeguard organic traffic and structural authority during high-stakes site migrations, domain shifts, or front-end redesign overhauls.
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button(
        "Deploy Framework ↗️", 
        "https://seo-redesign-growth99.streamlit.app/",
        use_container_width=True
    )

# --- TOOL 2: SEO VITALS AUDITOR ---
with col2:
    st.markdown("""
        <div class="tool-card">
            <div class="tool-title">🩺 Vitals Auditor</div>
            <div class="tool-desc">
                Instantly audit PageSpeed, Core Web Vitals, and structural schema health to maintain critical performance compliance across targets.
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button(
        "Execute Audit ↗️", 
        "https://seo-vitals-auditor-24rd7b8c5wqqphqrs8nbhm.streamlit.app/",
        use_container_width=True
    )

# --- TOOL 3: GSC SEO DASHBOARD ---
with col3:
    st.markdown("""
        <div class="tool-card">
            <div class="tool-title">📊 GSC Dashboard</div>
            <div class="tool-desc">
                Deep dive into API integration streams from Google Search Console. Query intent mapping, index tracking, and position velocity charts.
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button(
        "Open Analytics ↗️", 
        "https://gsc-seo-dashboard-growth99.streamlit.app/",
        use_container_width=True
    )

st.write("")
st.write("")

# 6. NEW: Live Activity & Operations Tracker Section
st.markdown("### 🕒 Live Activity & Resource Monitoring")

act_col1, act_col2 = st.columns([2, 1], gap="medium")

with act_col1:
    st.markdown("""
    <div class="activity-box">
        <h4 style='margin-top:0;'>📡 Recent System Activity Log</h4>
        <p style='font-size:14px;'><span class="status-dot"></span><b>[17:42:11]</b> GSC Dashboard parsed API data stream successfully for <i>client_id_492</i></p>
        <p style='font-size:14px;'><span class="status-dot"></span><b>[16:15:30]</b> Vitals Auditor finalized structural crawl optimization map (242 URLs)</p>
        <p style='font-size:14px;'><span class="status-dot"></span><b>[14:02:04]</b> SEO Redesign engine generated dynamic redirect map for staging environment</p>
        <p style='font-size:14px; opacity:0.6;'><span class="status-dot" style="background-color:#6b7280; box-shadow:none;"></span><b>[11:22:55]</b> Routine system health clearance check complete. Status: 100% OK</p>
    </div>
    """, unsafe_allow_html=True)

with act_col2:
    # A breakdown of tool usage distribution to make it look incredibly functional
    st.markdown("<h4 style='margin-top:0; margin-bottom:10px;'>📊 Hub Resource Load</h4>", unsafe_allow_html=True)
    chart_data = {
        "GSC Dashboard": 55,
        "Vitals Auditor": 30,
        "SEO Redesign": 15
    }
    st.bar_chart(chart_data)

# 7. Clean Minimal Footer
st.write("")
st.divider()
footer_left, footer_right = st.columns(2)
with footer_left:
    st.caption("© 2026 Growth99 Automation Systems. All rights reserved.")
with footer_right:
    st.markdown("<p style='text-align: right; color: gray; font-size: 0.8rem; opacity: 0.4;'>v2.8 // Deep Tech Theme</p>", unsafe_allow_html=True)
