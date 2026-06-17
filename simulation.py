import numpy as np
import matplotlib.pyplot as plt

def simulate_trap_release(snapback_factor=0.05):
    """
    Simulates the energy state of an atom in a trap vs. the release.
    snapback_factor: Represents the strength of the anomalous restorative energy (Delta E).
    """
    # 1. Define Physical Constants (Simplified units)
    time = np.linspace(0, 10, 100) # Microseconds
    trap_state = np.ones_like(time)
    
    # 2. Model the Energy
    # While trapped, energy is stable (Potential + Kinetic)
    energy_trapped = 0.5 * np.ones_like(time)
    
    # 3. Model the Release (At time = 5)
    # Standard physics says energy should be conserved (Constant)
    # Kinetic Restoration Hypothesis predicts a 'Snapback' Spike
    energy_output = np.zeros_like(time)
    
    for i, t in enumerate(time):
        if t < 5:
            energy_output[i] = 0.5 # Trapped state energy
        else:
            # Standard Prediction: Energy drops as potential is lost
            standard_physics = 0.25 
            # Your Theory: The Snapback Spike (Anomalous Energy)
            snapback_spike = snapback_factor * np.exp(-(t - 5.1)**2 / 0.05)
            energy_output[i] = standard_physics + snapback_spike

    return time, energy_output

# Run the Simulation
time, energy = simulate_trap_release(snapback_factor=0.3)

# Plotting the Result
plt.figure(figsize=(10, 6))
plt.plot(time, energy, label="Measured Energy (Theoretical)", color='blue', linewidth=2)
plt.axvline(x=5, color='red', linestyle='--', label="Trap Release (Cutoff)")
plt.title("Kinetic Restoration Hypothesis: Temporal Snapback Prediction")
plt.xlabel("Time (Microseconds)")
plt.ylabel("Energy Output (Arbitrary Units)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
