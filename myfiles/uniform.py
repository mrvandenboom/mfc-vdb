#!/usr/bin/env python3

import json
import math

import numpy as np

#===============================================================================
# Example for subsonic viscous flow over a cylinder
#===============================================================================

# Set Inlet Mach, Calculate rest based on Inlet Conditions
Ma = 0.1                        # Mach Number                 
Re = 300

m = 450
n = 300
m = 300
n = 200


# ===========================================================================
# ===========================================================================
# ====================== USER CONFIGURABLE VALUES ===========================
# ===========================================================================
# ===========================================================================
# Fluid Properties
Mu    = 1.84e-05                   # Dynamic Viscosity (kg/(m·s))
gam_a = 1.4                     # Specific Heat Ratio         
Rgas  = 287.05                      # Specific gas constant for air (J/(kg·K))

P0 = 101325                   # Outlet Pressure (Pa)             
T0 = 300                      # Outlet Temperature (K)       
rho0 = P0 / (Rgas * T0)

c0 = np.sqrt(gam_a * P0 / rho0)

#Ma = 0.2
#U1 = Ma * c0
#print(U1)

T_2 = 300
P_2 = 101325
T0_T = (1 + (gam_a - 1) / 2 * Ma**2) # Stagnation to Static Temp Ratio 
P0_P = (T0_T)**(gam_a/(gam_a - 1))   # Stagnation to Static Pressure Ratio
T_1 = T0_T * T_2                     # Inlet Temperature (K)   
P_1 = P0_P * P_2                     # Inlet Pressure (Pa)     
rho_1 = P_1 / (Rgas * T_1)              # Inlet Density (kg/m^3)  
#print(T0_T,P0_P,rho_1/rho0)

#c = math.sqrt(gam_a * P_1 / rho_1)   # Speed of sound (m/s) for ideal gas 
#U_1 = Ma * c                         # Inlet Velocity (m/s)    
#Re = 300
#dp0 = Re * Ma / (rho_1 * U_1)
#print(U_1)
#print(dp0)


c = math.sqrt(gam_a * P_1 / rho_1)   # Speed of sound (m/s) for ideal gas 
U_1 = Ma * c                         # Inlet Velocity (m/s)    

dp0 = Re * Ma / (rho_1 * U_1)
rp = dp0 / 2
#print(dp0)
#exit()

A = dp0
norm = 0.5*rho_1*U_1**2*A
tau = 2*rp / U_1

t_stop = 5*tau
t_save = t_stop / 12


# COMPUTATIONAL GEOMETRY ====================================================
L_xbeg = -10*dp0
L_xend =  20*dp0
L_ybeg = -10*dp0
L_yend =  10*dp0

x_len = L_xend - L_xbeg        # Domain length in x (meters)
y_len = L_yend - L_ybeg        # Domain length in y (meters)

dx = x_len / (m+1)            # Grid resolution in x (meters)
dy = y_len / (n+1)            # Grid resolution in y (meters)

grid_res_x = int(dp0/dx)
grid_res_y = int(dp0/dy)


"""
gam = gam_a
Ma0 = Ma
c0 = math.sqrt(gam)
u0 = Ma0 * c0

cfl = 0.5
T = 1.0 / Ma0
dt = cfl * dx / (u0 + c0) / 10.
Ntfinal = int(T / dt)
Ntstart = 0
Nfiles = 12
t_save = int(math.ceil((Ntfinal - 0) / float(Nfiles)))
Nt = t_save * Nfiles
t_step_start = Ntstart
t_step_stop = int(Nt)
"""

# Make nondimensional using dp0 as length scale
dp0 = 16.0e-6 # 16 micron diameter particle
dp0 = 0.08
L_xbeg = -20
L_xend =  40
L_ybeg = -15
L_yend =  15
x_len = L_xend - L_xbeg        # Domain length in x (meters)
y_len = L_yend - L_ybeg        # Domain length in y (meters)
dx = x_len / (m+1)            # Grid resolution in x (meters)
dy = y_len / (n+1)            # Grid resolution in y (meters)
grid_res_x = int(1/dx)
grid_res_y = int(1/dy)

Mu    = 1.84e-05                   # Dynamic Viscosity (kg/(m·s))
gam_a = 1.4                     # Specific Heat Ratio         
Rgas  = 287.05                      # Specific gas constant for air (J/(kg·K))

P0 = 101325
T0 = 300
rho0 = P0 / (Rgas * T0)
c0 = np.sqrt(gam_a * P0 / rho0)

T0_T = (1 + (gam_a - 1) / 2 * Ma**2) # Stagnation to Static Temp Ratio 
P0_P = (T0_T)**(gam_a/(gam_a - 1))   # Stagnation to Static Pressure Ratio
T1 = T0_T * T0                       # Inlet Temperature (K)   
P1 = P0_P * P0                       # Inlet Pressure (Pa)     
rho1 = P1 / (Rgas * T1)              # Inlet Density (kg/m^3)  

Re = 20
U1 = Mu * Re / (rho0 * dp0)
Ma = U1 / c0
rho1 = (Ma**2)*P1 / (Rgas * T1)              # Inlet Density (kg/m^3)  

Ma = 0.1
U0 = Ma / c0
Mu = rho0*dp0*U0/Re
#print(rho0,c0,U0,Ma,Mu,dp0)
#print(rho1,T1,P1,U1,Mu,dp0)
#exit()

# Now scale by P0, rho0, U0
#Pscale = P0
#rscale = rho0
#uscale = np.sqrt(P0/rho0)
#uscale = U0
#c1 = c0 / uscale
#P_1 = P0 / Pscale
#rho_1 = rho0 / rscale
#U_1 = U0 / uscale
#print(U_1)

#T = 1 / Ma
#cfl = 0.4
#dt = cfl * dx / (U_1+c1)
#print(t_stop)
#t_stop = int(T / dt)

#A = 1
#norm = 0.5*rho_1*U_1**2*A
#tau = 1 / U_1
#print(norm, tau)
#exit()

# Redo
ga = 1.4
#Re = 20.0
#Ma = 0.1
#p0 = 101325
#dp0 = 16.0e-6
#rho0 = 1
#c0 = np.sqrt(ga * p0 / rho0)
##V0 = Ma * c0
##Mu = V0 * dp0 * rho0 / Re
#V0 = Mu * Re / (dp0 * rho0)

Re = 40
dp0 = 80.e-6
P0 = 101325
T0 = 300
#rho0 = ga*P0/((ga-1)*T0)
rho0 = P0 / (Rgas * T0)
rho0 = 1
c0 = np.sqrt(1.4*P0/rho0)
#V0 = 40.0
#Mu = rho0 * V0 * dp0 / Re

#Mu    = 1.84e-05                   # Dynamic Viscosity (kg/(m·s))
Mu = 1.7160E-5   # Value used in ppiclf, kg/m-s
V0 = Mu * Re / (rho0 * dp0)

Ma = V0 / c0

A = dp0
norm = 0.5*rho0*V0**2*A
tau = dp0 / (V0 + c0)
tau_v = Re * dp0 / U0
tau_adv = dp0 / U0


Lscale = dp0
pscale = P0
rhoscale = rho0
Uscale = np.sqrt(P0/rho0)
tscale = Lscale / Uscale

dp0 = dp0 / Lscale
P0 = P0 / pscale
rho0 = rho0 / rhoscale
V0 = V0 / Uscale
tau = tau / tscale
Mu = 1.0/Re
Area = 1
norm = 0.5*rho0*V0**2*Area


m = 400
n = 300
L_xbeg = -10*dp0
L_xend =  20*dp0
L_ybeg = -10*dp0
L_yend =  10*dp0
x_len = L_xend - L_xbeg        # Domain length in x (meters)
y_len = L_yend - L_ybeg        # Domain length in y (meters)
dx = x_len / (m+1)            # Grid resolution in x (meters)
dy = y_len / (n+1)            # Grid resolution in y (meters)
grid_res_x = int(dp0/dx)
grid_res_y = int(dp0/dy)

t_stop = 120*tau

# set values used below in code
P_1 = P0
rho_1 = rho0
U_1 = V0
#print(c0,V0,Mu)
#print(norm,tau,t_stop)
#exit()




# ============================================================================
# CONFIGURING CASE DICTIONARY ================================================
output = {
            # DEFINE OUTPUT PARAMETERS AND FORMATTING ========================
            "run_time_info"                          : "T", 
            "format"                                 : 1,   
            "precision"                              : 2,   
            "prim_vars_wrt"                          : "T", 
            "E_wrt"                                  : "T", 
            "parallel_io"                            : "F", 
            #"schlieren_wrt"                          : "T", 
            "fd_order"                               : 4,   
            #"schlieren_alpha(1)"                     : 20,   
            #"schlieren_alpha(2)"                     : 20,   
            #"schlieren_alpha(3)"                     : 10,   
            # ================================================================

            # COMPUTATIONAL DOMAIN PARAMETERS ================================
            "x_domain%beg"                           : L_xbeg,
            "x_domain%end"                           : L_xend,
            # y direction
            "y_domain%beg"                           : L_ybeg,
            "y_domain%end"                           : L_yend,

            "m"                                      : m,
            "n"                                      : n,
            "p"                                      : 0,

            "cyl_coord"                              : "F",
            # ================================================================

            # TIME STEPPING PARAMETERS =======================================
            "cfl_adap_dt"                          : "T", 
            "cfl_target"                           : 0.5, 
            "n_start"                              : 0,   
            "t_stop"                               : t_stop,
            "t_save"                               : t_stop/12,
            #"dt": dt,
            #"t_step_start": t_step_start,
            #"t_step_stop": t_step_stop,
            #"t_step_save": t_save,
            # ================================================================

            # SIMULATION ALGORITHM PARAMETERS ================================
            # Only one patch is necessary for the background liquid
            #"num_patches"                            : 1, 
            #"model_eqns"                             : 2,
            #"num_fluids"                             : 1,
            #"time_stepper"                           : 3,
            #"weno_order"                             : 5,
            #"weno_eps"                               : 1.0e-16,
            ##"mapped_weno"                            : "T",
            #"wenoz"                                  : "T",
            #"riemann_solver"                         : 2,
            #"low_Mach"                               : 2,
            #"wave_speeds"                            : 1,
            #"avg_state"                              : 2,
            #"viscous"                                : "T",

            # Use the 5 equation model
            "num_patches"                            : 1, 
            "model_eqns"                             : 2,
            "alt_soundspeed"                         : "F",
            "num_fluids"                             : 1,
            "mpp_lim"                                : "F",
            "mixture_err"                            : "F",
            "time_stepper"                           : 3,
            "weno_order"                             : 5,
            "weno_eps"                               : 1.0e-16,
            "weno_avg"                               : "T",
            "weno_Re_flux"                           : "T",
            "avg_state"                              : 2,
            "mapped_weno"                            : "T",
            "null_weights"                           : "F",
            "mp_weno"                                : "T",
            "riemann_solver"                         : 2,
            "wave_speeds"                            : 1,
            "viscous"                                : "T",

            # Low Mach number
            # ================================================================

            # DEFINE FLUID DOMAIN ============================================
            "patch_icpp(1)%geometry"                 : 3,
            "patch_icpp(1)%x_centroid"               : (L_xbeg+L_xend)/2,
            "patch_icpp(1)%y_centroid"               : (L_ybeg+L_yend)/2,
            "patch_icpp(1)%length_x"                 : x_len,
            "patch_icpp(1)%length_y"                 : y_len,
            "patch_icpp(1)%vel(1)"                   : V0,
            "patch_icpp(1)%vel(2)"                   : 0.0e00,
            "patch_icpp(1)%pres"                     : P0,
            "patch_icpp(1)%alpha_rho(1)"             : rho0,
            "patch_icpp(1)%alpha(1)"                 : 1.0e00,
            # ================================================================

            # SET BOUNDARY CONDITIONS =========================================
            # CBC Left Face (Subsonic Inflow)
            "bc_x%beg"                               : -3,
            #"bc_x%beg"                               : -7,
            #"bc_x%grcbc_in": "T",
            #"bc_x%vel_in(1)": V0,
            #"bc_x%vel_in(2)": 0,
            #"bc_x%pres_in": P0,
            #"bc_x%alpha_rho_in(1)": rho0,
            #"bc_x%alpha_in(1)": 1,

            # # CBC Right Face (Subsonic Outflow)
            "bc_x%end"                               : -3,
            #"bc_x%end"                               : -8,
            #"bc_x%grcbc_out": "T",
            #"bc_x%pres_out": P_2,
            
            # Use periodic BCs on top/bottom and front/back
            "bc_y%beg"                               : -15,
            "bc_y%end"                               : -15,
            # ================================================================

            # SET INITIAL CONDITIONS IN THE DOMAIN ===========================
            # Use uniform freestream conditions

            # Fluids Physical Parameters
            "fluid_pp(1)%gamma"                      : 1 / (gam_a - 1),
            "fluid_pp(1)%pi_inf"                     : 0,
            "fluid_pp(1)%Re(1)"                      : 1 / Mu,
            # ================================================================

            # DEFINE IMMERSED BOUNDARY(IES) ==================================
            "ib"                                     : "T",
            "num_ibs"                                : 1,
            "patch_ib(1)%geometry"                   : 2,
            "patch_ib(1)%x_centroid"                 : 0.0,
            "patch_ib(1)%y_centroid"                 : 0.0,
            "patch_ib(1)%radius"                     : dp0 / 2,
            "patch_ib(1)%slip"                       : "F",

            # ================================================================            
}
# ===========================================================================
# ===========================================================================
# ===================== END USER CONFIGURABLE VALUES ========================
# ===========================================================================
# ===========================================================================


print(json.dumps(output, indent=4))
#with open("output_uniform.txt", "w", encoding="utf-8") as f:
#    json.dump(output,f, indent=4)
#    f.write("\n")


with open("info_case.txt", "w", encoding="utf-8") as f:
    f.write(f'{grid_res_x :< 30}{'# Grid resolution':<20} \n')
    f.write(f'{grid_res_y :< 30}{'# Grid resolution':<20} \n')
    f.write(f'{dx :< 30}{'# Grid delta-x':<20} \n')
    f.write(f'{dy :< 30}{'# Grid delta-y':<20} \n')
    f.write(f'{dp0 :<30}{'# Particle diameter':<20} \n')
    f.write(f'{Ma :<30}{'# Shock Mach number' :<20} \n')
    f.write(f'{norm :<30}{'# Norm' :<20} \n')
    f.write(f'{tau :<30}{'# tau' :<20} \n')
    f.write(f'{Re :<30}{'# Reynolds number' :<20} \n')
    f.write(f'{m+1 :<30}{'# Grid nx' :<20} \n')
    f.write(f'{n+1 :<30}{'# Grid ny' :<20} \n')
    f.write(f'{P_1 :<30}{'# Inlet pressure' :<20} \n')
    f.write(f'{rho_1 :<30}{'# Inlet density' :<20} \n')
    f.write(f'{U_1 :<30}{'# Inlet velocity' :<20} \n')
    f.write(f'{Mu :<30}{'# Shear viscosity' :<20} \n')
with open("output_uniform.txt", "w", encoding="utf-8") as f:
    f.write(f'Inlet values')
    f.write(f'   p2 = {P_1} \n')
    f.write(f'   rho2 = {rho_1} \n')
    f.write(f'   u2 = {U_1} \n')
    f.write(f'   M2 = {Ma} \n')
    f.write(f'   T2 = {T_1} \n')

    f.write(f'Other values \n')
    f.write(f'dp = {dp0},    {dp0*1e6} \n')
    f.write(f'norm = {norm} \n')
    f.write(f'tau (s)  = {tau} \n')
    f.write(f'tau (ms) = {tau*1e3} \n')
    f.write(f'Re = {rho_1 * U_1 * dp0 / Ma} \n')


    f.write("\n")
    json.dump(output,f, indent=4)
    f.write("\n")