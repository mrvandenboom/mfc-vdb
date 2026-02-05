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
SHOW_FIG = False               # Display window

# ============================================================================

# Load data
data = np.loadtxt(FILENAME)

# Extract columns
time = data[:, 0]
fx = data[:, 1]
fy = data[:, 2]

# Calculate force magnitude
if data.shape[1] == 4:  # 2D case
    f_mag = np.sqrt(fx**2 + fy**2)
else:  # 3D case
    fz = data[:, 3]
    f_mag = np.sqrt(fx**2 + fy**2 + fz**2)

# Create plot
fig, ax = plt.subplots(figsize=(10, 6))
fig.suptitle(f'IB Total Force\n{FILENAME}', fontsize=14, fontweight='bold')

ax.plot(time, f_mag, 'k-', linewidth=1.5, label='|F|')
ax.set_xlabel('Time')
ax.set_ylabel('Force Magnitude')
ax.grid(True, alpha=0.3)
ax.legend()

plt.tight_layout()

# Save
if SAVE_FIG:
    output = FILENAME.replace('.dat', '.png')
    plt.savefig(output, dpi=300, bbox_inches='tight')
    print(f'Saved: {output}')

# Show
if SHOW_FIG:
    plt.show()