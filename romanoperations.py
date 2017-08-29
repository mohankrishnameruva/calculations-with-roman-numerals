import sys

print('Welcome')
print(' Here you can do arithmetic operations on Roman Numerals')
print('Type your operands and operator')

#First we convert roman numbers to arabic and perform required operation and covert them back
#to roman numbers which are ready for output
def romantoarabic(roman):
# We add roman numbers to "tot" in left to right order
	roman_conver=[  (1,'I'),
		   			(5,'V'),
		   			(10,'X'),
		   			(50,'L'),
		   			(100,'C'),
		   			(500,'D'),
		   			(1000,'M')
		   						]
	tot = 0             			#Initialize our required arabic number
	prev = 10000					# In case of IV(4) and IX(9) we need to remember the previous values to subtract 
									# them when the followning number is larger
	for i in range(0,len(roman)):
		for each in roman_conver:
									# We take each element in roman and compare it with roman_conver
			if roman[i]==each[1]:
				if each[0]>prev:
					tot = tot + each[0] - 2*prev
				else:
					tot = tot + each[0]
				prev = each[0]       #updating previous value
	return tot

def arabictoroman(arabic):
		conv = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
	           [ 100, 'C'], [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'],
	           [  10, 'X'], [  9, 'IX'], [  5, 'V'], [  4, 'IV'],
	          [   1, 'I']]
		i = 0 
		tot = str()
		while arabic > 0:
	  		while conv[i][0] > arabic: i = i + 1 
	  		tot = tot + conv[i][1] 
	  		arabic = arabic - conv[i][0]
		return tot

loop = 'y'
while loop == 'y':
	operand_1 = input('Input your first operand:')
	operator = input('Input operator:')
	operand_2 = input('Input second operand:')

	romannumerals= ['I','V','X','L','C','D','M']

	value_1 = romantoarabic(operand_1.upper())
	value_2 = romantoarabic(operand_2.upper())
	for each in operand_1.upper():
		if each not in romannumerals:
			print('Error :operand_1 is not a roman number')
			sys.exit(1)
			break
	for each in operand_2.upper():
		if each not in romannumerals:
			print('Error :operand_2 is not a roman number')
			sys.exit(1)
			break
	if operator == '+':
		result = value_1 + value_2
		print(operand_1.upper() + operator + operand_2.upper() + '=' + arabictoroman(result))
	elif operator == '-':
		result = value_1 - value_2
		print(operand_1.upper() + operator + operand_2.upper() + '=' + arabictoroman(result))
	elif operator == '*':
		result = value_1 * value_2
		print(operand_1.upper() + operator + operand_2.upper() + '=' + arabictoroman(result))
	elif operator == '/':
		result = value_1 / value_2
		print(operand_1.upper() + operator + operand_2.upper() + '=' + arabictoroman(result))
	else:
		print("Error :Operation not possible.Please try again. Operator should be one of '+','-','/','*'")	
	# Alternative arabic to roman conversion(Manual)
	# def arabictoroman(arabic):	
	# 	tot = str()
	# 	no =0
	# 	while arabic!=0:
	# 		if arabic>=1000:	
	# 			no = arabic//1000
	# 			arabic = arabic % 1000
	# 			tot = tot + str('M'*int(no))
	# 		if arabic<1000 and arabic>=900:	
	# 			no = arabic//900
	# 			arabic = arabic % 900
	# 			tot = tot + str('CM'*int(no))
	# 		if arabic<900 and arabic>=500:
	# 			no = arabic//500
	# 			arabic = arabic % 500
	# 			tot = tot + str('D'*int(no))
	# 		if arabic<500 and arabic>=400:
	# 			no = arabic//400
	# 			arabic = arabic % 400
	# 			tot = tot + str('CD'*int(no))
	# 		if arabic>=100 and arabic <400:	
	# 			no = arabic//100
	# 			arabic = arabic % 100
	# 			tot = tot + str('C'*int(no))
	# 		if arabic<100 and arabic>=90:
	# 			no = arabic//90
	# 			arabic = arabic % 90
	# 			tot = tot + str('XC'*int(no))
	# 		if arabic<90 and arabic>=50:
	# 			no = arabic//50
	# 			arabic = arabic % 50
	# 			tot = tot + str('L'*int(no))
	# 		if arabic>=40 and arabic<50:	
	# 			no = arabic//40
	# 			arabic = arabic % 40
	# 			tot = tot + str('XL'*int(no))
	# 		if arabic>=10 and arabic<40:	
	# 			no = arabic//10
	# 			arabic = arabic % 10
	# 			tot = tot + str('X'*int(no))
	# 		if arabic<10 and arabic>=9:
	# 			no = arabic//9
	# 			arabic = arabic % 9
	# 			tot = tot + str('IX'*int(no))
	# 		if arabic<9 and arabic>=5:
	# 			no = arabic//5
	# 			arabic = arabic % 5
	# 			tot = tot + str('V'*int(no))		
	# 		if arabic<5 and arabic>=4:
	# 			no = arabic//4
	# 			arabic = arabic % 4
	# 			tot = tot + str('IV'*int(no))
	# 		if arabic<4:
	# 			no = arabic//1
	# 			arabic = arabic % 1
	# 			tot = tot + str('I'*int(no))				
	# 	return tot
	loop = input('To continue press "y" To abort press "n"')

