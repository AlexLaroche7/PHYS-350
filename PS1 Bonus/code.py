import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Circle

def point_charge_ring(n=13,m=12,q=1):
    """n: equally spaced slots in a ring
       m: charges with charge q/m in consecutive slots.
       q: total charge of point charges on ring.
       
       Returns: Plot of E field and E field at oriign."""
    
    # Individual point charge
    c = q/m
    
    # Initialize plot
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
    
    # Initialize E field x,y components and individual point charges
    ex=[]
    ey=[]
    qi=[]
    
    # Creating charges and calculating individual electric fields
    # Constants ignored for simplicity
    for i in range (m):
        qi.append([c, np.cos(np.pi/2 + 2*np.pi*(i+1)/n), np.sin(np.pi/2 + 2*np.pi*(i+1)/n)])
        ax.add_artist(Circle((qi[i][1],qi[i][2]), 0.05, color='k'))
        ex.append(np.sqrt((xm-qi[i][1])**2 + (ym-qi[i][2])**2)**(-3) * c * (xm - qi[i][1]))
        ey.append(np.sqrt((xm-qi[i][1])**2 + (ym-qi[i][2])**2)**(-3) * c * (ym - qi[i][2]))
        
    #centre charge Q
    ax.add_artist(Circle((0,0), 0.1, color='k'))
    
    #total electric field components
    Ex = sum(ex)
    Ey = sum(ey)
    
    #normalize for aesthetic purposes
    Ex_norm = Ex/np.sqrt(Ex**2+Ey**2)
    Ey_norm = Ey/np.sqrt(Ex**2+Ey**2)

    #plotting electric field
    ax.quiver(xm, ym, Ex_norm, Ey_norm, scale=40)

    ax.set_xlim(-1.4,1.4)
    ax.set_ylim(-1.4,1.4)
    ax.set_aspect('equal')

    plt.show()

    #value of electric field felt by center Q
    print("E(0,0) =", Ex[50][50],"i +", Ey[50][50],"j")
    
    return



def center_charge_ring(n):
    """n: odd number of equally spaced slots.
       q=1 and Q=1 for simplicity.
    
       Returns: Force at center as a function of n"""
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    m = int((n-1)/2)
    c = 1/m
    
    # Set up 2d plane
    x = np.linspace(-2, 2, 101)
    y = np.linspace(-2, 2, 101)
    xm, ym = np.meshgrid(x, y)
    
    # Initialize E field x,y components and individual point charges
    qn=[]
    
    #creating charges and calculating individual electric fields
    for i in range(n):  
        if i % 2 != 0: 
            
            ex = np.zeros(n)
            ey = np.zeros(n)
            
            for j in range (m):
    
                qn.append([c, np.cos(np.pi/2 + 2*np.pi*(j+1)/n), np.sin(np.pi/2 + 2*np.pi*(j+1)/n)])
                ex[i] += np.sqrt((0-qn[j][1])**2 + (0-qn[j][2])**2)**(-3) * c * (0 - qn[j][1])
                ey[i] += np.sqrt((0-qn[j][1])**2 + (0-qn[j][2])**2)**(-3) * c * (0 - qn[j][2])
            
            if i==1:
                ax.plot(i, sum(ex), marker='.', color='k', label='Ex')
                ax.plot(i, -sum(ey), marker='.', color='r', label='Ey')
            else:
                ax.plot(i, sum(ex), marker='.', color='k')
                ax.plot(i, -sum(ey), marker='.', color='r')
    
    plt.legend()
    plt.show()
            
    return
    
