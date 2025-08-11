
import numpy as np
# adm1_params.py
# All ADM1 model parameters and constants for reuse

## unit for each parameter is commented after it is declared (inline)
## if the suggested value for the parameter is different -
## The original default value from the original ADM1 report by Batstone et al (2002), is commented after each unit (inline)


mixing_ratio=0.99999 # feed1/total

####################


## unit for each parameter is commented after it is declared (inline)
## if the suggested value for the parameter is different -
## The original default value from the original ADM1 report by Batstone et al (2002), is commented after each unit (inline)

##constant definition from the Rosen et al (2006) BSM2 report
R =  0.083145 #bar.M^-1.K^-1
T_base =  298.15 #K
p_atm =  1.013 #bar
T_op =  308.15 #k ##T_ad #=35 C

##parameter definition from the Rosen et al (2006) BSM2 report bmadm1_report
# Stoichiometric parameter


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


C_su =  0.0313 #kmole C.kg^-1COD
C_aa =  0.03 #kmole C.kg^-1COD
f_fa_li =  0.95
C_fa =  0.0217 #kmole C.kg^-1COD
f_h2_su =  0.19
f_bu_su =  0.13
f_pro_su =  0.27
f_ac_su =  0.41
N_bac =  0.08 / 14 #kmole N.kg^-1COD
C_bu =  0.025 #kmole C.kg^-1COD
C_pro =  0.0268 #kmole C.kg^-1COD
C_ac =  0.0313 #kmole C.kg^-1COD
C_bac =  0.0313 #kmole C.kg^-1COD
Y_su =  0.1
f_h2_aa =  0.06
f_va_aa =  0.23
f_bu_aa =  0.26
f_pro_aa =  0.05
f_ac_aa =  0.40
C_va =  0.024 #kmole C.kg^-1COD
Y_aa =  0.08
Y_fa =  0.06
Y_c4 =  0.06
Y_pro =  0.04
C_ch4 =  0.0156 #kmole C.kg^-1COD
Y_ac =  0.05
Y_h2 =  0.06

####################

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


# Define parameters for both substrates

variation_factor3=1

k_dis1 = 0.55    # Disintegration rate for Substrate 1 (d^-1)
k_dis2 = 0.55    # Disintegration rate for Substrate 2 (d^-1)

variation_factor3=1

# Hydrolysis rates for Substrate 1 (d^-1)
k_hyd_ch1 = 10; k_hyd_pr1 = 10; k_hyd_li1 = 10
#k_hyd_ch1 = 10; k_hyd_pr1 = 10; k_hyd_li1 = 10


# Hydrolysis rates for Substrate 2 (d^-1)

k_hyd_ch2 = 5.22; k_hyd_pr2 = 1.86; k_hyd_li2 = variation_factor3*1.24
#k_hyd_ch2 = 10; k_hyd_pr2 = 10; k_hyd_li2 = 10


##########################


# Biochemical parameter values from the Rosen et al (2006) BSM2 report
K_S_IN =  10 ** -4 #M
k_m_su =  30 #d^-1
K_S_su =  0.5 #kgCOD.m^-3
pH_UL_aa =  5.5
pH_LL_aa =  4
k_m_aa =  50 #d^-1
K_S_aa =  0.3 ##kgCOD.m^-3
k_m_fa =  6 #d^-1
K_S_fa =  0.4 #kgCOD.m^-3
K_I_h2_fa =  5 * 10 ** -6 #kgCOD.m^-3
k_m_c4 =  20 #d^-1
K_S_c4 =  0.2 #kgCOD.m^-3
K_I_h2_c4 =  10 ** -5 #kgCOD.m^-3
k_m_pro =  13 #d^-1
K_S_pro =  0.1 #kgCOD.m^-3
K_I_h2_pro =  3.5 * 10 ** -6 #kgCOD.m^-3
k_m_ac =  8 #kgCOD.m^-3
K_S_ac =  0.15 #kgCOD.m^-3
K_I_nh3 =  0.0018 #M
pH_UL_ac =  7
pH_LL_ac =  6
k_m_h2 =  35 #d^-1
K_S_h2 =  7 * 10 ** -6 #kgCOD.m^-3
pH_UL_h2 =  6
pH_LL_h2 =  5
k_dec_X_su =  0.02 #d^-1
k_dec_X_aa =  0.02 #d^-1
k_dec_X_fa =  0.02 #d^-1
k_dec_X_c4 =  0.02 #d^-1
k_dec_X_pro =  0.02 #d^-1
k_dec_X_ac =  0.02 #d^-1
k_dec_X_h2 =  0.02 #d^-1
## M is kmole m^-3




#########################



# Physico-chemical parameter values from the Rosen et al (2006) BSM2 report
T_ad =  308.15 #K


K_w =  10 ** -14.0 * np.exp((55900 / (100 * R)) * (1 / T_base - 1 / T_ad)) #M #2.08 * 10 ^ -14

K_a_va =  10 ** -4.86 #M  ADM1 value = 1.38 * 10 ^ -5
K_a_bu =  10 ** -4.82 #M #1.5 * 10 ^ -5
K_a_pro =  10 ** -4.88 #M #1.32 * 10 ^ -5
K_a_ac =  10 ** -4.76 #M #1.74 * 10 ^ -5


K_a_co2 =  10 ** -6.35 * np.exp((7646 / (100 * R)) * (1 / T_base - 1 / T_ad)) #M #4.94 * 10 ^ -7
K_a_IN =  10 ** -9.25 * np.exp((51965 / (100 * R)) * (1 / T_base - 1 / T_ad)) #M #1.11 * 10 ^ -9


k_A_B_va =  10 ** 10 #M^-1 * d^-1
k_A_B_bu =  10 ** 10 #M^-1 * d^-1
k_A_B_pro =  10 ** 10 #M^-1 * d^-1
k_A_B_ac =  10 ** 10 #M^-1 * d^-1
k_A_B_co2 =  10 ** 10 #M^-1 * d^-1
k_A_B_IN =  10 ** 10 #M^-1 * d^-1


p_gas_h2o =  0.0313 * np.exp(5290 * (1 / T_base - 1 / T_ad)) #bar #0.0557
k_p = 5 * 10 ** 4 #m^3.d^-1.bar^-1 #only for BSM2 AD conditions, recalibrate for other AD cases #gas outlet friction
k_L_a =  200.0 #d^-1
K_H_co2 =  0.035 * np.exp((-19410 / (100 * R))* (1 / T_base - 1 / T_ad)) #Mliq.bar^-1 #0.0271
K_H_ch4 =  0.0014 * np.exp((-14240 / (100 * R)) * (1 / T_base - 1 / T_ad)) #Mliq.bar^-1 #0.00116
K_H_h2 =  7.8 * 10 ** -4 * np.exp(-4180 / (100 * R) * (1 / T_base - 1 / T_ad)) #Mliq.bar^-1 #7.38*10^-4



#########################

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


# SciPy ADM1 input array from Pettigrew (2017) jADM1 and Rosen et al (2006) BSM2 report
# initiate variables (initial values for the reactor state at t0)


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

variation_factor=50


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
#S_nh4_ion = 0.126138 #kmole N.m^-3 the initial value is from Rosen et al (2006) BSM2 report and it is calculated further down and does not need to be initiated
#S_co2 = 0.0093003 #kmole C.m^-3 the initial value is from Rosen et al (2006) BSM2 report and it is calculated further down and does not need to be initiated
S_gas_h2 = 4.91 * 10 ** -6 #kg COD.m^-3
S_gas_ch4 = 1.78 #kg COD.m^-3
S_gas_co2 = 0.025 #kmole C.m^-3




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


# related to pH inhibition taken from BSM2 report, they are global variables to avoid repeating them in DAE part
K_pH_aa =  (10 ** (-1 * (pH_LL_aa + pH_UL_aa) / 2.0))
nn_aa =  (3.0 / (pH_UL_aa - pH_LL_aa)) #we need a differece between N_aa and n_aa to avoid typos and nn_aa refers to the n_aa in BSM2 report
K_pH_ac = (10 ** (-1 * (pH_LL_ac + pH_UL_ac) / 2.0))
n_ac =  (3.0 / (pH_UL_ac - pH_LL_ac))
K_pH_h2 =  (10 ** (-1 * (pH_LL_h2 + pH_UL_h2) / 2.0))
n_h2 =  (3.0 / (pH_UL_h2 - pH_LL_h2))

#pH equation
#pH = - np.log10(S_H_ion)
pH = 7.4655377 # initial pH



#####################

q_ad =  500
#q_ad =  1000

q_ad1 =  mixing_ratio*q_ad #m^3.d^-1 initial flow rate (can be modified during the simulation by the control algorithm)
q_ad2= q_ad-q_ad1


density=1000  #kg/m3

VS=0.1 #kg/kg
VS_in=density*q_ad*VS*0.001   #tonne

print(q_ad1, q_ad2, VS_in)


######################


# Physical parameter values

# Physical parameter values used in BSM2 from the Rosen et al (2006) BSM2 report
HRT=20  #days

V_liq =HRT*q_ad   #m^3
V_gas =  0.088*V_liq #m^3
#V_liq =  10000 #m^3
#V_gas =  1000 #m^3
V_ad = V_liq + V_gas #m^-3


print(V_liq)
print(V_gas)


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


# Define the labels for each state variable
state_labels = [
    "S_su", "S_aa", "S_fa", "S_va", "S_bu", "S_pro", "S_ac", "S_h2", "S_ch4",
    "S_IC", "S_IN", "S_I", "X_xc1", "X_ch1", "X_pr1", "X_li1", "X_xc2", "X_ch2", 
    "X_pr2", "X_li2", "X_su", "X_aa", "X_fa", "X_c4", "X_pro", "X_ac", "X_h2", 
    "X_I", "S_cation", "S_anion", "S_H_ion", "S_va_ion", "S_bu_ion", "S_pro_ion", 
    "S_ac_ion", "S_hco3_ion", "S_co2", "S_nh3", "S_nh4_ion", "S_gas_h2", 
    "S_gas_ch4", "S_gas_co2"
]

input_labels = [
    "S_su_in", "S_aa_in", "S_fa_in", "S_va_in", "S_bu_in", "S_pro_in", "S_ac_in", 
    "S_h2_in", "S_ch4_in", "S_IC_in", "S_IN_in", "S_I_in", "X_xc1_in", "X_ch1_in", 
    "X_pr1_in", "X_li1_in", "X_xc2_in", "X_ch2_in", "X_pr2_in", "X_li2_in", "X_su_in", 
    "X_aa_in", "X_fa_in", "X_c4_in", "X_pro_in", "X_ac_in", "X_h2_in", "X_I_in", 
    "S_cation_in", "S_anion_in"
]

# Printing state_zero
print("State Zero Values:")
for label, value in zip(state_labels, state_zero):
    print(f"{label}: {value}")

print("\nState Input Values:")
for label, value in zip(input_labels, state_input):
    print(f"{label}: {value}")



##############################
##time definition
days = 150
timeSteps = days*24 #every 15 minutes 
t = np.linspace(0, days, timeSteps) #sequence of timesteps as fractions of days


#####################

#switch between ODE (0) and DAE (1) implementations
DAE_switch = 1

t0=0
n=0