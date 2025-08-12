
import numpy as np


# Scenario / mixing fractions
mixing_ratio: float = 0.99999  # feed1 / total (can be overridden per scenario)



#####################

q_ad =  500
#q_ad =  1000
q_ad1 =  mixing_ratio*q_ad #m^3.d^-1 initial flow rate (can be modified during the simulation by the control algorithm)
q_ad2= q_ad-q_ad1
density=1000  #kg/m3
VS=0.1 #kg/kg
VS_in=density*q_ad*VS*0.001   #tonne
print("q_ad1:", q_ad1, "q_ad2:", q_ad2, "VS_in:", VS_in)

######################


# Physical parameter values used in BSM2 from the Rosen et al (2006) BSM2 report
# OLR (Organic Loading Rate) calculation: OLR = VS_in * 1000 / (q_ad * HRT)
# If you want to set OLR directly, comment the next line and set OLR as desired.
OLR = 6  # [kg VS/m3/d] Default value, can be overridden

# Calculate HRT based on OLR, or set HRT directly if needed
HRT = density * VS / OLR  # [days]
V_liq = HRT * q_ad   # [m^3]
V_gas = 0.1 * V_liq  # [m^3]
V_ad = V_liq + V_gas # [m^3]

print("V_liq", V_liq)
print("V_gas", V_gas)
print("V_ad", V_ad)
print("OLR", OLR)
print("HRT", HRT)

# If you want to calculate OLR from VS_in, q_ad, and HRT:
# OLR_calc = VS_in * 1000 / (q_ad * HRT)
# print("OLR (calculated)", OLR_calc)


##variable definition
# Steady-state input values (influent/feed) for BSM2 ADM1 from the Rosen et al (2006) BSM2 report

S_su_in = 0.001 #kg COD.m^-3
S_aa_in = 0.001 #kg COD.m^-3
S_fa_in = 0.001 #kg COD.m^-3
S_va_in = 0.001 #kg COD.m^-3
S_bu_in = 0.001 #kg COD.m^-3
S_pro_in = 0.001 #kg COD.m^-3
S_ac_in = 0.001 #kg COD.m^-3
S_h2_in = 10 ** -8  #kg COD.m^-3
S_ch4_in = 10 ** -5  #kg COD.m^-3
S_IC_in = 0.04 #kmole C.m^-3
S_IN_in = 0.01 #kmole N.m^-3
S_I_in = 0.02 #kg COD.m^-3

#______________Feed1 input_____________________

X_xc1_in = mixing_ratio*0 #kg COD.m^-3
X_ch1_in = mixing_ratio*20.057 #kg COD.m^-3
X_pr1_in = mixing_ratio*12.674 #kg COD.m^-3
X_li1_in = mixing_ratio*9.997 #kg COD.m^-3

#______________Feed2 input_____________________

variation_factor4=1

X_xc2_total=variation_factor4*259.992
X_ch2_fraction=0.79
X_pr2_fraction=0.184
X_li2_fraction=0.026

X_xc2_in = (1-mixing_ratio)*0 #kg COD.m^-3
X_ch2_in = (1-mixing_ratio)*X_ch2_fraction*X_xc2_total      #205.31 #kg COD.m^-3
X_pr2_in = (1-mixing_ratio)*X_pr2_fraction*X_xc2_total  #kg COD.m^-3
X_li2_in = (1-mixing_ratio)*X_li2_fraction*X_xc2_total  #kg COD.m^-3

#__________________________________________

X_su_in = 0.0 #kg COD.m^-3
X_aa_in = 0.0 #kg COD.m^-3
X_fa_in = 0.0 #kg COD.m^-3
X_c4_in = 0.0 #kg COD.m^-3
X_pro_in = 0.0 #kg COD.m^-3
X_ac_in = 0.0 #kg COD.m^-3
X_h2_in = 0.0 #kg COD.m^-3
X_I_in = 25.0 #kg COD.m^-3
S_cation_in = 0.04 #kmole.m^-3
S_anion_in = 0.02 #kmole.m^-3

#########################



state_input = [S_su_in,
              S_aa_in,
              S_fa_in,
              S_va_in,
              S_bu_in,
              S_pro_in,
              S_ac_in,
              S_h2_in,
              S_ch4_in,
              S_IC_in,
              S_IN_in,
              S_I_in,
              X_xc1_in,
              X_ch1_in,
              X_pr1_in,
              X_li1_in,
              X_xc2_in,
              X_ch2_in,
              X_pr2_in,
              X_li2_in,
              X_su_in,
              X_aa_in,
              X_fa_in,
              X_c4_in,
              X_pro_in,
              X_ac_in,
              X_h2_in,
              X_I_in,
              S_cation_in,
              S_anion_in]


########################################




input_labels = [
    "S_su_in", "S_aa_in", "S_fa_in", "S_va_in", "S_bu_in", "S_pro_in", "S_ac_in", 
    "S_h2_in", "S_ch4_in", "S_IC_in", "S_IN_in", "S_I_in", "X_xc1_in", "X_ch1_in", 
    "X_pr1_in", "X_li1_in", "X_xc2_in", "X_ch2_in", "X_pr2_in", "X_li2_in", "X_su_in", 
    "X_aa_in", "X_fa_in", "X_c4_in", "X_pro_in", "X_ac_in", "X_h2_in", "X_I_in", 
    "S_cation_in", "S_anion_in"
]


print("\nState Input Values:")
for label, value in zip(input_labels, state_input):
    print(f"{label}: {value}")


