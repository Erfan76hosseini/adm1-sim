# SciPy ADM1 input array from Pettigrew (2017) jADM1 and Rosen et al (2006) BSM2 report
# initiate variables (initial values for the reactor state at t0)
import numpy as np

from adm1.influent import *

# Scenario / mixing fractions
mixing_ratio: float = 0.99999  # feed1 / total (can be overridden per scenario)

S_su = 0.00001 #kg COD.m^-3
S_aa = 0.00001 #kg COD.m^-3
S_fa = 0.00001 #kg COD.m^-3
S_va = 0.00001 #kg COD.m^-3
S_bu = 0.00001 #kg COD.m^-3
S_pro = 0.00001 #kg COD.m^-3
S_ac = 0.00001 #kg COD.m^-3
S_h2 =  10 ** -8
S_ch4 = 10** -5 #kg COD.m^-3
S_IC = 0.04 #kg COD.m^-3
S_IN = 0.01 #kmole C.m^-3
S_I = 0.02 #kmole N.m^-3

#______________Feed1 initial_____________________

X_xc1 = mixing_ratio*(2/(2+5+20+5))*0.00001 #kg COD.m^-3
X_ch1 = mixing_ratio*(5/(2+5+20+5))*0.00001 #COD.m^-3
X_pr1 = mixing_ratio*(20/(2+5+20+5))*0.00001 #kg COD.m^-3
X_li1 = mixing_ratio*(5/(2+5+20+5))*0.00001 #kg COD.m^-3

#______________Feed2 initial_____________________

X_xc2 = (1-mixing_ratio)*(0/(205+47.76+6.925))*0.00001 #kg COD.m^-3
X_ch2 = (1-mixing_ratio)*(205/(205+47.76+6.925))*0.00001 #kg COD.m^-3
X_pr2 = (1-mixing_ratio)*(47.76/(205+47.76+6.925))*0.00001 #kg COD.m^-3
X_li2 = (1-mixing_ratio)*(6.925/(205+47.76+6.925))*0.00001 #kg COD.m^-3
#_________________________________________

variation_factor=1


X_su = 1.41 #kg COD.m^-3
X_aa = 0.75 #kg COD.m^-3
X_fa = 0.38 #kg COD.m^-3
X_c4 = 0.35 #kg COD.m^-3
X_pro = variation_factor*0.197 #kg COD.m^-3
X_ac = variation_factor*0.95 #kg COD.m^-3
X_h2 = 0.466 #kg COD.m^-3
X_I = 25.6 #kg COD.m^-3


#________________________________________



S_cation = 0.04000 #kmole.m^-3
S_anion = 0.02 #kmole.m^-3


pH = 7.4655377
S_H_ion = 6.04e-8 #kmole H.m^-3
S_va_ion = 0.0082  #kg COD.m^-3
S_bu_ion = 0.0156 #kg COD.m^-3
S_pro_ion = 0.0172 #kg COD.m^-3
S_ac_ion = 0.11199 #kg COD.m^-3
S_hco3_ion = 0.15415 #kmole C.m^-3
S_nh3 = 0.0025 #kmole N.m^-3
S_nh4_ion = 0.126138 #kmole N.m^-3 the initial value is from Rosen et al (2006) BSM2 report and it is calculated further down and does not need to be initiated
S_co2 = 0.0093003 #kmole C.m^-3 the initial value is from Rosen et al (2006) BSM2 report and it is calculated further down and does not need to be initiated
S_gas_h2 = 4.91 * 10 ** -6 #kg COD.m^-3
S_gas_ch4 = 1.78 #kg COD.m^-3
S_gas_co2 = 0.025 #kmole C.m^-3



#########################


state_zero = [S_su,
              S_aa,
              S_fa,
              S_va,
              S_bu,
              S_pro,
              S_ac,
              S_h2,
              S_ch4,
              S_IC,
              S_IN,
              S_I,
              X_xc1,
              X_ch1,
              X_pr1,
              X_li1,
              X_xc2,
              X_ch2,
              X_pr2,
              X_li2,
              X_su,
              X_aa,
              X_fa,
              X_c4,
              X_pro,
              X_ac,
              X_h2,
              X_I,
              S_cation,
              S_anion,
              S_H_ion,
              S_va_ion,
              S_bu_ion,
              S_pro_ion,
              S_ac_ion,
              S_hco3_ion,
              S_co2,
              S_nh3,
              S_nh4_ion,
              S_gas_h2,
              S_gas_ch4,
              S_gas_co2]



# Define the labels for each state variable
state_labels = [
    "S_su", "S_aa", "S_fa", "S_va", "S_bu", "S_pro", "S_ac", "S_h2", "S_ch4",
    "S_IC", "S_IN", "S_I", "X_xc1", "X_ch1", "X_pr1", "X_li1", "X_xc2", "X_ch2", 
    "X_pr2", "X_li2", "X_su", "X_aa", "X_fa", "X_c4", "X_pro", "X_ac", "X_h2", 
    "X_I", "S_cation", "S_anion", "S_H_ion", "S_va_ion", "S_bu_ion", "S_pro_ion", 
    "S_ac_ion", "S_hco3_ion", "S_co2", "S_nh3", "S_nh4_ion", "S_gas_h2", 
    "S_gas_ch4", "S_gas_co2"]



# Printing state_zero
print("State Zero Values:")
for label, value in zip(state_labels, state_zero):
    print(f"{label}: {value}")
