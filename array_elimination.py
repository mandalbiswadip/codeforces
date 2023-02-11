

def array_eliminations(arr, n):
    bit_count = [0 for _ in range(30)]

    num = 1

    
    for i in range(30):

        for elm in arr:
            k = elm & num
            if k != 0:
                bit_count[i] += 1
        num *= 2 
    results = []
    for k in range(1, n+1):
        
        flag = True
        for i in range(30):
            if bit_count[i] % k != 0:
                flag = False
                break 
        
        if flag:
            results.append(str(k))
    return " ".join(results)




t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    ans = array_eliminations(a, n)

    print(ans)
