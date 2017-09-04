def cubeNumbers(M, N):
    count = 0
    for A in range(M+1):
        for B in range(N+1):
            if (A>=1 and A <=M):
                if (B>=1 and A <=N):
                    ans = (A**(1./3.)) + (B**(1./3.))
                    if (ans ** 3).is_integer():
                        count = count + 1
    return count

print(cubeNumbers(1,8))