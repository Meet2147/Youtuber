import streamlit as st
from pytube import YouTube
import os
import base64
# Create a Streamlit web app
st.title("YouTube Video Downloader")

# User input for the YouTube video URL
video_url = st.text_input("Enter the YouTube video URL:")

# Function to download the video
def download_video(url):
    try:
        st.text("Downloading...")
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").first()

        # Get the user's download directory
        download_folder = os.path.expanduser("~" + os.path.sep + "Downloads")
        
        # Download the video to the user's download directory
        stream.download(output_path=download_folder)
        
        st.success(f"Download completed: {yt.title}")

        # Provide a download link to the user
        download_link = os.path.join(download_folder, yt.title + ".mp4")
        st.markdown(get_binary_file_downloader_html(download_link), unsafe_allow_html=True)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Function to generate a download link
def get_binary_file_downloader_html(bin_file, file_label='Click here to download the video'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'data:application/octet-stream;base64,{bin_str}'
    return f'<a href="{href}" download="{os.path.basename(bin_file)}">{file_label}</a>'

# Button to trigger the download
if st.button("Download Video"):
    download_video(video_url)
