def tribulle(T1,T2,T4,T5):
    n=len(T1)
    for j in range(n-1,0,-1):
        nbr_permutation=0
        for i in range(j):
            if T1[i]<T1[i+1]:
                T1[i],T1[i+1]=T1[i+1],T1[i]
                T2[i],T2[i+1]=T2[i+1],T2[i]
                T4[i],T4[i+1]=T4[i+1],T4[i]
                T5[i],T5[i+1]=T5[i+1],T5[i]
                nbr_permutation=nbr_permutation+1
        if nbr_permutation==0: break
    return T1,T2,T4,T5
def adjacent(M,i,j):
    flag=False #False means ligne i et colonne j non adjacentes
    if M[i][j]==0 and i!=j:
        flag=False
    elif M[i][j]==1 and i!=j:
        flag=True
    return flag 
def occurence(l,a):
    s=0
    for i in range(len(l)):
        if l[i]==a:
            s=s+1
    return s       
def ajouter(a,j,l):
    for i in range(len(l)):
        if i==j:
            l[i]=a
    return l       
def Tableau_de_coloration(Madj):
    nbr_lignes=len(Madj)
    T1=[]
    T2=[]
    T3=[0]*(len(Madj))
    T3
    T4=[]
    T5=[]
    T6=[0]*(len(Madj))
    T7=[]
    nbr_colonnes=nbr_lignes
    for i in range(nbr_lignes):
        deg=0
        for j in range(nbr_colonnes):
            deg=deg+Madj[i][j]    
        T1.append(deg)
        T2.append(chr(65+i))
        T4.append(i)
        T5.append(i)   
    T1,T2,T4,T5=tribulle(T1,T2,T4,T5)
    for i in range(nbr_lignes):
        b="couleur",i+1
        T7.append(b)
    for i in range(nbr_lignes):
        a=T7[0]
        if T3[i]==0: 
            T3=ajouter(a,i,T3)
            for j in range(i+1,nbr_colonnes):
                if T3[j]==0 and adjacent(M,T4[i],T5[j])==False and occurence(T3,a)==1:
                    T3=ajouter(a,j,T3)
                    T6=ajouter(a,j,T6)
                elif T3[j]==0 and adjacent(M,T4[i],T5[j])==False and occurence(T3,a)!=1:
                    flag1=True
                    for l in range(len(T6)):
                        if T6[l]==a and adjacent(M,T4[l],T5[j])==False:
                            flag1=False
                        elif T6[l]==a and adjacent(M,T4[l],T5[j])==True:
                            flag1=True
                    if flag1==False:        
                        T3=ajouter(a,j,T3)
            T7.remove(T7[0]) 
    print("********************************")
    print("*sommet*","degré*","   couleur     *")
    print("********************************")               
    for i in range(len(T1)):
        print("*",T2[i],"   *",T1[i],"   *",T3[i],"*")
        print("********************************")    
    return "c'est la table de coloration"

M=[[0,1,1,1,0,0,1,1],[1,0,0,0,1,1,1,0],[1,0,0,1,0,1,1,1],[1,0,1,0,1,0,0,1],[0,1,0,1,0,1,1,0],[0,1,1,0,1,0,0,0],[1,1,1,0,1,0,0,0],[1,0,1,1,0,0,0,0]]
print(Tableau_de_coloration(M))