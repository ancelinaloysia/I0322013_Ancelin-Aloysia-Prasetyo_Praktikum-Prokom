kelas =["ani","budi","tono","dinda"]



print("=================")

for i in range(0,len(kelas)):
# output yang berulang
    print("nama mahasiswa ke", i, " adalah = ", kelas[i])



# program matrik 3 x 3

# input
matriksA=[[1,2,3],
         [5,1,7],
         [2,9,1]]
matriksB=[[2,3,5],
          [9,7,6],
          [8,7,3]]

print("bentuk pertama memanjang", matriksA)
print("====")
print(matriksA)

for x in range(0, len(matriksA)):
    print()
    for y in range(0,len(matriksA[0])):
        print(matriksA[x][y]+matriksB[x][y], end=" ")

    print()

print("=====")
    
