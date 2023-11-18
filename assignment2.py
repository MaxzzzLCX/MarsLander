# Chenxu (Max) Lyu
# 2023.06.29 

# IA Mars Lander Assignment 2

import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D


def mag(x):
    # Calculates the magnitude of an vector
    sum = 0
    for i in x:
        sum += i**2
    return np.sqrt(sum)

def acc(x):
    # Calculate the acceleration (vector) of object at position x
    a = (-G * M / (mag(x)**3)) * x
    return a

def cir_speed(x):
    # Calculating the speed (scalar) of circular motion
    # a = v^2/r THUS v = sqrt(a*r)

    return np.sqrt(mag(acc(x))*mag(x))

def escape_speed(x):
    # Calculating the escape speed (scalar)
    # 1/2mv^2 - GMm/r = 0;  To escape (reach infinity), E = 0
    # THUS: sqrt(2GM/r)
    
    return np.sqrt(2*G*M/mag(x))


# constants
m = 1
k = 1
G = 6.67e-11
M = 6.42e23
R = 3390e3

# simulation time, timestep and time
# For case 1/2 use 20000; case 3 use 130000
t_max = 20000 
dt = 0.1
t_array = np.arange(0, t_max, dt)


def case_1():

    # Case 1: Straight Down Descent - Initial Conditions
    x = np.array([2*R,0,0])
    v = np.array([0,0,0])
    a = np.zeros(3)

    # initialise empty lists to record trajectories
    position_list = []
    velocity_list = []
    altitude_list = []

    # Euler Integration
    for t in t_array:

        # append current state to trajectories
        position_list.append(x)
        velocity_list.append(v)
        altitude_list.append(mag(x))

        
        if x[0]+dt*v[0] <= 0:
            x = np.array([0,0,0])
        else:
            # calculate new position and velocity
            a = (-G * M / (mag(x)**3)) * x # a(t)
            x = x + dt * v # x(t+dt) = x(t) + dt*v(t)
            v = v + dt * a # v(t+dt) = v(t) + dt*a(t)

    altitude_array = np.array(altitude_list)

    plt.figure(1)
    plt.clf()
    plt.xlabel('time (s)')
    plt.grid()
    plt.plot(t_array, altitude_array, label='h (m)')
    plt.title("Vertical Descent",fontsize=20)
    plt.legend()
    plt.show()

def case_2():

    # Case 2: Circular Orbit
    x = np.array([2*R,0,0])
    v = np.array([0,cir_speed(x),0])
    a = np.zeros(3)

    # initialise empty lists to record trajectories
    position_list = []
    velocity_list = []
    altitude_list = []

    # Euler Integration
    for t in t_array:

        # append current state to trajectories
        position_list.append(x)
        velocity_list.append(v)
        altitude_list.append(mag(x))

        # calculate new position and velocity
        a = (-G * M / (mag(x)**3)) * x # a(t)
        x = x + dt * v # x(t+dt) = x(t) + dt*v(t)
        v = v + dt * a # v(t+dt) = v(t) + dt*a(t)

    altitude_array = np.array(altitude_list)
    x_array = np.array(position_list)
    v_array = np.array(velocity_list)

    fig = plt.figure()
    sub = fig.add_subplot(111,projection='3d')
    sub.plot(x_array[:,0],x_array[:,1],x_array[:,2])
    sub.set_xlabel('$x$',fontsize=15)
    sub.set_ylabel('$y$',fontsize=15)
    sub.set_zlabel('$z$',fontsize=15)
    sub.set_title('Circular Motion', fontsize=20)
    plt.show()

def case_3():
    # Case 3: Elliptical Orbit
    x = np.array([2*R,0,0])
    v = np.array([0,3300,0])
    a = np.zeros(3)

    # print(escape_speed(x))
    # print(cir_speed(x))

    # initialise empty lists to record trajectories
    position_list = []
    velocity_list = []
    altitude_list = []

    # Euler Integration
    for t in t_array:

        # append current state to trajectories
        position_list.append(x)
        velocity_list.append(v)
        altitude_list.append(mag(x))

        # calculate new position and velocity
        a = (-G * M / (mag(x)**3)) * x # a(t)
        x = x + dt * v # x(t+dt) = x(t) + dt*v(t)
        v = v + dt * a # v(t+dt) = v(t) + dt*a(t)

    altitude_array = np.array(altitude_list)
    x_array = np.array(position_list)
    v_array = np.array(velocity_list)

    fig = plt.figure()
    sub = fig.add_subplot(111,projection='3d')
    sub.plot(x_array[:,0],x_array[:,1],x_array[:,2])
    sub.set_xlabel('$x$',fontsize=15)
    sub.set_ylabel('$y$',fontsize=15)
    sub.set_zlabel('$z$',fontsize=15)
    sub.set_xticks([-4e7,-2e7,0,2e7,4e7])
    sub.set_yticks([-4e7,-2e7,0,2e7,4e7])
    sub.set_title('Elliptical Motion', fontsize=20)
    plt.show()

def case_4():
    # Case 4: Hyperbolic
    x = np.array([2*R,0,0])
    v = np.array([0,escape_speed(x)*1.05,0])
    a = np.zeros(3)


    # initialise empty lists to record trajectories
    position_list = []
    velocity_list = []
    altitude_list = []

    # Euler Integration
    for t in t_array:

        # append current state to trajectories
        position_list.append(x)
        velocity_list.append(v)
        altitude_list.append(mag(x))

        # calculate new position and velocity
        a = (-G * M / (mag(x)**3)) * x # a(t)
        x = x + dt * v # x(t+dt) = x(t) + dt*v(t)
        v = v + dt * a # v(t+dt) = v(t) + dt*a(t)

    altitude_array = np.array(altitude_list)
    x_array = np.array(position_list)
    v_array = np.array(velocity_list)

    fig = plt.figure()
    sub = fig.add_subplot(111,projection='3d')
    sub.plot(x_array[:,0],x_array[:,1],x_array[:,2])
    sub.set_xlabel('$x$',fontsize=15)
    sub.set_ylabel('$y$',fontsize=15)
    sub.set_zlabel('$z$',fontsize=15)
    # sub.set_xticks([-4e7,-2e7,0,2e7,4e7])
    # sub.set_yticks([-4e7,-2e7,0,2e7,4e7])
    sub.set_title('Hyperbolic Motion', fontsize=20)
    plt.show()



case_4()



