#pattern 21
'''
0 1 0 1 0 
0 0 0 0 0 
0 1 0 1 0 
0 0 0 0 0 
0 1 0 1 0 
'''
k=1
for i in range(1,6):
    for j in range(0,5):
        k=(i*j)%2
        print(k,end=" ")
    print()
