import math
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from AnomalyDetection import run
import pandas as pd

# Use %matplotlib notebook or %matplotlib qt for interactive plotting if running in Jupyter Notebook
# %matplotlib notebook
# %matplotlib qt

def generate_data_stream(t, base_value, amplitude, frequency, seasonal_func, noise_std):
    """
    Generates a data point for the simulated data stream.
    Args:
        t: Time step (e.g., hour)
        base_value: Average value of the data stream.
        amplitude: Maximum deviation due to the regular pattern.
        frequency: Number of cycles of the regular pattern per unit time.
        seasonal_func: Function representing the seasonal trend.
        noise_std: Standard deviation of the random noise.
    Returns:
        A floating-point number representing the data point at time t.
    """
    regular_pattern = amplitude * math.sin(2 * math.pi * frequency * t)
    seasonal_trend = seasonal_func(t)
    noise = random.gauss(0, noise_std)
    return base_value + regular_pattern + seasonal_trend + noise

# Define function parameters
base_value = 100.0
amplitude = 20.0
frequency = 1  # Daily seasonality
seasonal_period = 24
noise_std = 5.0

# Initialize data and time steps
time_steps = np.arange(100)  # Initial data points to display
data = [generate_data_stream(t, base_value, amplitude, frequency, lambda t: math.sin(2*math.pi*t/seasonal_period), noise_std) for t in time_steps]

# Function to update data and plot
def update(frame):
    global data, time_steps
    # Generate new data point
    new_data_point = generate_data_stream(frame, base_value, amplitude, frequency, lambda t: math.sin(2*math.pi*t/seasonal_period), noise_std)
    data.append(new_data_point)
    time_steps = np.arange(len(data))

    # Update plot data
    ax.clear()
    ax.plot(time_steps, data)

    pred = run(data)
    ax.scatter(time_steps[pred == 1], np.array(data)[pred == 1], color='red', label='Detected Points')

    # Set plot limits for visualization
    ax.set_xlim([time_steps[0], time_steps[-1]])
    ax.set_ylim([base_value - amplitude - noise_std - 5, base_value + amplitude + noise_std + 5])

    # Set plot labels and title
    ax.set_xlabel("Time (hours)")
    ax.set_ylabel("Data Value")
    ax.set_title("Simulated Data Stream with Regular Patterns, Seasonal Elements, and Noise")
    plt.grid(True)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)

fig, ax = plt.subplots()

# Create line object for data
line, = ax.plot(time_steps, data)

# Animate the plot
ani = FuncAnimation(fig, update, frames=range(100, 200), interval=50)  # Update every 0.05 seconds

plt.show()
