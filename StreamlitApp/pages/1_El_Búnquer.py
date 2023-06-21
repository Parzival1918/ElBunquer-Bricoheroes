import streamlit as st
import json

st.set_page_config(
    page_title="El Búnquer",
)

st.title("El Búnquer")

#Load the video link data to count the number of episodes
filePath = "/Users/parzival1918/Documents/GitHub/ElBunquer-Bricoheroes/Data/ElBunquer/videoInfo.json"
with open(filePath, "r") as f:
    videoInfo = json.load(f)

videoCount = videoInfo["videoCount"]
videosData = videoInfo["videoData"]

st.sidebar.metric("Episodis", videoCount)

options = st.multiselect('Selecciona contingut que mostrar', \
                         ['Temporada 1', 'Temporada 2', 'Temporada 3', 'Extres'],\
                         default=['Temporada 1'])

if not options:
    st.warning("Selecciona contingut a mostrar")
else:
    numericOptions = []
    for option in options:
        if option == 'Temporada 1':
            numericOptions.append(1)
        elif option == 'Temporada 2':
            numericOptions.append(2)
        elif option == 'Temporada 3':
            numericOptions.append(3)
        elif option == 'Extres':
            numericOptions.append(4)

    col1, col2, col3 = st.columns(3)

    column = 1
    for videoData in videosData:
        if videoData["season"] in numericOptions:
            if column == 1:
                c = col1.container()
            elif column == 2:
                c = col2.container()
            elif column == 3:
                c = col3.container()

            c.image(videoData["videoThumbnails"]['medium']['url'], use_column_width=True)
            c.subheader(videoData["videoTitle"])
            expander = c.expander("Descripció")
            expander.write(videoData["videoDescription"])
            c.write("Link: " + videoData["videoLink"])
            c.divider()

            column += 1
            if column > 3:
                column = 1