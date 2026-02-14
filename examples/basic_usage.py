"""
Example script demonstrating basic usage of the SmartNIC Agentic AI system.
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from smartnic import SmartNICInterface
from llm import LLMInference
from utils import setup_logging

import logging

logger = logging.getLogger(__name__)


def main():
    """Main example function."""
    # Setup logging
    setup_logging(level=logging.INFO)
    
    logger.info("Starting SmartNIC Agentic AI example")
    
    # Initialize SmartNIC interface
    logger.info("Initializing SmartNIC interface...")
    smartnic = SmartNICInterface(device_id="0000:00:00.0")
    
    if not smartnic.initialize():
        logger.error("Failed to initialize SmartNIC")
        return 1
    
    # Initialize LLM inference
    logger.info("Initializing LLM inference engine...")
    llm = LLMInference(model_name="distilgpt2", device="cpu")
    
    if not llm.load_model():
        logger.error("Failed to load LLM model")
        smartnic.close()
        return 1
    
    # Example inference
    logger.info("Running example inference...")
    input_text = "Hello, this is a test of the SmartNIC AI system"
    output_text = llm.infer(input_text, max_length=50)
    
    if output_text:
        logger.info(f"Input: {input_text}")
        logger.info(f"Output: {output_text}")
    else:
        logger.error("Inference failed")
    
    # Get model info
    model_info = llm.get_model_info()
    logger.info(f"Model info: {model_info}")
    
    # Get SmartNIC stats
    stats = smartnic.get_stats()
    logger.info(f"SmartNIC stats: {stats}")
    
    # Cleanup
    logger.info("Cleaning up...")
    smartnic.close()
    
    logger.info("Example completed successfully")
    return 0


if __name__ == "__main__":
    sys.exit(main())
