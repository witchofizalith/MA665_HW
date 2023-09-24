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

#Question 3

#Set the parameters
def QIF(I, C, R, Vth, Vreset, duration, plot=False):
  # where the parameters are: I = input, C = capacitance, R = resistance, Vth = Threshold voltage, Vreset = Reset voltage, and duration = duration of simulation
  dt = 0.01       # Set the timestep.
  num_steps = int(duration / dt) # Number of time steps
  V = np.zeros(num_steps)
  V[0] = 0.2       # Initial condition
  spikes = 0       # Counter for spikes

  for k in range(num_steps - 1):
    # Modified voltage update equation with quadratic term
    dVdt = (I - V[k] / R) / C + a * V[k] ** 2

    V[k + 1] = V[k] + dt * dVdt

    if V[k + 1] > Vth:      # Check if the voltage exceeds the threshold
      V[k + 1] = Vreset  # Reset the voltage
      spikes += 1

  firing_rate = spikes / duration # Calculate firing rate

  if plot:
    t = np.arange(num_steps) * dt # Time axis
    plt.plot(t, V)
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.title(f'QIF Neuron Model (I = {I}, Firing Rate = {firing_rate} Hz)')
    plt.grid(True)
    plt.show()

  return firing_rate

#Question 4
def FLIF(I, C, R, Vth, Vreset, duration, plot=False):
    # where the parameters are: I = input, C = capacitance, R = resistance, Vth = Threshold voltage, Vreset = Reset voltage, and duration = duration of simulation
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

##Questions 6: Quad LIF f-i curve
def QIF_neuron(I, C, duration, dt):
    num_steps = int(duration / dt)
    V = np.zeros(num_steps)
    V[0] = 0.0  # Initial condition for membrane potential

    for step in range(1, num_steps):
        dVdt = (V[step - 1] ** 2 + I) / C
        V[step] = V[step - 1] + dt * dVdt
         # Check for spike (reset when the potential reaches a threshold)
        if V[step] >= 1.0:
            V[step] = 0.0
    t = np.arange(0, duration, dt)
    return t, V
# Simulation parameters
I_values = [0.5, 1.0, 1.5]  # Input currents to test
C = 1.0  # Membrane capacitance
duration = 5.0  # Duration of simulation in seconds
dt = 0.001  # Time step for simulation

# Simulate the QIF neuron for different input currents
plt.figure(figsize=(10, 6))
for I in I_values:
    t, V = QIF_neuron(I, C, duration, dt)
    plt.plot(t, V, label=f'I = {I}')

plt.xlabel('Time (s)')
plt.ylabel('Membrane Potential (V)')
plt.title('Quadratic Integrate-and-Fire (QIF) Neuron')
plt.legend()
plt.grid(True)
plt.show()