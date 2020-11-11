count = 0
sum = 0
while True:
    a = input("Enter a number:")
    if a == 'done':
        break
    else:
        try:
            b = float(a)
            sum = sum + b
            count = count + 1
            continue
        except:
            print('Invalid input')
            continue

print(sum,count,sum/count)
