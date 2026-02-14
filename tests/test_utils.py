"""
Unit tests for utility functions.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from utils import format_bytes, validate_config, measure_latency
import time


def test_format_bytes():
    """Test byte formatting."""
    assert format_bytes(0) == "0.00 B"
    assert format_bytes(1024) == "1.00 KB"
    assert format_bytes(1024 * 1024) == "1.00 MB"
    assert format_bytes(1024 * 1024 * 1024) == "1.00 GB"


def test_validate_config_success():
    """Test successful config validation."""
    config = {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3"
    }
    required = ["key1", "key2"]
    
    assert validate_config(config, required) is True


def test_validate_config_failure():
    """Test failed config validation."""
    config = {
        "key1": "value1"
    }
    required = ["key1", "key2", "key3"]
    
    assert validate_config(config, required) is False


def test_measure_latency_decorator():
    """Test latency measurement decorator."""
    @measure_latency
    def sample_function():
        time.sleep(0.01)
        return "done"
    
    result = sample_function()
    assert result == "done"
