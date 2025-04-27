def test(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            x=(i+j-2)%n + 1
            print("i:" + str(i) + " j:" + str(j) + " x:" + str(x))

test(5)