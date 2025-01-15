#!/usr/bin/env python3

def printmat(mat):
    for i in mat: 
        print(i)

def det2x2(mat): 
    return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]

def cofactor(mat): 
    cofactor = [[], [], []]
    x = [[mat[1][1], mat[1][2]], [mat[2][1], mat[2][2]]]
    cofactor[0].append(det2x2(x))
    x = [[mat[1][0], mat[1][2]], [mat[2][0], mat[2][2]]]
    cofactor[0].append(det2x2(x))
    x = [[mat[1][0], mat[1][1]], [mat[2][0], mat[2][1]]]
    cofactor[0].append(det2x2(x))
    
    x = [[mat[0][1], mat[0][2]], [mat[2][1], mat[2][2]]]
    cofactor[1].append(det2x2(x))
    x = [[mat[0][0], mat[0][2]], [mat[2][0], mat[2][2]]]
    cofactor[1].append(det2x2(x))
    x = [[mat[0][0], mat[0][1]], [mat[2][0], mat[2][1]]]
    cofactor[1].append(det2x2(x))
    
    x = [[mat[0][1], mat[0][2]], [mat[1][1], mat[1][2]]]
    cofactor[0].append(det2x2(x))
    x = [[mat[0][0], mat[0][2]], [mat[1][0], mat[1][2]]]
    cofactor[0].append(det2x2(x))
    x = [[mat[0][0], mat[0][1]], [mat[1][0], mat[1][1]]]
    cofactor[0].append(det2x2(x))
    


 
    


def inv2x2(mat): 
    inv = []
    for i in range(len(mat)): 
        inv.append([])
        for j in range(len(mat)): 
            inv[i].append(mat[i][j]*(1/det2x2(mat)))
    return inv

print("Matrix Inverse")
size = int(input("Number of rows in square matrix: "))
mat = []
for i in range(size): 
    mat.append([])
    for j in range(size): 
        num = int(input(f"A{i+1}{j+1}: "))
        mat[i].append(num)

print("Original Matrix: ")
printmat(mat)
print("Inverse: ")
if size == 2: 
    printmat(inv2x2(mat))
else: 
    printmat(inv3x3(mat))
