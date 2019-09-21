# Chaos function
def main():
	print("This program illustrates a chaotic behavior")
	x = eval(input("Enter a number between 0 and 1: "))
  value = eval(input("Enter the number of repetitions: " ))
	for i in range(value):
		x = 3.9 * x * (1-x)
		print(x)  
               
main()
