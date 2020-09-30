Input = input("Enter a phrase: ").upper()

lzt = list(Input)

k = 0

for i in range(len(lzt)):

	k = k + 1

	for j in range(k):

		print(lzt[j], end = "")
		
	print()