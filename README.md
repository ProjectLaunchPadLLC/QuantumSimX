# QuantumSimX

**QuantumSimX** is a custom quantum simulation library created for educational and research purposes. The library allows you to simulate basic quantum circuits, including superposition and entanglement, with custom gates and operations. This library avoids dependencies on major quantum toolkits, providing a minimal yet powerful quantum simulator.

## Features

- Quantum state representation and manipulation.
- A set of quantum gates (Hadamard, Pauli-X, CNOT, etc.).
- Circuit construction and simulation.
- Measurement with probabilistic outcomes.

## Installation

To install the library, use `pip`:

```bash
pip install quantum-simx
Usage
Creating a Quantum State
python
Copy code
from quantum_simx.quantum_state import QuantumState
state = QuantumState(2)  # 2 qubits
Applying a Gate
python
Copy code
from quantum_simx.quantum_gate import H_gate, X_gate
state.apply_gate(H_gate, [0])  # Apply Hadamard gate to qubit 0
Building a Quantum Circuit
python
Copy code
from quantum_simx.quantum_circuit import QuantumCircuit
circuit = QuantumCircuit(2)
circuit.add_gate(H_gate, [0])  # Apply Hadamard gate to qubit 0
Measurement
python
Copy code
outcome = state.measure()  # Simulate measurement
Contributing
Feel free to fork this project and submit your pull requests. We welcome any contributions or suggestions for new features.

yaml
Copy code

---

### **Step 4: Create the `requirements.txt` File**

This file will list the dependencies required to run the project.

#### 4.1 **`requirements.txt`**

**Path**: `QuantumSimX/requirements.txt`

numpy

arduino
Copy code

---

### **Step 5: Create the Test File**

To ensure that the code works correctly, let's create a simple test file to validate basic operations.

#### 5.1 **`test_quantum_simx.py`**

**Path**: `QuantumSimX/tests/test_quantum_simx.py`

```python
import unittest
import numpy as np
from quantum_simx.quantum_state import QuantumState
from quantum_simx.quantum_gate import H_gate, X_gate
from quantum_simx.quantum_circuit import QuantumCircuit

class TestQuantumSimX(unittest.TestCase):

    def test_quantum_state_initialization(self):
        state = QuantumState(2)
        self.assertEqual(np.abs(state.get_state()) ** 2, [1, 0, 0, 0])  # |00> state

    def test_apply_gate(self):
        state = QuantumState(1)
        state.apply_gate(H_gate, [0])
        state_vec = state.get_state()
        self.assertAlmostEqual(np.abs(state_vec[0]) ** 2, 0.5)
        self.assertAlmostEqual(np.abs(state_vec[1]) ** 2, 0.5)

    def test_measurement(self):
        state = QuantumState(1)
        state.apply_gate(H_gate, [0])
        outcome = state.measure()
        self.assertIn(outcome, [0, 1])

    def test_quantum_circuit(self):
        state = QuantumState(2)
        circuit = QuantumCircuit(2)
        circuit.add_gate(H_gate, [0])
        circuit.add_gate(X_gate, [1])
        final_state = circuit.apply(state)
        self.assertNotEqual(final_state.get_state()[0], 1)  # |01> state is expected

if __name__ == '__main__':
    unittest.main()
Step 6: Upload to GitHub
Once all files are created, you can upload the project to GitHub:

Initialize a git repository:
bash
Copy code
git init
``








