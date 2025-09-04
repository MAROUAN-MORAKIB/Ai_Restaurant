import streamlit as st
import requests
import model

# --- Page config ---
st.set_page_config(
    page_title="AI Restaurant Menu Generator",
    page_icon="🍽️",
    layout="wide",
)

# --- App title ---
st.markdown(
    """
    <h1 style="text-align: center; color: #FF6B35; font-family: 'Trebuchet MS', sans-serif;">
        🍽️ AI Restaurant Menu Generator
    </h1>
    <p style="text-align: center; color: #555; font-size:18px;">
        Enter a cuisine type and get a fancy restaurant name with a menu — complete with images!
    </p>
    <hr>
    """,
    unsafe_allow_html=True,
)

# Sidebar input
cuisine = st.sidebar.text_input("👉 Enter Cuisine Type (e.g., Italian, Chinese, etc.)")

# Secrets
# UNSPLASH_ACCESS_KEY = st.secrets["UNSPLASH_ACCESS_KEY"]
# PEXELS_API_KEY = st.secrets["PEXELS_API_KEY"]

PEXELS_API_KEY = "tal9pr67wItKgEeUte5itgIPINBLADpTdffxG6GlJ644qMbf3t3WNkhu"  
UNSPLASH_ACCESS_KEY = "vIKeT7IGLK9db2bp1hxkseS-v5kQgHXrdw60EQh9Qow"


# --- Image fetcher ---
def get_image_for_item(item):
    # Try Unsplash first
    unsplash_url = f"https://api.unsplash.com/photos/random?query={item},food&client_id={UNSPLASH_ACCESS_KEY}"
    response = requests.get(unsplash_url)
    if response.status_code == 200:
        data = response.json()
        if "urls" in data:
            return data["urls"]["regular"]

    # Fallback to Pexels
    pexels_url = f"https://api.pexels.com/v1/search?query={item},food&per_page=1"
    headers = {"Authorization": PEXELS_API_KEY}
    response = requests.get(pexels_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data.get("photos"):
            return data["photos"][0]["src"]["large"]

    # Generic fallback
    return "https://images.unsplash.com/photo-1504674900247-0877df9cc836"

# --- Main logic ---
if cuisine:
    restaurant_data = model.get_restaurant_name_items(cuisine)
    st.markdown(
        f"<h2 style='text-align:center; color:#FF6B35;'>{restaurant_data['restaurant_name'].strip()}</h2>",
        unsafe_allow_html=True,
    )

    menu_items = restaurant_data['menu_items'].strip().split(',')
    st.markdown("### 📜 Menu Items")

    cols = st.columns(2)  # Two columns layout
    for idx, item in enumerate(menu_items):
        item_name = item.strip()
        img_url = get_image_for_item(item_name)

        with cols[idx % 2]:
            st.markdown(
                f"""
                <div style="border:1px solid #ddd; border-radius:12px; padding:10px; margin-bottom:20px; background:#fafafa; box-shadow:2px 2px 6px rgba(0,0,0,0.05);">
                    <h4 style="color:#333; text-align:center;">{item_name}</h4>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.image(img_url, use_column_width=True)