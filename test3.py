def sub(m,r1,r2,n):
    if n==0:
        if m[r2][r1]!=0:
            for i in range(len(m[r1])):
                m[r2][i]-=m[r1][i]
    else:
        for i in range(len(m[r1])):
            m[r2][i]-=n*m[r1][i]
    
    return m
def first_nonzero(m,row):
    a=0
    b=1
    for i in range(len(m[row])):
        if m[row][i]!=0:
            a=i
            b=m[row][i]
            break
    return a,b

def further_set(m):
    r_c={}
    new_matrix= []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]!=0:
                r_c[j]=i
                break
        
    for i in sorted(list(r_c.keys())):
        new_matrix.append(m[r_c[i]])
    k = len(list(r_c.keys()))
    rows = len(m)

    for i in range(rows-k):
        new_matrix.append([0 for x in range(len(m[0]))])
    
    return new_matrix

def set_m(m,row,k):
    if m[row][k]==0 and row<(len(m)-1):
        n=0
        while n<(len(m)-row):
            if m[row][k]!=0:
                break
            else:
                m[row],m[row+n]=m[row+n],m[row]
            n+=1
    if m[row][k]!=0:
        n=m[row][k]
        for j in range(len(m[row])):
            m[row][j]=m[row][j]/n
    return m

def rref(m):
    if len(m[0])==len(m) or len(m[0])<len(m):
        for j in range(len(m[0])):
            for i in range(j,len(m[0])):
                set_m(m,i,j)
            for i in range(j+1,len(m)):
                sub(m,j,i,0)
    elif len(m[0])>len(m):
        for j in range(len(m)):
            for i in range(j,len(m)):
                set_m(m,i,j)
            for i in range(j+1,len(m)):
                sub(m,j,i,0)
    for i in m:
        for j in range(len(i)):
            if abs(i[j])<=0.001:
                i[j]=0
            i[j]=round(i[j],4)
    return m

def further_rref(m):
    for i in range(1,len(m)):
        for j in range(1,len(m)):
            if i+j>len(m):
                break
            else:
                t=first_nonzero(m,-i)
                ind=t[0]
                e=t[1]
                row1=-i
                if m[-i-j][ind]!=0:
                    f=m[-i-j][ind]/e
                    row2=-i-j
                    k=0
                    while True:
                        row2-=k
                        if abs(row2)>len(m):
                            break
                        else:
                            sub(m,row1,row2,f)
                        k+=1

    for i in m:
        for j in range(len(i)):
            if abs(i[j])<=0.001:
                i[j]=0
            i[j]=round(i[j],3)
    return m

def pivots(matrix):
    n = len(matrix)
    pivots = [0] * n
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                pivots[i] = j+1               
                break
    for i in pivots:
        if i==0:
            pivots.remove(0)
    return pivots

def get_rows(m,r):
    l=[]
    for i in range(len(m)):
        l.append(m[i][r])
    return l

def solution(m):
    sol=[]
    zero_sol=[0 for _ in range(len(m[0]))]
    piv=pivots(m)
    gen_l=[i for i in range(1,len(m[0])+1)]
    free_var=[]
    for i in range(len(piv)):
        if piv[i]==gen_l[i]:
            gen_l[i]=0
    free_var=list(set(gen_l))
    free_var.remove(0)
    for i in free_var: #range(1,(len(m[0])-len(free_var)+1)):
        sol.append(get_rows(m,i-1))
    for i in range(len(sol)):
        for _ in range((len(m[0])-len(m))):
            sol[i].append(0)
    for i in range(len(free_var)):
        ind=free_var[i]-1
        sol[i][ind]=1
    print(zero_sol,end='')
    for i in range(len(free_var)):
        print(f'+ x_{free_var[i]}*{sol[i]} ',end="")
    return sol

with open('C:\Coding Folders\Python Programming\College\Math_prgms\input.txt', 'r') as f:
    m = [[int(num) for num in line.split()] for line in f if line.strip() != "" ]
rref(m)
a=further_rref(further_set(m))
print("-----------Final RREF Matrix----------------")
for i in a:
    print(i)
print()
print("Pivots------>",pivots(m))
print()
print("---------------Solution Set----------------------")
solution(m)
        