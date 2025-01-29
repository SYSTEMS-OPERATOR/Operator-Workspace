# Lorenz Attractor Documentation

This document provides an overview of the Lorenz attractor implementation used in the project. The Lorenz attractor is a system of differential equations that exhibit chaotic behavior. It is often used as a benchmark for testing and analyzing chaotic systems.

## Implementation Details

The Lorenz attractor is implemented using a neural network model in TensorFlow. The model consists of the following components:

1. **E1: Time Input** - The time input is a single scalar value representing the current time step.
2. **E2: Spatial Input (X, Y, Z)** - The spatial input consists of three values representing the X, Y, and Z coordinates of the Lorenz attractor.
3. **Embedding Layer** - The embedding layer is a dense layer with 16 units and a ReLU activation function. It is used to create a dense representation of the input dynamics.
4. **Hidden Layer** - The hidden layer is a dense layer with 16 units and a ReLU activation function. It is used to further process the embedding.
5. **Output Layer** - The output layer is a dense layer with 3 units and a linear activation function. It is used to predict the next X, Y, and Z coordinates of the Lorenz attractor.

## Training and Validation

The model is trained using the mean squared error (MSE) loss function and the Adam optimizer. The training process includes the following steps:

1. **Generate Lorenz Data** - The Lorenz attractor data is generated using the specified parameters (sigma, beta, rho, dt, and steps).
2. **Prepare Target Data** - The target data is prepared by shifting the spatial data by one timestep.
3. **Split Data** - The data is split into training and validation sets.
4. **Train Model** - The model is trained using the training data and validated using the validation data.

## Visualization

The training history is visualized using a plot of the training loss and validation loss over the epochs. Additionally, the true and predicted X coordinates of the Lorenz attractor are plotted for the validation data.

## Usage

The Lorenz attractor implementation can be used as a benchmark for testing and analyzing chaotic systems. It can also be used as a starting point for developing more complex models and algorithms for chaotic systems.
