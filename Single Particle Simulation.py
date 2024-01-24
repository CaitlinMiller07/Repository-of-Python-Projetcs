from matplotlib import pyplot as plt
from tqdm import tqdm

plt.rcParams ["figure.figsize"] = [7.50,3.50]
plt.rcParams     ["figure.autolayout"] = True


dt = 1e-6 #the timestep of the simulation
total_time = 10 #Total run-time of the simulation
n = int (total_time / dt) #number of steps

r = [0,0] #the starting position of the particle, stored in r 

v = [1,1] #initial velocity v

a = [0,-1] #acceleration of the particle

C = [0]

x_hist = [] #empty list of the particle's x position
y_hist = [] #empty list of the particle's y position
t_hist = [] #empty list of t
C_hist = [] #empty list of C

for i in tqdm(range(n)): #i is the loop iterator. It loops n times
    r_x = r[0] #the x position of the particle
    r_y = r[1] #the y position of the particle    
            
    v_x = v[0] #the velocity in the x-direction
    v_y = v[1] #the velocity in the y-direction
    
    a_x = a[0] #the acceleration in the x-direction
    a_y = a[1] #the acceleration in the y-direction
            
    next_v_x = v_x + a_x * dt #calculates the velocity at v_x(n+1)
    next_v_y = v_y + a_y * dt #calculates the velocity at v_y(n+1)
    
    next_r_x = r_x + next_v_x * dt #calculates the new x position of the particle
    next_r_y = r_y + next_v_y * dt #calculates the new y position of the particle
 
    r[0] = next_r_x #array for the next x-positions of the particle
    r[1] = next_r_y #array for the next y-positions of the particle
    
    v[0] = next_v_x #array for all the velocity in the x-direction
    v[1] = next_v_y #array for all the velocity in the y-direction
    
    x_hist.append(r[0]) #all the x-positions
    y_hist.append(r[1]) #all the y-positions
    t_hist.append((i+1) * dt)
    C_hist.append(C) 


plt.grid() #creates a griod for the graph
plt.plot(x_hist,y_hist) #plots all the x and y positions
