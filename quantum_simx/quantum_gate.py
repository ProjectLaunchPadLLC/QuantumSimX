import numpy as np

class QuantumGate:
    def __init__(self, matrix):
        """
        A quantum gate is represented by a unitary matrix.
        """
        self.matrix = matrix

    def get_matrix(self):
        """Return the matrix representation of the quantum gate."""
        return self.matrix

# Pauli-X (NOT) gate
X_gate = QuantumGate(np.array([[0, 1], [1, 0]]))

# Hadamard gate (H)
H_gate = QuantumGate(np.array([[1, 1], [1, -1]]) / np.sqrt(2))

# CNOT gate (Control qubit 0, Target qubit 1)
CNOT_gate = QuantumGate(np.array([[1, 0, 0, 0],
                                   [0, 1, 0, 0],
                                   [0, 0, 0, 1],
                                   [0, 0, 1, 0]]))
