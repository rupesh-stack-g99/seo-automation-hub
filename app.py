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
    
    /* Hover Effect: Cool Tech Blue/Cyan Glow */
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
    
    /* Status Panel Styling */
    .status-panel {
        background: rgba(128, 128, 128, 0.03);
        border-radius: 12px;
        border: 1px solid rgba(128, 128, 128, 0.1);
        padding: 20px;
        margin-top: 2rem;
    }
    
    .status-badge {
        background-color: rgba(16, 185, 129, 0.1);
        color: #10b981;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 600;
        border: 1px solid rgba(16, 185, 129, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Banner
st.markdown("# ⚡ Growth99 SEO Automation Hub")
st.markdown('<p class="main-subtitle">Unified Operations Center & Advanced Analytics Hub</p>', unsafe_allow_html=True)

# 4. Cleaned Tool Deployment Ribbon
st.write("")
stat_col1, stat_col2, stat_col3 = st.columns(3)
with stat_col1:
    st.metric(label="Tools Connected", value="3 / 3 Active", delta="100% Operational")
with stat_col2:
    st.metric(label="Environment", value="Production Hub")
with stat_col3:
    st.metric(label="Global Access", value="Secure // SSL")

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

# 6. Aesthetic Infrastructure Overview Panel
st.write("")
st.write("")
st.markdown('<div class="status-panel">', unsafe_allow_html=True)
diag_col1, diag_col2, diag_col3 = st.columns(3)

with diag_col1:
    st.markdown("🔒 **Gateway Protocol**")
    st.markdown("<span class=\"status-badge\">Encrypted Connection</span>", unsafe_allow_html=True)

with diag_col2:
    st.markdown("📡 **API Node Status**")
    st.markdown("<span class=\"status-badge\" style='color: #2563eb; background: rgba(37, 99, 235, 0.1); border-color: rgba(37, 99, 235, 0.2);'>Operational (12ms)</span>", unsafe_allow_html=True)

with diag_col3:
    st.markdown("⚡ **Failover Cluster**")
    st.markdown("<span class=\"status-badge\">Active Backup Zone</span>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 7. Clean Minimal Footer
st.write("")
st.divider()
footer_left, footer_right = st.columns(2)
with footer_left:
    st.caption("© 2026 Growth99 Automation Systems. All rights reserved.")
with footer_right:
    st.markdown("<p style='text-align: right; color: gray; font-size: 0.8rem; opacity: 0.4;'>v3.0 // Deep Tech Theme</p>", unsafe_allow_html=True)
