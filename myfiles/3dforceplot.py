#!/usr/bin/env python3
"""
Simple plotter for immersed boundary forces from MFC simulation.
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# CONFIGURATION
# ============================================================================

FILENAME = 'ib_1_forces.dat'  # File to plot
SAVE_FIG = True                # Save PNG file
SHOW_FIG = True                # Display window

# ============================================================================

# Load data
data = np.loadtxt(FILENAME)

# Extract columns
time = data[:, 0]
fx = data[:, 1]
fy = data[:, 2]

# Check if 2D or 3D
if data.shape[1] == 4:  # 2D case
    tau_z = data[:, 3]
    
    # Create 2D plot
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))
    fig.suptitle(f'IB Forces and Torque (2D)\n{FILENAME}', fontsize=14, fontweight='bold')
    
    # Forces
    f_mag = np.sqrt(fx**2 + fy**2)
    axes[0].plot(time, fx, 'r-', linewidth=1.2, label='$F_x$')
    axes[0].plot(time, fy, 'b-', linewidth=1.2, label='$F_y$')
    axes[0].plot(time, f_mag, 'k--', linewidth=1.5, label='|F|')
    axes[0].set_xlabel('Time')
    axes[0].set_ylabel('Force')
    axes[0].grid(True, alpha=0.3)
    axes[0].legend()
    
    # Torque
    axes[1].plot(time, tau_z, 'g-', linewidth=1.5, label='$τ_z$')
    axes[1].set_xlabel('Time')
    axes[1].set_ylabel('Torque')
    axes[1].grid(True, alpha=0.3)
    axes[1].legend()
    
else:  # 3D case
    fz = data[:, 3]
    tau_x = data[:, 4]
    tau_y = data[:, 5]
    tau_z = data[:, 6]
    
    # Create 3D plot
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle(f'IB Forces and Torques (3D)\n{FILENAME}', fontsize=14, fontweight='bold')
    
    # Force magnitude
    f_mag = np.sqrt(fx**2 + fy**2 + fz**2)
    axes[0, 0].plot(time, f_mag, 'k-', linewidth=1.5, label='|F|')
    axes[0, 0].set_xlabel('Time')
    axes[0, 0].set_ylabel('Force Magnitude')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].legend()
    
    # Force components
    axes[0, 1].plot(time, fx, 'r-', linewidth=1.2, label='$F_x$')
    axes[0, 1].plot(time, fy, 'b-', linewidth=1.2, label='$F_y$')
    axes[0, 1].plot(time, fz, 'g-', linewidth=1.2, label='$F_z$')
    axes[0, 1].set_xlabel('Time')
    axes[0, 1].set_ylabel('Force Components')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].legend()
    
    # Torque magnitude
    tau_mag = np.sqrt(tau_x**2 + tau_y**2 + tau_z**2)
    axes[1, 0].plot(time, tau_mag, 'k-', linewidth=1.5, label='|τ|')
    axes[1, 0].set_xlabel('Time')
    axes[1, 0].set_ylabel('Torque Magnitude')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].legend()
    
    # Torque components
    axes[1, 1].plot(time, tau_x, 'r-', linewidth=1.2, label='$τ_x$')
    axes[1, 1].plot(time, tau_y, 'b-', linewidth=1.2, label='$τ_y$')
    axes[1, 1].plot(time, tau_z, 'g-', linewidth=1.2, label='$τ_z$')
    axes[1, 1].set_xlabel('Time')
    axes[1, 1].set_ylabel('Torque Components')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].legend()

plt.tight_layout()

# Save
if SAVE_FIG:
    output = FILENAME.replace('.dat', '.png')
    plt.savefig(output, dpi=300, bbox_inches='tight')
    print(f'Saved: {output}')

# Show
if SHOW_FIG:
    plt.show()