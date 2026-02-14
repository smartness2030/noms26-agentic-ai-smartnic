"""
Utility functions for the SmartNIC Agentic AI project.
"""

import logging
import time
from typing import Callable, Any

logger = logging.getLogger(__name__)


def setup_logging(level: int = logging.INFO, log_file: str = None):
    """
    Setup logging configuration.
    
    Args:
        level: Logging level (e.g., logging.INFO, logging.DEBUG)
        log_file: Optional log file path
    """
    handlers = [logging.StreamHandler()]
    
    if log_file:
        handlers.append(logging.FileHandler(log_file))
    
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=handlers
    )


def measure_latency(func: Callable) -> Callable:
    """
    Decorator to measure function execution time.
    
    Args:
        func: Function to measure
        
    Returns:
        Wrapped function that logs execution time
    """
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        latency = (end_time - start_time) * 1000  # Convert to milliseconds
        logger.info(f"{func.__name__} execution time: {latency:.2f} ms")
        
        return result
    
    return wrapper


def format_bytes(num_bytes: int) -> str:
    """
    Format bytes into human-readable string.
    
    Args:
        num_bytes: Number of bytes
        
    Returns:
        str: Formatted string (e.g., "1.5 MB")
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if num_bytes < 1024.0:
            return f"{num_bytes:.2f} {unit}"
        num_bytes /= 1024.0
    return f"{num_bytes:.2f} PB"


def validate_config(config: dict, required_keys: list) -> bool:
    """
    Validate that a configuration dictionary contains required keys.
    
    Args:
        config: Configuration dictionary to validate
        required_keys: List of required key names
        
    Returns:
        bool: True if all required keys present, False otherwise
    """
    missing_keys = [key for key in required_keys if key not in config]
    
    if missing_keys:
        logger.error(f"Missing required configuration keys: {missing_keys}")
        return False
    
    return True
