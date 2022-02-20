# import os
# os.system("pip install -r requirements.txt")

import streamlit as st
import folium
from streamlit_folium import folium_static
import requests
import urllib.parse
import pandas as pd
from map_format import add_legends_popup
from core_data import get_data
from PIL import Image


st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)

col2, col3 = st.columns([6,1])
image = Image.open('image/log_regtangular.png')

with col2:
    st.image(image, width=700)

with col3:
    st.write("")

# st.image(image, width=500)

st.header("Parking Queen")
st.subheader("Find Meter Parking in Los Angeles")

location = st.text_input("Enter Your Destination: (e.g. Santa Monica Beach or 105 W 9th St)")

time = st.select_slider(
     'Select Time You Want to Park: ',
     options=['1 hour', '2 hours', '3 hours', '4+ hours'])


radius = st.slider('Select Radius (miles): ', 0.0, 5.0, 1.0)

space_type = st.radio(
     "Select Space Type",
     ('Single-Space', 'Multi-Space'))


def empty_map():
    folium_map = folium.Map(location=[34.0522, -118.2437], zoom_start=12)
    return folium_map


if st.button('Find Parking Space'):
    data, lat, long = get_data(location, radius, time, space_type)
    print(location, radius, time, space_type)
    if len(data) == 0:
        st.write("Woops... No spots found. Maybe try another radius?")
    else:
        st.write("We found " + str(len(data)) + " spots for you!")
    if 3 <= radius <= 5:
        zoom_start = 12
    else:
        zoom_start = 15
    folium_map = add_legends_popup(data, folium.Map(zoom_start=zoom_start, location=[lat, long]), lat, long)
else:
     folium_map = empty_map()


# folium_map = generate_map("700 W 9th St")
folium_static(folium_map)
