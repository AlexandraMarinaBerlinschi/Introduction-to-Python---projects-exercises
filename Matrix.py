1.
The cipher of Eratosthenes. Give a natural number n. Create a list of prime numbers less than or equal to n

n=int(input())
ls=[]
i=2
while i<=n:
    d=2
    k=0
    while d<i:
        if i%d==0:
            k+=1
        d=d+1
    if k==0:
        ls.append(i)
    i=i+1
print(ls)

2.
Given a vector v of n<100 natural numbers of at most two digits. Determine the number of disjoint pairs of of equal elements (of the form (v[i], v[j]) 
with i!=j and v[i]=v[j]) that can be formed with the elements of the vector.

v=[int(n) for n in input().split()] 
print(v)
k=0
print(len(v))
for i in range(len(v)):
    for j in range(len(v)):
        if v[i]==v[j] and i!=j:
            k=k+1
print(k//2)

3.
Given two crowds with the elements ordered in ascending order (the elements of each crowd will be given on a line separated by space). Determine efficiently 
the union and intersection of the two crowds (without using set).

v=[int(x) for x in input().split()]
w=[int(y) for y in input().split()]
reuniune=[]
intersectie=[i for i in v if i in w]
reuniune=[i for i in v if i not in w]
reuniune=reuniune+[j for j in w if j not in v]
reuniune=reuniune+intersectie
reuniune.sort()
print(intersectie)
print(reuniune)

4.
We read m, n and a matrix with m rows and n columns, the elements of a row being given on a line (the elements of a line given on a line separated by a space). 
Create a list of the maximum on each line

m=int(input())
n=int(input())
matrice=[]
maxim=0
ls=[]
for i in range(m):
    a=[]
    for j in range(n):
        c=int(input())
        if j==0:
            d=c
        a.append(c)
        if j>0:
            maxim=max(c,d)
            d=c
    matrice.append(a)
    ls.append(maxim)
print(ls)

5.
Read m, n and a matrix with m rows and n columns, the elements of a row being given on a line (the elements of a line given on a line separated by a space).
In addition, a natural number k is read. Insert a new line with all 0 elements between lines k and k+1 of the matrix.

m=int(input())
n=int(input())
matrice=[]
k=int(input())
for i in range(m):
    a=[]
    for j in range(n):
        c=int(input())
        a.append(c)
    matrice.append(a)
for i in range(m):
    for j in range(n):
        print(matrice[i][j],end=" ")
    print()
    if i==k:
        for j in range(n):
            print(0,end= " ")
        print()

6.
Read m, n and a matrix with m rows and n columns, the elements of a row being given on a line (the elements of a line given on a line separated by a space).
In addition, a natural number k is read. Permute each line of the matrix circular to the right by k positions (Equivalent: permute the columns of the matrix
circular to the right by k positions)

m=int(input())
n=int(input())
k=int(input())
matrice=[]
matrice_noua=[]
d=0
b=[]
for i in range(m):
    a=[]
    for j in range(n):
        c=int(input())
        a.append(c)
        d=d+1
        if d>m*n-k:
            b.append(c)
        if len(b)==n:
            matrice_noua.append(b)
            b=[]
            d1=0
    matrice.append(a)
d=0
for i in range(m):
    for j in range(n):
        d=d+1
        if d<=m*n-k:
            b.append(matrice[i][j])
            print(b)
        if len(b)==n:
            matrice_noua.append(b)
            b = []
for i in range(m):
    for j in range(n):
        print(matrice_noua[i][j],end=" ")
    print()
    
7.
Read m, n and a matrix with m rows and n columns, the elements of a row being given on a line (the elements of a line given on a line separated by a space). 
Construct in memory and display the transposed matrix (also using comprehension).

m=int(input())
n=int(input())
matrice=[]
matrice_transpusa=[]
for i in range(m):
    a=[]
    for j in range(n):
        c=int(input())
        a.append(c)
    matrice.append(a)
for i in range(n):
    a=[]
    for j in range(m):
        a.append(0)
    matrice_transpusa.append(a)
for i in range(len(matrice)):
    for j in range(len(matrice[0])):
        matrice_transpusa[j][i]=matrice[i][j]
for i in range(len(matrice)):
    for j in range(len(matrice[0])):
        print(matrice_transpusa[j][i],end=" ")
    print()
    
8.
Read m, n and a matrix with m rows and n columns, the elements of a row being given on a line (the elements of a line given on a line separated by a space).
Determine the number of even values in the matrix (using also comprehension)

m=int(input())
n=int(input())
k=0
matrice=[]
ls=[]
for i in range(m):
    for j in range(n):
        c=int(input())
        matrice.append(c)
ls=[int(x) for x in matrice if x%2==0]
print(len(ls))

9.
Read m, n and a matrix with m rows and n columns, the elements of a row being given on a line (the elements of a line given on a line separated by a space).
Determine, for each line, the smallest value that can be obtained by adding the elements on the line except one (using also comprehension).

m=int(input())
n=int(input())
matrice=[]
ls=[]
a=[]
for i in range(m):
    a=[]
    max=0
    for j in range(n):
        c=int(input())
        if max<c:
            max=c
        a.append(c)
    matrice.append([x for x in a if x!=max])
sum=0
for i in range(len(matrice)):
    for j in range(len(matrice[i])):
        sum=sum+matrice[i][j]
    print(sum)

10.
Read m, n and a matrix with m rows and n columns (the numbers are given one per row).Sort the elements in the first column in ascending order by line 
interchanges and display the resulting matrix (each element is given in the first column). will be displayed on 4 characters).

m=int(input())
n=int(input())
matrice=[]
prima=[]
for i in range(m):
    a=[]
    for j in range(n):
        c=int(input())
        if j==0:
            prima.append(c)
        else:
            a.append(c)
    matrice.append(a)
s=0
for i in range(len(matrice)):
    for j in range(len(matrice[i])+1):
        if j==0:
            print(prima[s],end=" ")
            s=s+1
        else:
            print(matrice[i][j-1],end=" ")
    print()
    
11.
Give a natural number n>2. Show the first n lines of Pascal's triangle (if c is the maximum number of digits of a number in the triangle, all numbers will 
be displayed in c+1 digits). For example, for n=6 it will display:

#1
#1  1
#1  2  1
#1  3  3  1
#1  4  6  4  1
#1  5 10 10  5  1


n=int(input())
triunghi=[]
for j in range(n+1):
    a = []
    for i in range(j):
        if i==j-1 or i==0:
            a.append(1)
        elif j>1 and i>0:
            a.append(triunghi[j-1][i-1]+triunghi[j-1][i])
    triunghi.append(a)
for i in range(len(triunghi)):
    for j in range(len(triunghi[i])):
        print(triunghi[i][j],end=" ")
    print()
    
12.
Read a natural number N.
a) Generate and display a matrix of size NxN, with elements from 1 to N*N - in ascending order from left to right and top to bottom. (using comprehension).

n=int(input())
matrice=[]
matrice=[i for i in range(n*n+1)]
matrice.remove(0)
m=1
for i in range(len(matrice)):
    print(matrice[i],end=" ")
    if m%n==0:
        print()
    m+=1
    
b)To go through the elements of the spiral matrix, starting from the left-up corner (right, down, left, up, ...), first obtain a list with elements of type
tuple (row, column) representing positions to be covered in this spiral.

print()
lista_poz=[]
for j in range(n):
    a=(0,j)
    lista_poz.append(a)
for i in range(n):
    if i>0:
        a=(i,4)
        lista_poz.append(a)
for i in range(n-2,-1,-1):
    a=(4,i)
    lista_poz.append(a)
for i in range(n-2,0,-1):
    a=(0,i)
    lista_poz.append(a)
print(lista_poz)

