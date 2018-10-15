fizbuz= (int(input("Type a number: "))+1)

count=0
while count < fizbuz:
    if count % 5 == 0 and count % 3 == 0:
        print ("FizzBuzz")
    elif count % 3 == 0:
        print("Fizz")
    elif count % 5 == 0:
        print("Buzz")
    else:
        print (count)
    
    count = count + 1



