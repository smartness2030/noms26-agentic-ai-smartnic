# NOMS 2026: Towards Network Agentic AI - Offloading Small Language Models to SmartNICs

This repository contains the implementation and experiments for the NOMS 2026 paper on offloading Small Language Models (SLMs) to SmartNICs for network agentic AI applications.

## Overview

This project explores the offloading of Small Language Models to SmartNICs to enable intelligent, low-latency network processing. By leveraging the computational capabilities of SmartNICs, we aim to perform AI inference directly at the network edge, reducing latency and improving overall system performance.

## Project Structure

```
.
├── src/                    # Source code
│   ├── smartnic/          # SmartNIC interface and drivers
│   ├── llm/               # LLM model loading and inference
│   └── utils/             # Utility functions
├── experiments/           # Experiment scripts and data
│   ├── benchmarks/        # Performance benchmarks
│   └── data/              # Experimental data
├── docs/                  # Documentation and paper materials
├── tests/                 # Unit and integration tests
├── configs/               # Configuration files
└── requirements.txt       # Python dependencies
```

## Installation

### Prerequisites

- Python 3.8 or higher
- CUDA-capable GPU (optional, for development)
- SmartNIC hardware (for deployment)
- DPDK (Data Plane Development Kit)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/smartness2030/noms26-agentic-ai-smartnic.git
cd noms26-agentic-ai-smartnic
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running Experiments

```bash
python experiments/benchmarks/run_inference.py
```

### Configuration

Configuration files are located in the `configs/` directory. You can customize model parameters, network settings, and hardware configurations.

## Features

- **SmartNIC Integration**: Direct hardware interface for efficient packet processing
- **LLM Offloading**: Optimized model inference on SmartNIC hardware
- **Low Latency**: Minimized processing time for real-time applications
- **Scalability**: Support for multiple concurrent inference requests
- **Benchmarking Tools**: Comprehensive performance evaluation suite

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## Citation

If you use this code in your research, please cite our paper:

```bibtex
@inproceedings{noms2026-agentic-smartnic,
  title={Towards Network Agentic AI: Offloading Small Language Models to SmartNICs},
  author={[Authors]},
  booktitle={IFIP/IEEE Network Operations and Management Symposium (NOMS)},
  year={2026}
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or collaborations, please open an issue on GitHub or contact the maintainers.

## Acknowledgments

This research is presented at NOMS 2026 (IFIP/IEEE Network Operations and Management Symposium).
