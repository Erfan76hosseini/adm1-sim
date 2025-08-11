# adm1/solver.py
# Place your simulation runner here



from scipy.integrate import solve_ivp



from adm1.ode import ADM1_ODE
from adm1.params import state_input, state_zero


def simulate(t_step, y0, state_input, solvermethod):
    def ode_func(t, y):
        return ADM1_ODE(t, y, state_input)
    r = solve_ivp(ode_func, t_step, y0, method=solvermethod)
    return r.y