import pytest
import pandas as pd
import os
from chapter11_core import Chapter11Core

@pytest.fixture(scope="module")
def core():
    return Chapter11Core()

def test_book_numbers_exist(core):
    """Verify that all expected book numbers are loaded."""
    expected_metrics = [
        "protocol_unlock_2030",
        "leadership_factor_base",
        "entropy_level_base",
        "carbon_command_coeff_base",
        "stability_poly_degree_base",
        "isolated_sprint_figure_11_2_point1_x",
        "isolated_sprint_figure_11_2_point1_y",
        "isolated_sprint_figure_11_2_point2_x",
        "isolated_sprint_figure_11_2_point2_y",
        "protocol_leadership_figure_11_2_point1_x",
        "protocol_leadership_figure_11_2_point1_y",
        "protocol_leadership_figure_11_2_point2_x",
        "protocol_leadership_figure_11_2_point2_y",
        "entropy_old_model_figure_11_5_point1_x",
        "entropy_old_model_figure_11_5_point1_y",
        "entropy_old_model_figure_11_5_point2_x",
        "entropy_old_model_figure_11_5_point2_y",
        "protocol_entropy_reduction_figure_11_5_point1_x",
        "protocol_entropy_reduction_figure_11_5_point1_y",
        "protocol_entropy_reduction_figure_11_5_point2_x",
        "protocol_entropy_reduction_figure_11_5_point2_y",
        "renewables_2023",
        "solar_capacity_2023",
        "negative_prices_2023",
        "renewables_2030",
        "solar_capacity_2030",
        "negative_prices_2030",
        "phi_mcp_2026",
        "phi_mcp_2030",
        "psi_mcp_2030",
        "mer_reset_subsidy",
        "protocol_multiplier_storage",
        "protocol_multiplier_grid_intelligence",
        "protocol_multiplier_carbon_command",
        "protocol_multiplier_stability",
        "protocol_multiplier_sovereign_dawn",
    ]
    for metric in expected_metrics:
        assert core.get_book_number(metric) is not None, f"Metric {metric} not found in book_numbers.csv"

def test_isolated_sprint_vs_protocol_leadership_calculation(core):
    """Verify the Isolated Sprint vs Protocol Leadership calculation with book values."""
    # Using book values for a specific point or range
    # This is a conceptual test as the equation is illustrative.
    protocol_unlock = core.protocol_unlock_2030
    leadership_factor = core.leadership_factor_base
    expected_performance = 50 + (protocol_unlock * 0.3) + (leadership_factor * 5)
    assert core.isolated_sprint_vs_protocol_leadership(protocol_unlock, leadership_factor) == pytest.approx(expected_performance)

def test_entropy_reduction_simulation_calculation(core):
    """Verify the Entropy Reduction simulation with book values."""
    entropy_level = core.entropy_old_model_figure_11_5_point2_y # 0.8 at 2026
    protocol_depth_factor = 0.5 # Example value for testing
    expected_reduced_entropy = entropy_level * (1 - (protocol_depth_factor * 0.1))
    assert core.entropy_reduction_simulation(entropy_level, protocol_depth_factor) == pytest.approx(expected_reduced_entropy)

def test_carbon_command_equation_calculation(core):
    """Verify the Carbon Command Equation with example values from Figure 11.2."""
    # Values from Figure 11.2 for 2030
    delta_co2_domestic = -240 # Mt
    delta_co2_embodied = 45 # Mt
    phi_mcp = core.phi_mcp_2030 # 1.2 from book
    expected_ccmd = delta_co2_domestic + (delta_co2_embodied * phi_mcp)
    assert core.carbon_command_equation(delta_co2_domestic, delta_co2_embodied, phi_mcp) == pytest.approx(expected_ccmd)

def test_stability_threshold_projection_calculation(core):
    """Verify the Stability Threshold Projection with example values."""
    efficiency_eta = 0.9
    coupling_factor = 0.8
    storage_stability = 0.7
    psi_mcp = core.psi_mcp_2030 # 1.5 from book
    complexity = 0.5
    dependency = 0.6
    expected_stability = (efficiency_eta * coupling_factor * storage_stability * psi_mcp) / (complexity * dependency)
    assert core.stability_threshold_projection(efficiency_eta, coupling_factor, storage_stability, psi_mcp, complexity, dependency) == pytest.approx(expected_stability)

def test_success_polynomial_calculation(core):
    """Verify the conceptual Success Polynomial calculation."""
    asset_factors = [0.5, 0.7]
    protocol_multipliers = [core.protocol_multiplier_storage, core.protocol_multiplier_grid_intelligence]
    expected_success = (asset_factors[0] * protocol_multipliers[0]) + (asset_factors[1] * protocol_multipliers[1])
    assert core.success_polynomial(asset_factors, *protocol_multipliers) == pytest.approx(expected_success)

def test_ssp_framework_description(core):
    """Verify that the SSP framework description is not empty."""
    assert len(core.ssp_framework_description()) > 0

def test_sdp_framework_description(core):
    """Verify that the SDP framework description is not empty."""
    assert len(core.sdp_framework_description()) > 0

def test_book_values_table_11_1(core):
    """Verify key values from Table 11.1."""
    assert core.get_book_number("renewables_2023") == pytest.approx(0.52)
    assert core.get_book_number("solar_capacity_2023") == pytest.approx(82)
    assert core.get_book_number("negative_prices_2023") == pytest.approx(300)
    assert core.get_book_number("renewables_2030") == pytest.approx(0.82)
    assert core.get_book_number("solar_capacity_2030") == pytest.approx(160)
    assert core.get_book_number("negative_prices_2030") == pytest.approx(50)

def test_book_values_figure_11_2(core):
    """Verify key values from Figure 11.2."""
    assert core.get_book_number("phi_mcp_2026") == pytest.approx(0)
    assert core.get_book_number("phi_mcp_2030") == pytest.approx(1.2) # From Figure 11.2 text
    assert core.get_book_number("psi_mcp_2030") == pytest.approx(1.5)


# To run these tests, navigate to the Renewables_Migration_Chapter11_Proof_Engine directory and run:
# python3 -m pytest tests/test_book_numbers.py
