# Définition fonction

def sumdigits (n):
    s=str(n)
    sum=0
    for elt in s :
        sum +=int(elt)
    return sum

def solve_16(n):
    return sumdigits(n)

#séparation des mots et tri alphabétique
f=open('names.txt', 'r')
L=[]                    #liste des noms non triée
for ligne in f :
    L=L+ligne.split('","')          #on sépare les noms
L[0]=L[0][1:]
L[-1]=L[-1][0:-1]          #on enlève " dans les premiers et derniers noms
names=sorted(L)            #liste des noms triée

def name_score(name):        #renvoie le score d'un mot
    namescore=0
    for l in name:         #on parcourt les lettres du mot
        namescore +=ord(l)-64
    return namescore
  
def solve_22(names):
    score=0
    i=1
    for elt in names :              #pour chaque nom du fichier
        score+=i*name_score(elt)
        i+=1
    return score

def lychrel(n):
    l=str(n)
    r=l[::-1]
    l=str(int(l)+int(r))
    r=l[::-1]
    i=1
    while l != r and i<50:
        i+=1
        l=str(int(l)+int(r))
        r=l[::-1]
    if l==r :
        return 0
    else :
        return 1
    
def solve_55(max):
    total=0
    for i in range (max):
        total+=lychrel(i)
    return total

# Code à exécuter

assert solve_16(2**15)==26

print(solve_16(2**1000))
print(names)

assert name_score('COLIN')==53

print(solve_22(names))
    
assert lychrel(349)==0
assert lychrel(196)==1

print(solve_55(10000))