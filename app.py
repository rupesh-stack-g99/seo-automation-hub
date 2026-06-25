import json
import re
import xml.etree.ElementTree as ET
from urllib.parse import urlparse
import bs4
import pandas as pd
import requests
import streamlit as st

# --- Core Crawler Functions ---


def get_slug_from_url(url):
    """Extracts purely the clean path slug from any URL string, ignoring domains and trailing slashes."""
    if not url:
        return ""
    try:
        parsed_url = urlparse(url.strip())
        path = parsed_url.path
        slug = path.strip().strip("/").lower()
        return slug if slug else "homepage"
    except Exception:
        return ""


def extract_urls_from_sitemap_url(sitemap_url):
    """Deep parses sitemap XML data recursively to handle nested WordPress setups."""
    urls = set()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    try:
        response = requests.get(sitemap_url.strip(), headers=headers, timeout=15)
        if response.status_code != 200:
            return []

        xml_text = re.sub(r'\sxmlns="[^"]+"', "", response.text, count=1)
        root = ET.fromstring(xml_text.encode("utf-8"))

        sitemaps = root.findall(".//sitemap/loc")
        if sitemaps:
            for sitemap_node in sitemaps:
                if sitemap_node.text:
                    sub_url = sitemap_node.text.strip()
                    sub_urls = extract_urls_from_sitemap_url(sub_url)
                    urls.update(sub_urls)

        locs = root.findall(".//url/loc")
        for loc in locs:
            if loc.text:
                urls.add(loc.text.strip())

        return list(urls)
    except Exception:
        return []


def scrape_current_live_site_seo(url):
    """Crawls a target webpage to gather all standard, Facebook, and Twitter SEO tags."""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers, timeout=12)
        if response.status_code != 200:
            return None

        soup = bs4.BeautifulSoup(response.text, "html.parser")
        title = soup.title.string.strip() if soup.title else ""
        desc_tag = soup.find("meta", attrs={"name": "description"})
        meta_desc = desc_tag["content"].strip() if desc_tag else ""
        canonical_tag = soup.find("link", rel="canonical")
        canonical = canonical_tag["href"].strip() if canonical_tag else ""

        keywords_tag = soup.find("meta", attrs={"name": "keywords"})
        keywords = keywords_tag["content"].strip() if keywords_tag else ""

        social_tags = {}
        for tag in soup.find_all("meta"):
            prop = tag.get("property", "")
            name = tag.get("name", "")
            key = prop if prop else name
            if key.startswith("og:") or key.startswith("twitter:"):
                social_tags[key] = tag.get("content", "").strip()

        schemas = []
        schema_tags = soup.find_all("script", type="application/ld+json")
        for tag in schema_tags:
            try:
                if tag.string:
                    schemas.append(json.loads(tag.string.strip()))
            except Exception:
                schemas.append(tag.string.strip() if tag.string else "")

        return {
            "title": title,
            "meta_description": meta_desc,
            "canonical": canonical,
            "keywords": keywords,
            "schema_json_ld": json.dumps(schemas, ensure_ascii=False),
            "fb_title": social_tags.get("og:title", title),
            "fb_desc": social_tags.get("og:description", meta_desc),
            "fb_image": social_tags.get("og:image", ""),
            "tw_title": social_tags.get("twitter:title", title),
            "tw_desc": social_tags.get("twitter:description", meta_desc),
            "tw_image": social_tags.get("twitter:image", ""),
        }
    except Exception:
        return None


def extract_wordpress_page_id(url):
    """Dual-Engine dynamic discovery system. Falls back to WP-JSON API endpoints to guarantee ID capture."""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = bs4.BeautifulSoup(response.text, "html.parser")

            body = soup.find("body")
            if body and body.has_attr("class"):
                classes = " ".join(body["class"])
                match = re.search(
                    r"(?:page-id-|postid-|id-)(\d+)", classes, re.IGNORECASE
                )
                if match:
                    return match.group(1)

            shortlink = soup.find("link", rel="shortlink")
            if shortlink and shortlink.has_attr("href"):
                match = re.search(r"[?&](?:p|page_id)=(\d+)", shortlink["href"])
                if match:
                    return match.group(1)

        parsed_url = urlparse(url)
        base_domain = f"{parsed_url.scheme}://{parsed_url.netloc}"
        slug = get_slug_from_url(url)

        api_url = (
            f"{base_domain}/wp-json/wp/v2/pages?per_page=1"
            if slug == "homepage"
            else f"{base_domain}/wp-json/wp/v2/pages?slug={slug}"
        )
        api_res = requests.get(api_url, headers=headers, timeout=8)
        if api_res.status_code == 200:
            data = api_res.json()
            if data and isinstance(data, list) and len(data) > 0:
                return str(data[0].get("id", ""))

        if slug != "homepage":
            cpt_api_url = f"{base_domain}/wp-json/wp/v2/posts?slug={slug}"
            cpt_res = requests.get(cpt_api_url, headers=headers, timeout=8)
            if cpt_res.status_code == 200:
                data = cpt_res.json()
                if data and isinstance(data, list) and len(data) > 0:
                    return str(data[0].get("id", ""))

        return ""
    except Exception:
        return ""


def get_domain_prefix(url):
    """Extracts clean domain name string to generate unique file export signatures."""
    try:
        parsed = urlparse(url.strip())
        domain = parsed.netloc if parsed.netloc else parsed.path
        domain = domain.replace("www.", "")
        clean_name = re.sub(r"[^\w\-_]", "_", domain)
        return clean_name.strip("_") if clean_name else "live_site"
    except Exception:
        return "live_site"


# --- Cache Management ---
if "audit_results" not in st.session_state:
    st.session_state.audit_results = None
if "w1_count" not in st.session_state:
    st.session_state.w1_count = 0
if "w2_count" not in st.session_state:
    st.session_state.w2_count = 0
if "match_count" not in st.session_state:
    st.session_state.match_count = 0

# --- Advanced Modern Theme & UI Engine ---
st.set_page_config(
    page_title="Growth99 SEO Migration Suite", page_icon="⚡", layout="wide"
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    /* Responsive Glassmorphic Cards & Neon Gradient Headers */
    .dashboard-header {
        background: linear-gradient(135deg, #7F00FF 0%, #00F2FE 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
        font-size: 2.8rem !important;
        letter-spacing: -1px;
        margin-bottom: 0px;
    }
    
    .dashboard-tagline {
        font-size: 1.1rem !important;
        font-weight: 500 !important;
        opacity: 0.85;
        margin-bottom: 2px;
    }
    
    .brand-pill {
        background: linear-gradient(90deg, rgba(127,0,255,0.15) 0%, rgba(0,242,254,0.15) 100%);
        border: 1px solid rgba(0,242,254,0.3);
        padding: 4px 14px;
        border-radius: 20px;
        color: #00F2FE !important;
        font-weight: 700 !important;
        font-size: 0.75rem !important;
        letter-spacing: 2px;
        display: inline-block;
        margin-bottom: 30px;
    }
    
    /* Universal Adaptive Metrics Cards */
    div[data-testid="stMetric"] {
        background: rgba(127, 0, 255, 0.04) !important;
        border: 1px solid rgba(127, 0, 255, 0.15) !important;
        border-radius: 16px !important;
        padding: 22px !important;
        backdrop-filter: blur(10px);
        transition: transform 0.2s ease;
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        border-color: rgba(0, 242, 254, 0.4) !important;
    }
    
    div[data-testid="stMetricValue"] {
        background: linear-gradient(135deg, #7F00FF 0%, #00F2FE 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
        font-size: 3rem !important;
    }
    
    /* Multi-Theme Adaptive Button Structural Adjustments */
    button[aria-label="⚡ LAUNCH HIGH-SPEED MIGRATION AUDIT"] {
        background: linear-gradient(135deg, #7F00FF 0%, #00F2FE 100%) !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 16px !important;
        box-shadow: 0 8px 24px -6px rgba(127, 0, 255, 0.4) !important;
        letter-spacing: 0.5px;
    }
    
    div.stDownloadButton > button {
        border-radius: 12px !important;
        border: 1px solid rgba(127, 0, 255, 0.3) !important;
        background-color: transparent !important;
        font-weight: 600 !important;
        transition: all 0.2s ease;
    }
    div.stDownloadButton > button:hover {
        background: linear-gradient(135deg, rgba(127,0,255,0.05) 0%, rgba(0,242,254,0.05) 100%) !important;
        border-color: #00F2FE !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    "<h1 class='dashboard-header'>⚡ Growth99 Enterprise Migration Suite</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<div class='dashboard-tagline'>Automated cross-mapping schema synchronization engine supporting synchronized RankMath configurations.</div>",
    unsafe_allow_html=True,
)
st.markdown("<div class='brand-pill'>PRODUCTION V3.2 NEXTGEN</div>", unsafe_allow_html=True)

# Main Application Configuration Layout
col1, col2 = st.columns(2)
with col1:
    sitemap_1_input = st.text_input(
        "🔗 Current Live Site (Sitemap XML URL)",
        placeholder="https://livesite.com/page-sitemap.xml",
    )
    live_csv_file = st.file_uploader(
        "📥 Optional: Upload Live Site Backend RankMath Export (CSV Backup File)",
        type=["csv"],
    )
with col2:
    sitemap_2_input = st.text_input(
        "🧪 Target Beta Site (Sitemap XML URL)",
        placeholder="https://beta.devsite.com/page-sitemap.xml",
    )
    beta_csv_file = st.file_uploader(
        "📥 Optional: Upload Beta Site Backend RankMath Export (CSV Backup File)",
        type=["csv"],
    )

st.write("")
_, center_btn_col, _ = st.columns([1, 2, 1])
with center_btn_col:
    action_btn = st.button(
        "⚡ LAUNCH HIGH-SPEED MIGRATION AUDIT",
        type="primary",
        use_container_width=True,
    )

if action_btn:
    if not sitemap_1_input.strip() or not sitemap_2_input.strip():
        st.error("Missing core required parameter mapping endpoints.")
    else:
        live_backup_df = (
            pd.read_csv(live_csv_file) if live_csv_file is not None else None
        )
        beta_backup_df = (
            pd.read_csv(beta_csv_file) if beta_csv_file is not None else None
        )

        with st.spinner("Executing structural index parsing pipelines..."):
            w1_urls = extract_urls_from_sitemap_url(sitemap_1_input.strip())
            w2_urls = extract_urls_from_sitemap_url(sitemap_2_input.strip())

        if len(w1_urls) == 0 or len(w2_urls) == 0:
            st.error("Failed to safely discover valid sitemap trees.")
        else:
            st.session_state.w1_count = len(w1_urls)
            st.session_state.w2_count = len(w2_urls)

            w1_slug_to_url = {}
            for url in w1_urls:
                slug = get_slug_from_url(url)
                if slug:
                    w1_slug_to_url[slug] = url

            w1_seo_data = {}
            progress_bar = st.progress(0)
            status_text = st.empty()

            for i, (slug, url) in enumerate(w1_slug_to_url.items()):
                status_text.markdown(f"🔍 `Harvesting Properties:` **/{slug}**")

                fallback_found = False
                if live_backup_df is not None and "slug" in live_backup_df.columns:
                    match_row = live_backup_df[live_backup_df["slug"] == slug]
                    if not match_row.empty:
                        row = match_row.iloc[0]
                        w1_seo_data[slug] = {
                            "title": row.get("seo_title", ""),
                            "meta_description": row.get("seo_description", ""),
                            "canonical": row.get("canonical_url", ""),
                            "keywords": row.get("focus_keyword", ""),
                            "schema_json_ld": row.get("schema_data", ""),
                            "fb_title": row.get("social_facebook_title", ""),
                            "fb_desc": row.get("social_facebook_description", ""),
                            "fb_image": row.get("social_facebook_thumbnail", ""),
                            "tw_title": row.get("social_twitter_title", ""),
                            "tw_desc": row.get("social_twitter_description", ""),
                            "tw_image": row.get("social_twitter_thumbnail", ""),
                        }
                        fallback_found = True

                if not fallback_found:
                    seo = scrape_current_live_site_seo(url)
                    if seo:
                        w1_seo_data[slug] = seo

                progress_bar.progress((i + 1) / len(w1_slug_to_url))

            progress_bar.empty()
            status_text.empty()

            final_rows = []
            matched_counter = 0

            beta_progress = st.progress(0)
            beta_status = st.empty()

            for idx, w2_url in enumerate(w2_urls, start=1):
                w2_slug = get_slug_from_url(w2_url)
                display_w2_slug = "/" if w2_slug == "homepage" else f"/{w2_slug}"
                beta_status.markdown(
                    f"🧬 `Synchronizing Database Records:` **{display_w2_slug}**"
                )

                wp_page_id = ""
                if beta_backup_df is not None and "slug" in beta_backup_df.columns:
                    match_beta = beta_backup_df[beta_backup_df["slug"] == w2_slug]
                    if not match_beta.empty:
                        wp_page_id = str(match_beta.iloc[0].get("id", ""))

                if not wp_page_id:
                    wp_page_id = extract_wordpress_page_id(w2_url)

                if w2_slug in w1_slug_to_url:
                    w1_url = w1_slug_to_url[w2_slug]
                    display_w1_slug = display_w2_slug
                    match_status = "MATCHED"
                    matched_counter += 1

                    seo = w1_seo_data.get(w2_slug, None)
                    meta_title = seo["title"] if seo else ""
                    meta_desc = seo["meta_description"] if seo else ""
                    canonical = seo["canonical"] if seo else ""
                    keywords = seo["keywords"] if seo else ""
                    schema = seo["schema_json_ld"] if seo else ""

                    fb_title = seo["fb_title"] if seo else ""
                    fb_desc = seo["fb_desc"] if seo else ""
                    fb_image = seo["fb_image"] if seo else ""
                    tw_title = seo["tw_title"] if seo else ""
                    tw_desc = seo["tw_desc"] if seo else ""
                    tw_image = seo["tw_image"] if seo else ""
                else:
                    w1_url = "N/A"
                    display_w1_slug = "N/A"
                    match_status = "NO MATCH"
                    meta_title, meta_desc, canonical, keywords, schema = (
                        "",
                        "",
                        "",
                        "",
                        "",
                    )
                    fb_title, fb_desc, fb_image, tw_title, tw_desc, tw_image = (
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                    )

                final_rows.append(
                    {
                        "#": idx,
                        "Beta WP Page ID": wp_page_id,
                        "Current Live Site Slug": display_w1_slug,
                        "Beta Site Slug": display_w2_slug,
                        "Match Status": match_status,
                        "Meta Tags / Keywords": keywords,
                        "Current Live Site Raw URL": w1_url,
                        "Beta Site Raw URL": w2_url,
                        "Meta Title (from Live)": meta_title,
                        "Meta Description (from Live)": meta_desc,
                        "Canonical Tag (from Live)": canonical,
                        "Schema JSON-LD": schema,
                        "fb_title": fb_title,
                        "fb_desc": fb_desc,
                        "fb_image": fb_image,
                        "tw_title": tw_title,
                        "tw_desc": tw_desc,
                        "tw_image": tw_image,
                    }
                )
                beta_progress.progress((idx) / len(w2_urls))

            beta_progress.empty()
            beta_status.empty()

            st.session_state.match_count = matched_counter
            st.session_state.audit_results = pd.DataFrame(final_rows)
            st.toast("Portfolio Matrix Created Successfully!", icon="✨")

if st.session_state.audit_results is not None:
    st.write("---")
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(label="Live Portfolio Size", value=st.session_state.w1_count)
    with m2:
        st.metric(label="Beta System Footprint", value=st.session_state.w2_count)
    with m3:
        st.metric(label="Successfully Intersected", value=st.session_state.match_count)

    st.write("")
    st.subheader("📊 Dynamic Cross-Mapping Inspection Grid")
    st.dataframe(
        st.session_state.audit_results, use_container_width=True, hide_index=True
    )

    st.write("")
    site_prefix = get_domain_prefix(sitemap_1_input)
    btn_col1, btn_col2, btn_col3 = st.columns(3)

    with btn_col1:
        csv_data = st.session_state.audit_results.to_csv(
            index=False, encoding="utf-8-sig"
        )
        st.download_button(
            label="📥 DOWNLOAD MASTER MIGRATION MATRIX",
            data=csv_data,
            file_name=f"{site_prefix}_seo_master_migration_matrix.csv",
            mime="text/csv",
            use_container_width=True,
        )

    with btn_col2:
        matched_df = st.session_state.audit_results[
            st.session_state.audit_results["Match Status"] == "MATCHED"
        ].copy()

        rankmath_complete_df = pd.DataFrame(
            {
                "id": matched_df["Beta WP Page ID"],
                "object_type": "post",
                "slug": matched_df["Beta Site Slug"].str.strip("/"),
                "seo_title": matched_df["Meta Title (from Live)"],
                "seo_description": matched_df["Meta Description (from Live)"],
                "is_pillar_content": 0,
                "focus_keyword": matched_df["Meta Tags / Keywords"],
                "seo_score": 80,
                "robots": "index, follow",
                "advanced_robots": "",
                "canonical_url": matched_df["Canonical Tag (from Live)"],
                "primary_term": "",
                "schema_data": matched_df["Schema JSON-LD"],
                "social_facebook_thumbnail": matched_df["fb_image"],
                "social_facebook_title": matched_df["fb_title"],
                "social_facebook_description": matched_df["fb_desc"],
                "social_twitter_thumbnail": matched_df["tw_image"],
                "social_twitter_title": matched_df["tw_title"],
                "social_twitter_description": matched_df["tw_desc"],
            }
        )

        rankmath_all_csv = rankmath_complete_df.to_csv(
            index=False, encoding="utf-8-sig"
        )
        st.download_button(
            label="🚀 EXPORT NATIVE RANKMATH COMPLIANT CSV",
            data=rankmath_all_csv,
            file_name=f"{site_prefix}_rankmath_ready_export.csv",
            mime="text/csv",
            use_container_width=True,
        )

    with btn_col3:
        if st.button("🔄 CLEAR ENGINE & RUN NEW AUDIT", use_container_width=True):
            st.session_state.audit_results = None
            st.session_state.w1_count = 0
            st.session_state.w2_count = 0
            st.session_state.match_count = 0
            st.rerun()

    # Brand Value Addition Section: Schema Structural Inspector Blueprint Panel
    st.write("---")
    st.subheader("🛡️ Deep Schema Blueprint Inspector")
    valid_schemas = st.session_state.audit_results[
        (st.session_state.audit_results["Schema JSON-LD"] != "")
        & (st.session_state.audit_results["Schema JSON-LD"] != "N/A")
    ]

    if not valid_schemas.empty:
        selected_slug = st.selectbox(
            "Select an isolated page URL mapping to preview discovered Rich Snippets:",
            valid_schemas["Beta Site Slug"].unique(),
        )
        json_str = valid_schemas[valid_schemas["Beta Site Slug"] == selected_slug][
            "Schema JSON-LD"
        ].values[0]
        try:
            st.json(json.loads(json_str))
        except Exception:
            st.code(json_str, language="json")
    else:
        st.info("No nested structured data graphs found across target profiles.")
