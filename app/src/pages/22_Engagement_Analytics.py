import logging
import requests
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)

st.set_page_config(layout='wide')

SideBarLinks()

# Page Title
st.markdown(
    "<h1 style='color: #c0392b;'>Engagement Analytics</h1>",
    unsafe_allow_html=True,
)

# Load Engagement Analytics Data from API
def load_engagement_data():
    try:
        response = requests.get('http://api:4000/ea/engagementAnalytics')
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch engagement analytics data: {e}")
        st.error("Failed to load data from the server. Please try again later.")
        return pd.DataFrame()

# Load data
data = load_engagement_data()

# Ensure the DataFrame is not empty
if data.empty:
    st.error("No data available. Please check your backend or database.")
    st.stop()

# Extract unique features and calculate top 3 most used features
top_features = (
    data.groupby("feature")["usageCount"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
    .index.tolist()
)

# Top Features Overview Section
st.markdown(
    "<h3 style='color: #c0392b;'>Top 3 Engagement Features Overview</h3>",
    unsafe_allow_html=True,
)

top_cols = st.columns(3)  # Create 3 columns for side-by-side graphs

for i, feature in enumerate(top_features):
    feature_data = data[data["feature"] == feature]
    with top_cols[i]:
        # Plot feature graph
        plt.figure(figsize=(4, 3))
        plt.plot(
            pd.to_datetime(feature_data["date"]),
            feature_data["usageCount"],
            marker="o",
            linestyle="-",
            label=feature,
            color="#c0392b",
        )
        plt.title(f"{feature}", fontsize=14, color="#c0392b")
        plt.xlabel("Date", fontsize=10, color="#c0392b")
        plt.ylabel("Usage Count", fontsize=10, color="#c0392b")
        plt.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.7)
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        plt.tight_layout()
        st.pyplot(plt)

# Sidebar Filters
st.sidebar.markdown(
    "<h3 style='color: #c0392b;'>Filters</h3>",
    unsafe_allow_html=True,
)
features = data['feature'].unique()
selected_feature = st.sidebar.selectbox(
    "Select Feature",
    features,
    index=0,
)
selected_date_range = st.sidebar.date_input(
    "Select Date Range",
    value=[
        pd.to_datetime(data['date']).min(),
        pd.to_datetime(data['date']).max(),
    ],
)

# Filter data based on user selections
filtered_data = data[
    (data["feature"] == selected_feature)
    & (pd.to_datetime(data["date"]) >= pd.to_datetime(selected_date_range[0]))
    & (pd.to_datetime(data["date"]) <= pd.to_datetime(selected_date_range[1]))
]

# Display filtered data
st.markdown(
    f"<h3 style='color: #c0392b;'>Filtered Engagement Data for '{selected_feature}'</h3>",
    unsafe_allow_html=True,
)
if not filtered_data.empty:
    st.dataframe(filtered_data)
else:
    st.warning("No data found for the selected filters.")

# Visualize engagement trends
st.markdown(
    f"<h3 style='color: #c0392b;'>Engagement Trends</h3>",
    unsafe_allow_html=True,
)
if not filtered_data.empty:
    plt.figure(figsize=(10, 5))
    plt.plot(
        pd.to_datetime(filtered_data["date"]),
        filtered_data["usageCount"],
        marker="o",
        linestyle="-",
        label=selected_feature,
        color="#c0392b",
    )
    plt.title(f"Engagement Trends for '{selected_feature}'", color="#c0392b")
    plt.xlabel("Date", fontsize=12, color="#c0392b")
    plt.ylabel("Usage Count", fontsize=12, color="#c0392b")
    plt.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.7)
    plt.legend()
    st.pyplot(plt)
else:
    st.warning("No data to visualize for the selected filters.")

# ADD NEW RECORD
st.markdown("<h3 style='color: #c0392b;'>Add New Engagement Record</h3>", unsafe_allow_html=True)
with st.form("add_record_form"):
    new_feature = st.text_input("Feature")
    new_date = st.date_input("Date")
    new_usage_count = st.number_input("Usage Count", min_value=0, step=1)
    add_submit = st.form_submit_button("Add Record")

    if add_submit:
        if new_feature and new_date and new_usage_count >= 0:
            payload = {
                "feature": new_feature,
                "date": new_date.strftime("%Y-%m-%d"),
                "usageCount": new_usage_count
            }
            try:
                response = requests.post('http://api:4000/ea/engagementAnalytics', json=payload)
                if response.status_code == 201:
                    st.success("Record added successfully!")
                else:
                    st.error("Failed to add record. Please try again.")
            except Exception as e:
                st.error("Error adding record. Please check the logs.")
                logger.error(f"Error adding record: {e}")
        else:
            st.error("All fields are required.")

# UPDATE RECORD
st.markdown("<h3 style='color: #c0392b;'>Update Existing Engagement Record</h3>", unsafe_allow_html=True)
update_id = st.number_input("Enter Analytics ID to Update", min_value=1, step=1)
update_feature = st.text_input("Updated Feature", value="")
update_date = st.date_input("Updated Date")
update_usage_count = st.number_input("Updated Usage Count", min_value=0, step=1)
if st.button("Update Record"):
    payload = {}
    if update_feature:
        payload["feature"] = update_feature
    if update_date:
        payload["date"] = update_date.strftime("%Y-%m-%d")
    if update_usage_count >= 0:
        payload["usageCount"] = update_usage_count

    if payload:
        try:
            response = requests.put(f'http://api:4000/ea/engagementAnalytics/{update_id}', json=payload)
            if response.status_code == 200:
                st.success("Record updated successfully!")
            else:
                st.error("Failed to update record. Please try again.")
        except Exception as e:
            st.error("Error updating record. Please check the logs.")
            logger.error(f"Error updating record: {e}")
    else:
        st.error("At least one field is required to update.")

# DELETE RECORD
st.markdown("<h3 style='color: #c0392b;'>Delete Engagement Record</h3>", unsafe_allow_html=True)
delete_id = st.number_input("Enter Analytics ID to Delete", min_value=1, step=1)
if st.button("Delete Record"):
    try:
        response = requests.delete(f'http://api:4000/ea/engagementAnalytics/{delete_id}')
        if response.status_code == 200:
            st.success("Record deleted successfully!")
        else:
            st.error("Failed to delete record. Please try again.")
    except Exception as e:
        st.error("Error deleting record. Please check the logs.")
        logger.error(f"Error deleting record: {e}")