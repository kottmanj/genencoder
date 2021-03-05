from genencoder import CircuitGenEncoder
import tequila as tq

my_tequila_circuit =  tq.gates.H(0)
my_tequila_circuit += tq.gates.X(target=4,control=2)
my_tequila_circuit += tq.gates.Rx(angle="a", target=0) 
my_tequila_circuit += tq.gates.Rx(angle="b", target=2, control=1)

encoder = CircuitGenEncoder()

# encode circuit
circuit_string1 = encoder(my_tequila_circuit)
print(circuit_string1)

# encode circuit with explicit variables
# this will determine only variable a, variable b stays a variable after decoding
circuit_string2 = encoder(my_tequila_circuit, variables={"a":1.0})
print(circuit_string2)

# deconde circuit
the_same_tequila_circuit = encoder(circuit_string1)

# make png (same as tequila.circuit.export_to, but sets the correct compile options)
encoder.export_to(my_tequila_circuit, filename="my_tequila_circuit.png")
