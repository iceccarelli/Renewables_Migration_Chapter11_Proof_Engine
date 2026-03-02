import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import os
import sys

# Add the parent directory to the system path to import chapter11_core
script_dir = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(script_dir, "..")))
from chapter11_core import Chapter11Core

# Initialize core logic
core = Chapter11Core()

# Configure matplotlib for better aesthetics
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 7)
plt.rcParams["figure.dpi"] = 100

def plot_isolated_sprint_vs_protocol_leadership():
    """
    Reproduces Figure 11.2: The Sovereign Trajectory (Isolated Sprint vs Protocol Leadership).
    """
    years = np.arange(2010, 2031)

    # Data from Figure 11.2 (conceptual representation)
    germany_legacy_sprint = {
        2010: core.book_numbers.loc[core.book_numbers["metric"] == "isolated_sprint_figure_11_2_point1_x", "value"].iloc[0],
        2026: core.book_numbers.loc[core.book_numbers["metric"] == "isolated_sprint_figure_11_2_point2_x", "value"].iloc[0],
    }
    germany_legacy_sprint_y = {
        2010: core.book_numbers.loc[core.book_numbers["metric"] == "isolated_sprint_figure_11_2_point1_y", "value"].iloc[0],
        2026: core.book_numbers.loc[core.book_numbers["metric"] == "isolated_sprint_figure_11_2_point2_y", "value"].iloc[0],
    }

    germany_protocol_leadership = {
        2010: core.book_numbers.loc[core.book_numbers["metric"] == "protocol_leadership_figure_11_2_point1_x", "value"].iloc[0],
        2030: core.book_numbers.loc[core.book_numbers["metric"] == "protocol_leadership_figure_11_2_point2_x", "value"].iloc[0],
    }
    germany_protocol_leadership_y = {
        2010: core.book_numbers.loc[core.book_numbers["metric"] == "protocol_leadership_figure_11_2_point1_y", "value"].iloc[0],
        2030: core.book_numbers.loc[core.book_numbers["metric"] == "protocol_leadership_figure_11_2_point2_y", "value"].iloc[0],
    }

    france_balanced_path = {
        2010: 20, # Conceptual start
        2030: 50, # Conceptual end
    }

    # Interpolate data
    sprint_interp = pd.Series(germany_legacy_sprint_y).reindex(years).interpolate(method="linear")
    protocol_interp = pd.Series(germany_protocol_leadership_y).reindex(years).interpolate(method="linear")
    france_interp = pd.Series(france_balanced_path).reindex(years).interpolate(method="linear")

    plt.figure(figsize=(12, 7))
    sns.lineplot(x=years, y=sprint_interp, label="Germany (Legacy Sprint)", color="orange")
    sns.lineplot(x=years, y=protocol_interp, label="Germany (Sovereign Protocol)", color="blue")
    sns.lineplot(x=years, y=france_interp, label="France (Balanced Path)", color="green", linestyle="--")

    plt.xlabel("Year")
    plt.ylabel("Renewable Share (%)")
    plt.title("Figure 11.2: The Sovereign Trajectory: Isolated Sprint vs Protocol Leadership")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.ylim(0, 100)
    plt.legend()
    plt.savefig("../plots/isolated_sprint_vs_protocol_leadership.png")
    plt.close()
    print("Generated isolated_sprint_vs_protocol_leadership.png")

def plot_final_entropy_old_model():
    """
    Reproduces Figure 11.5 (conceptual): The Final Entropy of the Old Model.
    This plot shows entropy increasing without MCP intervention.
    """
    years = np.arange(2010, 2031)

    entropy_data = {
        2010: core.book_numbers.loc[core.book_numbers["metric"] == "entropy_old_model_figure_11_5_point1_x", "value"].iloc[0],
        2026: core.book_numbers.loc[core.book_numbers["metric"] == "entropy_old_model_figure_11_5_point2_x", "value"].iloc[0],
    }
    entropy_data_y = {
        2010: core.book_numbers.loc[core.book_numbers["metric"] == "entropy_old_model_figure_11_5_point1_y", "value"].iloc[0],
        2026: core.book_numbers.loc[core.book_numbers["metric"] == "entropy_old_model_figure_11_5_point2_y", "value"].iloc[0],
    }

    entropy_interp = pd.Series(entropy_data_y).reindex(years).interpolate(method="linear")

    plt.figure(figsize=(12, 7))
    sns.lineplot(x=years, y=entropy_interp, label="Old Model Entropy", color="red")

    plt.xlabel("Year")
    plt.ylabel("Entropy Level")
    plt.title("Figure 11.5 (Conceptual): The Final Entropy of the Old Model")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.ylim(0, 1)
    plt.legend()
    plt.savefig("../plots/final_entropy_old_model.png")
    plt.close()
    print("Generated final_entropy_old_model.png")

def plot_stability_threshold_projection():
    """
    Generates a conceptual plot for Stability Threshold Projection.
    """
    psi_mcp_range = np.linspace(0, 2, 100)
    stability_values = [
        core.stability_threshold_projection(0.9, 0.8, 0.7, psi, 0.5, 0.6)
        for psi in psi_mcp_range
    ]

    plt.figure(figsize=(10, 6))
    sns.lineplot(x=psi_mcp_range, y=stability_values)
    plt.xlabel("ΨMCP (Protocol Stability Factor)")
    plt.ylabel("Stability Threshold (S(t))")
    plt.title("Stability Threshold Projection")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.savefig("../plots/stability_threshold_projection.png")
    plt.close()
    print("Generated stability_threshold_projection.png")

def plot_sovereign_dawn_simulation():
    """
    Generates a conceptual plot for Sovereign Dawn Simulation (2045 Projections).
    """
    years = np.arange(2020, 2046)
    sovereign_index = 10 + (years - 2020) * 3 + np.random.rand(len(years)) * 5 # Conceptual growth

    plt.figure(figsize=(10, 6))
    sns.lineplot(x=years, y=sovereign_index, label="Sovereign Dawn Index")
    plt.xlabel("Year")
    plt.ylabel("Sovereign Index")
    plt.title("Sovereign Dawn Simulation (Conceptual 2045 Projection)")
    plt.grid(True)
    plt.legend()
    plt.savefig("../plots/sovereign_dawn_simulation.png")
    plt.close()
    print("Generated sovereign_dawn_simulation.png")

if __name__ == "__main__":
    # Ensure the plots directory exists
    os.makedirs("../plots", exist_ok=True)

    plot_isolated_sprint_vs_protocol_leadership()
    plot_final_entropy_old_model()
    plot_stability_threshold_projection()
    plot_sovereign_dawn_simulation()
