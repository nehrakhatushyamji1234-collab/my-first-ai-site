import streamlit as st

# Page Configuration
st.set_page_config(page_title="Global AI Tools Directory", page_icon="🚀", layout="wide")

# Custom CSS for Premium Dark UI
st.markdown("""
<style>
    .main { background-color: #0f111a; color: #ffffff; }
    .stButton>button { background-color: #6c5ce7; color: white; border-radius: 8px; border: none; width: 100%; }
    .stButton>button:hover { background-color: #a29bfe; color: black; }
    .card { background-color: #1a1c29; padding: 20px; border-radius: 12px; border: 1px solid #2d3748; margin-bottom: 20px; }
    .card-title { color: #00cec9; font-size: 22px; font-weight: bold; }
    .card-tag { background-color: #2d3748; color: #b2bec3; padding: 4px 10px; border-radius: 20px; font-size: 12px; display: inline-block; margin-bottom: 10px; }
    .pricing-free { color: #2ecc71; font-weight: bold; }
    .pricing-paid { color: #e74c3c; font-weight: bold; }
    .pricing-freemium { color: #f1c40f; font-weight: bold; }
</style>
""", unsafe_html=True)

# Dummy Database for AI Tools
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

# Header Section
st.title("🚀 Global AI Tools Directory")
st.subheader("Discover the world's most powerful AI tools to supercharge your workflow.")
st.write("---")

# Sidebar for Search and Filtering
st.sidebar.header("🔍 Filter AI Tools")
search_query = st.sidebar.text_input("Search Tools by Name or Keywords", "")

categories = ["All", "Copywriting", "Video Generation", "Voice & Audio", "Image & Design", "Developer Tools"]
selected_category = st.sidebar.selectbox("Select Category", categories)

pricing_filters = ["All", "Free", "Freemium", "Paid"]
selected_pricing = st.sidebar.selectbox("Pricing Model", pricing_filters)

# Filtering Logic
filtered_tools = ai_tools_data

if search_query:
    filtered_tools = [t for t in filtered_tools if search_query.lower() in t['name'].lower() or search_query.lower() in t['desc'].lower()]

if selected_category != "All":
    filtered_tools = [t for t in filtered_tools if t['category'] == selected_category]

if selected_pricing != "All":
    filtered_tools = [t for t in filtered_tools if t['pricing'] == selected_pricing]

# Displaying Tools in Grid Layout (3 Columns)
if filtered_tools:
    cols = st.columns(3)
    for index, tool in enumerate(filtered_tools):
        with cols[index % 3]:
            pricing_class = tool['pricing'].lower()
            st.markdown(f"""
            <div class="card">
                <span class="card-tag">{tool['category']}</span>
                <div class="card-title">{tool['name']}</div>
                <p style="font-size:14px; margin-top:10px; min-height:60px;">{tool['desc']}</p>
                <p style="font-size:13px;">Pricing: <span class="pricing-{pricing_class}">{tool['pricing']}</span> | 👥 Used by: {tool['clicks']}+</p>
            </div>
            """, unsafe_html=True)
            
            # Action Button
            st.link_button(f"Get Access to {tool['name']}", tool['url'])
else:
    st.info("Aapki search ke hisab se koi tool nahi mila. Please filters change karein.")

# Sidebar Footer
st.sidebar.write("---")
st.sidebar.markdown("💡 **Want to feature your AI Tool?**")
st.sidebar.caption("Contact: sponsor@yourdomain.com (Earn $200/listing)")
