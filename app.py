import streamlit as st

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
    
    /* Modern Subtitle Gradient text */
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
    
    /* Premium Static Utility Directory Panel */
    .directory-panel {
        background: rgba(128, 128, 128, 0.03);
        border-radius: 12px;
        border: 1px solid rgba(128, 128, 128, 0.1);
        padding: 24px;
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Banner
st.markdown("# ⚡ Growth99 SEO Automation Hub")
st.markdown('<p class="main-subtitle">Unified Operations Center & Advanced Analytics Hub</p>', unsafe_allow_html=True)

# 4. Tool Deployment Ribbon
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

with col1:
    st.markdown("""
        <div class="tool-card">
            <div class="tool-title">🎨 SEO Redesign</div>
            <div class="tool-desc">
                Safeguard organic traffic and structural authority during high-stakes site migrations, domain shifts, or front-end redesign overhauls.
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Deploy Framework ↗️", "https://seo-redesign-growth99.streamlit.app/", use_container_width=True, type="primary")

with col2:
    st.markdown("""
        <div class="tool-card">
            <div class="tool-title">🩺 Vitals Auditor</div>
            <div class="tool-desc">
                Instantly audit PageSpeed, Core Web Vitals, and structural schema health to maintain critical performance compliance across targets.
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Execute Audit ↗️", "https://seo-vitals-auditor-24rd7b8c5wqqphqrs8nbhm.streamlit.app/", use_container_width=True, type="primary")

with col3:
    st.markdown("""
        <div class="tool-card">
            <div class="tool-title">📊 GSC Dashboard</div>
            <div class="tool-desc">
                Deep dive into API integration streams from Google Search Console. Query intent mapping, index tracking, and position velocity charts.
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Open Analytics ↗️", "https://gsc-seo-dashboard-growth99.streamlit.app/", use_container_width=True, type="primary")

st.write("")
st.write("")
st.divider()

# 6. NEW Replacement Section: Clean Global Directory & Specifications
st.markdown("### 📁 Platform Manifest & Operational Resources")
st.caption("Central technical configurations and architectural references for the Growth99 automation network.")

st.write("")
st.markdown('<div class="directory-panel">', unsafe_allow_html=True)
dir_col1, dir_col2, dir_col3 = st.columns(3)

with dir_col1:
    st.markdown("📋 **Documentation Registry**")
    st.caption("Access central configuration guides, structural schema onboarding guidelines, and platform migration playbooks.")

with dir_col2:
    st.markdown("🔒 **Compliance & Encryption**")
    st.caption("End-to-end SSL protocols active. Data streaming tunnels between Google Search Console engines are fully isolated.")

with dir_col3:
    st.markdown("⚙️ **Global Network Cluster**")
    st.caption("Distributed microservice topology. Individual module instances are managed via secure remote origin nodes.")
st.markdown('</div>', unsafe_allow_html=True)

# 7. Footer
st.write("")
st.divider()
footer_left, footer_right = st.columns(2)
with footer_left:
    st.caption("© 2026 Growth99 Automation Systems. All rights reserved.")
with footer_right:
    st.markdown("<p style='text-align: right; color: gray; font-size: 0.8rem; opacity: 0.4;'>v4.0 // Enterprise Minimalist Build</p>", unsafe_allow_html=True)
