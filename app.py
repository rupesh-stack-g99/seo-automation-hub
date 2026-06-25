import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Growth99 SEO Automation Hub", 
    page_icon="🚀", 
    layout="wide"
)

# 2. Header Section
st.title("🚀 Growth99 SEO Automation Hub")
st.write("Welcome to your central command center. Click any tool below to launch it instantly in a new tab.")
st.divider()

# 3. Create a 3-column layout for the 3 tools
col1, col2, col3 = st.columns(3)

# Tool 1: SEO Redesign
with col1:
    st.markdown("### 🎨 SEO Redesign")
    st.write("Manage and track SEO metrics during website redesigns to protect rankings.")
    st.link_button(
        "Launch Tool ➡️", 
        "https://seo-redesign-growth99.streamlit.app/",
        use_container_width=True
    )

# Tool 2: SEO Vitals Auditor
with col2:
    st.markdown("### 🩺 SEO Vitals Auditor")
    st.write("Audit core web vitals, performance metrics, and on-page SEO health.")
    st.link_button(
        "Launch Tool ➡️", 
        "https://seo-vitals-auditor-24rd7b8c5wqqphqrs8nbhm.streamlit.app/",
        use_container_width=True
    )

# Tool 3: GSC SEO Dashboard
with col3:
    st.markdown("### 📊 GSC SEO Dashboard")
    st.write("Deep dive into Google Search Console data to track impressions, clicks, and queries.")
    st.link_button(
        "Launch Tool ➡️", 
        "https://gsc-seo-dashboard-growth99.streamlit.app/",
        use_container_width=True
    )

# 4. Footer
st.divider()
st.caption("Growth99 SEO Tools • Built with Streamlit")
