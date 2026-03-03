my_set_1 = set()
my_set_2 = set()
my_set_3 = set()
my_set_4 = set()

N = 100

#even numbers 0-100
for number in range(2,N+1,2):
    my_set_1.add(number)
print("Even numbers: ",my_set_1)

#odd numbers 0-100
for number in range(0,N):
    if number % 2 != 0:
        my_set_2.add(number)
print("Odd numbers: ",my_set_2)

#pollaplasia tou 3 , 0-100
for number in range(3,N,3):
    my_set_3.add(number)
print("Multiples 3: ",my_set_3)

#What is a prime number in maths?
#A prime number is any positive number that can only be divided by itself and the number 1
#ta sinola twn prwtwn apo to 0 ews to 100

for number in range(2, N+1):  # ξεκινάμε από το 2
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        my_set_4.add(number)

print("Prime numbers: ",my_set_4)



