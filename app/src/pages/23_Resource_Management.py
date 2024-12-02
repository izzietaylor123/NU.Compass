import logging
logger = logging.getLogger(__name__)

import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

SideBarLinks()

st.title("Resource Management")

# load resources and locations data ??? * check correct way to do this
@st.cache_data
def load_resources():
    return pd.read_csv("SQL for LISAA csv files/Resources.csv")

@st.cache_data
def load_locations():
    return pd.read_csv("SQL for LISAA csv files/Location.csv")

resources_data = load_resources()
locations_data = load_locations()

# raw data option
if st.checkbox("Show Raw Resources Data"):
    st.dataframe(resources_data)

# filter by location
st.sidebar.subheader("Filters")
locations = locations_data['City'] + ", " + locations_data['Country']
selected_location = st.sidebar.selectbox("Select Location", locations)

# get LocationID for selected location
location_id = locations_data[locations_data['City'] + ", " + locations_data['Country'] == selected_location]['LocationID'].iloc[0]
filtered_resources = resources_data[resources_data['LocationID'] == location_id]

st.subheader(f"Resources for {selected_location}")
if not filtered_resources.empty:
    st.dataframe(filtered_resources)
else:
    st.warning(f"No resources found for {selected_location}")

# edit resources section
st.subheader("Edit Resources")
for index, resource in filtered_resources.iterrows():
    with st.expander(f"Edit Resource: {resource['Type']}"):
        # modify resource data (type, description, link)
        new_type = st.text_input(f"Edit Type ({resource['Type']})", value=resource['Type'])
        new_description = st.text_area(f"Edit Description", value=resource['Description'])
        new_url = st.text_input(f"Edit URL", value=resource['URL'])

        if st.button(f"Save Changes to {resource['Type']}"):
            # update the resource
            resources_data.loc[resources_data['ResourceID'] == resource['ResourceID'], 'Type'] = new_type
            resources_data.loc[resources_data['ResourceID'] == resource['ResourceID'], 'Description'] = new_description
            resources_data.loc[resources_data['ResourceID'] == resource['ResourceID'], 'URL'] = new_url
            st.success(f"Resource '{resource['Type']}' updated successfully!")

# archive resources
st.subheader("Archive Resources")
for index, resource in filtered_resources.iterrows():
    if st.button(f"Archive {resource['Type']}"):
        resources_data.loc[resources_data['ResourceID'] == resource['ResourceID'], 'Status'] = "Archived"
        st.success(f"Resource '{resource['Type']}' archived.")

# show archived resources
st.subheader("Archived Resources")
archived_resources = resources_data[resources_data.get('Status', '') == "Archived"]
if not archived_resources.empty:
    st.dataframe(archived_resources)
else:
    st.write("No archived resources.")
