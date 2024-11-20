from .quantum_gate import QuantumGate

class QuantumCircuit:
    def __init__(self, num_qubits):
        """
        Initialize a quantum circuit with a given number of qubits.
        """
        self.num_qubits = num_qubits
        self.gates = []

    def add_gate(self, gate, qubits):
        """
        Add a gate to the quantum circuit.
        `gate` is an instance of the QuantumGate class, 
        `qubits` is a tuple/list of qubit indices affected by the gate.
        """
        self.gates.append((gate, qubits))

    def apply(self, state):
        """
        Apply all the gates in the circuit to the provided quantum state.
        """
        for gate, qubits in self.gates:
            state.apply_gate(gate, qubits)
        return state
