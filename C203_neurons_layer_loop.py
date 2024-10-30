# Using loops
inputs = [1, 2, 3, 2.5]
weights = [
        [0.2, 0.8, -0.5, 1],
        [0.5, -0.91, 0.26, -0.5],
        [-0.26, -0.27, 0.17, 0.87]
    ]

biases = [2, 3, 0.5]

# Output of the current layer
layer_output = []
# For each neuron
for neuron_weight, neuron_bias in zip(weights, biases):
    
    neuron_output = 0
    # For each input and weight to the neuron
    for input, weight in zip(inputs, neuron_weight):
        # Multiply the associated weight to this input, 
        # and add the neuron's output variable
        neuron_output += input*weight
    # Add bias
    neuron_output += neuron_bias
    # Append each neuron's resultant to the layer's ouput list
    layer_output.append(neuron_output)

print(layer_output)