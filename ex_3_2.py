score = input("Enter Score: ")
s = float(score)

if s>=0&&s<=1:
	if s>=0.9:
		print('A')
	elif (s>=0.8&&s<0.9):
		print('B')
	elif (s>=0.7&&s<0.8):
		print('C')
	elif (s>=0.6&&s<0.7):
		print('D')
	elif (s<0.6):
		print('F')
else:
    print('Error')
