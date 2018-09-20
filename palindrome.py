
a = 1234321
temp_a = a
b = 0
while temp_a>0:
    b = 10*b+(temp_a%10)
    temp_a = temp_a//10
    print (a,b)
if a==b:
    print ("it is palindrome")