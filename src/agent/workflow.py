import sys
from typing import Dict, Any, Tuple
from src.logger import logging
from src.exception import CustomException
from src.components.model_predictor import predict_disease
from src.components.remedy_generator import generate_remedy

def run_analysis_pipeline(image_data: Any) -> Dict[str, Any]:
    """
    Orchestrates the end-to-end analysis pipeline.

    This function serves as the central workflow manager. It takes the raw image
    data from the user interface, passes it to the computer vision model for
    disease prediction, and then uses that prediction to generate a detailed
    remedy plan from the language model.

    Args:
        image_data (Any): The image data uploaded by the user, typically a
                          file-like object from Streamlit.

    Returns:
        Dict[str, Any]: A dictionary containing the final, user-friendly
                        analysis results.
    
    Raises:
        CustomException: If any step in the pipeline fails, it logs the error
                         and raises a custom exception with detailed context.
    """
    try:
        logging.info("--- Analysis Pipeline Started ---")


        logging.info("Calling the model predictor component...")
        disease_name, confidence = predict_disease(image_data)
        logging.info(f"Prediction successful. Detected disease: '{disease_name}' with confidence: {confidence:.2f}")


        logging.info("Calling the remedy generator component...")
        remedy_plan = generate_remedy(disease_name)
        logging.info("Remedy generation successful.")

        display_disease_name = disease_name.replace('___', ' ').replace('_', ' ')


        result = {
            "disease_name": display_disease_name,
            "confidence": confidence,
            "remedy_plan": remedy_plan
        }
        
        logging.info("--- Analysis Pipeline Completed Successfully ---")
        return result

    except Exception as e:
        logging.error(f"An error occurred in the main analysis pipeline: {e}")

        raise CustomException(e, sys)

