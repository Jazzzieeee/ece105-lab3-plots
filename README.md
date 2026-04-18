# ECE105 Lab 3 — Sensor Plots

Generate synthetic temperature sensor data and produce publication-quality
visualizations (scatter, histogram, and box plot) saved as a single PNG file.

## Installation

1. Activate the conda environment used for the course:

```bash
conda activate ece105
# or with mamba if you prefer
mamba activate ece105
```

2. Install the required packages (recommended via conda/mamba):

```bash
conda install -c conda-forge numpy matplotlib
# or
mamba install -c conda-forge numpy matplotlib
```

If you do not use conda/mamba, you can install with pip in your active
environment:

```bash
pip install numpy matplotlib
```

## Usage

Run the script from the repository root:

```bash
python generate_plots.py
```

The script uses a default seed (`1234`) for reproducible synthetic data;
edit the script or call `main()` with a different seed if you need
different realizations.

## Example output

The script saves a single PNG file named `sensor_analysis.png` (150 DPI)
containing three subplots arranged in a 1×3 layout:

- **Scatter (Temperature vs Time):** Sensor A (blue) and Sensor B
     (orange) temperature readings plotted against timestamps in seconds.
- **Overlaid Histogram:** 30-bin histograms for both sensors with
     semi-transparent colors (alpha=0.5) and dashed vertical lines showing
     each sensor's sample mean.
- **Box Plot:** Side-by-side boxplots for Sensor A and Sensor B with
     colored boxes, emphasized medians, and a horizontal dashed red line
     indicating the combined overall mean.

These plots match the visual styling used in the corresponding Jupyter
notebook for the lab.

## AI tools used and disclosure

PLACEHOLDER — Describe any AI assistance used (for example, code
generation, refactoring, or documentation) and how it was applied. Fill
this section with the details you want to disclose about AI involvement.

