import streamlit as st
import json

st.set_page_config(
    page_title="Bricoheroes",
)

st.title("Bricoheroes")

#Load the video link data to count the number of episodes
filePath = "/Users/parzival1918/Documents/GitHub/ElBunquer-Bricoheroes/Data/Bricoheroes/videoInfo.json"
with open(filePath, "r") as f:
    videoInfo = json.load(f)

videoCount = videoInfo["videoCount"]

st.sidebar.metric("Episodis", videoCount)