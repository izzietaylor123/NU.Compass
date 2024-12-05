import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout="wide")

SideBarLinks()

# Page Title
st.markdown(
    "<h1 style='color: #c0392b;'>GEO Contact Information</h1>",
    unsafe_allow_html=True,
)

# Adam Brody's Information
adam_info = {
    "name": "Adam Brody",
    "phone": "+1 (123) 456-7890",
    "email": "adam.brody@northeastern.edu",
    "blurb": (
        "Hi, I'm Adam Brody, your Northeastern GEO advisor. I'm here to assist with "
        "any questions you may have about studying abroad, including housing, academics, "
        "or adjusting to life in a new country. Don't hesitate to reach out!"
    ),
    "photo_url": "assets/Adam_Headshot.jpg",  # Path to the photo
}

# Page Layout
col1, col2 = st.columns([1, 2])

# Photo and Contact Info
with col1:
    st.image(
        adam_info['photo_url'],
        caption=adam_info['name'],
        use_container_width=True,  # Adjusted parameter
        width=80,
    )
    st.markdown(
        """
        <style>
            img {
                border-radius: 50%;
                border: 3px solid #c0392b;
                display: block;
                margin: auto;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
        <h2 style='color: #c0392b;'>{adam_info['name']}</h2>
        <p><strong>Phone:</strong> {adam_info['phone']}</p>
        <p><strong>Email:</strong> <a href='mailto:{adam_info['email']}' style='color: #c0392b;'>{adam_info['email']}</a></p>
        <p>{adam_info['blurb']}</p>
        """,
        unsafe_allow_html=True,
    )

    # Additional Useful Information
    st.markdown("<h3 style='color: #c0392b;'>Additional Information</h3>", unsafe_allow_html=True)

    st.markdown(
        """
        - **Office Hours:** Monday to Friday, 9:00 AM - 5:00 PM EST
        - **Location:** Northeastern University Global Experience Office, 360 Huntington Ave, Boston, MA 02115
        - **Emergency Contact:** +1 (987) 654-3210 (Available 24/7 for urgent abroad concerns)
        - **Resource Links:**
            - [Study Abroad FAQs](https://studyabroad.northeastern.edu/faqs)
            - [Student Handbook](https://studyabroad.northeastern.edu/handbook)
        """,
        unsafe_allow_html=True,
    )
