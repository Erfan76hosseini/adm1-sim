"""Influent (feed) composition definitions and builder.

Separated from params.py to allow scenario-specific feed manipulation without
editing kinetic or physical parameter code.
"""
from __future__ import annotations

from typing import List

# Scenario / mixing fractions
mixing_ratio: float = 0.99999  # feed1 / total (can be overridden per scenario)
variation_factor4: float = 1.0  # scaling for second feed total COD

# Feed2 total particulate COD (example baseline)
X_xc2_total = variation_factor4 * 259.992
X_ch2_fraction = 0.79
X_pr2_fraction = 0.184
X_li2_fraction = 0.026

# Soluble influent concentrations (kg COD.m^-3 or kmole m^-3 as noted)
S_su_in = 0.001
S_aa_in = 0.001
S_fa_in = 0.001
S_va_in = 0.001
S_bu_in = 0.001
S_pro_in = 0.001
S_ac_in = 0.001
S_h2_in = 1e-8
S_ch4_in = 1e-5
S_IC_in = 0.04   # kmole C.m^-3
S_IN_in = 0.01   # kmole N.m^-3
S_I_in = 0.02    # kg COD.m^-3

# Particulate influent Substrate 1
X_xc1_in = mixing_ratio * 0.0
X_ch1_in = mixing_ratio * 20.057
X_pr1_in = mixing_ratio * 12.674
X_li1_in = mixing_ratio * 9.997

# Particulate influent Substrate 2
X_xc2_in = (1 - mixing_ratio) * 0.0
X_ch2_in = (1 - mixing_ratio) * X_ch2_fraction * X_xc2_total
X_pr2_in = (1 - mixing_ratio) * X_pr2_fraction * X_xc2_total
X_li2_in = (1 - mixing_ratio) * X_li2_fraction * X_xc2_total

# Biomass influent (usually zero except inert)
X_su_in = 0.0
X_aa_in = 0.0
X_fa_in = 0.0
X_c4_in = 0.0
X_pro_in = 0.0
X_ac_in = 0.0
X_h2_in = 0.0
X_I_in = 25.0

S_cation_in = 0.04  # kmole.m^-3
S_anion_in = 0.02   # kmole.m^-3

input_labels = [
    "S_su_in", "S_aa_in", "S_fa_in", "S_va_in", "S_bu_in", "S_pro_in", "S_ac_in",
    "S_h2_in", "S_ch4_in", "S_IC_in", "S_IN_in", "S_I_in", "X_xc1_in", "X_ch1_in",
    "X_pr1_in", "X_li1_in", "X_xc2_in", "X_ch2_in", "X_pr2_in", "X_li2_in", "X_su_in",
    "X_aa_in", "X_fa_in", "X_c4_in", "X_pro_in", "X_ac_in", "X_h2_in", "X_I_in",
    "S_cation_in", "S_anion_in"
]

state_input: List[float] = [
    S_su_in, S_aa_in, S_fa_in, S_va_in, S_bu_in, S_pro_in, S_ac_in, S_h2_in, S_ch4_in,
    S_IC_in, S_IN_in, S_I_in, X_xc1_in, X_ch1_in, X_pr1_in, X_li1_in, X_xc2_in, X_ch2_in,
    X_pr2_in, X_li2_in, X_su_in, X_aa_in, X_fa_in, X_c4_in, X_pro_in, X_ac_in, X_h2_in,
    X_I_in, S_cation_in, S_anion_in
]


def build_state_input() -> List[float]:
    """Return a fresh copy of the influent vector (length 30)."""
    return list(state_input)

__all__ = [name for name in globals().keys() if not name.startswith("_")]
