import numpy as np
import matplotlib.pyplot as plt

def FLIF(I, C, R, Vth, Vreset, duration, plot=False):
    # Input parameters:
    # I: Input current
    # C: Membrane capacitance
    # R: Membrane resistance
    # Vth: Threshold voltage
    # Vreset: Reset voltage
    # duration: Duration of simulation
    # plot: Boolean flag to plot the voltage vs. time

    dt = 0.01              # Set the timestep.
    num_steps = int(duration / dt)  # Number of time steps
    V = np.zeros(num_steps)
    V[0] = 0.2             # Initial condition
    spikes = 0             # Counter for spikes

    for k in range(num_steps - 1):
        dVdt = (I - V[k] / R) / C  # Modified voltage update equation with leakage
        V[k + 1] = V[k] + dt * dVdt

        if V[k + 1] > Vth:        # Check if the voltage exceeds the threshold
            V[k + 1] = Vreset    # Reset the voltage
            spikes += 1

    firing_rate = spikes / duration  # Calculate firing rate

    if plot:
        t = np.arange(num_steps) * dt  # Time axis
        plt.plot(t, V)
        plt.xlabel('Time (s)')
        plt.ylabel('Voltage (V)')
        plt.title(f'LIF Neuron Model (I = {I}, Firing Rate = {firing_rate} Hz)')
        plt.grid(True)
        plt.show()

    return firing_rate

# Input current values to test
input_currents = np.linspace(0.2, 2.0, 10)  # Vary the input current from 0.2 to 2.0
firing_rates = []

for I in input_currents:
    firing_rate = FLIF(I, 1.0, 1.0, 1.0, 0.0, duration=1.0, plot=False)
    firing_rates.append(firing_rate)

# Plot firing rate vs. input current
plt.plot(input_currents, firing_rates, marker='o')
plt.xlabel('Input Current (I)')
plt.ylabel('Firing Rate (Hz)')
plt.title('Firing Rate vs. Input Current (LIF Neuron)')
plt.grid(True)
plt.show()
