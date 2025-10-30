N=int(input())
prime_sum=0
for i in range(2,N+1):
    is_prime=True
    for j in range(2,int(i**0.5)+1):
        if i %j==0:
            is_prime=False
            break
    if is_prime:
        prime_sum +=i 

print(prime_sum)
