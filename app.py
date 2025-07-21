import streamlit as st
from PIL import Image
import sys

from src.agent.workflow import run_analysis_pipeline
from src.exception import CustomException
from src.logger import logging
st.set_page_config(
    page_title="Fasal Doctor - AI Plant Disease Diagnosis",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="auto"
)


st.title("🌿 Fasal Doctor")
st.markdown(
    "Welcome! Upload a clear photo of a plant leaf, and our AI assistant "
    "will diagnose the disease and provide a recommended action plan."
)


uploaded_file = st.file_uploader(
    "Click here to choose an image...",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption='Your Uploaded Image.', use_column_width=True)
    

    if st.button("Analyze Image"):

        with st.spinner("Our AI is analyzing the image. Please wait..."):
            try:
                logging.info("Analysis started from Streamlit UI.")
                

                result = run_analysis_pipeline(uploaded_file)
                
                # Display the results
                st.success("Analysis Complete!")
                st.markdown("---")
                
                st.subheader(f"Diagnosis: {result['disease_name']}")
                st.metric(label="Confidence", value=f"{result['confidence']*100:.2f}%")
                
                st.subheader("Recommended Action Plan:")
                st.markdown(result['remedy_plan'])
                
                logging.info("Results displayed successfully on Streamlit UI.")

            except CustomException as e:
                # Handle custom exceptions gracefully
                error_message = f"An error occurred during analysis: {e}"
                logging.error(error_message)
                st.error(error_message)
            except Exception as e:
                # Handle any other unexpected exceptions
                error_message = f"An unexpected error occurred: {e}"
                logging.error(error_message)
                st.error(error_message)
