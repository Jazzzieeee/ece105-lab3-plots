"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""


# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.
import numpy as np


def generate_data(seed):
    """Generate synthetic sensor data for two temperature sensors.

    Parameters
    ----------
    seed : int or None
        Seed for NumPy's random generator. If ``None``, a non-deterministic
        generator will be used.

    Returns
    -------
    sensor_a : numpy.ndarray, shape (200,), dtype float64
        Simulated temperature readings (°C) from Sensor A (mean=25, std=3).
    sensor_b : numpy.ndarray, shape (200,), dtype float64
        Simulated temperature readings (°C) from Sensor B (mean=27, std=4.5).
    timestamps : numpy.ndarray, shape (200,), dtype float64
        Sorted timestamps in seconds sampled uniformly from 0 to 10 seconds.

    Notes
    -----
    This uses :func:`numpy.random.default_rng` for reproducible, modern RNG
    behavior and matches the parameters used in the notebook (200 samples,
    Sensor A μ=25 σ=3, Sensor B μ=27 σ=4.5, timestamps in [0, 10]).
    """

    n_readings = 200
    rng = np.random.default_rng(seed)

    # timestamps: uniform on [0, 10], sorted for monotonic time
    timestamps = rng.uniform(0.0, 10.0, size=n_readings)
    timestamps.sort()

    # sensor readings: normal distributions with specified means/stds
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=n_readings).astype(np.float64)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=n_readings).astype(np.float64)

    return sensor_a, sensor_b, timestamps


# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.


def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Draw scatter plots of two sensors versus time on a provided Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray, shape (N,)
        Temperature readings from Sensor A in degrees Celsius.
    sensor_b : numpy.ndarray, shape (N,)
        Temperature readings from Sensor B in degrees Celsius.
    timestamps : numpy.ndarray, shape (N,)
        Timestamps in seconds corresponding to each reading (expected in
        the range 0 to 10). This need not be sorted, but typically is.
    ax : matplotlib.axes.Axes
        Matplotlib Axes object to draw the scatter plot onto. This function
        modifies the Axes in place and returns ``None``.

    Returns
    -------
    None

    Notes
    -----
    The visual styling mirrors the notebook: Sensor A uses ``tab:blue``,
    Sensor B uses ``tab:orange``, marker size is chosen for readability,
    and a dashed grid is enabled for easier reading of overlapping points.
    """

    ax.scatter(timestamps, sensor_a, c='tab:blue', label='Sensor A', s=40, alpha=0.8)
    ax.scatter(timestamps, sensor_b, c='tab:orange', label='Sensor B', s=40, alpha=0.8)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Scatter: Temperature vs Time (Sensor A & B)')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.5)
    return None