import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate
#from adm1.ode import ADM1_ODE
import scipy
# Import custom plotting functions
from adm1 import params
from adm1_params import S_gas_h2
from plot_utils import plot_biomass_and_substrate, plot_gas_and_inhibition, plot_ph
from adm1.influent import reactor_setup
from adm1.influent import get_influent
from adm1.initial_state import get_initial_state
from adm1.params import PARAMETER_SETS, set_global_params_from_dict
from adm1.params import get_adm1_params
#from adm1.params import *
from adm1.dae import DAESolve  # pure DAE solver
from adm1.solver import simulate
from adm1.params import get_VSS 


def ADM1_coAD(
    q_ad_init=500,              # Initial influent flow rate [m^3/d]
    density=1,               # Influent density [tonne/m^3]
    VS_per_TS=0.9,            # Volatile solids per  total solids [kg VS/kg TS]     
    TS_fraction=0.03,        # Fraction of TS in influent
    mixing_ratio=0.99999,       # Fraction for feed 1 / total (can be overridden per scenario)
    OLR=5,                      # Organic Loading Rate [kg VS/m3/d]
    T_ad =  308.15, #K
    T_base =  298.15, #K
    T_op =  308.15, #k ##T_ad #=35 C
    influent=None,              # Optional: pass custom influent dict
    initials=None,              # Optional: pass custom initial state dict
    recycle_ratio=0.2               
):


    if influent is None:
        influent = get_influent(mixing_ratio)
    else:
        influent = influent
    S_su_in = influent['S_su_in']
    S_aa_in = influent['S_aa_in']
    S_fa_in = influent['S_fa_in']
    S_va_in = influent['S_va_in']
    S_bu_in = influent['S_bu_in']
    S_pro_in = influent['S_pro_in']
    S_ac_in = influent['S_ac_in']
    S_h2_in = influent['S_h2_in']
    S_ch4_in = influent['S_ch4_in']
    S_IC_in = influent['S_IC_in']
    S_IN_in = influent['S_IN_in']
    S_I_in = influent['S_I_in']
    X_xc1_in = influent['X_xc1_in']
    X_ch1_in = influent['X_ch1_in']
    X_pr1_in = influent['X_pr1_in']
    X_li1_in = influent['X_li1_in']
    X_xc2_in = influent['X_xc2_in']
    X_ch2_in = influent['X_ch2_in']
    X_pr2_in = influent['X_pr2_in']
    X_li2_in = influent['X_li2_in']
    X_su_in = influent['X_su_in']
    X_aa_in = influent['X_aa_in']
    X_fa_in = influent['X_fa_in']
    X_c4_in = influent['X_c4_in']
    X_pro_in = influent['X_pro_in']
    X_ac_in = influent['X_ac_in']
    X_h2_in = influent['X_h2_in']
    X_I_in = influent['X_I_in']
    S_cation_in = influent['S_cation_in']
    S_anion_in = influent['S_anion_in']

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

    #print("\nState Input Values:")
    #for label, value in zip(input_labels, state_input):
    #    print(f"{label}: {value}")

    # Initial state
    if initials is None:
        initial_state = get_initial_state(mixing_ratio)
    else:
        initial_state = initials

    S_su=initial_state['S_su']
    S_aa=initial_state['S_aa']
    S_fa=initial_state['S_fa']
    S_va=initial_state['S_va']
    S_bu=initial_state['S_bu']
    S_pro=initial_state['S_pro']
    S_ac=initial_state['S_ac']
    S_h2=initial_state['S_h2']
    S_ch4=initial_state['S_ch4']
    S_IC=initial_state['S_IC']
    S_IN=initial_state['S_IN']
    S_I=initial_state['S_I']
    X_xc1=initial_state['X_xc1']
    X_ch1=initial_state['X_ch1']
    X_pr1=initial_state['X_pr1']
    X_li1=initial_state['X_li1']
    X_xc2=initial_state['X_xc2']
    X_ch2=initial_state['X_ch2']
    X_pr2=initial_state['X_pr2']
    X_li2=initial_state['X_li2']
    X_su=initial_state['X_su']
    X_aa=initial_state['X_aa']
    X_fa=initial_state['X_fa']
    X_c4=initial_state['X_c4']
    X_pro=initial_state['X_pro']
    X_ac=initial_state['X_ac']
    X_h2=initial_state['X_h2']
    X_I=initial_state['X_I']
    S_cation=initial_state['S_cation']
    S_anion=initial_state['S_anion']
    pH=initial_state['pH']
    S_H_ion=initial_state['S_H_ion']
    S_va_ion=initial_state['S_va_ion']
    S_bu_ion=initial_state['S_bu_ion']
    S_pro_ion=initial_state['S_pro_ion']
    S_ac_ion=initial_state['S_ac_ion']
    S_hco3_ion=initial_state['S_hco3_ion']
    S_nh3=initial_state['S_nh3']
    S_nh4_ion=initial_state['S_nh4_ion']
    S_co2=initial_state['S_co2']
    S_gas_h2=initial_state['S_gas_h2']
    S_gas_ch4=initial_state['S_gas_ch4']
    S_gas_co2=initial_state['S_gas_co2']

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

    reactor = reactor_setup(
    influent,               # Influent scenario function
    initial_state,          # Initial state scenario function
    q_ad_init,                # Initial influent flow rate [m^3/d]
    density,                    # Influent density [tonne/m^3]
    VS_per_TS,                # Volatile solids per  total solids [kg VS/kg TS]    
    TS_fraction,         # Fraction of water in influent
    mixing_ratio,   # Fraction for feed 1 # feed1 / total (can be overridden per scenario)
    OLR,                        # Organic Loading Rate [kg VS/m3/d]
    recycle_ratio                # Recycle ratio [m^3/d]
    )
    # --- Set up reactor for this scenario ---

    q_in = reactor['q_in']
    q_in1 = reactor['q_in1']
    q_in2 = reactor['q_in2']
    q_ad = reactor['q_ad']
    q_out = reactor['q_out']
    q_r = reactor['q_r']
    VS_in = reactor['VS_in']
    HRT = reactor['HRT']
    V_liq = reactor['V_liq']
    V_gas = reactor['V_gas']
    V_ad = reactor['V_ad']

    # --- End  Reactor Setup ---

    # Printing state_zero
    #print("State Zero Values:")
    #or label, value in zip(state_labels, state_zero):
    #    print(f"{label}: {value}")

    
    S_nh4_ion =  (S_IN - S_nh3)

    S_co2 =  (S_IC - S_hco3_ion)

    #pH equation

    ######################

    # Physical parameter values

    t0=0
    n=0



    # Choose scenario: 'mesophilic_high_rate', 'mesophilic_solids', or 'thermophilic_solids'
    params2 = PARAMETER_SETS["mesophilic_solids"]
    set_global_params_from_dict(params2)
    params=get_adm1_params(T_ad, T_base, params2, mixing_ratio)

    params.update({
        'q_in': reactor['q_in'],
        'q_in1': reactor['q_in1'],
        'q_in2': reactor['q_in2'],
        'q_ad': reactor['q_ad'],
        'q_out': reactor['q_out'],
        'q_r': reactor['q_r'],
        'VS_in': reactor['VS_in'],
        'HRT': reactor['HRT'],
        'V_liq': reactor['V_liq'],
        'V_gas': reactor['V_gas'],
        'V_ad': reactor['V_ad'],
        'OLR': reactor['OLR'],
        'density': reactor['density'],
        'mixing_ratio': reactor['mixing_ratio']
    })

    for k, v in params.items():
        globals()[k] = v

    




    # Initiate the cache data frame for storing simulation results
    simulate_results = pd.DataFrame([state_zero])
    columns = ["S_su", "S_aa", "S_fa", "S_va", "S_bu", "S_pro", "S_ac", "S_h2", "S_ch4", "S_IC", "S_IN", "S_I", "X_xc1", "X_ch1", "X_pr1", "X_li1", "X_xc2", "X_ch2", "X_pr2", "X_li2", "X_su", "X_aa", "X_fa", "X_c4", "X_pro", "X_ac", "X_h2", "X_I", "S_cation", "S_anion", "pH", "S_va_ion", "S_bu_ion", "S_pro_ion", "S_ac_ion", "S_hco3_ion", "S_co2", "S_nh3", "S_nh4_ion", "S_gas_h2", "S_gas_ch4", "S_gas_co2"]
    simulate_results.columns = columns

    # Initiate cache data frame for storing gasflow values
    initflow = {'p_gas_h2': [0],'p_gas_ch4': [0],'p_gas_co2': [0],'p_gas': [0],'q_gas': [0], 'q_ch4': [0], 'total_ch4': [0],'p_gas_ch4/p_gas': [0],'p_gas_co2/p_gas': [0], 'ch4_yield':[0], 'co2_yield':[0] }
    gasflow = pd.DataFrame(initflow)
    total_ch4 = 0

    # Initiate cache data frame for storing inhibition values
    initflow = {'I_5': [0],'I_7': [0],'I_8': [0],'I_10': [0],'I_12': [0],'I_pH_aa': [0],'I_pH_h2': [0],'I_IN_lim': [0],'I_h2_fa': [0],'I_h2_c4': [0], 'I_h2_pro': [0]}
    inhibition = pd.DataFrame(initflow)

    # Initiate cache data frame for storing ions values
    initflow = {'S_cation': [0],'S_anion': [0],'S_H_ion': [0],'S_va_ion': [0],'S_bu_ion': [0],'S_pro_ion': [0],'S_ac_ion': [0],'S_hco3_ion': [0],'S_nh4_ion': [0]}
    ions = pd.DataFrame(initflow)

    ##############################
    ##time definition
    days = 50
    timeSteps = days*24 #every 15 minutes 
    t = np.linspace(0, days, timeSteps) #sequence of timesteps as fractions of days



    solvermethod = 'DOP853'
    # solvermethod = 'BDF'

    # --- Recycle stream integration ---
    # Initialize effluent_state for recycling (use initial state for first step)
 

    for u in t[1:]:
        n += 1

        effluent_state = {
        'S_su_in': S_su, 'S_aa_in': S_aa, 'S_fa_in': S_fa, 'S_va_in': S_va, 'S_bu_in': S_bu, 'S_pro_in': S_pro,
        'S_ac_in': S_ac, 'S_h2_in': S_h2, 'S_ch4_in': S_ch4, 'S_IC_in': S_IC, 'S_IN_in': S_IN, 'S_I_in': S_I,
        'X_xc1_in': X_xc1, 'X_ch1_in': X_ch1, 'X_pr1_in': X_pr1, 'X_li1_in': X_li1, 'X_xc2_in': X_xc2,
        'X_ch2_in': X_ch2, 'X_pr2_in': X_pr2, 'X_li2_in': X_li2, 'X_su_in': X_su, 'X_aa_in': X_aa,
        'X_fa_in': X_fa, 'X_c4_in': X_c4, 'X_pro_in': X_pro, 'X_ac_in': X_ac, 'X_h2_in': X_h2,
        'X_I_in': X_I, 'S_cation_in': S_cation, 'S_anion_in': S_anion
        }
        # Mix recycled effluent with fresh influent
        mixed_influent = {}
        for key in effluent_state:
            mixed_influent[key] = recycle_ratio * effluent_state[key] + (1 - recycle_ratio) * influent[key] if influent and key in influent else effluent_state[key]

        # Update state_input for this time step
        state_input = [mixed_influent['S_su_in'], mixed_influent['S_aa_in'], mixed_influent['S_fa_in'], mixed_influent['S_va_in'], mixed_influent['S_bu_in'], mixed_influent['S_pro_in'], 
                    mixed_influent['S_ac_in'], mixed_influent['S_h2_in'], mixed_influent['S_ch4_in'], mixed_influent['S_IC_in'], mixed_influent['S_IN_in'], mixed_influent['S_I_in'],
                    mixed_influent['X_xc1_in'], mixed_influent['X_ch1_in'], mixed_influent['X_pr1_in'], mixed_influent['X_li1_in'], mixed_influent['X_xc2_in'], 
                    mixed_influent['X_ch2_in'], mixed_influent['X_pr2_in'], mixed_influent['X_li2_in'], mixed_influent['X_su_in'], mixed_influent['X_aa_in'], 
                    mixed_influent['X_fa_in'], mixed_influent['X_c4_in'], mixed_influent['X_pro_in'], mixed_influent['X_ac_in'], mixed_influent['X_h2_in'], 
                    mixed_influent['X_I_in'], mixed_influent['S_cation_in'], mixed_influent['S_anion_in']]

        # Span for next time step
        tstep = [t0, u]

        # ...existing simulation code...
        # After simulation step, update effluent_state with new effluent values (from output)
        # effluent_state = ... (update with output from simulation)

        # Build current state vector (y0)
        current_state = [S_su, S_aa, S_fa, S_va, S_bu, S_pro, S_ac, S_h2, S_ch4, S_IC, S_IN, S_I,
                        X_xc1, X_ch1, X_pr1, X_li1, X_xc2, X_ch2, X_pr2, X_li2,
                        X_su, X_aa, X_fa, X_c4, X_pro, X_ac, X_h2, X_I, S_cation, S_anion,
                        S_H_ion, S_va_ion, S_bu_ion, S_pro_ion, S_ac_ion, S_hco3_ion, S_co2, S_nh3, S_nh4_ion,
                        S_gas_h2, S_gas_ch4, S_gas_co2]

        # ODE integration
        sim = simulate(tstep, current_state, state_input, solvermethod,params)

        # Unpack solution arrays
        (sim_S_su, sim_S_aa, sim_S_fa, sim_S_va, sim_S_bu, sim_S_pro, sim_S_ac, sim_S_h2, sim_S_ch4, sim_S_IC, sim_S_IN, sim_S_I,
        sim_X_xc1, sim_X_ch1, sim_X_pr1, sim_X_li1, sim_X_xc2, sim_X_ch2, sim_X_pr2, sim_X_li2,
        sim_X_su, sim_X_aa, sim_X_fa, sim_X_c4, sim_X_pro, sim_X_ac, sim_X_h2, sim_X_I, sim_S_cation, sim_S_anion,
        sim_S_H_ion, sim_S_va_ion, sim_S_bu_ion, sim_S_pro_ion, sim_S_ac_ion, sim_S_hco3_ion, sim_S_co2, sim_S_nh3, sim_S_nh4_ion,
        sim_S_gas_h2, sim_S_gas_ch4, sim_S_gas_co2) = sim

        # Take last values
        S_su, S_aa, S_fa, S_va, S_bu, S_pro, S_ac, S_h2, S_ch4, S_IC, S_IN, S_I, \
        X_xc1, X_ch1, X_pr1, X_li1, X_xc2, X_ch2, X_pr2, X_li2, \
        X_su, X_aa, X_fa, X_c4, X_pro, X_ac, X_h2, X_I, S_cation, S_anion, \
        S_H_ion, S_va_ion, S_bu_ion, S_pro_ion, S_ac_ion, S_hco3_ion, S_co2, S_nh3, S_nh4_ion, \
        S_gas_h2, S_gas_ch4, S_gas_co2 = \
            sim_S_su[-1], sim_S_aa[-1], sim_S_fa[-1], sim_S_va[-1], sim_S_bu[-1], sim_S_pro[-1], sim_S_ac[-1], sim_S_h2[-1], sim_S_ch4[-1], sim_S_IC[-1], sim_S_IN[-1], sim_S_I[-1], \
            sim_X_xc1[-1], sim_X_ch1[-1], sim_X_pr1[-1], sim_X_li1[-1], sim_X_xc2[-1], sim_X_ch2[-1], sim_X_pr2[-1], sim_X_li2[-1], \
            sim_X_su[-1], sim_X_aa[-1], sim_X_fa[-1], sim_X_c4[-1], sim_X_pro[-1], sim_X_ac[-1], sim_X_h2[-1], sim_X_I[-1], sim_S_cation[-1], sim_S_anion[-1], \
            sim_S_H_ion[-1], sim_S_va_ion[-1], sim_S_bu_ion[-1], sim_S_pro_ion[-1], sim_S_ac_ion[-1], sim_S_hco3_ion[-1], sim_S_co2[-1], sim_S_nh3[-1], sim_S_nh4_ion[-1], \
            sim_S_gas_h2[-1], sim_S_gas_ch4[-1], sim_S_gas_co2[-1]

        # Algebraic update (pure DAE) - pass state, receive corrected state & pH
        state_for_dae = [S_su, S_aa, S_fa, S_va, S_bu, S_pro, S_ac, S_h2, S_ch4, S_IC, S_IN, S_I,
                        X_xc1, X_ch1, X_pr1, X_li1, X_xc2, X_ch2, X_pr2, X_li2,
                        X_su, X_aa, X_fa, X_c4, X_pro, X_ac, X_h2, X_I, S_cation, S_anion,
                        S_H_ion, S_va_ion, S_bu_ion, S_pro_ion, S_ac_ion, S_hco3_ion, S_co2, S_nh3, S_nh4_ion,
                        S_gas_h2, S_gas_ch4, S_gas_co2]
        
        
        new_state, pH_value = DAESolve(state_for_dae,state_input,params)

        # Overwrite updated components from new_state (others unchanged)
        S_h2 = new_state[7]
        S_H_ion = new_state[30]
        S_va_ion = new_state[31]
        S_bu_ion = new_state[32]
        S_pro_ion = new_state[33]
        S_ac_ion = new_state[34]
        S_hco3_ion = new_state[35]
        S_co2 = new_state[36]
        S_nh3 = new_state[37]
        S_nh4_ion = new_state[38]
        # pH_value available if needed for direct storage/inhibition calcs

        prevS_H_ion = S_H_ion

        I_pH_aa =  ((K_pH_aa ** nn_aa) / (S_H_ion ** nn_aa + K_pH_aa ** nn_aa))
        I_pH_ac =  ((K_pH_ac ** n_ac) / (S_H_ion ** n_ac + K_pH_ac ** n_ac))
        I_pH_h2 =  ((K_pH_h2 ** n_h2) / (S_H_ion ** n_h2 + K_pH_h2 ** n_h2))
        I_IN_lim =  (1 / (1 + (K_S_IN / S_IN)))
        I_h2_fa =  (1 / (1 + (S_h2 / K_I_h2_fa)))
        I_h2_c4 =  (1 / (1 + (S_h2 / K_I_h2_c4)))
        I_h2_pro =  (1 / (1 + (S_h2 / K_I_h2_pro)))
        I_nh3 =  (1 / (1 + (S_nh3 / K_I_nh3)))

        I_5 = I_pH_aa * I_IN_lim
        I_6 = I_5
        I_7 = I_pH_aa * I_IN_lim * I_h2_fa
        I_8 = I_pH_aa * I_IN_lim * I_h2_c4
        I_9 = I_8
        I_10 = I_pH_aa * I_IN_lim * I_h2_pro
        I_12 = I_pH_h2 * I_IN_lim

        inhibittemp = {'I_5': I_5,'I_7': I_7,'I_8': I_8,'I_10': I_10,'I_12': I_12, 'I_pH_aa': I_pH_aa,'I_pH_ac': I_pH_ac,'I_pH_h2': I_pH_h2, 'I_IN_lim': I_IN_lim,'I_h2_fa': I_h2_fa,'I_h2_c4': I_h2_c4,'I_h2_pro': I_h2_pro,'I_nh3': I_nh3}
        inhibition = pd.concat([inhibition, pd.DataFrame([inhibittemp])], ignore_index=True)

        ################

        S_nh4_ion =  (S_IN - S_nh3)
        S_co2 =  (S_IC - S_hco3_ion)
        #pH = - np.log10(S_H_ion)

        # Algebraic equations 

        p_gas_h2 =  (S_gas_h2 * R * T_op / 16)
        p_gas_ch4 =  (S_gas_ch4 * R * T_op / 64)
        p_gas_co2 =  (S_gas_co2 * R * T_op)
        
        Rho_T_8 =  (k_L_a * (S_h2 - 16 * K_H_h2 * p_gas_h2))
        Rho_T_9 =  (k_L_a * (S_ch4 - 64 * K_H_ch4 * p_gas_ch4))
        Rho_T_10 =  (k_L_a * (S_co2 - K_H_co2 * p_gas_co2))
        
        p_gas=  (p_gas_h2 + p_gas_ch4 + p_gas_co2 + p_gas_h2o)
        q_gas =  (k_p * (p_gas- p_atm))
        
        #q_gas= (R*T_op/(p_atm-p_gas_h2o))*V_liq*(Rho_T_8/16+Rho_T_9/64+Rho_T_10)
        
        if q_gas < 0:    
            q_gas = 0
        
        q_ch4 = q_gas * (p_gas_ch4/p_gas) # methane flow
        q_co2 = q_gas * (p_gas_co2/p_gas) # co2 flow
        q_h2 = q_gas * (p_gas_h2/p_gas) # h2 flow

        if q_ch4 < 0:
            q_ch4 = 0

        total_ch4 = total_ch4 + q_ch4 

        flowtemp = {'p_gas_h2': p_gas_h2,'p_gas_ch4': p_gas_ch4,'p_gas_co2': p_gas_co2,'p_gas': p_gas,'q_gas': q_gas, 'q_ch4': q_ch4, 'total_ch4': total_ch4, 'p_gas_ch4/p_gas': p_gas_ch4/p_gas,'p_gas_co2/p_gas': p_gas_co2/p_gas, 'ch4_yield':q_ch4/VS_in, 'co2_yield':q_co2/VS_in, 'h2_yield':q_h2/VS_in}
        gasflow = pd.concat([gasflow, pd.DataFrame([flowtemp])], ignore_index=True)

        total_ch4 = total_ch4 + q_ch4     
        
        ############
        
        ionstemp = {'S_cation': S_cation,'S_anion': S_anion,'S_H_ion': S_H_ion,'S_va_ion': S_va_ion,'S_bu_ion': S_bu_ion,'S_pro_ion': S_pro_ion,'S_ac_ion': S_ac_ion,'S_hco3_ion': S_hco3_ion,'S_nh4_ion': S_nh4_ion}
        ions = pd.concat([ions, pd.DataFrame([ionstemp])], ignore_index=True)

        ##############

        # Rebuild and append state (store pH later)
        state_zero = [S_su, S_aa, S_fa, S_va, S_bu, S_pro, S_ac, S_h2, S_ch4, S_IC, S_IN, S_I, \
                    X_xc1, X_ch1, X_pr1, X_li1, X_xc2, X_ch2, X_pr2, X_li2, \
                    X_su, X_aa, X_fa, X_c4, X_pro, X_ac, X_h2, X_I, S_cation, S_anion, \
                    S_H_ion, S_va_ion, S_bu_ion, S_pro_ion, S_ac_ion, S_hco3_ion, S_co2, S_nh3, S_nh4_ion, \
                    S_gas_h2, S_gas_ch4, S_gas_co2]

        dfstate_zero = pd.DataFrame([state_zero], columns=columns)
        simulate_results = pd.concat([simulate_results, dfstate_zero], ignore_index=True)
        t0 = u

    p_gas_h2 =  (S_gas_h2 * R * T_op / 16)
    p_gas_ch4 =  (S_gas_ch4 * R * T_op / 64)
    p_gas_co2 =  (S_gas_co2 * R * T_op)
    Rho_T_8 =  (k_L_a * (S_h2 - 16 * K_H_h2 * p_gas_h2))
    Rho_T_9 =  (k_L_a * (S_ch4 - 64 * K_H_ch4 * p_gas_ch4))
    Rho_T_10 =  (k_L_a * (S_co2 - K_H_co2 * p_gas_co2))
        
    p_gas=  (p_gas_h2 + p_gas_ch4 + p_gas_co2 + p_gas_h2o)
    q_gas =  (k_p * (p_gas- p_atm))

    #q_gas= (R*T_op/(p_atm-p_gas_h2o))*V_liq*(Rho_T_8/16+Rho_T_9/64+Rho_T_10)

    if q_gas < 0:    
        q_gas = 0

    q_ch4 = q_gas * (p_gas_ch4/p_gas) # methane flow
    if q_ch4 < 0:
        q_ch4 = 0
  
    phlogarray = -1 * np.log10(simulate_results['pH'])
    simulate_results['pH'] = phlogarray
    



    return {
        "simulate_results": simulate_results,
        "S_su": S_su,
        "S_aa": S_aa,
        "S_fa": S_fa,
        "S_va": S_va,
        "S_bu": S_bu,
        "S_pro": S_pro,
        "S_ac": S_ac,
        "S_h2": S_h2,
        "S_ch4": S_ch4,
        "S_IC": S_IC,
        "S_IN": S_IN,
        "S_I": S_I,
        "X_xc1": X_xc1,
        "X_ch1": X_ch1,
        "X_pr1": X_pr1,
        "X_li1": X_li1,
        "X_xc2": X_xc2,
        "X_ch2": X_ch2,
        "X_pr2": X_pr2,
        "X_li2": X_li2,
        "X_su": X_su,
        "X_aa": X_aa,
        "X_fa": X_fa,
        "X_c4": X_c4,
        "X_pro": X_pro,
        "X_ac": X_ac,
        "X_h2": X_h2,
        "X_I": X_I,
        "S_cation": S_cation,
        "S_anion": S_anion,
        "S_H_ion": S_H_ion,
        "S_va_ion": S_va_ion,
        "S_bu_ion": S_bu_ion,
        "S_pro_ion": S_pro_ion,
        "S_ac_ion": S_ac_ion,
        "S_hco3_ion": S_hco3_ion,
        "S_co2": S_co2,
        "S_nh3": S_nh3,
        "S_nh4_ion": S_nh4_ion,
        "S_gas_h2": S_gas_h2,
        "S_gas_ch4": S_gas_ch4,
        "S_gas_co2": S_gas_co2,
        "p_gas_h2": p_gas_h2,
        "p_gas_ch4": p_gas_ch4,
        "p_gas_co2": p_gas_co2,
        "p_gas": p_gas,
        "q_gas": q_gas,
        "q_ch4": q_ch4,
        "biomethane_yield": q_ch4 / VS_in,
        "biomethane_yield2": q_ch4 / V_ad,
        "q_in": q_in,
        "q_out": q_out,
        "q_recycle": q_r,
        "HRT": HRT
    }
