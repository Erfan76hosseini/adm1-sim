"""Core physical constants for the ADM1 model.

Separated from params.py so scenario / kinetic variations can override only
what changes without duplicating universal physical values.

All values use the original units from the ADM1 / BSM2 references.
"""
from __future__ import annotations

# Universal / physical constants (scenario-independent)
R: float = 0.083145  # bar·M^-1·K^-1 (gas constant in required units)
p_atm: float = 1.013  # bar (standard atmospheric pressure)
T_base: float = 298.15  # K (reference temperature)

__all__ = ["R", "p_atm", "T_base"]
