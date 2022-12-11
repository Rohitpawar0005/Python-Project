def prime_composite(num):
    if num == 1:
        print("1 is neither prime nor composite")
    elif num == 2 or num == 3:
        print(num,"is a Prime number")
    elif num > 3:
        for i in range(2,num):
            if num%i == 0:
                print(num,"is a Composite number")
                break
        else:
            print(num,"is a Prime number")
    else:
        print("Enter a number greater than zero")
        

n1 = int(input("Your Starting Number: "))
n2 = int(input("Your Ending Number: "))
print("Range is ({},{})".format(n1,n2))
#prime_composite(n)

for i in range(n1,n2+1):
    prime_composite(i)