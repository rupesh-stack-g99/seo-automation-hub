import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Growth99 SEO Automation Hub", 
    page_icon="📈", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS for Beautiful Cards & UI Enhancements
st.markdown("""
    <style>
    /* Main background tweak for a clean look */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Custom Styling for the Tool Cards */
    .tool-card {
        background-color: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        min-height: 220px;
    }
    
    /* Hover effect to make it feel premium */
    .tool-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 16px rgba(0, 0, 0, 0.1);
        border-color: #ff4b4b;
    }
    
    /* Card Title Styling */
    .tool-title {
        color: #1c1c1e;
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    /* Card Description Styling */
    .tool-desc {
        color: #48484a;
        font-size: 15px;
        line-height: 1.5;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)  # <-- Fixed this line!

# 3. Header Banner
st.markdown("# 📈 Growth99 SEO Automation Hub")
st.markdown("##### Your central command center for advanced search engine optimization and website performance auditing.")

# Small Quick Stats Ribbon
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

# 4. Create a 3-column layout for the beautifully designed cards
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
    st.markdown("<p style='text-align: right; color: gray; font-size: 0.8rem;'>Powered by Streamlit Enterprise</p>", unsafe_allow_html=True)
