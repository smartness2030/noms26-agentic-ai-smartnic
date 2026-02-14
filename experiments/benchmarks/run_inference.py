"""
Benchmark script for measuring inference latency and throughput.
"""

import sys
import os
import time
import statistics
from typing import List

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from llm import LLMInference
from utils import setup_logging, format_bytes

import logging

logger = logging.getLogger(__name__)


def measure_latency(llm: LLMInference, input_text: str, num_iterations: int = 100) -> List[float]:
    """
    Measure inference latency over multiple iterations.
    
    Args:
        llm: LLM inference engine
        input_text: Input text for inference
        num_iterations: Number of iterations to run
        
    Returns:
        list: List of latency measurements in milliseconds
    """
    latencies = []
    
    logger.info(f"Running {num_iterations} iterations...")
    
    for i in range(num_iterations):
        start_time = time.time()
        output = llm.infer(input_text)
        end_time = time.time()
        
        latency_ms = (end_time - start_time) * 1000
        latencies.append(latency_ms)
        
        if (i + 1) % 10 == 0:
            logger.info(f"Completed {i + 1}/{num_iterations} iterations")
    
    return latencies


def main():
    """Main benchmark function."""
    setup_logging(level=logging.INFO)
    
    logger.info("=== SmartNIC AI Inference Benchmark ===")
    
    # Initialize LLM
    logger.info("Initializing LLM inference engine...")
    llm = LLMInference(model_name="distilgpt2", device="cpu")
    
    if not llm.load_model():
        logger.error("Failed to load model")
        return 1
    
    # Test input
    input_text = "What is the purpose of SmartNIC in network processing?"
    
    # Warmup
    logger.info("Running warmup iterations...")
    for _ in range(10):
        llm.infer(input_text)
    
    # Run benchmark
    num_iterations = 100
    latencies = measure_latency(llm, input_text, num_iterations)
    
    # Calculate statistics
    mean_latency = statistics.mean(latencies)
    median_latency = statistics.median(latencies)
    min_latency = min(latencies)
    max_latency = max(latencies)
    std_latency = statistics.stdev(latencies) if len(latencies) > 1 else 0
    
    # Calculate throughput
    throughput = 1000.0 / mean_latency  # requests per second
    
    # Print results
    logger.info("\n=== Benchmark Results ===")
    logger.info(f"Number of iterations: {num_iterations}")
    logger.info(f"Mean latency: {mean_latency:.2f} ms")
    logger.info(f"Median latency: {median_latency:.2f} ms")
    logger.info(f"Min latency: {min_latency:.2f} ms")
    logger.info(f"Max latency: {max_latency:.2f} ms")
    logger.info(f"Std deviation: {std_latency:.2f} ms")
    logger.info(f"Throughput: {throughput:.2f} requests/second")
    
    # Model info
    model_info = llm.get_model_info()
    logger.info(f"\nModel: {model_info['name']}")
    logger.info(f"Device: {model_info['device']}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
