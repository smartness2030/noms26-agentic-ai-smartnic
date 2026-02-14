# Architecture Documentation

## System Overview

The SmartNIC Agentic AI system is designed to offload Small Language Model (SLM) inference to SmartNIC hardware, enabling low-latency AI processing at the network edge.

## Components

### 1. SmartNIC Interface (`src/smartnic/`)

The SmartNIC interface module provides the hardware abstraction layer for communicating with SmartNIC devices.

**Key Features:**
- PCIe device management
- Packet sending and receiving
- Hardware statistics monitoring
- Queue management

**Classes:**
- `SmartNICInterface`: Main interface for SmartNIC operations

### 2. LLM Inference Engine (`src/llm/`)

The LLM inference module handles loading, optimizing, and running inference with Small Language Models.

**Key Features:**
- Model loading and initialization
- Inference execution (single and batch)
- Model optimization (quantization, pruning)
- Performance monitoring

**Classes:**
- `LLMInference`: Main inference engine

### 3. Utilities (`src/utils/`)

Helper functions for logging, timing, and configuration management.

**Key Functions:**
- `setup_logging()`: Configure logging
- `measure_latency()`: Decorator for timing functions
- `format_bytes()`: Format byte sizes
- `validate_config()`: Configuration validation

## Data Flow

```
Network Packet → SmartNIC Interface → LLM Inference → Response → SmartNIC Interface → Network
```

1. Packets arrive at the SmartNIC
2. SmartNIC extracts relevant data and forwards to LLM engine
3. LLM performs inference
4. Results are packaged and sent back through SmartNIC
5. SmartNIC forwards response to destination

## Optimization Strategies

### Model Optimization
- **Quantization**: Reduce model precision (INT8, INT4)
- **Pruning**: Remove less important weights
- **Knowledge Distillation**: Create smaller models from larger ones

### Hardware Optimization
- **Batching**: Process multiple requests together
- **Caching**: Cache frequent queries
- **Queue Management**: Optimize packet processing queues

## Performance Metrics

Key metrics to monitor:
- **Latency**: End-to-end inference time
- **Throughput**: Requests per second
- **Resource Utilization**: CPU/GPU/SmartNIC usage
- **Packet Loss**: Dropped packets due to overload

## Configuration

The system uses YAML configuration files located in `configs/`:
- Device IDs and hardware settings
- Model parameters
- Inference settings
- Logging configuration

## Future Work

- Support for additional model architectures
- Multi-model deployment
- Advanced caching strategies
- RDMA support for improved performance
