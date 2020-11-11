count = 0
sum = 0
largest = None
smallest = None
while True:
    a = input("Enter a number:")
    if a == 'done':
        break
    else:
        try:
            b = float(a)
            sum = sum + b
            count = count + 1
        except:
            print('Invalid input')
            continue

    if smallest is None:
        smallest = b
    elif smallest > b:
        smallest = b
    if largest is None:
        largest = b
    elif largest < b:
        largest = b

print("Maximum is",int(largest))
print("Minimum is",int(smallest))
