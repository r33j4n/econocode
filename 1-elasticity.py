import numpy as np
from shapely.geometry import  LineString
#Funtion for Calculation part
def calc(a, b, c, d):
	return (a*d)/(b*c)

def ped():
	print("What do you want to calculate ?")
	print('''
				[1] Price Elasticity Demand
				[2] Current Quantity Demanded
				[3] Current Price Demanded
				[4] Initial Quantity Demanded
				[5] Initial Price

		''')
	ans= int(input("Enter the number of the Calculation"))
	print("If Any Data not related to the Calculation input 0 and hit Enter")
	cd = float(input("Enter current quantity demanded :"))
	cp = float(input("Enter current price :"))
	q  = float(input("Enter Initial Quantity Demanded :"))
	p  = float(input("Enter Initial Price :"))
	e  = float(input("Enter Elasticity of Demand :"))
	e*=-1
	dq = cd-q
	dp = cp-p
	if (ans==1):
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
		rev(cp, cd, q, p,pedval)
	elif (ans==2):
		cd=calc(e, p, 1/dp, q)+q
		print("Current Quantity Demanded is ",calc(e, p, 1/dp, q)+q," Units")
	elif (ans==3):
		cp=calc(e, dp, 1/q, dp)+p
		print("Current Price is ",calc(p, e, q, dq)+p," Rupees")
	elif (ans==4):
		q=calc(cd, 1, (e*dp+p), p)
		print("Initial Quanity Demanded is ",calc(cd, 1, (e*dp+p), p)," Units")
	elif (ans==5):
		p=calc(e, (dq+e*q), 1/cp, q)
		print("Initial Price is ",calc(e, (dq+e*q), 1/cp, q)," Rupees")
	print("------------------------------------------------------")
	if(ans!=1):
		rev(cp, cd, q, p,-1*e)


#Function for Queriying Cross Elsticity Demand
def xED():
	print("What do you want to calculate ?")
	print('''
				[1] Cross Elasticity Demand
				[2] Current Quantity Demand of Good X
				[3] Current Price of Good Y
				[4] Initial Quantity Demand of Good X
				[5] Initial Price of Good Y

		''')
	ans= int(input("Enter the number of the Calculation"))
	cxq = float(input("Enter current quantity demanded of Good X :"))
	cyp = float(input("Enter current price of Good Y :"))
	xq  = float(input("Enter Initial Quantity Demanded of Good X :"))
	yp  = float(input("Enter Initial Price of Good Y :"))
	e   = float(input("Input Cross Elasticity Demand"))
	dp=cyp-yp
	dq=cxq-xq
	print("------------------------------------------------------")
	if(ans==1):
		xedval = calc(cxq-xq, cyp-yp, xq, yp)
		print("Cross Elasticity of Demand is :", round(xedval, 2))
		if xedval > 0:
			print("Good X and Good Y are Close Subtitude Goods")
		else:
			print("Good X and Good Y are Complementary Goods")
	elif (ans==2):
		print("Current Quantity Demanded is ",calc(e, yp, 1/dp, xq)+xq," Units")
	elif (ans==3):
		print("Current Price is ",calc(yp, e, xq, dq)+yp," Rupees")
	elif (ans==4):
		print("Initial Quantity Demand of Good X is ",calc(cxq, 1, (e*dp+yp), yp)," Units")
	elif (ans==5):
		print("Initial Price is ",calc(e, (dq+e*xq), 1/cyp, xq)," Rupees")

#Function for Queriying Income Elsticity Demand
def yED():
	print("What do you want to calculate ?")
	print('''
				[1] Income Elasticity Demand
				[2] Current Quantity Demand
				[3] Current Income
				[4] Initial Quantity Demand
				[5] Initial Income

		''')
	ans= int(input("Enter the number of the Calculation"))
	cxq = float(input("Enter current quantity demanded of Good :"))
	cyinc = float(input("Enter current Income :"))
	xq = float(input("Enter Initial Quantity Demanded of Good :"))
	yinc = float(input("Enter Initial Income :"))
	e = float(input("Enter Income elsticity demamd:"))
	dq=cxq-xq
	dp=cyinc-yinc
	if (ans==1):
		yedval = calc(cxq-xq, cyinc-yinc, xq, yinc)
		print("------------------------------------------------------")
		print("Income Elasticity of Demand is :", round(yedval, 2))
		if yedval > 0:
			print("Good is Normal Good")
		else:
			print("Good is Inferior Good")
	elif (ans==2):
		print("Current Quantity Demanded is ",calc(e, yinc, 1/dp, xq)+xq," Units")
	elif (ans==3):
		print("Current Income is ",calc(yinc, e, xq, dq)+yinc," Rupees")
	elif (ans==4):
		print("Initial Quanity Demanded is ",calc(cxq, 1, (e*dp+yinc), yinc)," Units")
	elif (ans==5):
		print("Initial Income is ",calc(e, (dq+e*xq), 1/cyinc, xq)," Rupees")


#Function for Queriying Price Elsticity Supply
def pes():
	print("What do you want to calculate ?")
	print('''
				[1] Supply Elasticity Demand
				[2] Current Quantity Supplied
				[3] Current Price Demanded
				[4] Initial Quantity Supplied
				[5] Initial Price

		''')
	ans= int(input("Enter the number of the Calculation"))
	print("If Any Data not related to the Calculation input 0 and hit Enter")
	cs = float(input("Enter current quantity supplied :"))
	cp = float(input("Enter current price :"))
	s = float(input("Enter Initial Quantity supplied :"))
	p = float(input("Enter Initial Price :"))
	e= float(input("Enter Price Elasticity of Supply"))
	dq=cs-s
	dp=cp-p
	pesval = calc(cs-s, cp-p, s, p)
	if (ans==1):
		if pesval > 0:
			pesval = pesval
		else:
			pesval *= -1
		print("------------------------------------------------------")
		print("Price Elasticity of Supply is :", round(pesval, 2))
	elif (ans==2):
		print("Current Quantity Supplied ",calc(e, p, 1/dp, s)+s," Units")
	elif (ans==3):
		print("Current Price Demanded ",calc(p, e, s, dq)+p," Rupees")
	elif (ans==4):
		print("Initial Quantity Supplied ",calc(cs, 1, (e*dp+p), p)," Units")
	elif (ans==5):
		print("Initial Price ",calc(e, (dq+e*s), 1/cp, s)," Rupees")


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
def equb():
	supply = [12,10,8,6,4,2,0]
	demand = [0,2,2,3,4,5,6]
	price = [4000,3600,3200,2800,2400,2000,1600]
	line_1 = LineString(np.column_stack((supply, price)))
	line_2 = LineString(np.column_stack((demand, price)))
	intersection = line_1.intersection(line_2)
	x,y = intersection.xy
	print(x,y)


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
