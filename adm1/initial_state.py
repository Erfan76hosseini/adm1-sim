"""Initial reactor state vector definition for ADM1.

Contains the dynamic state at t0 prior to integration. Separated from params
so that startup / seeding scenarios can be swapped independently of feeds or
kinetics.
"""
from __future__ import annotations

from typing import List

from .influent import mixing_ratio
from .kinetics import (pH_LL_aa, pH_UL_aa, pH_LL_ac, pH_UL_ac, pH_LL_h2, pH_UL_h2)

# Baseline initial soluble concentrations
S_su = 1e-5
S_aa = 1e-5
S_fa = 1e-5
S_va = 1e-5
S_bu = 1e-5
S_pro = 1e-5
S_ac = 1e-5
S_h2 = 1e-8
S_ch4 = 1e-5
S_IC = 0.04
S_IN = 0.01
S_I = 0.02

# Particulate substrate 1 fractions (example distribution)
X_xc1 = mixing_ratio * (2/(2+5+20+5)) * 1e-5
X_ch1 = mixing_ratio * (5/(2+5+20+5)) * 1e-5
X_pr1 = mixing_ratio * (20/(2+5+20+5)) * 1e-5
X_li1 = mixing_ratio * (5/(2+5+20+5)) * 1e-5

# Particulate substrate 2 fractions
X_xc2 = (1-mixing_ratio) * (0/(205+47.76+6.925)) * 1e-5
X_ch2 = (1-mixing_ratio) * (205/(205+47.76+6.925)) * 1e-5
X_pr2 = (1-mixing_ratio) * (47.76/(205+47.76+6.925)) * 1e-5
X_li2 = (1-mixing_ratio) * (6.925/(205+47.76+6.925)) * 1e-5

# Biomass (operational startup)
variation_factor = 50
X_su = 1.41
X_aa = 0.75
X_fa = 0.38
X_c4 = 0.35
X_pro = variation_factor * 0.197
X_ac = variation_factor * 0.95
X_h2 = 0.466
X_I = 25.6

S_cation = 0.04
S_anion = 0.02

# Acid-base & gas species
pH = 7.4655377
S_H_ion = 6.04e-8
S_va_ion = 0.0082
S_bu_ion = 0.0156
S_pro_ion = 0.0172
S_ac_ion = 0.11199
S_hco3_ion = 0.15415
S_nh3 = 0.0025
S_nh4_ion = S_IN - S_nh3
S_co2 = S_IC - S_hco3_ion

S_gas_h2 = 4.91e-6
S_gas_ch4 = 1.78
S_gas_co2 = 0.025

state_labels = [
    "S_su","S_aa","S_fa","S_va","S_bu","S_pro","S_ac","S_h2","S_ch4","S_IC","S_IN","S_I",
    "X_xc1","X_ch1","X_pr1","X_li1","X_xc2","X_ch2","X_pr2","X_li2","X_su","X_aa","X_fa","X_c4",
    "X_pro","X_ac","X_h2","X_I","S_cation","S_anion","S_H_ion","S_va_ion","S_bu_ion","S_pro_ion",
    "S_ac_ion","S_hco3_ion","S_co2","S_nh3","S_nh4_ion","S_gas_h2","S_gas_ch4","S_gas_co2"
]

state_zero: List[float] = [
    S_su, S_aa, S_fa, S_va, S_bu, S_pro, S_ac, S_h2, S_ch4, S_IC, S_IN, S_I,
    X_xc1, X_ch1, X_pr1, X_li1, X_xc2, X_ch2, X_pr2, X_li2, X_su, X_aa, X_fa, X_c4,
    X_pro, X_ac, X_h2, X_I, S_cation, S_anion, S_H_ion, S_va_ion, S_bu_ion, S_pro_ion,
    S_ac_ion, S_hco3_ion, S_co2, S_nh3, S_nh4_ion, S_gas_h2, S_gas_ch4, S_gas_co2
]

def build_state_zero() -> List[float]:
    return list(state_zero)

STATE_INDEX = {label: i for i,label in enumerate(state_labels)}

__all__ = [name for name in globals().keys() if not name.startswith("_")]
