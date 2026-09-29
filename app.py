import streamlit as st

# 1. Page Configuration (Sabse upar hona zaroori hai)
st.set_page_config(page_title="Global AI Tools Directory", page_icon="🚀", layout="wide")

# 2. Dummy Database for AI Tools
ai_tools_data = [
    {
        "name": "VantaBlack AI Writer",
        "category": "Copywriting",
        "pricing": "Freemium",
        "desc": "Create ultra-engaging marketing copies and blogs in 100+ languages using neuro-linguistic AI models.",
        "url": "https://google.com",
        "clicks": 1420
    },
    {
        "name": "Synthesia Video Gen",
        "category": "Video Generation",
        "pricing": "Paid",
        "desc": "Turn text into high-quality videos with realistic AI avatars and voiceovers in minutes.",
        "url": "https://google.com",
        "clicks": 985
    },
    {
        "name": "ElevenLabs Voice Pro",
        "category": "Voice & Audio",
        "pricing": "Freemium",
        "desc": "The most realistic AI voice generator that clones human emotions and accents flawlessly.",
        "url": "https://google.com",
        "clicks": 2310
    },
    {
        "name": "Midjourney Helper",
        "category": "Image & Design",
        "pricing": "Free",
        "desc": "Generate hyper-realistic art prompts and master text-to-image variations easily.",
        "url": "https://google.com",
        "clicks": 3110
    }
]

# 3. TOP ADSENSE PLACEHOLDER (Website ke sabse upar ka Ad box)
# Jab aapko AdSense ka code milega, toh aap 'YAHAN APNA ADSENSE CODE DALEIN' ko mita kar apna asli code paste kar denge.
st.markdown("""
<div style="background-color: #f8f9fa; padding: 10px; text-align: center; border: 1px dashed #cccccc; margin-bottom: 20px; color: #666666;">
    📢 [Google AdSense Horizontal Banner Ad Place - YAHAN APNA CODE DALEIN]
</div>
""", unsafe_html=True)

# 4. Header Section
st.title("🚀 Global AI Tools Directory")
st.subheader("Discover the world's most powerful AI tools to supercharge your workflow.")
st.write("---")

# 5. Sidebar for Search and Filtering
st.sidebar.header("🔍 Filter AI Tools")
search_query = st.sidebar.text_input("Search Tools by Name or Keywords", "")

categories = ["All", "Copywriting", "Video Generation", "Voice & Audio", "Image & Design"]
selected_category = st.sidebar.selectbox("Select Category", categories)

pricing_filters = ["All", "Free", "Freemium", "Paid"]
selected_pricing = st.sidebar.selectbox("Pricing Model", pricing_filters)

# 6. SIDEBAR ADSENSE PLACEHOLDER (Sidebar ke niche ka Ad box)
st.sidebar.write("---")
st.sidebar.markdown("### 📢 Sponsored Ad")
st.sidebar.markdown("""
<div style="background-color: #f8f9fa; padding: 20px; text-align: center; border: 1px dashed #cccccc; height: 250px; color: #666666;">
    [Google AdSense Vertical Banner Ad Place - YAHAN APNA CODE DALEIN]
</div>
""", unsafe_html=True)

# 7. Filtering Logic
filtered_tools = ai_tools_data

if search_query:
    filtered_tools = [t for t in filtered_tools if search_query.lower() in t['name'].lower() or search_query.lower() in t['desc'].lower()]

if selected_category != "All":
    filtered_tools = [t for t in filtered_tools if t['category'] == selected_category]

if selected_pricing != "All":
    filtered_tools = [t for t in filtered_tools if t['pricing'] == selected_pricing]

# 8. Displaying Tools in Grid Layout (3 Columns)
if filtered_tools:
    cols = st.columns(3)
    for index, tool in enumerate(filtered_tools):
        with cols[index % 3]:
            with st.container(border=True):
                st.write(f"🏷️ **{tool['category']}**")
                st.subheader(tool['name'])
                st.write(tool['desc'])
                st.write(f"💰 Pricing: **{tool['pricing']}** | 👥 Clicks: {tool['clicks']}+")
                st.link_button(f"Get Access to {tool['name']}", tool['url'])
else:
    st.info("Aapki search ke hisab se koi tool nahi mila. Please filters change karein.")

# 9. Sidebar Footer
st.sidebar.write("---")
st.sidebar.markdown("💡 **Want to feature your AI Tool?**")
st.sidebar.caption("Contact: sponsor@yourdomain.com (Earn $200/listing)")
