def count_even_numbers(A, B):
    result = []
    for i in range(len(B)):
        count = 0
        print(B[1][0])
        for j in range(B[i][0], B[i][1] + 1):
            if A[j] % 2 == 0:
                count += 1
        result.append(count)
    return result
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = []
for i in range(0,len(B),2):
    C.append([B[i],B[i+1]])
print(count_even_numbers(A, C))