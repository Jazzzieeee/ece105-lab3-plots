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
import matplotlib.pyplot as plt


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


# Create plot_histogram(sensor_a, sensor_b, ax) that draws
# a histogram of both sensors onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.


def plot_histogram(sensor_a, sensor_b, ax):
    """Draw overlaid histograms for two sensors on a provided Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray, shape (N,)
        Temperature readings from Sensor A in degrees Celsius.
    sensor_b : numpy.ndarray, shape (N,)
        Temperature readings from Sensor B in degrees Celsius.
    ax : matplotlib.axes.Axes
        Matplotlib Axes object to draw the histograms onto. This function
        modifies the Axes in place and returns ``None``.

    Returns
    -------
    None

    Notes
    -----
    Uses 30 bins and ``alpha=0.5`` so both distributions remain visible when
    overlapped. Vertical dashed lines indicate each sensor's sample mean.
    Colors match other plotting helpers: ``tab:blue`` for Sensor A and
    ``tab:orange`` for Sensor B.
    """

    bins = 30
    ax.hist(sensor_a, bins=bins, alpha=0.5, color='tab:blue', label='Sensor A')
    ax.hist(sensor_b, bins=bins, alpha=0.5, color='tab:orange', label='Sensor B')
    mean_a = sensor_a.mean()
    mean_b = sensor_b.mean()
    ax.axvline(mean_a, color='tab:blue', linestyle='--', linewidth=2, label='Sensor A mean')
    ax.axvline(mean_b, color='tab:orange', linestyle='--', linewidth=2, label='Sensor B mean')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Count')
    ax.set_title('Overlaid Histogram: Sensor Temperature Distributions')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.4)
    return None


# Create plot_boxplot(sensor_a, sensor_b, ax) that draws
# a box plot comparing both sensors onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.


def plot_boxplot(sensor_a, sensor_b, ax):
    """Draw side-by-side box plots comparing two sensors on a provided Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray, shape (N,)
        Temperature readings from Sensor A in degrees Celsius.
    sensor_b : numpy.ndarray, shape (N,)
        Temperature readings from Sensor B in degrees Celsius.
    ax : matplotlib.axes.Axes
        Matplotlib Axes object to draw the box plots onto. This function
        modifies the Axes in place and returns ``None``.

    Returns
    -------
    None

    Notes
    -----
    The function colors the boxes to match other helpers (``tab:blue`` and
    ``tab:orange``), emphasizes the medians, and draws a horizontal dashed
    line at the overall mean of both sensors combined. A concise legend is
    created using proxy artists so the box colors and the mean line are
    labeled.
    """

    sensor_a = np.asarray(sensor_a, dtype=float)
    sensor_b = np.asarray(sensor_b, dtype=float)

    data = [sensor_a, sensor_b]
    labels = ['Sensor A', 'Sensor B']

    box = ax.boxplot(data, labels=labels, patch_artist=True, widths=0.6)

    colors = ['tab:blue', 'tab:orange']
    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)

    for median in box['medians']:
        median.set_color('black')
        median.set_linewidth(2)

    overall_mean = np.concatenate((sensor_a, sensor_b)).mean()
    ax.axhline(overall_mean, color='red', linestyle='--', linewidth=1.5, label='Overall mean')

    # Create legend proxies for boxes and mean line
    from matplotlib.patches import Patch
    from matplotlib.lines import Line2D
    handles = [
        Patch(facecolor='tab:blue', label='Sensor A'),
        Patch(facecolor='tab:orange', label='Sensor B'),
        Line2D([0], [0], color='red', linestyle='--', label='Overall mean')
    ]
    ax.legend(handles=handles)

    ax.set_ylabel('Temperature (deg C)')
    ax.set_title('Box Plot: Sensor Temperature Comparison')
    ax.grid(True, axis='y', linestyle='--', alpha=0.4)
    return None


def main(seed=1234):
    """Generate data, create a 2×2 grid of plots, and save the figure.

    Parameters
    ----------
    seed : int or None, optional
        Seed passed to :func:`generate_data` for reproducible output.
        Default is ``1234`` to match the notebook example.

    Returns
    -------
    None

    Notes
    -----
    Creates a 2×2 subplot figure with the scatter (top-left), overlaid
    histogram (top-right), box plot (bottom-left), and a bottom-right
    summary panel containing basic statistics. Saves the result to
    ``sensor_analysis.png`` at 150 DPI using a tight bounding box.
    """

    # Generate the data
    sensor_a, sensor_b, timestamps = generate_data(seed)

    # Create a 2x2 figure and draw each plot into its Axes
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    ax_scatter = axes[0, 0]
    ax_hist = axes[0, 1]
    ax_box = axes[1, 0]
    ax_summary = axes[1, 1]

    plot_scatter(sensor_a, sensor_b, timestamps, ax_scatter)
    plot_histogram(sensor_a, sensor_b, ax_hist)
    plot_boxplot(sensor_a, sensor_b, ax_box)

    # Summary statistics in the fourth panel
    mean_a = float(sensor_a.mean())
    std_a = float(sensor_a.std(ddof=1))
    mean_b = float(sensor_b.mean())
    std_b = float(sensor_b.std(ddof=1))
    combined_mean = float(np.concatenate((sensor_a, sensor_b)).mean())
    n = sensor_a.size

    summary_lines = [
        f"Samples per sensor: {n}",
        "",
        f"Sensor A — mean: {mean_a:.2f} °C, std: {std_a:.2f} °C",
        f"Sensor B — mean: {mean_b:.2f} °C, std: {std_b:.2f} °C",
        "",
        f"Combined mean: {combined_mean:.2f} °C"
    ]
    summary_text = "\n".join(summary_lines)

    ax_summary.axis('off')
    ax_summary.text(0.01, 0.99, summary_text, va='top', ha='left', fontsize=10, family='monospace')

    plt.tight_layout()
    fig.savefig('sensor_analysis.png', dpi=150, bbox_inches='tight')
    plt.close(fig)
    return None


if __name__ == '__main__':
    main()


# Create main() that generates data, creates a 1x3 subplot figure,
# calls each plot function, adjusts layout, and saves as sensor_analysis.png
# at 150 DPI with tight bounding box.