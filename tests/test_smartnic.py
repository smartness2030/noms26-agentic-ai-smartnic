"""
Unit tests for SmartNIC interface module.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from smartnic import SmartNICInterface


def test_smartnic_initialization():
    """Test SmartNIC interface initialization."""
    smartnic = SmartNICInterface(device_id="0000:00:00.0")
    assert smartnic.device_id == "0000:00:00.0"
    assert not smartnic.initialized


def test_smartnic_initialize():
    """Test SmartNIC hardware initialization."""
    smartnic = SmartNICInterface(device_id="0000:00:00.0")
    result = smartnic.initialize()
    assert result is True
    assert smartnic.initialized


def test_smartnic_stats():
    """Test retrieving SmartNIC statistics."""
    smartnic = SmartNICInterface(device_id="0000:00:00.0")
    smartnic.initialize()
    
    stats = smartnic.get_stats()
    assert isinstance(stats, dict)
    assert "packets_sent" in stats
    assert "packets_received" in stats
    assert "errors" in stats


def test_smartnic_not_initialized_error():
    """Test that operations fail when SmartNIC not initialized."""
    smartnic = SmartNICInterface(device_id="0000:00:00.0")
    
    with pytest.raises(RuntimeError):
        smartnic.send_packet(b"test data")
    
    with pytest.raises(RuntimeError):
        smartnic.receive_packet()
    
    with pytest.raises(RuntimeError):
        smartnic.get_stats()


def test_smartnic_close():
    """Test SmartNIC interface cleanup."""
    smartnic = SmartNICInterface(device_id="0000:00:00.0")
    smartnic.initialize()
    assert smartnic.initialized
    
    smartnic.close()
    assert not smartnic.initialized
