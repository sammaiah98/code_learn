# Prime Program

nums = [n for n in range(50)]
prim_numbers = []

for n in nums:
    prime_num = 1
    if n > 1 :
        for i in range(2, round(n/2)+1):
            if (n%i) == 0:
                prime_num = 0
                break
    else:
        prime_num = 0
    if prime_num == 1:
        prim_numbers.append(n)
print(prim_numbers)

