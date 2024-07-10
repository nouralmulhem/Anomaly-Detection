import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from AnomalyDetection import run
from utils import *

df = create_time_series(start_date='1/1/2020', end_date='05/01/2021', num_periods=2000)

# Initialize data and time steps
time_steps = np.arange(1000)  # Initial data points to display
data = df['values'].tolist()

# Function to update data and plot
def update(frame):
    global data, time_steps
    # Generate new data point

    data_to_plot = data[:frame]
    time_steps = np.arange(frame)

    # Update plot data
    ax.clear()
    ax.plot(time_steps, data_to_plot)

    pred = run(data_to_plot)
    ax.scatter(time_steps[pred == 1], np.array(data_to_plot)[pred == 1], color='red', label='Detected Points')

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
line, = ax.plot(time_steps, data[:1000])

# Animate the plot
ani = FuncAnimation(fig, update, frames=range(1000, 2000), interval=50)  # Update every 0.05 seconds

plt.show()
