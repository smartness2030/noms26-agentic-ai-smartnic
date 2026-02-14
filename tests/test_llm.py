"""
Unit tests for LLM inference module.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from llm import LLMInference


def test_llm_initialization():
    """Test LLM inference initialization."""
    llm = LLMInference(model_name="distilgpt2", device="cpu")
    assert llm.model_name == "distilgpt2"
    assert llm.device == "cpu"
    assert llm.model is None


def test_llm_load_model():
    """Test LLM model loading."""
    llm = LLMInference(model_name="distilgpt2", device="cpu")
    result = llm.load_model()
    assert result is True


def test_llm_infer():
    """Test LLM inference."""
    llm = LLMInference(model_name="distilgpt2", device="cpu")
    llm.load_model()
    
    input_text = "Test input"
    output = llm.infer(input_text, max_length=50)
    
    assert output is not None
    assert isinstance(output, str)


def test_llm_batch_infer():
    """Test LLM batch inference."""
    llm = LLMInference(model_name="distilgpt2", device="cpu")
    llm.load_model()
    
    inputs = ["Test 1", "Test 2", "Test 3"]
    outputs = llm.batch_infer(inputs, max_length=50)
    
    assert len(outputs) == len(inputs)
    assert all(output is not None for output in outputs)


def test_llm_model_info():
    """Test getting model information."""
    llm = LLMInference(model_name="distilgpt2", device="cpu")
    
    # Before loading
    info = llm.get_model_info()
    assert info["loaded"] is False
    
    # After loading
    llm.load_model()
    info = llm.get_model_info()
    assert info["loaded"] is True
    assert info["name"] == "distilgpt2"


def test_llm_not_loaded_error():
    """Test that inference fails when model not loaded."""
    llm = LLMInference(model_name="distilgpt2", device="cpu")
    
    with pytest.raises(RuntimeError):
        llm.infer("test")
    
    with pytest.raises(RuntimeError):
        llm.batch_infer(["test"])
    
    with pytest.raises(RuntimeError):
        llm.optimize_for_smartnic()
