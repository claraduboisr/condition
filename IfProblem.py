try:
    gross = int(input("gross"))
    kids = int(input("kids"))

except:
    print ("check input")

if gross<1000:
    tax = 0.1
elif gross<2000:
    tax = 0.12
elif gross<4000:
    tax = 0.14
else:
    tax = 0.18
if gross<2000:
    tax = tax - kids * 0.09
else:
    tax = tax - kids *0.005

net = gross*(1-tax)
print(net)