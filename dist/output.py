##New python script
def main():
	num1, num2, may = 0, 0, 0
	print("digite un numero entero positivo ")
	num1 = input()
	print("digite un numero entero positivo ")
	num2 = input()
	may=mayor(num1,num2)
	print("El numero mayor es ",may)

if __name__ == '__main__':
	main() 

def mayor(num1,num2) : 
 	res=0
	if num1>num2:
		res=num1
	else:
		res=num2
	return res


##Termine :)
 