import streamlit as st
import json

st.set_page_config(
    page_title="El Búnquer",
)

st.title("El Búnquer")

st.write("This is the intro page")

#Load the video link data to count the number of episodes
filePath = "/Users/parzival1918/Documents/GitHub/ElBunquer-Bricoheroes/Data/ElBunquer/videoInfo.json"
with open(filePath, "r") as f:
    videoInfo = json.load(f)

videoCount = videoInfo["videoCount"]

st.sidebar.metric("Episodis", videoCount)