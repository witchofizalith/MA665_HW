import numpy as np
import matplotlib.pyplot as plt

#Question 1-2
def LIF(I, C, R, Vth, Vreset, plot = True):                
    #Input important parameters, and an option to plot V vs t.
    #in which I = input current, C = membrane capacitance, R = membrane resistance
    dt=0.01                      #Set the timestep.
    #num_steps = 1000  ; this is the option to make time steps not as an array, like below, instead you would do v = np.zeros(num_steps)
    V = np.zeros([1000,1])       #Initialize V (where number of time steps = 1000)
    V[0]=0.2;                    #Initial condition.

    for k in range(1000 - 1):       #March forward in time,
        dVdt = (I - V[k] / R) / C
        V[k + 1] = V[k] + dt * dVdt

        if V[k + 1] > Vth:        # Check if the voltage exceeds the threshold
            V[k + 1] = Vreset    # Reset the voltage

        #V[k+1] = V[k] + dt*(I/C) #Update the voltage,
        #if V[k+1] > Vth:         #... and check if the voltage exceeds the threshold.
         #   V[k+1] = Vreset      #... if so, reset the voltage
            
    t = np.arange(0,len(V))*dt   #Define the time axis.
    
    if plot:                     #If the plot flag is on, plot V vs t.
        plt.plot(t,V)
        plt.xlabel('Time (s)')
        plt.ylabel('Voltage (V)')
        plt.title('Voltage vs Time')
        plt.show()

LIF(1.0, 1.0, 1.0, 1.0, 0.0, True) #Reference above, def IF(I, C, R, Vth, Vreset, plot = True)

#Question 3-4
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
