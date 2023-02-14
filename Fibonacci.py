a = int(input("Introduceti valoarea="))
n1 , n2 = 0 , 1
sum = 0
if a <= 0:
    print("Introduceti o valoarea mai mare ca 0")
else:
    for i in range(0, a):
     print(sum, end=" ")
     n1 = n2
     n2 = sum
     sum = n1 + n2
     

