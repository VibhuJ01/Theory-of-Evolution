from matplotlib import pyplot as plt

def graph(x,y,z,n):

    gen = [i+1 for i in range(n//25)]

    plt.plot(gen, x, label = "Deterministic")
    plt.plot(gen, y, label = "Non-Deterministic")
    plt.plot(gen, z, label = "Natural Selection")
    
    plt.xlabel('Generations')
    plt.ylabel('Varaince')
    plt.title('Variance VS Generation')
    
    plt.legend()
    plt.show()
