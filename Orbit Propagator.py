import math
from tqdm import tqdm
from matplotlib import pyplot as plt

#timestep and total time
dt = 1e-6
tot_time = 10

#number of steps
n = int (tot_time/dt)

#charges of both particles
q_e = 1.6e-19
q_a = 10*q_e
q_b = 1*q_e

#electrostatic constant in simulation
K = 8.988*(10**6)

#initial velocity of particle b
v_b = [1,0]

#acceleration of particle b
a_b = [0,0]

#initial positions of particles a and b
r_b = [0,0]
r_a = [0,1]

#mass of particles
m_e = 9.1094e-31

#mass of particle b
m_b = 1*m_e

#force of the particle
F = [0]

#angle of the particle
angle_hist = []

#position of particle b
bx_hist = []
by_hist = []

#time of the simulation
t_hist  = []

for i in tqdm(range(n)):
 
    r_bx = r_b[0]
    r_by = r_b[1]
    
    r_ax = r_a[0]
    r_ay = r_a[1]
    
    v_bx = v_b[0]
    v_by = v_b[1]
    
    a_bx = a_b[0]
    a_by = a_b[1]
    
    r = ((r_bx - r_ax)**2 + (r_by - r_ay)**2)**0.5
    θ = math.atan2((r_by-r_ay), (r_bx-r_ax)) 
    F = -(K*q_a*q_b) / (r**2)
    F_x = F * math.cos(θ)
    F_y = F * math.sin(θ)
   

    a_bx = F_x / m_b
    a_by = F_y /m_b   
    
    next_v_bx = v_bx + a_bx * dt
    next_v_by = v_by + a_by * dt
    
    next_r_bx = r_bx + next_v_bx * dt 
    next_r_by = r_by + next_v_by * dt
        
    r_b[0] = next_r_bx
    r_b[1] = next_r_by
    
    v_b[0] = next_v_bx
    v_b[1] = next_v_by
    
    angle_hist.append(θ)
    bx_hist.append(r_b[0])
    by_hist.append(r_b[1])
    t_hist.append((i+1)* dt)
    
#sets up plot of the position of the particle, and sets the aspect ratio of the plot equal
plt.grid()
plt.plot(bx_hist,by_hist)
plt.axis('equal')
