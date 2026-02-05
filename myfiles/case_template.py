import json
import math
import numpy as np

# ===========================================================================
# ===========================================================================
# ====================== USER CONFIGURABLE VALUES ===========================
# ===========================================================================
# ===========================================================================          
L           = 0.02      # length of sides on square domain
D           = 0.001     # Diameter of immersed cylinder(s)
m           = 300
n           = 300

rho         = 1.184     # kg/m^3  (static fluid density)
Re          = 300.0     # Reynolds number
nu          = 1.56e-5   # m^2/s    (kinematic viscosity)
gamma       = 1.4       # -        (specific-heat ratio)
P           = 1.013e5   # Assume ambient pressure
Cd_cyl      = 1.18      # drag on a cylinder at Re=300

U  = Re*nu/D                                  # m/s
q  = 0.5 * rho * U**2
Fd = q * D * Cd_cyl  # drag force per unit span
A_dom = L * L
Fb = Fd / A_dom

# Configuring case dictionary
print(
    json.dumps(
        {
            # DEFINE OUTPUT PARAMETERS AND FORMATTING ========================
            "run_time_info"                          : "T", 
            "format"                                 : 1,   
            "precision"                              : 2,   
            "prim_vars_wrt"                          : "T", 
            "E_wrt"                                  : "T", 
            "parallel_io"                            : "T", 
            "schlieren_wrt"                          : "T", 
            "fd_order"                               : 4,   
            "schlieren_alpha(1)"                     : 10,   
            "schlieren_alpha(2)"                     : 10,     
            # ================================================================

            # COMPUTATIONAL DOMAIN PARAMETERS ================================
            # For these computations, the cylinder is placed at the (0,0)
            # rectangular domain origin.
            "x_domain%beg"                           : -L/2,
            "x_domain%end"                           : L/2,
            "y_domain%beg"                           : -L/2,
            "y_domain%end"                           : L/2,
            "m"                                      : m,
            "n"                                      : n,
            "cyl_coord"                              : "F",
            # ================================================================

            # TIME STEPPING PARAMETERS =======================================
            "cfl_adap_dt"                          : "T", 
            "cfl_target"                           : 0.5, 
            "n_start"                              : 0,   
            "t_save"                               : 0.00003,
            "t_stop"                               : 0.0003,
            # ================================================================
            
            # SIMULATION ALGORITHM PARAMETERS ================================
            # Only one patch is necessary for the background liquid
            "num_patches"                            : 1, 
            "num_fluids"                             : 1,
            # Use the 5 equation model
            "model_eqns"                             : 2,
            "alt_soundspeed"                         : "F",
            "mpp_lim"                                : "F",
            "mixture_err"                            : "T",
            # Use TVD RK3 for time marching
            "time_stepper"                           : 3,
             # Use WENO5
            "weno_order"                             : 5,
            "weno_eps"                               : 1.0e-16,
            "weno_Re_flux"                           : "T",
            "weno_avg"                               : "T",
            "avg_state"                              : 2,
            # Use the mapped WENO weights to maintain monotinicity
            "mapped_weno"                            : "T",
            "null_weights"                           : "F",
            "mp_weno"                                : "T",
            # Use the HLLC  Riemann solver
            "riemann_solver"                         : 2,
            "wave_speeds"                            : 1,
            # Include viscous effects
            "viscous"                                : "T",
            # ================================================================

            # DEFINE FLUID DOMAIN ============================================
            "patch_icpp(1)%geometry"                 : 3, #cylinderical tube

            "patch_icpp(1)%x_centroid"               : 0,
            "patch_icpp(1)%y_centroid"               : 0,

            "patch_icpp(1)%length_x"                 : L,
            "patch_icpp(1)%length_y"                 : L,
            # ================================================================

            # SET BOUNDARY CONDITIONS =========================================
            # Use doubly periodic BCs
            "bc_x%beg"                               : -1,
            "bc_x%end"                               : -1,
            "bc_y%beg"                               : -1,
            "bc_y%end"                               : -1,
            # ================================================================

            # SET INITIAL CONDITIONS IN THE DOMAIN ===========================
            # Use uniform freestream conditions
            "patch_icpp(1)%vel(1)"                   : U,
            "patch_icpp(1)%vel(2)"                   : 0.0e00,
            "patch_icpp(1)%pres"                     : P,
            "patch_icpp(1)%alpha_rho(1)"             : rho,
            "patch_icpp(1)%alpha(1)"                 : 1.0e00,

            "perturb_flow"                           : "T",
            "perturb_flow_fluid"                     : 1,  
            "perturb_flow_mag"                       : 1e-4 * U,

            # Fluids Physical Parameters
            "fluid_pp(1)%gamma": 1.0e00 / (gamma - 1.0e00),  # Stiffend gas param based on specific heat ratio
            "fluid_pp(1)%pi_inf": 0,
            "fluid_pp(1)%Re(1)": Re,

            # Body Forces
            "bf_x": "T",
            "k_x": 0.0,
            "w_x": 0.0,
            "p_x": 0.0,
            "g_x": Fb,
            # ================================================================

            # DEFINE IMMERSED BOUNDARY(IES) ==================================
            "ib"                                     : "T",
            "num_ibs"                                : 1,

            # Patch: Cylinder Immersed Boundary
            "patch_ib(1)%geometry": 2,
            "patch_ib(1)%x_centroid": 0,
            "patch_ib(1)%y_centroid": 0,
            "patch_ib(1)%radius": .5 * D,
            "patch_ib(1)%slip": "F",
            # ================================================================
        }, indent=4
    )
)
