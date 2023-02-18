# 1686 B - NIT Destroys the Universe


def destroy_count(a, n):
    # count positive subarrays
    count = 0

    if a[0] != 0:
        count += 1

    for i in range(1,n):
        if a[i-1] == 0 and a[i] != 0:
            count += 1
            if count > 2:
                return 2
    return count


t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    ans = destroy_count(a, n)

    print(ans)
