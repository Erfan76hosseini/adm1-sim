
import numpy as np
from adm1.params import get_VSS 


# ---  Reactor Setup ---
def reactor_setup(
    influent,               # Influent scenario function
    initial_state,          # Initial state scenario function
    q_ad_init,                # Initial influent flow rate [m^3/d]
    density,                    # Influent density [tonne/m^3]
    VS_per_TS,                # Volatile solids per  total solids [kg VS/kg TS]    
    TS_fraction,         # Fraction of water in influent
    mixing_ratio,   # Fraction for feed 1 # feed1 / total (can be overridden per scenario)
    OLR,                        # Organic Loading Rate [kg VS/m3/d]
    recycle_ratio                # Recycle ratio [m^3/d]
):
    """
    Calculate influent and reactor parameters for ADM1.
    Returns a dict with all relevant values.
    """
    VSS=get_VSS(influent,q_ad_init, mixing_ratio) #tonne/day
    TS=VSS / VS_per_TS  # Total solids [tonne TS/day]
    water_content=(TS*(1-TS_fraction))/TS_fraction # [tonne/d]
    q_in = (water_content + TS)/density  # New total influent flow [m^3/d]

    # Feed split
    q_in1 = mixing_ratio * q_in
    q_in2 = q_in - q_in1

    #Digestate (liquid effluent) flowrate (m^3/d)
    q_out=q_in/(1-recycle_ratio)

    # Recycle flowrate (m^3/d)
    q_r=recycle_ratio*q_out

    q_ad = q_out

    VS_in=get_VSS(influent,q_ad_init, mixing_ratio)+get_VSS(initial_state,q_ad, mixing_ratio) #[tonne/d]

    # Recalculate VS fraction after evaporation
    #vs_frac_actual = vs_content / q_ad if q_ad > 0 else 0
    #VS_in = density * q_ad * vs_frac_actual * 0.001  # [tonne/d]

    # Hydraulic Retention Time (HRT) and reactor volumes
    HRT = VS_in*1000 / (q_ad*OLR*(1+recycle_ratio)) if OLR > 0 else 0  # [days]
    V_liq = HRT * q_ad  # [m^3]
    V_gas = 0.1 * V_liq # [m^3]
    V_ad = V_liq + V_gas # [m^3]

    return {
        'q_in': q_in,
        'q_in1': q_in1,
        'q_in2': q_in2,
        'q_ad': q_ad,
        'q_out': q_out,
        'q_r': q_r,
        'VS_in': VS_in,
        'HRT': HRT,
        'V_liq': V_liq,
        'V_gas': V_gas,
        'V_ad': V_ad,
        'OLR': OLR,
        'density': density,
        'mixing_ratio': mixing_ratio
    }




# --- Influent scenario function ---
def get_influent(mixing_ratio):
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

    # Feed1 input
    X_xc1_in = mixing_ratio*0 #kg COD.m^-3
    X_ch1_in = mixing_ratio*20.057 #kg COD.m^-3
    X_pr1_in = mixing_ratio*12.674 #kg COD.m^-3
    X_li1_in = mixing_ratio*9.997 #kg COD.m^-3

    # Feed2 input
    variation_factor4 = 1
    X_xc2_total = variation_factor4*259.992
    X_ch2_fraction = 0.79
    X_pr2_fraction = 0.184
    X_li2_fraction = 0.026

    X_xc2_in = (1-mixing_ratio)*0 #kg COD.m^-3
    X_ch2_in = (1-mixing_ratio)*X_ch2_fraction*X_xc2_total      #kg COD.m^-3
    X_pr2_in = (1-mixing_ratio)*X_pr2_fraction*X_xc2_total  #kg COD.m^-3
    X_li2_in = (1-mixing_ratio)*X_li2_fraction*X_xc2_total  #kg COD.m^-3

    # Other variables
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

    return {
        'S_su_in': S_su_in,
        'S_aa_in': S_aa_in,
        'S_fa_in': S_fa_in,
        'S_va_in': S_va_in,
        'S_bu_in': S_bu_in,
        'S_pro_in': S_pro_in,
        'S_ac_in': S_ac_in,
        'S_h2_in': S_h2_in,
        'S_ch4_in': S_ch4_in,
        'S_IC_in': S_IC_in,
        'S_IN_in': S_IN_in,
        'S_I_in': S_I_in,
        'X_xc1_in': X_xc1_in,
        'X_ch1_in': X_ch1_in,
        'X_pr1_in': X_pr1_in,
        'X_li1_in': X_li1_in,
        'X_xc2_in': X_xc2_in,
        'X_ch2_in': X_ch2_in,
        'X_pr2_in': X_pr2_in,
        'X_li2_in': X_li2_in,
        'X_su_in': X_su_in,
        'X_aa_in': X_aa_in,
        'X_fa_in': X_fa_in,
        'X_c4_in': X_c4_in,
        'X_pro_in': X_pro_in,
        'X_ac_in': X_ac_in,
        'X_h2_in': X_h2_in,
        'X_I_in': X_I_in,
        'S_cation_in': S_cation_in,
        'S_anion_in': S_anion_in
    }
