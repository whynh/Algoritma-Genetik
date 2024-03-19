import random
#%%
# y = 15x - x^2
# 0 <= x <= 15 --> 4 bit

# 0 --> 0000
# 1 --> 0001
# 2 --> 0010
#   ...
#15 --> 1111 

#Representasi Input
N=3
rows, cols = (N, 4)
induk = [[0 for i in range(cols)] for j in range(rows)]
print (induk)

N_Anak=6
rows, cols = (N_Anak, 4)
anak = [[0 for i in range(cols)] for j in range(rows)]
print (anak)

#%%
def hitungInt(ind=[]):
    #a = 0
    #for i in range(4):
    #    a = a + ind[i]*2^(3-i)
    
    #0010  = ind[0]*2^3 + ind[1]*2^2 + ind[2]*2^1 + ind[3]*2^0 
    a = ind[3]*1 #ind[3]*2^0
    a = a + ind[2]*2 #ind[2]*2^1
    a = a + ind[1]*4 #ind[1]*2^2
    a = a + ind[0]*8 #ind[0]*2^3
    return a

def hitungFitness(ind=[]):
    x = hitungInt(ind) #0010
    y = 15*x-x*x
    return y

def crossover(ind1=[], ind2=[]):
    anak1 = [0, 0, 0, 0]
    anak2 = [0, 0, 0, 0]
    #Untuk anak1 
    anak1[0] = ind1[0]
    anak1[1] = ind1[1]
    anak1[2] = ind2[2]
    anak1[3] = ind2[3]
    #Untuk anak2
    anak2[0] = ind2[0]
    anak2[1] = ind2[1]
    anak2[2] = ind1[2]
    anak2[3] = ind1[3]
    return anak1, anak2

def mutasi(ind=[]):
    # 0010
    #  |
    # 0110    
    ind[1] = 1 - ind[1]
    return ind
#%%
#Insialisasi
Pc = 0.7
Pm = 0.3

for i in range(N):
    a = random.randint(0, 15)
    # a=1 <-- 0001
    induk[i] = [int(x) for x in '{:04b}'.format(a)]

#induk[0] = [int(x) for x in '{:04b}'.format(1)]
#induk[1] = [int(x) for x in '{:04b}'.format(2)]
#induk[2] = [int(x) for x in '{:04b}'.format(14)]

print(induk)    

i=1
epochs=100
MaxFitness = [0 for j in range(epochs)] #<-- output

#mencari nilai maximum fitness untuk populasi (i) = 0
for j in range(N):
    if (hitungFitness(induk[j])>MaxFitness[0]):
        MaxFitness[0] = hitungFitness(induk[j])

while i<epochs:
    #Seleksi
    # N = 3 --> Tidak seleksi untuk induk
    # Roulette, tournament, rank based
    
    #Reproduksi
    a = random.random()        
    if (a<Pc):
        #crossover: 1-point crossover
        anak[0], anak[1] = crossover(induk[0], induk[1])
        anak[2], anak[3] = crossover(induk[0], induk[2])
        anak[4], anak[5] = crossover(induk[1], induk[2])
    if (a<Pm):
        #Mutasi disini
        induk[0] = mutasi(induk[0])
        induk[1] = mutasi(induk[1])
        induk[2] = mutasi(induk[2])
    
    #Elitism
    minFitness = 10000
    idx = 0
    for j in range(len(induk)):
        if (hitungFitness(induk[j])<minFitness):
            minFitness = hitungFitness(induk[j])
            idx = j
    idxAnak=0
    maxFit = 0
    for j in range(len(anak)):
        if (hitungFitness(anak[j])>maxFit):
            maxFit = hitungFitness(anak[j])
            idxAnak = j
    #Replacement steady-state        
    induk[idx] = anak[idxAnak]        
    
    #cari maxFitness
    for j in range(N):
        if (hitungFitness(induk[j])>MaxFitness[i]):
            MaxFitness[i] = hitungFitness(induk[j])
    i+=1
#%%    
#Output
import matplotlib.pyplot as plt    

x = [i for i in range(epochs)]
#print(x)
plt.plot(x, MaxFitness)
plt.show()
