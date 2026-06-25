import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Growth99 SEO Automation Hub", 
    page_icon="📈", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Hybrid-Theme CSS (Adapts to Light & Dark Automatically)
st.markdown("""
    <style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Dynamic Tool Cards using Streamlit CSS Variables */
    .tool-card {
        /* Mixes a tiny bit of theme text color into the background for a premium tint */
        background-color: rgba(128, 128, 128, 0.08);
        
        /* Semi-transparent border that works perfectly on white or black backgrounds */
        border: 1px solid rgba(128, 128, 128, 0.2);
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
        transition: all 0.3s ease;
        min-height: 220px;
    }
    
    /* Premium Hover effect that uses Streamlit's primary theme color */
    .tool-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 20px rgba(0, 0, 0, 0.1);
        border-color: #ff4b4b; /* Glows up on hover */
    }
    
    /* Dynamically inherits the user's current theme text color */
    .tool-title {
        color: var(--text-color);
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    /* Slightly muted description text that remains readable in both modes */
    .tool-desc {
        color: var(--text-color);
        opacity: 0.85;
        font-size: 15px;
        line-height: 1.5;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Banner
st.markdown("# 📈 Growth99 SEO Automation Hub")
st.markdown("##### Your central command center for advanced search engine optimization and website performance auditing.")

# Metrics Bar (Streamlit handles light/dark mode for these natively)
st.write("")
stat_col1, stat_col2, stat_col3, _ = st.columns([1, 1, 1, 2])
with stat_col1:
    st.metric(label="Active Tools", value="3 / 3")
with stat_col2:
    st.metric(label="Environment", value="Production")
with stat_col3:
    st.metric(label="Access Level", value="Global")

st.divider()
st.write("")

# 4. 3-Column Layout
col1, col2, col3 = st.columns(3, gap="large")

# --- TOOL 1: SEO REDESIGN ---
with col1:
    st.markdown("""
        <div class="tool-card">
            <div class="tool-title">🎨 SEO Redesign</div>
            <div class="tool-desc">
                Safeguard traffic and organic rankings during site migrations or UI overhauls. Track structural changes and monitor URL mapping smoothly.
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button(
        "Launch Redesign Tool 🚀", 
        "https://seo-redesign-growth99.streamlit.app/",
        use_container_width=True,
        type="primary"
    )

# --- TOOL 2: SEO VITALS AUDITOR ---
with col2:
    st.markdown("""
        <div class="tool-card">
            <div class="tool-title">🩺 SEO Vitals Auditor</div>
            <div class="tool-desc">
                Audit Core Web Vitals, page speed performance, and crucial technical on-page health factors instantly to ensure peak search engine crawlability.
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button(
        "Launch Auditor Tool 🔬", 
        "https://seo-vitals-auditor-24rd7b8c5wqqphqrs8nbhm.streamlit.app/",
        use_container_width=True,
        type="primary"
    )

# --- TOOL 3: GSC SEO DASHBOARD ---
with col3:
    st.markdown("""
        <div class="tool-card">
            <div class="tool-title">📊 GSC SEO Dashboard</div>
            <div class="tool-desc">
                Deep dive into your Google Search Console API. Uncover hidden query trends, analyze click-through rates (CTR), and track keyword impressions.
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button(
        "Launch GSC Analytics 📉", 
        "https://gsc-seo-dashboard-growth99.streamlit.app/",
        use_container_width=True,
        type="primary"
    )

# 5. Clean Footer
st.write("")
st.write("")
st.divider()
footer_left, footer_right = st.columns(2)
with footer_left:
    st.caption("© 2026 Growth99 Automation Systems. All rights reserved.")
with footer_right:
    st.markdown("<p style='text-align: right; color: gray; font-size: 0.8rem; opacity: 0.6;'>Powered by Streamlit Enterprise</p>", unsafe_allow_html=True)
