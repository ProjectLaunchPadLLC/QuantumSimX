import numpy as np

class QuantumState:
    def __init__(self, num_qubits):
        """
        Initialize a quantum state with the given number of qubits. 
        Initially, the state is set to the |0...0> state (all qubits in the |0> state).
        """
        self.num_qubits = num_qubits
        self.state = np.zeros(2 ** num_qubits)
        self.state[0] = 1  # Initial state |0>^n

    def apply_gate(self, gate, qubits):
        """
        Apply a quantum gate to specific qubits in the state.
        The gate is represented as a matrix.
        """
        gate_matrix = gate.get_matrix()
        # Apply the gate by matrix multiplication
        self.state = np.dot(gate_matrix, self.state)
    
    def get_state(self):
        """Return the quantum state vector."""
        return self.state

    def measure(self):
        """
        Simulate the measurement of the quantum state.
        The measurement outcome is probabilistic.
        """
        probabilities = np.abs(self.state) ** 2
        outcome = np.random.choice(len(probabilities), p=probabilities)
        return outcome
