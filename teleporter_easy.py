

def minimum_teleports(a, c, n):
    actual_cost = [ a[i] + i + 1  for i  in range(n)]
    actual_cost = sorted(actual_cost)

    rem_cost = c
    counter = 0
    for cost in actual_cost:
        if cost > rem_cost:
            break
        rem_cost -= cost
        counter += 1

    return counter




t = int(input().strip())

for _ in range(t):
    n, c = list(map(int, input().rstrip().split()))
    a = list(map(int, input().rstrip().split()))

    ans = minimum_teleports(a, c, n)

    print(ans)
