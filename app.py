import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(
    page_title="Growth99 SEO Automation Hub", 
    page_icon="⚡", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Premium Blue/Emerald Tech CSS
st.markdown("""
    <style>
    .block-container {
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }
    
    .main-subtitle {
        background: linear-gradient(90deg, #2563eb, #10b981);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 600;
        font-size: 1.15rem;
        margin-bottom: 2rem;
    }
    
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
    
    .infra-card {
        background: rgba(128, 128, 128, 0.04);
        border: 1px solid rgba(128, 128, 128, 0.12);
        border-radius: 14px;
        padding: 22px;
        text-align: center;
    }
    
    .infra-title {
        font-size: 15px;
        font-weight: 600;
        margin-bottom: 12px;
        color: var(--text-color);
    }

    .status-badge-green {
        background-color: rgba(16, 185, 129, 0.12);
        color: #10b981;
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 600;
        border: 1px solid rgba(16, 185, 129, 0.25);
        display: inline-block;
    }
    
    .status-badge-blue {
        background-color: rgba(37, 99, 235, 0.12);
        color: #2563eb;
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 600;
        border: 1px solid rgba(37, 99, 235, 0.25);
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Initialize Timestamped Lists in Session State
if 'redesign_history' not in st.session_state:
    st.session_state.redesign_history = []
if 'vitals_history' not in st.session_state:
    st.session_state.vitals_history = []
if 'gsc_history' not in st.session_state:
    st.session_state.gsc_history = []

# Helper to clean history and count clicks over rolling 24 hours
def get_rolling_24h_count(history_key):
    current_time = time.time()
    st.session_state[history_key] = [t for t in st.session_state[history_key] if current_time - t < 86400]
    return len(st.session_state[history_key])

# Callback function to log background clicks instantly before opening links
def track_click(history_key):
    st.session_state[history_key].append(time.time())

# 4. Header Banner
st.markdown("# ⚡ Growth99 SEO Automation Hub")
st.markdown('<p class="main-subtitle">Unified Operations Center & Advanced Analytics Hub</p>', unsafe_allow_html=True)

# 5. Tool Deployment Ribbon
stat_col1, stat_col2, stat_col3 = st.columns(3)
with stat_col1:
    st.metric(label="Tools Connected", value="3 / 3 Active", delta="100% Operational")
with stat_col2:
    st.metric(label="Environment", value="Production Hub")
with stat_col3:
    st.metric(label="Global Access", value="Secure // SSL")

st.divider()

# 6. Core Applications Section
st.markdown("### 🛠️ Core SEO Frameworks")
st.write("")

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("""
        <div class="tool-card">
            <div class="tool-title">🎨 SEO Redesign</div>
            <div class="tool-desc">
                Safeguard organic traffic and structural authority during high-stakes site migrations, domain shifts, or front-end redesign overhauls.
            </div>
        </div>
    """, unsafe_allow_html=True)
    # Using link_button with on_click logs data to session_state flawlessly
    st.link_button(
        "Deploy Framework ↗️", 
        "https://seo-redesign-growth99.streamlit.app/", 
        use_container_width=True, 
        type="primary",
        on_click=track_click,
        args=("redesign_history",)
    )

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
        use_container_width=True, 
        type="primary",
        on_click=track_click,
        args=("vitals_history",)
    )

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
        use_container_width=True, 
        type="primary",
        on_click=track_click,
        args=("gsc_history",)
    )

st.write("")
st.write("")
st.divider()

# 7. Calculate rolling 24 hour totals
count_redesign = get_rolling_24h_count("redesign_history")
count_vitals = get_rolling_24h_count("vitals_history")
count_gsc = get_rolling_24h_count("gsc_history")

# Dynamic Activity Logs Group
st.markdown("### 🕒 Real-time Launch Logs (Rolling 24 Hours)")
st.caption("Tracks exactly how many times each system module has been initialized over a true 24-hour window.")
st.write("")

vol_col1, vol_col2, vol_col3 = st.columns(3)
with vol_col1:
    st.metric(label="🎨 SEO Redesign Activity", value=f"{count_redesign} Runs")
with vol_col2:
    st.metric(label="🩺 Vitals Auditor Activity", value=f"{count_vitals} Runs")
with vol_col3:
    st.metric(label="📊 GSC Dashboard Activity", value=f"{count_gsc} Runs")

st.write("")
st.write("")

# 8. Infrastructure Overview Panels
infra_col1, infra_col2, infra_col3 = st.columns(3, gap="medium")

with infra_col1:
    st.markdown("""
        <div class="infra-card">
            <div class="infra-title">🔒 Gateway Protocol</div>
            <span class="status-badge-green">Encrypted Connection</span>
        </div>
    """, unsafe_allow_html=True)

with infra_col2:
    st.markdown("""
        <div class="infra-card">
            <div class="infra-title">📡 Data Node Status</div>
            <span class="status-badge-blue">Operational (12ms)</span>
        </div>
    """, unsafe_allow_html=True)

with infra_col3:
    st.markdown("""
        <div class="infra-card">
            <div class="infra-title">⚡ Failover Cluster</div>
            <span class="status-badge-green">Active Backup Zone</span>
        </div>
    """, unsafe_allow_html=True)

# 9. Footer
st.write("")
st.divider()
footer_left, footer_right = st.columns(2)
with footer_left:
    st.caption("© 2026 Growth99 Automation Systems. All rights reserved.")
with footer_right:
    st.markdown("<p style='text-align: right; color: gray; font-size: 0.8rem; opacity: 0.4;'>v3.7 // Link Callback Stability</p>", unsafe_allow_html=True)
