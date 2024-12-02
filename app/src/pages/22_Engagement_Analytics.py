import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')

# Display the appropriate sidebar links for the role of the logged-in user
SideBarLinks()

st.title('Engagement Analytics')

# load engagement analytics Data
@st.cache_data
def load_engagement_data():
    # load data from CSV file ??*************
    return pd.read_csv("SQL for LISAA csv files/engagementAnalytics.csv")

data = load_engagement_data()

# raw data for debugging purposes
if st.checkbox("raw Data"):
    st.dataframe(data)

# unique features to filter by
features = data['Feature'].unique()

# filters for engagement data
st.sidebar.subheader("Filters")
selected_feature = st.sidebar.selectbox("Select Feature", features, index=0)
selected_date_range = st.sidebar.date_input(
    "Select Date Range",
    value=[
        pd.to_datetime(data['Date']).min(),
        pd.to_datetime(data['Date']).max()
    ]
)

# filter data
filtered_data = data[
    (data['Feature'] == selected_feature) &
    (pd.to_datetime(data['Date']) >= pd.to_datetime(selected_date_range[0])) &
    (pd.to_datetime(data['Date']) <= pd.to_datetime(selected_date_range[1]))
]

# display filtered data
st.subheader(f"Filtered Engagement Data for '{selected_feature}'")
if not filtered_data.empty:
    st.dataframe(filtered_data)
else:
    st.warning("No data found for the selected filters.")

# visualize engagement trends
st.subheader("Engagement Trends")
if not filtered_data.empty:
    plt.figure(figsize=(10, 5))
    plt.plot(
        pd.to_datetime(filtered_data['Date']),
        filtered_data['UsageCount'],
        marker='o',
        linestyle='-',
        label=selected_feature
    )
    plt.title(f"Engagement Trends for '{selected_feature}'")
    plt.xlabel("Date")
    plt.ylabel("Usage Count")
    plt.legend()
    st.pyplot(plt)
else:
    st.warning("No data to visualize for the selected filters.")

# search for Features
st.subheader("Search Feature Engagement")
search_query = st.text_input("Search Features: ")

# filter feature buttons based on the search query
filtered_features = [feature for feature in features if search_query.lower() in feature.lower()]
for feature in filtered_features:
    if st.button(f"View Analytics for {feature}"):
        st.session_state['selected_feature'] = feature
        st.experimental_rerun()