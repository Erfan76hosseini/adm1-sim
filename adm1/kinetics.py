"""Kinetic, stoichiometric, and inhibition parameters for ADM1.

This module isolates kinetic/biochemical rates, saturation constants, yields,
acid/base equilibria, gas transfer, and decay constants from the broader
params.py to support cleaner scenario management.

All variables are kept at module level for backward compatibility; consider
wrapping into a dataclass for advanced scenario handling.
"""
from __future__ import annotations

import numpy as np
from .constants import R, T_base

# Temperature (operational) may be scenario dependent; default typical mesophilic
T_ad: float = 308.15  # K (operating temperature)

# Acid/base dissociation and water constants (temperature dependent expressions)
K_w = 10 ** -14.0 * np.exp((55900 / (100 * R)) * (1 / T_base - 1 / T_ad))  # M
K_a_va = 10 ** -4.86  # M
K_a_bu = 10 ** -4.82  # M
K_a_pro = 10 ** -4.88  # M
K_a_ac = 10 ** -4.76  # M
K_a_co2 = 10 ** -6.35 * np.exp((7646 / (100 * R)) * (1 / T_base - 1 / T_ad))  # M
K_a_IN = 10 ** -9.25 * np.exp((51965 / (100 * R)) * (1 / T_base - 1 / T_ad))  # M

# Gas transfer / Henry constants (temperature dependent)
K_H_co2 = 0.035 * np.exp((-19410 / (100 * R)) * (1 / T_base - 1 / T_ad))  # Mliq.bar^-1
K_H_ch4 = 0.0014 * np.exp((-14240 / (100 * R)) * (1 / T_base - 1 / T_ad))  # Mliq.bar^-1
K_H_h2 = 7.8e-4 * np.exp(-4180 / (100 * R) * (1 / T_base - 1 / T_ad))  # Mliq.bar^-1

# Water vapour saturation partial pressure (bar) at T_ad (from BSM2 expression)
p_gas_h2o = 0.0313 * np.exp(5290 * (1 / T_base - 1 / T_ad))  # bar

# Kinetic maximum rates (d^-1)
k_m_su = 30.0
k_m_aa = 50.0
k_m_fa = 6.0
k_m_c4 = 20.0
k_m_pro = 13.0
k_m_ac = 8.0
k_m_h2 = 35.0

# Saturation / half-saturation constants
K_S_su = 0.5       # kgCOD.m^-3
K_S_aa = 0.3       # kgCOD.m^-3
K_S_fa = 0.4       # kgCOD.m^-3
K_S_c4 = 0.2       # kgCOD.m^-3
K_S_pro = 0.1      # kgCOD.m^-3
K_S_ac = 0.15      # kgCOD.m^-3
K_S_h2 = 7e-6      # kgCOD.m^-3
K_S_IN = 1e-4      # M

# Inhibition constants / thresholds
K_I_h2_fa = 5e-6       # kgCOD.m^-3
K_I_h2_c4 = 1e-5       # kgCOD.m^-3
K_I_h2_pro = 3.5e-6    # kgCOD.m^-3
K_I_nh3 = 0.0018       # M

# pH limits (dimensionless)
pH_UL_aa, pH_LL_aa = 5.5, 4.0
pH_UL_ac, pH_LL_ac = 7.0, 6.0
pH_UL_h2, pH_LL_h2 = 6.0, 5.0

# pH inhibition helper constants (derived) - typical Hill-like
K_pH_aa = 10 ** (-(pH_LL_aa + pH_UL_aa) / 2.0)
nn_aa = 3.0 / (pH_UL_aa - pH_LL_aa)
K_pH_ac = 10 ** (-(pH_LL_ac + pH_UL_ac) / 2.0)
n_ac = 3.0 / (pH_UL_ac - pH_LL_ac)
K_pH_h2 = 10 ** (-(pH_LL_h2 + pH_UL_h2) / 2.0)
n_h2 = 3.0 / (pH_UL_h2 - pH_LL_h2)

# Disintegration & hydrolysis rates (d^-1)
k_dis1 = 0.55
k_dis2 = 0.55
k_hyd_ch1 = 10.0
k_hyd_pr1 = 10.0
k_hyd_li1 = 10.0
k_hyd_ch2 = 5.22
k_hyd_pr2 = 1.86
k_hyd_li2 = 1.24  # subject to variation factors externally

# Biomass decay rates (d^-1)
k_dec_X_su = 0.02
k_dec_X_aa = 0.02
k_dec_X_fa = 0.02
k_dec_X_c4 = 0.02
k_dec_X_pro = 0.02
k_dec_X_ac = 0.02
k_dec_X_h2 = 0.02

# Gas transfer / mass transfer
k_L_a = 200.0       # d^-1
k_p = 5e4           # m^3.d^-1.bar^-1 (gas outlet friction)

# Acid-base reaction kinetics (very fast, pseudo-equilibrium constants)
k_A_B_va = 1e10
k_A_B_bu = 1e10
k_A_B_pro = 1e10
k_A_B_ac = 1e10
k_A_B_co2 = 1e10
k_A_B_IN = 1e10

# Stoichiometric carbon / nitrogen distribution factors & yields
f_h2_su = 0.19
f_bu_su = 0.13
f_pro_su = 0.27
f_ac_su = 0.41
f_h2_aa = 0.06
f_va_aa = 0.23
f_bu_aa = 0.26
f_pro_aa = 0.05
f_ac_aa = 0.40

Y_su = 0.1
Y_aa = 0.08
Y_fa = 0.06
Y_c4 = 0.06
Y_pro = 0.04
Y_ac = 0.05
Y_h2 = 0.06

# Elemental composition factors (retain for completeness)
N_bac = 0.08 / 14

__all__ = [name for name in globals().keys() if not name.startswith("_")]
