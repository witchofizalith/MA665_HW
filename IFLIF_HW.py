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
