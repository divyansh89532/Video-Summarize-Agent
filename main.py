import streamlit as st 
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file,get_file
import time 
import os
from pathlib import Path  # to handle.env file
import tempfile
import google.generativeai as genai


from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GOOGLE_API_KEY')

if API_KEY:
    genai.configure(api_key=API_KEY)





# Set up the agent
st.set_page_config(page_title="Agent Chatbot", layout="wide",page_icon=":robot:")

st.title("Video Agent")
st.header("Welcome to our virtual vidoe summarizer tool !")


@st.cache_resource
def intialize_agent():
    return Agent(
        name="Video Summarizer", 
        model=Gemini(id='gemini-2.0-flash-exp'),
        tools=[DuckDuckGo()],
        markdown=True
    )

agent = intialize_agent()

video_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"],help="Select a video file to summarize.")

if video_file:
    with tempfile.NamedTemporaryFile(delete=False,suffix='.mp4') as temp_video:
        temp_video.write(video_file.read())
        video_path = temp_video.name

    st.video(video_path,format="video/mp4",start_time=0)

    user_query = st.text_area(
        "What insights are you looking from the video?",
        placeholder="Type your question here...",
        help="Provide specific details about the video content.",
    )

    if st.button("Summarize", key="analyze_video_button"):
        if not user_query:
            st.warning("Please provide a question to summarize the video.")
        else:
            try:
                with st.spinner("Uploading and processing the video..."):
                    processed_video = upload_file(video_path)

                    # Wait until the video is in an ACTIVE state
                    max_retries = 30  # Adjust if needed
                    retries = 0
                    while processed_video.state.name != "ACTIVE" and retries < max_retries:
                        time.sleep(2)  # Wait 2 seconds before checking again
                        processed_video = get_file(processed_video.name)
                        retries += 1

                    if processed_video.state.name != "ACTIVE":
                        st.error("The video processing took too long. Please try again later.")
                    else:
                        analysis_prompt = (
                            f"""
                            Analyze the uploaded video for content and context.
                            Respond to the following query using video insights and supplementary web research.
                            {user_query}
                            Provide a detailed, user-friendly summary of the video content.
                            """
                        )

                        response = agent.run(analysis_prompt, videos=[processed_video])   

                    st.subheader("Result:")
                    st.markdown(response.content)     

            except Exception as e:
                st.error(f"An error occurred while summarizing the video: {str(e)}")
            finally:
                Path(video_path).unlink(missing_ok=True)
else:
    st.info("Please upload a video file to start summarizing.")     




# will work for videos maximum size of 200MB

