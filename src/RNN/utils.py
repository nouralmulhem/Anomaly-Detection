import pandas as pd
import timesynth as ts

import matplotlib.pyplot as plt
import numpy as np
from jupyterthemes import jtplot
from matplotlib import pyplot as plt


jtplot.style()

def plot_series(X, y):
  # Ensure X and y are numpy arrays
  X = np.asarray(X)
  y = np.asarray(y)

  # Generate date range based on the length of X
  periods = len(X)
  start_date = pd.to_datetime('2020-01-01')
  date_range = pd.date_range(start=start_date, periods=periods, freq='D')

  # Create a DataFrame
  df = pd.DataFrame({'Date': date_range, 'Value': X, 'Label': y})

  # Plot the time series data
  plt.figure(figsize=(10, 6))

  plt.plot(df['Date'], df['Value'], label='Random Walk')

  # Plot points where y == 1 in red
  plt.scatter(df.loc[df['Label'] == 1, 'Date'], df.loc[df['Label'] == 1, 'Value'], color='red', label='Detected Points')

  # Set plot labels and title
  plt.xlabel('Date')
  plt.ylabel('Value')
  plt.title('Time Series Plot with Conditional Coloring')
  plt.legend()
  plt.grid(True)

  # Display the plot
  plt.show()

def create_time_series(start_date, end_date, num_periods):
    df = pd.DataFrame([])
    time_gen = ts.TimeSampler(stop_time=20)
    
    # Generate irregular time samples
    irregular_samples = time_gen.sample_irregular_time(num_points=20000, keep_percentage=100)
    
    # Create sinusoidal signal
    sinusoidal_signal = ts.signals.Sinusoidal(frequency=0.25)
    
    # Create Gaussian noise
    gaussian_noise = ts.noise.GaussianNoise(std=0.3)
    
    # Initialize TimeSeries with signal and noise
    time_series_generator = ts.TimeSeries(sinusoidal_signal, noise_generator=gaussian_noise)
    generated_samples, generated_signals, generated_errors = time_series_generator.sample(irregular_samples)
    
    df["values"] = generated_samples
    
    timestamps = pd.date_range(start_date, end_date, periods=num_periods)
    time_series = pd.Series(timestamps, name='TimeStamp')
    
    df.insert(0, 'TimeStamp', time_series)
    df.set_index('TimeStamp', inplace=True)
    
    return df