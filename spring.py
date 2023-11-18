# uncomment the next line if running in a notebook
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# mass, spring constant, initial position and velocity
m = 1
k = 1
x = 0
v = 1

# simulation time, timestep and time
t_max = 100
dt = 0.005
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
x_list = []
v_list = []

# Euler Integration
for t in t_array:

    # append current state to trajectories
    x_list.append(x)
    v_list.append(v)

    # calculate new position and velocity
    a = -k * x / m # a(t)
    x = x + dt * v # x(t+dt) = x(t) + dt*v(t)
    v = v + dt * a # v(t+dt) = v(t) + dt*a(t)

# Verlet Integration Algorithm:
x = 0
v = 1

x_list_verlet = []
v_list_verlet = []


for t in t_array:

    # append current state of x and v
    x_list_verlet.append(x)
    v_list_verlet.append(v)

    # calculate x and v of next step of time
    if t == 0:
        # the reason including this checking of "t=0" here is because at t=0, there is no meaning of x(t-dt) and v(t-dt)
        a = -k * x / m # a(t)
        x = x + dt * v # x(t+dt) = x(t) + dt*v(t)
        v = v + dt * a # v(t+dt) = v(t) + dt*a(t)
    else:
        x_previous = x_list_verlet[-2] # x(t-dt)
        x_current = x_list_verlet[-1]  # x(t)
        a = -k * x / m                 # a(t)
        x = 2*x_current - x_previous + (-k * x_current / m)*(dt)**2 # x(t+dt) = 2x(t) - x(t-dt) + (dt^2)a(t)
        v = (x-x_current)/dt                                        # v(t+dt) = [x(t+dt) - x(t)] / dt

# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
x_array = np.array(x_list)
v_array = np.array(v_list)
x_array_verlet = np.array(x_list_verlet)
v_array_verlet = np.array(v_list_verlet)

# print(x_array)
# print(v_array)
for i in range (200):
    print("x_verlet: ",x_array_verlet[i], " x_euler: ",x_array[i])
    #print("v_verlet: ",v_array_verlet[i], " v_euler: ",v_array[i])


# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, x_array, label='x (m)')
plt.plot(t_array, v_array, label='v (m/s)')
plt.plot(t_array, x_array_verlet, label='x_verlet (m)')
plt.plot(t_array, v_array_verlet, label='v_verlet (m/s)')
plt.legend()
plt.show()
