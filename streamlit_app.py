import streamlit as st
from pytube import YouTube
import requests

st.set_page_config("Youtube Video Downloader")

if __name__ == '__main__':
    st.title("YouTube Video Downloader 🚀")
    url = st.text_input("Enter the YouTube Video URL:", placeholder="Paste URL here")
    button1 = st.button("Get Video Details")

    if button1 not in st.session_state:
        st.session_state.button1 = False

    if button1:
        st.session_state.button1 = True
    
    if st.session_state.button1:
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            video_url = stream.url

            with st.spinner("Getting video details..."):
                video_content = requests.get(video_url).content

            st.image(yt.thumbnail_url)
            st.markdown(yt.title)
        except Exception as e:
            st.error(f"Error: {e}")

        if 'video_content' in locals():
            st.download_button(
                label="Download Video",
                data=video_content,
                file_name=f"{yt.title}.mp4",
                mime="video/mp4"
            )

footer = """<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
text-align: center;
}
</style>
<div class="footer">
<p>🕸 developed by Harrish😎</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
