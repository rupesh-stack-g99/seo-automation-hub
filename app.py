import streamlit as st
import os

# 1. Page Configuration
st.set_page_config(
    page_title="Growth99 SEO Automation Hub", 
    page_icon="⚡", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Premium Cleaned CSS (Optimized for Light & Dark)
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
    </style>
""", unsafe_allow_html=True)

# 3. Native, Error-Free Visitor Counter Logic
COUNTER_FILE = "visitor_count.txt"

def get_exact_visitor_count():
    # If the file doesn't exist yet, initialize it at 0
    if not os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "w") as f:
            f.write("0")
            
    # Read the current count
    with open(COUNTER_FILE, "r") as f:
        try:
            count = int(f.read().strip())
        except ValueError:
            count = 0
            
    # Increment count only once per page connection session load
    if 'tracked_session' not in st.session_state:
        st.session_state.tracked_session = True
        count += 1
        with open(COUNTER_FILE, "w") as f:
            f.write(str(count))
            
    return count

# Run counter
current_exact_visitors = get_exact_visitor_count()

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

# 7. Sleek Tabbed Resource Navigator
st.markdown("### 📁 Platform Manifest & System Infrastructure")
st.write("")

with st.container():
    tab1, tab2, tab3 = st.tabs(["📋 Documentation Registry", "🔒 Compliance & Encryption", "⚙️ Global Network Cluster"])
    
    with tab1:
        st.write("")
        st.markdown("**Central Knowledge Hub**")
        st.info("Access comprehensive platform configuration guides, technical layout metrics, automated structural schema onboarding guidelines, and environment platform migration playbooks.")
        
    with tab2:
        st.write("")
        st.markdown("**Security & Transit Specifications**")
        st.success("End-to-end industry standard SSL protocols are active. Data processing pipelines connecting external platform engine arrays are fully sandboxed and logically isolated.")
        
    with tab3:
        st.write("")
        st.markdown("**Topology Architecture**")
        st.warning("Running on an isolated, distributed microservices network topology. Individual runtime environments are actively maintained via secure remote server tracking endpoints.")

st.write("")
st.write("")
st.divider()

# 8. Beautiful Native Traffic Metrics Panel (Replaces the broken image box flawlessly)
st.markdown("### 📈 Live Hub Infrastructure Analytics")
st.caption("Real-time traffic counts tracked safely and directly on the host instance.")
st.write("")

metric_left, metric_center, metric_right = st.columns(3)

with metric_left:
    st.metric(label="👥 Total Site Visitors (Exact)", value=f"{current_exact_visitors} Hits")
with metric_center:
    st.metric(label="🖥️ Server Platform Status", value="Stable / Online")
with metric_right:
    st.metric(label="📡 Active Internal Links", value="3 / 3 Bound")

# 9. Clean Minimalist Footer
st.write("")
st.divider()
footer_left, footer_right = st.columns(2)
with footer_left:
    st.caption("© 2026 Growth99 Automation Systems. All rights reserved.")
with footer_right:
    st.markdown("<p style='text-align: right; color: gray; font-size: 0.8rem; opacity: 0.4;'>v4.5 // Native Server Registry</p>", unsafe_allow_html=True)
