
import numpy as np
# adm1_params.py
# All ADM1 model parameters and constants for reuse

## unit for each parameter is commented after it is declared (inline)
## if the suggested value for the parameter is different -
## The original default value from the original ADM1 report by Batstone et al (2002), is commented after each unit (inline)


mixing_ratio=0.99999 # feed1/total


##parameter definition from the Rosen et al (2006) BSM2 report bmadm1_report
# Stoichiometric parameter

####################

from adm1.initial_state import *
from adm1.influent import *


# Composition fractions for particulate COD of each substrate

##Feed1

f_sI_xc1 = 0.1 
f_xI_xc1 = 0.2 
f_ch_xc1 = 0.2 
f_pr_xc1 = 0.2
f_li_xc1 = 0.3

##Feed2

f_sI_xc2 = 0.1
f_xI_xc2 = 0.2
f_ch_xc2 = 0.2
f_pr_xc2 = 0.2
f_li_xc2 = 0.3

#####################


## unit for each parameter is commented after it is declared (inline)
## if the suggested value for the parameter is different -
## The original default value from the original ADM1 report by Batstone et al (2002), is commented after each unit (inline)


N_xc =  0.0376 / 14
N_I =  0.06 / 14 #kmole N.kg^-1COD
N_aa =  0.007 #kmole N.kg^-1COD

C_xc =  mixing_ratio*0.02786 #kmole C.kg^-1COD
C_sI =  mixing_ratio*0.03 #kmole C.kg^-1COD
C_ch =  mixing_ratio*0.0313 #kmole C.kg^-1COD
C_pr =  mixing_ratio*0.03 #kmole C.kg^-1COD
C_li =  mixing_ratio*0.022 #kmole C.kg^-1COD
C_xI =  mixing_ratio*0.03 #kmole C.kg^-1COD

C_xc_ref = 0.02786 #kmole C.kg^-1COD
C_sI_ref =  0.03 #kmole C.kg^-1COD
C_ch_ref =  0.0313 #kmole C.kg^-1COD
C_pr_ref =  0.03 #kmole C.kg^-1COD
C_li_ref =  0.022 #kmole C.kg^-1COD
C_xI_ref =  0.03 #kmole C.kg^-1COD'
#_______________________

C_su =  0.0313 #kmole C.kg^-1COD

#_______________________

C_aa =  0.03 #kmole C.kg^-1COD
#_______________________
f_fa_li =  0.95
C_fa =  0.0217 #kmole C.kg^-1COD
#_______________________
f_h2_su =  0.19
f_bu_su =  0.13
f_pro_su =  0.27
f_ac_su =  0.41
N_bac =  0.08 / 14 #kmole N.kg^-1COD
C_bu =  0.025 #kmole C.kg^-1COD
C_pro =  0.0268 #kmole C.kg^-1COD
C_ac =  0.0313 #kmole C.kg^-1COD
C_bac =  0.0313 #kmole C.kg^-1COD

#_______________________
f_h2_aa =  0.06
f_va_aa =  0.23
f_bu_aa =  0.26
f_pro_aa =  0.05
f_ac_aa =  0.40
C_va =  0.024 #kmole C.kg^-1COD

#_______________________

#_______________________

#_______________________

#_______________________
C_ch4 =  0.0156 #kmole C.kg^-1COD

#_______________________




#########################



# Physico-chemical parameter values from the Rosen et al (2006) BSM2 report
T_ad =  308.15 #K
R =  0.083145 #bar.M^-1.K^-1
T_base =  298.15 #K
T_op =  308.15 #k ##T_ad #=35 C

#_______________________
K_w =  10 ** -14.0 * np.exp((55900 / (100 * R)) * (1 / T_base - 1 / T_ad)) #M #2.08 * 10 ^ -14
K_a_va =  10 ** -4.86 #M  ADM1 value = 1.38 * 10 ^ -5
K_a_bu =  10 ** -4.82 #M #1.5 * 10 ^ -5
K_a_pro =  10 ** -4.88 #M #1.32 * 10 ^ -5
K_a_ac =  10 ** -4.76 #M #1.74 * 10 ^ -5
K_a_co2 =  10 ** -6.35 * np.exp((7646 / (100 * R)) * (1 / T_base - 1 / T_ad)) #M #4.94 * 10 ^ -7
K_a_IN =  10 ** -9.25 * np.exp((51965 / (100 * R)) * (1 / T_base - 1 / T_ad)) #M #1.11 * 10 ^ -9
#_______________________

k_A_B_va =  10 ** 10 #M^-1 * d^-1
k_A_B_bu =  10 ** 10 #M^-1 * d^-1
k_A_B_pro =  10 ** 10 #M^-1 * d^-1
k_A_B_ac =  10 ** 10 #M^-1 * d^-1
k_A_B_co2 =  10 ** 10 #M^-1 * d^-1
k_A_B_IN =  10 ** 10 #M^-1 * d^-1

#_______________________

p_atm =  1.013 #bar
p_gas_h2o =  0.0313 * np.exp(5290 * (1 / T_base - 1 / T_ad)) #bar #0.0557
k_p = 5 * 10 ** 4 #m^3.d^-1.bar^-1 #only for BSM2 AD conditions, recalibrate for other AD cases #gas outlet friction
#_______________________
k_L_a =  200.0 #d^-1
#_______________________
K_H_co2 =  0.035 * np.exp((-19410 / (100 * R))* (1 / T_base - 1 / T_ad)) #Mliq.bar^-1 #0.0271
K_H_ch4 =  0.0014 * np.exp((-14240 / (100 * R)) * (1 / T_base - 1 / T_ad)) #Mliq.bar^-1 #0.00116
K_H_h2 =  7.8 * 10 ** -4 * np.exp(-4180 / (100 * R) * (1 / T_base - 1 / T_ad)) #Mliq.bar^-1 #7.38*10^-4

##################################

# related to pH inhibition taken from BSM2 report, they are global variables to avoid repeating them in DAE part
K_pH_aa =  (10 ** (-1 * (pH_LL_aa + pH_UL_aa) / 2.0))
nn_aa =  (3.0 / (pH_UL_aa - pH_LL_aa)) #we need a differece between N_aa and n_aa to avoid typos and nn_aa refers to n_aa in BSM2 report
K_pH_ac =  (10 ** (-1 * (pH_LL_ac + pH_UL_ac) / 2.0))
n_ac =  (3.0 / (pH_UL_ac - pH_LL_ac))
K_pH_h2 =  (10 ** (-1 * (pH_LL_h2 + pH_UL_h2) / 2.0))
n_h2 =  (3.0 / (pH_UL_h2 - pH_LL_h2))

S_nh4_ion =  (S_IN - S_nh3)

S_co2 =  (S_IC - S_hco3_ion)

#pH equation

######################

# Physical parameter values

t0=0
n=0




# ADM1  suggested biochemical parameter sets for different temperature phases (from Batstone et al. 2002 Table 6.2)

MESOPHILIC_HIGH_RATE = {
	"k_dis1": 0.4, #d^-1
    "k_dis2": 0.4, #d^-1
	"k_hyd_ch1": 0.25, #d^-1
	"k_hyd_pr1": 0.2, #d^-1
	"k_hyd_li1": 0.1, #d^-1
    "k_hyd_ch2": 5.22, #d^-1
	"k_hyd_pr2": 1.86, #d^-1
	"k_hyd_li2": 1.24, #d^-1
    #_______________________
	"k_dec_X_su":  0.02, #d^-1
    "k_dec_X_aa":  0.02, #d^-1
    "k_dec_X_fa":  0.02, #d^-1
    "k_dec_X_c4":  0.02, #d^-1
    "k_dec_X_pro":  0.02, #d^-1
    "k_dec_X_ac":  0.02, #d^-1
    "k_dec_X_h2":  0.02, #d^-1
    "K_S_IN":  10 ** -4, #M
    #_______________________
    "pH_UL_aa":  5.5,
    "pH_LL_aa":  4,
    #_______________________
    "k_m_su":  30, #d^-1
    "K_S_su":  0.5, #kgCOD.m^-3
    "Y_su":  0.1, #COD.COD^-1
    #_______________________
    "k_m_aa":  50, #d^-1
    "K_S_aa":  0.3, ##kgCOD.m^-3
    "Y_aa":  0.08, #COD.COD^-1
    #_______________________
    "k_m_fa":  6, #d^-1
    "K_S_fa":  0.4, #kgCOD.m^-3
    "Y_fa":  0.06, #COD.COD^-1
    "K_I_h2_fa":  5 * 10 ** -6, #kgCOD.m^-3
    #_______________________
    "k_m_c4":  20, #d^-1
    "K_S_c4":  0.3, #kgCOD.m^-3
    "Y_c4":  0.04, #COD.COD^-1
    "K_I_h2_c4":  3.5 ** -6, #kgCOD.m^-3
    #_______________________
    "k_m_pro":  13, #d^-1
    "K_S_pro":  0.3, #kgCOD.m^-3
    "Y_pro":  0.04, #COD.COD^-1
    "K_I_h2_pro":  3.5 * 10 ** -6, #kgCOD.m^-3
    #_______________________
    "k_m_ac":  8, #d^-1
    "K_S_ac":  0.15, #kgCOD.m^-3
    "Y_ac":  0.05, #COD.COD^-1
    "pH_UL_ac":  7,
    "pH_LL_ac":  6,
    "K_I_nh3":  0.0018, #M
    #_______________________
    "k_m_h2":  35, #d^-1
    "K_S_h2":  2.5 * 10 ** -5, #kgCOD.m^-3
    "Y_h2":  0.06, #COD.COD^-1
    "pH_UL_h2":  6,
    "pH_LL_h2":  5
}

MESOPHILIC_SOLIDS = {
	"k_dis1": 0.5, #d^-1
    "k_dis2": 0.5,  #d^-1
	"k_hyd_ch1": 10, #d^-1
	"k_hyd_pr1": 10, #d^-1
	"k_hyd_li1": 10, #d^-1
    "k_hyd_ch2": 5.22, #d^-1
	"k_hyd_pr2": 1.86, #d^-1
	"k_hyd_li2": 1.24, #d^-1
    #_______________________
	"k_dec_X_su":  0.02, #d^-1
    "k_dec_X_aa":  0.02, #d^-1
    "k_dec_X_fa":  0.02, #d^-1
    "k_dec_X_c4":  0.02, #d^-1
    "k_dec_X_pro":  0.02, #d^-1
    "k_dec_X_ac":  0.02, #d^-1
    "k_dec_X_h2":  0.02, #d^-1
    "K_S_IN":  10 ** -4, #M
    #_______________________
    "pH_UL_aa":  5.5,
    "pH_LL_aa":  4,
    #_______________________
    "k_m_su":  30, #d^-1
    "K_S_su":  0.5, #kgCOD.m^-3
    "Y_su":  0.1, #COD.COD^-1
    #_______________________
    "k_m_aa":  50, #d^-1
    "K_S_aa":  0.3, ##kgCOD.m^-3
    "Y_aa":  0.08, #COD.COD^-1
    #_______________________
    "k_m_fa":  6, #d^-1
    "K_S_fa":  0.4, #kgCOD.m^-3
    "Y_fa":  0.06, #COD.COD^-1
    "K_I_h2_fa":  5 * 10 ** -6, #kgCOD.m^-3
    #_______________________
    "k_m_c4":  20, #d^-1
    "K_S_c4":  0.3, #kgCOD.m^-3
    "Y_c4":  0.04,
    "K_I_h2_c4":  3.5 ** -6, #kgCOD.m^-3
    #_______________________
    "k_m_pro":  13, #d^-1
    "K_S_pro":  0.1, #kgCOD.m^-3
    "Y_pro":  0.04, #COD.COD^-1
    "K_I_h2_pro":  3.5 * 10 ** -6, #kgCOD.m^-3
    #_______________________
    "k_m_ac":  8, #d^-1
    "K_S_ac":  0.15, #kgCOD.m^-3
    "Y_ac":  0.05, #COD.COD^-1
    "pH_UL_ac":  7,
    "pH_LL_ac":  6,
    "K_I_nh3":  0.0018, #M
    #_______________________
    "k_m_h2":  35, #d^-1
    "K_S_h2":  7 * 10 ** -6, #kgCOD.m^-3
    "Y_h2":  0.06, #COD.COD^-1
    "pH_UL_h2":  6,
    "pH_LL_h2":  5
}

THERMOPHILIC_SOLIDS = {
	"k_dis1": 1.0 , #d^-1
    "k_dis2": 1.0 , #d^-1
	"k_hyd_ch1": 10, #d^-1
	"k_hyd_pr1": 10, #d^-1
	"k_hyd_li1": 10, #d^-1
    "k_hyd_ch2": 5.22, #d^-1
	"k_hyd_pr2": 1.86, #d^-1
	"k_hyd_li2": 1.24, #d^-1
    #_______________________
	"k_dec_X_su":  0.04, #d^-1
    "k_dec_X_aa":  0.04, #d^-1
    "k_dec_X_fa":  0.04, #d^-1
    "k_dec_X_c4":  0.04, #d^-1
    "k_dec_X_pro":  0.04, #d^-1
    "k_dec_X_ac":  0.04, #d^-1
    "k_dec_X_h2":  0.04, #d^-1
    "K_S_IN":  10 ** -4, #M
    #_______________________
    "pH_UL_aa":  5.5,
    "pH_LL_aa":  4,
    #_______________________
    "k_m_su":  70, #d^-1
    "K_S_su":  1, #kgCOD.m^-3
    "Y_su":  0.1, #COD.COD^-1
    #_______________________
    "k_m_aa":  70, #d^-1
    "K_S_aa":  0.3, ##kgCOD.m^-3
    "Y_aa":  0.08, #COD.COD^-1 
    #_______________________
    "k_m_fa": 10, #d^-1
    "K_S_fa":  0.4, #kgCOD.m^-3
    "Y_fa":  0.06, #COD.COD^-1
    "K_I_h2_fa":  5 * 10 ** -6, #kgCOD.m^-3
    #_______________________
    "k_m_c4":  30, #d^-1
    "K_S_c4":  0.4, #kgCOD.m^-3
    "Y_c4":  0.06, #COD.COD^-1
    "K_I_h2_c4":  3 ** -5, #kgCOD.m^-3
    #_______________________
    "k_m_pro":  20, #d^-1
    "K_S_pro":  0.3, #kgCOD.m^-3
    "Y_pro":  0.05, #COD.COD^-1
    "K_I_h2_pro":  1 * 10 ** -5, #kgCOD.m^-3
    #_______________________
    "k_m_ac":  16, #d^-1
    "K_S_ac":  0.3, #kgCOD.m^-3
    "Y_ac":  0.05, #COD.COD^-1
    "pH_UL_ac":  7,
    "pH_LL_ac":  6,
    "K_I_nh3":  0.011, #M
    #_______________________
    "k_m_h2":  35, #d^-1
    "K_S_h2":  5 * 10 ** -5, #kgCOD.m^-3
    "Y_h2":  0.06, #COD.COD^-1
    "pH_UL_h2":  6,
    "pH_LL_h2":  5
}

PARAMETER_SETS = {
	"mesophilic_high_rate": MESOPHILIC_HIGH_RATE,
	"mesophilic_solids": MESOPHILIC_SOLIDS,
	"thermophilic_solids": THERMOPHILIC_SOLIDS,
}