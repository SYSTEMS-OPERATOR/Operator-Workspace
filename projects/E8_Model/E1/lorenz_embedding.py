import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Concatenate, Reshape, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
import matplotlib.pyplot as plt

# Lorenz attractor parameters
sigma = 10.0
beta = 8.0 / 3.0
rho = 28.0
dt = 0.01
steps = 10000

# Lorenz attractor data generator
def generate_lorenz_data(steps, dt):
    x, y, z = 0.1, 0.0, 0.0  # Initial conditions
    data = np.zeros((steps, 3))  # X, Y, Z only
    time = np.linspace(0, steps * dt, steps).reshape(-1, 1)  # Normalized time

    for i in range(steps):
        dx = sigma * (y - x)
        dy = x * (rho - z) - y
        dz = x * y - beta * z

        x += dx * dt
        y += dy * dt
        z += dz * dt

        data[i] = [x, y, z]
    return time, data

# Generate Lorenz data
time_data, spatial_data = generate_lorenz_data(steps=steps, dt=dt)

# Prepare target data (next step in the Lorenz sequence for each X, Y, Z)
target_data = np.roll(spatial_data, -1, axis=0)  # Shift spatial data by one timestep

# Split into training and validation sets
train_size = int(0.8 * steps)
time_train, time_val = time_data[:train_size], time_data[train_size:]
spatial_train, spatial_val = spatial_data[:train_size], spatial_data[train_size:]
target_train, target_val = target_data[:train_size], target_data[train_size:]

# Neural network model
def build_model():
    # E1: Time Input
    time_input = Input(shape=(1,), name="E1_time_input")

    # E2: Spatial Input (X, Y, Z)
    spatial_input = Input(shape=(3,), name="E2_spatial_input")

    # Combine inputs
    combined_input = Concatenate(name="combined_input")([time_input, spatial_input])

    # Embedding layer (dense representation of input dynamics)
    embedding = Dense(16, activation="relu", name="embedding_layer")(combined_input)
    hidden = Dense(16, activation="relu", name="hidden_layer")(embedding)

    # Output layer (predicting next X, Y, Z)
    output = Dense(3, activation="linear", name="output_layer")(hidden)

    # Model definition
    model = Model(inputs=[time_input, spatial_input], outputs=output)
    model.compile(optimizer="adam", loss="mse", metrics=["mae"])
    return model

# Build the model
model = build_model()

# Add callbacks for training
checkpoint = ModelCheckpoint("best_lorenz_model.keras", save_best_only=True, monitor="val_loss", mode="min", verbose=1)
early_stopping = EarlyStopping(monitor="val_loss", patience=10, mode="min", verbose=1)

# Train the model
history = model.fit(
    [time_train, spatial_train],
    target_train,
    validation_data=([time_val, spatial_val], target_val),
    epochs=50,
    batch_size=64,
    verbose=1,
    callbacks=[checkpoint, early_stopping]
)

# Plot training history
plt.figure(figsize=(10, 5))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Training History')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.grid()
plt.show()

# Visualize predictions on validation data
predicted = model.predict([time_val[:500], spatial_val[:500]])
plt.figure(figsize=(12, 6))
plt.plot(range(500), spatial_val[:500, 0], label="True X", color="blue")
plt.plot(range(500), predicted[:, 0], label="Predicted X", color="orange", linestyle="dashed")
plt.title("Validation: True vs Predicted X (Lorenz Attractor)")
plt.xlabel("Time Step")
plt.ylabel("X")
plt.legend()
plt.grid()
plt.show()
