import streamlit as st
import pandas as pd

st.subheader("Uploading the CSV File.")
df = st.file_uploader("Upload the file : ",type= ['csv','xlsx'])
# if df is not None:
#     st.dataframe(df)

st.subheader("Loading the CSV File.")
df = pd.read_csv("D:\Data Science\Streamlit\Products.csv")
if df is not None:
    st.table(df.head())

# st.subheader('Dealing with images directly')
# st.image('img.png')

st.subheader('Working with Images')
image_file = st.file_uploader('Upload the Image file : ',type=['png','jpg','jpeg'])
if image_file is not None:
    st.image(image_file)

st.subheader("Working with Videos")
video_file = st.file_uploader('Upload the Video file : ',type=['mp4','mkv'])
if video_file is not None:
    st.video(video_file, start_time=0)

st.subheader("Working with Audios")
audio_file = st.file_uploader('Upload the Audio file : ',type=['mp3','wav'])
if audio_file is not None:
    st.audio(audio_file.read())
