#Funtion for Calculation part
def calc(a, b, c, d):
	return (a*c)/(b*d)

#Function for Queriying Price Elsticity Demand


def ped():
	cd = float(input("Enter current quantity demanded :"))
	cp = float(input("Enter current price :"))
	q = float(input("Enter Initial Quantity Demanded :"))
	p = float(input("Enter Initial Price :"))
	dq = cd-q
	dp = cp-p
	pedval = calc(dq, dp, q, p)
	if pedval > 0:
		pedval = pedval
	else:
		pedval *= (-1)
	print()
	print("------------------------------------------------------")
	print("Price Elasticity of Demand is :", round(pedval, 2))
	if 0 < pedval < 1:
		print("Price Elasticity of demand is Inelastic")
	elif pedval == 0:
		print("Price Elasticity of demand is Perfectly Inelastic")
	elif pedval == 1:
		print("Price Elasticity of demand is Unitary elastic")
	elif pedval > 1:
		print("Price Elasticity of demand is Elastic")
	elif dp == 0:
		print("Price Elasticity of demand is Perfectly Elastic")
	print("------------------------------------------------------")
	rev(cp, cd, q, p, pedval)

#Function for Queriying Cross Elsticity Demand


def xED():
	xdq = float(input("Enter Change in quantity demanded of Good X :"))
	ydp = float(input("Enter Change in price of Good Y :"))
	xq = float(input("Enter Initial Quantity Demanded of Good X :"))
	yp = float(input("Enter Initial Price of Good Y :"))
	xedval = calc(xdq, ydp, yp, xq)
	print("------------------------------------------------------")
	print("Cross Elasticity of Demand is :", round(xedval, 2))
	if xedval > 0:
		print("Good X and Good Y are Close Subtitude Goods")
	else:
		print("Good X and Good Y are Complementary Goods")

#Function for Queriying Income Elsticity Demand


def yED():
	xdq = float(input("Enter Change in quantity demanded of Good :"))
	dyinc = float(input("Enter Change in Income :"))
	xq = float(input("Enter Initial Quantity Demanded of Good :"))
	yinc = float(input("Enter Initial Income :"))
	yedval = calc(xdq, dyinc, xq, yinc)
	print("------------------------------------------------------")
	print("Income Elasticity of Demand is :", round(yedval, 2))
	if yedval > 0:
		print("Good is Normal Good")
	else:
		print("Good is Inferior Good")

#Function for Queriying Price Elsticity Supply


def pes():
	ds = float(input("Enter Change in quantity supplied :"))
	dp = float(input("Enter Change in price :"))
	s = float(input("Enter Initial Quantity supplied :"))
	p = float(input("Enter Initial Price :"))
	pesval = calc(ds, dp, s, p)
	if pesval > 0:
		pesval = pesval
	else:
		pesval *= -1
	print("------------------------------------------------------")
	print("Price Elasticity of Supply is :", round(pesval, 2))

#Function for calculating Total Revenue


def rev(a, b, c, d, e):
	int_rev = c*d
	new_rev = a*b
	print("Initial Revenue is: ", int_rev)
	print("New Revenue is: ", new_rev)
	if (e < 1) and ((a-d) > 0):
		print("Increase in Total Revenue is: ", round((new_rev-int_rev), 2))
	elif (e < 1) and ((a-d) < 0):
		print("Decrease in Total Revenue is: ", round((int_rev-new_rev), 2))
	elif (e > 1) and ((a-d) > 0):
		print("Decrease in Total Revenue is: ", round((int_rev-new_rev), 2))
	elif (e > 1) and ((a-d) < 0):
		print("Increase in Total Revenue is: ", round((new_rev-int_rev), 2))


#Main Function
while True:
	print("Elasticity-Calculator-204216D-IS1020-Assignment-2")
	print("What type of Elasiticity do you want to Calculate ..?")
	print('''
			  [1] Price Elasticity Demand
			  [2] Cross Elasticity Demand
			  [3] Income Elasticity of Demand
			  [4] Price Elasticity of Supply
		''')
	ans = int(input("Input Enter the number of the type: "))
	if ans == (1):
		ped()
	elif ans == (2):
		xED()
	elif ans == (3):
		yED()
	elif ans == (4):
		pes()
	else:
		continue
	print("------------------------------------------------------")
	ans_ = str(input("Do you want to calculate again (Y/N) ? "))
	if (ans_ == 'Y') or (ans_ == 'y') or (ans_ == 'Yes') or (ans_ == 'yes'):
		continue
	elif (ans_ == 'N') or (ans_ == 'n') or (ans_ == 'no') or (ans_ == 'No'):
		break
	else:
		print("Incorrect Input")
		print()
		break
