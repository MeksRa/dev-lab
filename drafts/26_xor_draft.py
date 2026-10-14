import math
import random


# 1. Activation function (Sigmoid) and its derivative
# Number Compressor
def sigmoid(x):
    """Takes any number and compresses it into the range from 0 to 1."""
    return 1 / (1 + math.exp(-x))


def sigmoid_derivative(output):
    return output * (1 - output)


# 2. Training data (XOR logic gate)
training_inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
training_outputs = [[0], [1], [1], [0]]

# -- -- -- --
# 3. Initialization (random weights)
# With every new run of your script, the random weights were generated in exactly the same way.
random.seed(42)

# Weights from input to hidden layer (2 inputs -> 3 neurons)
# limitation of the single-layer perceptron, 3 neurons min
# .uniform(a,b) generates random numbers within a range

# input (2 digits (e.g. [0, 1])) are multiplied by a 2x3 matrix with random numbers within a range(-1, 1),
# we obtain 3 intermediate values ​​(hidden layer)
weights_input_hidden = [
    [random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)],
    [random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)],
]

# multiply those 3 values by matrix 3x1
# Weights from hidden layer to output (3 neurons -> 1 output)
weights_hidden_output = [
    [random.uniform(-1, 1)],
    [random.uniform(-1, 1)],
    [random.uniform(-1, 1)],
]
# get 1 output (prediction)
#
# Inputs (2 numbers) -> multiply by matrix #1 (2x3) -> obtain 3 intermediate values ​​(hidden layer) ->
# -> multiply by matrix #2 (3x1) -> obtain 1 final answer.

# Learning rate
# Golden mean (0.5)
learning_rate = 0.5
# -- -- -- --

# 4. TRAINING LOOP
print("Training the neural network...")
for epoch in range(100000):
    for i in range(len(training_inputs)):
        inputs = training_inputs[i]

        # --- A) FORWARD PASS ---
        hidden_layer_input = [0.0, 0.0, 0.0]
        for j in range(3):
            hidden_layer_input[j] = (
                inputs[0] * weights_input_hidden[0][j]
                + inputs[1] * weights_input_hidden[1][j]
            )

        hidden_layer_output = [sigmoid(x) for x in hidden_layer_input]

        final_input = 0.0
        for j in range(3):
            final_input += hidden_layer_output[j] * weights_hidden_output[j][0]

        final_output = sigmoid(final_input)

        # --- B) ERROR CALCULATION & BACKPROPAGATION ---
        target = training_outputs[i][0]
        error = target - final_output

        d_output = error * sigmoid_derivative(final_output)

        d_hidden = [0.0, 0.0, 0.0]
        for j in range(3):
            d_hidden[j] = (
                d_output
                * weights_hidden_output[j][0]
                * sigmoid_derivative(hidden_layer_output[j])
            )

        # --- C) WEIGHTS CORRECTION (Gradient Descent) ---
        for j in range(3):
            weights_hidden_output[j][0] += (
                learning_rate * d_output * hidden_layer_output[j]
            )

        for j in range(2):
            for k in range(3):
                weights_input_hidden[j][k] += learning_rate * d_hidden[k] * inputs[j]

# 5. RESULTS CHECK
print("\nResults after training:")
for i in range(len(training_inputs)):
    inputs = training_inputs[i]

    hidden_layer_input = [
        inputs[0] * weights_input_hidden[0][j] + inputs[1] * weights_input_hidden[1][j]
        for j in range(3)
    ]
    hidden_layer_output = [sigmoid(x) for x in hidden_layer_input]
    final_input = sum(
        hidden_layer_output[j] * weights_hidden_output[j][0] for j in range(3)
    )
    prediction = sigmoid(final_input)

    print(
        f"Inputs: {inputs} -> Prediction: {prediction:.4f} (Expected: {training_outputs[i][0]})"
    )

# --- -- --- -- --- -- ---

# f(x) = 1/(1+e^-x)  # sigmoid

# If the prediction is greater than 0.5, we treat it as 1. If less, 0.
# prediction = 0.9815
# final_answer = 1 if prediction > 0.5 else 0
# print(final_answer)  # We get a solid 1!

# --- -- --- -- --- -- ---


# XOR
#          Y|(second input)
#           |
#           |
#     (1)   |        (0)
#    (0, 1) *     * (1, 1)
#           |
# ----------*-----*------> X(first input)
#    (0, 0) |       (1, 0)
#     (0)   |        (1)
#           |
#           |
#           |
#           |
