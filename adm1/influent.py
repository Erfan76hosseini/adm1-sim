
import numpy as np



# ---  Reactor Setup ---
def calculate_influent(
    q_ad_init=500,                # Initial influent flow rate [m^3/d]
    density=1000,                # Influent density [kg/m^3]
    water_fraction=0.97,         # Fraction of water in influent
    evaporated_water_volume=350, # Water lost to evaporation [m^3/d]
    mixing_ratio=0.99999,   # Fraction for feed 1 # feed1 / total (can be overridden per scenario)
    OLR=5                     # Organic Loading Rate [kg VS/m3/d]
):
    """
    Calculate influent and reactor parameters for ADM1.
    Returns a dict with all relevant values.
    """
    # Volatile solids (VS) fraction and content
    vs_frac = 1 - water_fraction  # [kg VS/kg total]
    vs_content = vs_frac * q_ad_init  # [m^3/d] (approximate, if 1 kg VS ~ 1 L)

    # Adjust for evaporation
    water_content = water_fraction * q_ad_init - evaporated_water_volume  # [m^3/d]
    q_ad = water_content + vs_content  # New total influent flow [m^3/d]

    # Feed split
    q_ad1 = mixing_ratio * q_ad
    q_ad2 = q_ad - q_ad1

    # Recalculate VS fraction after evaporation
    vs_frac_actual = vs_content / q_ad if q_ad > 0 else 0
    VS_in = density * q_ad * vs_frac_actual * 0.001  # [tonne/d]

    # Hydraulic Retention Time (HRT) and reactor volumes
    HRT = density * vs_frac_actual / OLR if OLR > 0 else 0  # [days]
    V_liq = HRT * q_ad  # [m^3]
    V_gas = 0.1 * V_liq # [m^3]
    V_ad = V_liq + V_gas # [m^3]

    return {
        'q_ad': q_ad,
        'q_ad1': q_ad1,
        'q_ad2': q_ad2,
        'vs_frac': vs_frac_actual,
        'VS_in': VS_in,
        'HRT': HRT,
        'V_liq': V_liq,
        'V_gas': V_gas,
        'V_ad': V_ad,
        'OLR': OLR,
        'density': density,
        'water_fraction': water_fraction,
        'evaporated_water_volume': evaporated_water_volume,
        'mixing_ratio': mixing_ratio
    }

# --- Set up influent for this scenario ---

influent = calculate_influent()
q_ad = influent['q_ad']
q_ad1 = influent['q_ad1']
q_ad2 = influent['q_ad2']
VS = influent['vs_frac']
VS_in = influent['VS_in']
HRT = influent['HRT']
V_liq = influent['V_liq']
V_gas = influent['V_gas']
V_ad = influent['V_ad']
OLR = influent['OLR']
density = influent['density']
water_fraction = influent['water_fraction']
evaporated_water_volume = influent['evaporated_water_volume']
mixing_ratio=influent['mixing_ratio']

# --- End  Reactor Setup ---


# --- Influent  ---

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
