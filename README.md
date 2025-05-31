# quantumpractice

A collection of hands-on quantum computing examples using Qiskit, designed for learning and practice. Each example demonstrates a fundamental concept in quantum computing, from basic superposition to multi-qubit entanglement.

---

## Project Overview
This repository provides:
- Ready-to-run Qiskit example scripts
- Step-by-step code comments and explanations
- Practice material for interviews and self-study

---

## Setup Instructions

**Requirements:**
- macOS (darwin 24.3.0 or later)
- Python 3.8 or later
- Homebrew (recommended for package management)

**Setup Steps:**
1. Install Homebrew (if not already installed):
   ```sh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Install Python 3 (if not already installed):
   ```sh
   brew install python
   ```
3. Create and activate a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Upgrade pip:
   ```sh
   pip install --upgrade pip
   ```
5. Install Qiskit and Qiskit Aer:
   ```sh
   pip install qiskit qiskit-aer
   ```

For more details, see [Requirements.md](./Requirements.md).

---

## How to Run the Examples

All example scripts are in the `examples/` folder. To run an example:

```sh
python examples/<example_file.py>
```

---

## Example Scripts

### 1. test_qiskit.py
- **Concept:** Single-qubit superposition and measurement
- **What it does:**
  - Creates a single qubit
  - Applies a Hadamard gate to put it in superposition
  - Measures the qubit
  - Prints the measurement results (should be close to 50/50 for '0' and '1')

### 2. bell_state.py
- **Concept:** Two-qubit entanglement (Bell state)
- **What it does:**
  - Creates two qubits
  - Applies a Hadamard gate to the first qubit
  - Applies a CNOT gate to entangle the two qubits
  - Measures both qubits
  - Prints the measurement results (should be only '00' and '11', showing perfect correlation)

### 3. ghz_state.py
- **Concept:** Three-qubit entanglement (GHZ state)
- **What it does:**
  - Creates three qubits
  - Applies a Hadamard gate to the first qubit
  - Applies two CNOT gates to entangle all three qubits
  - Measures all qubits
  - Prints the measurement results (should be only '000' and '111', showing perfect three-way correlation)

---

## Additional Resources
- [Qiskit Documentation](https://qiskit.org/documentation/)
- [IBM Quantum Lab](https://quantum-computing.ibm.com/)

For setup troubleshooting and more, see [Requirements.md](./Requirements.md). 