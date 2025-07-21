import sys
import os

# Import the main workflow and custom tools
from src.agent.workflow import run_analysis_pipeline
from src.exception import CustomException
from src.logger import logging

# --- Main Execution Block ---
if __name__ == "__main__":
    """
    This script is for command-line testing of the analysis pipeline.
    It allows developers to debug the backend without running the Streamlit UI.
    """
    try:
        logging.info("--- Starting Command-Line Test ---")

        # --- CONFIGURATION: Set the path to your test image here ---
        # Note: You need to have a test image in your project to use this script.
        # For example, create a 'test_images' folder in your project root.
        test_image_path = "test_images/test_tomato_leaf.jpg" 

        # Check if the test image exists
        if not os.path.exists(test_image_path):
            raise FileNotFoundError(f"Test image not found at path: {test_image_path}. Please create it.")

        logging.info(f"Using test image: {test_image_path}")

        # Open the image file in binary read mode
        with open(test_image_path, "rb") as image_file:
            # Call the main analysis pipeline with the image file object
            result = run_analysis_pipeline(image_file)

        # Print the results to the console
        print("\n--- ANALYSIS COMPLETE ---")
        print(f"  Disease Name: {result['disease_name']}")
        print(f"  Confidence:   {result['confidence']*100:.2f}%")
        print("\n--- REMEDY PLAN ---")
        print(result['remedy_plan'])
        print("\n--- TEST SUCCEEDED ---")

    except CustomException as e:
        logging.error(f"A custom exception occurred during the test: {e}")
        print(f"ERROR: {e}")
        sys.exit(1) # Exit with an error code
    except FileNotFoundError as e:
        logging.error(f"File not found error: {e}")
        print(f"ERROR: {e}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"An unexpected error occurred during the test: {e}")
        print(f"ERROR: An unexpected error occurred. Check logs for details.")
        sys.exit(1)

