import streamlit as st
import pandas as pd
import numpy as np
from chapter11_core import Chapter11Core

# Initialize core logic
core = Chapter11Core()

st.set_page_config(layout="wide", page_title="Chapter 11 Proof Engine")

st.title("Chapter 11: The Migration of the Sun - Proof Engine")
st.markdown("""
This interactive dashboard allows you to explore and verify every claim, equation, number, graph, and curve presented in **Chapter 11** of "The Renewables Migration" by Vincenzo Grimaldi.

**Mission:** Prove the book. Zero-tolerance for half-measures.
""")

# Spy Mode Toggle
spy_mode = st.sidebar.checkbox("Activate Spy Mode", False, help="Highlights exact book claims and their live calculations.")

# Streamlit Tabs
tab_names = [
    "Isolated Sprint vs Protocol Leadership Simulator",
    "Entropy and Maxwell’s Demon Calculator",
    "SSP Erratic to Stable Engine",
    "SDP Receipt to Revenue Explorer",
    "Carbon Command Equation Prover",
    "Stability Threshold Projection",
    "Prove Every Equation",
    "Download Book Data",
    "2045 Projections"
]

tabs = st.tabs(tab_names)

with tabs[0]:
    st.header("Isolated Sprint vs Protocol Leadership Simulator")
    st.markdown("""
    **Book Claim:** The Isolated Sprint vs Protocol Leadership curve (Figure 11.2) demonstrates how increasing protocol unlock and leadership factor improves performance.
    """)

    protocol_unlock = st.slider("Protocol Unlock Level (0-100%)", 0.0, 1.0, core.protocol_unlock_2030, 0.01)
    leadership_factor = st.slider("Leadership Factor (0-5)", 0.0, 5.0, core.leadership_factor_base, 0.1)

    performance = core.isolated_sprint_vs_protocol_leadership(protocol_unlock, leadership_factor)
    st.metric(label="Simulated Performance Index", value=f"{performance:.2f}")

    if spy_mode:
        st.subheader("Spy Mode: Book Claim Verification")
        st.write(f"* **Book Value (Protocol Unlock 2030):** {core.protocol_unlock_2030}")
        st.write(f"* **Book Value (Leadership Factor Base):** {core.leadership_factor_base}")
        st.write(f"* **Equation:** `50 + (protocol_unlock_level * 0.3) + (leadership_factor * 5)`")
        st.write(f"* **Live Calculation:** `50 + ({protocol_unlock} * 0.3) + ({leadership_factor} * 5) = {performance:.2f}`")

with tabs[1]:
    st.header("Entropy and Maxwell’s Demon Calculator")
    st.markdown("""
    **Book Claim:** The Protocol acts as a digital "Maxwell’s Demon," sorting high-value, low-carbon signals from entropic noise, thereby reducing overall entropy.
    """)

    entropy_level = st.slider("Initial Entropy Level (0-1)", 0.0, 1.0, core.entropy_level_base, 0.01)
    protocol_depth_factor = st.slider("Protocol Depth Factor (0-1)", 0.0, 1.0, 0.5, 0.01)

    reduced_entropy = core.entropy_reduction_simulation(entropy_level, protocol_depth_factor)
    st.metric(label="Reduced Entropy Level", value=f"{reduced_entropy:.2f}")

    if spy_mode:
        st.subheader("Spy Mode: Book Claim Verification")
        st.write(f"* **Book Value (Entropy Level Base):** {core.entropy_level_base}")
        st.write(f"* **Equation:** `entropy_level * (1 - (protocol_depth_factor * 0.1))`")
        st.write(f"* **Live Calculation:** `{entropy_level} * (1 - ({protocol_depth_factor} * 0.1)) = {reduced_entropy:.2f}`")

with tabs[2]:
    st.header("SSP Erratic to Stable Engine")
    st.markdown("""
    **Book Claim:** The Sovereign Sun Protocol (SSP) framework re-architects the energy grid, turning erratic behavior into stable, autonomous orchestration.
    """)
    st.write(core.ssp_framework_description())

    if spy_mode:
        st.subheader("Spy Mode: Book Claim Verification")
        st.write("The SSP framework details how MCP-enabled agents, autonomous optimization, and global protocol export contribute to grid stability.")
        st.write(f"* **Book Value (Merz-Reset Subsidy):** €{core.mer_reset_subsidy} Billion")

with tabs[3]:
    st.header("SDP Receipt to Revenue Explorer")
    st.markdown("""
    **Book Claim:** The Sovereign Dawn Protocol (SDP) framework transforms the "Human Receipt" into a global revenue stream by licensing the Sovereign Protocol.
    """)
    st.write(core.sdp_framework_description())

    if spy_mode:
        st.subheader("Spy Mode: Book Claim Verification")
        st.write("The SDP framework outlines how the 2026 crisis is resolved, global standard leadership is established, and the human receipt is closed.")

with tabs[4]:
    st.header("Carbon Command Equation Prover")
    st.markdown("""
    **Book Claim:** The Protocol-Enabled Carbon Command Equation (Ccmd = ∆CO2,domestic + ∆CO2,embodied · ΦM CP) quantifies net global emissions reduction.
    """)

    delta_co2_domestic = st.number_input("∆CO2,domestic (Mt)", value=-240.0, step=1.0)
    delta_co2_embodied = st.number_input("∆CO2,embodied (Mt)", value=45.0, step=1.0)
    phi_mcp = st.slider("ΦMCP (Transparency Multiplier)", 0.0, 2.0, core.phi_mcp_2030, 0.01)

    ccmd = core.carbon_command_equation(delta_co2_domestic, delta_co2_embodied, phi_mcp)
    st.metric(label="Carbon Command (Ccmd) (Mt)", value=f"{ccmd:.2f}")

    if spy_mode:
        st.subheader("Spy Mode: Book Claim Verification")
        st.write(f"* **Book Value (ΦMCP 2026):** {core.phi_mcp_2026} (implies no transparency multiplier)")
        st.write(f"* **Book Value (ΦMCP 2030):** {core.phi_mcp_2030} (implies full transparency multiplier)")
        st.write(f"* **Equation:** `Ccmd = ∆CO2,domestic + (∆CO2,embodied * ΦM CP)`")
        st.write(f"* **Live Calculation:** `{delta_co2_domestic} + ({delta_co2_embodied} * {phi_mcp}) = {ccmd:.2f}`")

with tabs[5]:
    st.header("Stability Threshold Projection")
    st.markdown("""
    **Book Claim:** The Protocol Stability Factor (ΨMCP) pushes the stability threshold into the "Thriving Zone," neutralizing risks of complexity and dependency.
    Equation: S(t) ≈ ηeff · Fcoupling · Sstorage (t) · ΨM CP / (Complexity(t) · Dependency(t))
    """)

    efficiency_eta = st.slider("ηeff (Efficiency)", 0.0, 1.0, 0.9, 0.01)
    coupling_factor = st.slider("Fcoupling (Coupling Factor)", 0.0, 1.0, 0.8, 0.01)
    storage_stability = st.slider("Sstorage (Storage Stability)", 0.0, 1.0, 0.7, 0.01)
    psi_mcp = st.slider("ΨMCP (Protocol Stability Factor)", 0.0, 2.0, core.psi_mcp_2030, 0.01)
    complexity = st.slider("Complexity", 0.1, 1.0, 0.5, 0.01)
    dependency = st.slider("Dependency", 0.1, 1.0, 0.6, 0.01)

    stability = core.stability_threshold_projection(efficiency_eta, coupling_factor, storage_stability, psi_mcp, complexity, dependency)
    st.metric(label="Stability Threshold (S(t))", value=f"{stability:.2f}")

    if spy_mode:
        st.subheader("Spy Mode: Book Claim Verification")
        st.write(f"* **Book Value (ΨMCP 2030):** {core.psi_mcp_2030} (projected to exceed 1.5)")
        st.write(f"* **Equation:** `S(t) ≈ (ηeff * Fcoupling * Sstorage (t) * ΨM CP) / (Complexity(t) * Dependency(t))`")
        st.write(f"* **Live Calculation:** `({efficiency_eta} * {coupling_factor} * {storage_stability} * {psi_mcp}) / ({complexity} * {dependency}) = {stability:.2f}`")

with tabs[6]:
    st.header("Prove Every Equation")
    st.markdown("""
    This section allows you to directly interact with the core equations from `chapter11_core.py`.
    """)

    st.subheader("Success Polynomial (SCP/SEP)")
    st.markdown("""
    **Book Claim:** The Success Polynomial represents the SCP/SEP frameworks, showing how asset factors and protocol multipliers contribute to overall success.
    """)
    num_asset_factors = st.number_input("Number of Asset Factors", min_value=1, max_value=5, value=2)
    asset_factors = []
    for i in range(num_asset_factors):
        asset_factors.append(st.slider(f"Asset Factor {i+1}", 0.0, 1.0, 0.5, 0.01))

    st.write("Protocol Multipliers (from book_numbers.csv):")
    st.write(f"- Storage: {core.protocol_multiplier_storage}")
    st.write(f"- Grid Intelligence: {core.protocol_multiplier_grid_intelligence}")
    st.write(f"- Carbon Command: {core.protocol_multiplier_carbon_command}")
    st.write(f"- Stability: {core.protocol_multiplier_stability}")
    st.write(f"- Sovereign Dawn: {core.protocol_multiplier_sovereign_dawn}")

    # Example usage of success_polynomial with selected multipliers
    selected_multipliers = [
        core.protocol_multiplier_storage,
        core.protocol_multiplier_grid_intelligence,
        core.protocol_multiplier_carbon_command,
        core.protocol_multiplier_stability,
        core.protocol_multiplier_sovereign_dawn
    ][:num_asset_factors] # Use only as many multipliers as asset factors

    success_value = core.success_polynomial(asset_factors, *selected_multipliers)
    st.metric(label="Sovereign Success Index", value=f"{success_value:.2f}")

    if spy_mode:
        st.subheader("Spy Mode: Book Claim Verification")
        st.write(f"* **Equation:** `sum(asset_factor * protocol_multiplier)` (conceptual weighted sum)")
        st.write(f"* **Live Calculation:** `sum({asset_factors} * {selected_multipliers}) = {success_value:.2f}`")

with tabs[7]:
    st.header("Download Book Data")
    st.markdown("""
    Download the raw data used to prove the claims in Chapter 11.
    """)
    st.download_button(
        label="Download book_numbers.csv",
        data=core.book_numbers.to_csv(index=False).encode("utf-8"),
        file_name="book_numbers.csv",
        mime="text/csv",
    )
    # Placeholder for appendix_a_extract.csv
    st.info("Appendix A data will be available here once extracted and formatted.")

with tabs[8]:
    st.header("2045 Projections")
    st.markdown("""
    **Book Claim:** By 2045, the Sovereign Protocol will have fully transformed the energy landscape, leading to significant shifts in renewable share, stability, and carbon command.
    """)
    st.write("This section will feature interactive simulations and visualizations of the 2045 projections based on the core equations.")

    if spy_mode:
        st.subheader("Spy Mode: Book Claim Verification")
        st.write(f"* **Book Value (Renewables 2045):** {core.get_book_number("renewables_2045")}")
        st.write(f"* **Book Value (Protocol Depth 2045):** {core.get_book_number("protocol_depth_2045")}")
        st.write(f"* **Book Value (Fragility 2045):** {core.get_book_number("fragility_2045")}")


# Add a placeholder for the appendix_a_extract.csv if it's not yet generated
# This will be handled in a later phase once the appendix data is extracted.
