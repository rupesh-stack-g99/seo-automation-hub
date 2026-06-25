import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Growth99 SEO Automation Hub", 
    page_icon="📈", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Premium Glassmorphism CSS (Ultra-Aesthetic Light & Dark Mode)
st.markdown("""
    <style>
    /* Clean up main container spacing */
    .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
    }
    
    /* Modern Subtitle Gradient text */
    .main-subtitle {
        background: linear-gradient(90deg, #ff4b4b, #ff8a00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 600;
        font-size: 1.15rem;
        margin-bottom: 2rem;
    }
    
    /* Glassmorphism Card Container */
    .tool-card {
        /* Works like tinted glass in both light and dark backgrounds */
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        
        /* Dual-mode optimized borders */
        border: 1px solid rgba(128, 128, 128, 0.15);
        border-radius: 16px;
        
        padding: 30px;
        margin-bottom: 15px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.04);
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        min-height: 230px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    /* Elegant Hover Effect: Card lifts up, border glows, shadow deepens */
    .tool-card:hover {
        transform: translateY(-6px);
        border-color: rgba(255, 75, 75, 0.5);
        box-shadow: 0 15px 35px rgba(255, 75, 75, 0.1);
        background: rgba(255, 255, 255, 0.06);
    }
    
    /* Dynamic Theme-Aware Typography */
    .tool-title {
        color: var(--text-color);
        font-size: 24px;
        font-weight: 700;
        letter-spacing: -0.5px;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .tool-desc {
        color: var(--text-color);
        opacity: 0.75;
        font-size: 15px;
        line-height: 1.6;
    }
    
    /* Aesthetic touch for metrics section container */
    .metrics-wrapper {
        background: rgba(128, 128, 128, 0.04);
        padding: 15px;
        border-radius: 12px;
        border: 1px solid rgba(128, 128, 128, 0.08);
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Banner
st.markdown("# 📈 Growth99 SEO Automation Hub")
st.markdown('<p class="main-subtitle">Central command center for advanced search engine optimization and website performance auditing.</p>', unsafe_allow_html=True)

# 4. Embedded Minimal Metrics Wrapper
st.markdown('<div class="metrics-wrapper">', unsafe_allow_html=True)
stat_col1, stat_col2, stat_col3, _ = st.columns([1, 1, 1, 2])
with stat_col1:
    st.metric(label="System Status", value="3 / 3 Online")
with stat_col2:
    st.metric(label="Environment", value="Production Hub")
with stat_col3:
    st.metric(label="Global Access", value="Authorized")
st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# 5. The 3-Column Layout with Premium Spacing
col1, col2, col3 = st.columns(3, gap="large")

# --- TOOL 1: SEO REDESIGN ---
with col1:
    st.markdown("""
        <div class="tool-card">
            <div>
                <div class="tool-title">🎨 SEO Redesign</div>
                <div class="tool-desc">
                    Safeguard organic traffic and structural authority during high-stakes site migrations, domain shifts, or front-end redesign overhauls.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button(
        "Open Application 🚀", 
        "https://seo-redesign-growth99.streamlit.app/",
        use_container_width=True,
        type="primary"
    )

# --- TOOL 2: SEO VITALS AUDITOR ---
with col2:
    st.markdown("""
        <div class="tool-card">
            <div>
                <div class="tool-title">🩺 Vitals Auditor</div>
                <div class="tool-desc">
                    Instantly audit PageSpeed, Core Web Vitals, and structural schema health to maintain critical performance compliance across targets.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button(
        "Open Application 🔬", 
        "https://seo-vitals-auditor-24rd7b8c5wqqphqrs8nbhm.streamlit.app/",
        use_container_width=True,
        type="primary"
    )

# --- TOOL 3: GSC SEO DASHBOARD ---
with col3:
    st.markdown("""
        <div class="tool-card">
            <div>
                <div class="tool-title">📊 GSC Dashboard</div>
                <div class="tool-desc">
                    Deep dive into API integration streams from Google Search Console. Query intent mapping, index tracking, and position velocity charts.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button(
        "Open Application 📉", 
        "https://gsc-seo-dashboard-growth99.streamlit.app/",
        use_container_width=True,
        type="primary"
    )

# 6. Sleek, Subtle Footer
st.write("")
st.write("")
st.divider()
footer_left, footer_right = st.columns(2)
with footer_left:
    st.caption("© 2026 Growth99 Automation Systems. All rights reserved.")
with footer_right:
    st.markdown("<p style='text-align: right; color: gray; font-size: 0.8rem; opacity: 0.4;'>v2.4 // Glassmorphic Interface</p>", unsafe_allow_html=True)
