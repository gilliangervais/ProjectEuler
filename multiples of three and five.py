def multiples_of_three_and_five():
    n = []
    for i in range(1,1000):
        if i % 3 == 0 or i % 5 == 0:
            n.append(i)
    return sum(n)
print multiples_of_three_and_five()

