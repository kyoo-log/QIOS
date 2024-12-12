# Simple Quantum-Inspired Optimization API

This is a simple API that demonstrates quantum-inspired optimization using the Quantum Approximate Optimization Algorithm (QAOA) to solve the MaxCut problem. It uses Qiskit for quantum circuit simulation and FastAPI for creating the API.

## Getting Started

1.  Clone the repository: `git clone https://github.com/kyoo-log/QIOS.git` (replace with your repo URL)
2.  Create a virtual environment (recommended): `python -m venv .venv`
3.  Activate the virtual environment:
    *   Windows: `.venv\Scripts\activate`
    *   macOS/Linux: `source .venv/bin/activate`
4.  Install dependencies: `pip install -r requirements.txt`
5.  Run the API: `uvicorn main:app --reload`

## Usage

Send a POST request to `/max_cut` with a JSON payload containing the adjacency matrix of the graph and the number of QAOA layers (`p`).

Example Request:

```json
{
  "graph": [[0, 1, 1], [1, 0, 1], [1, 1, 0]],
  "p": 2
}