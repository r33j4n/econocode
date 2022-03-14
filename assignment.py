#Funtion for Calculation
def calc(a,b,c,d):
	return (a*c)/(b*d)

#Function for Queriying Price Elsticity Demand
def ped():
	dq=float(input("Enter Change in quantity demanded :"))
	dp=float(input("Enter Change in price :"))
	q=float(input("Enter Initial Quantity Demanded :"))
	p=float(input("Enter Initial Price :"))
	pedval=calc(dq,dp,q,p)
	if pedval>0:
		pedval=pedval 
	else:
		pedval*=(-1)
	print("------------------------------------------------------")
	print("Price Elasticity of Demand is :",round(pedval,2))
	if 0<pedval<1:
		print("Price Elasticity of demand is Inelastic")
	elif pedval==0:
		print("Price Elasticity of demand is Inelastic")
	if pedval==1:
		print("Price Elasticity of demand is Unitary elastic")
	if pedval>1:
		print("Price Elasticity of demand is Elastic")
	if dp==0:
		print("Price Elasticity of demand is Perfectly Elastic")

#Function for Queriying Cross Elsticity Demand
def xED():
	xdq=float(input("Enter Change in quantity demanded of Good X :"))
	ydp=float(input("Enter Change in price of Good Y :"))
	xq=float(input("Enter Initial Quantity Demanded of Good X :"))
	yp=float(input("Enter Initial Price of Good Y :"))
	xedval=calc(xdq,ydp,xq,yp)
	print("------------------------------------------------------")
	print("Cross Elasticity of Demand is :",round(xedval,2))
	if xedval>0:
		print("Good X and Good Y are Close Subtitude Goods")
	else:
		print("Good X and Good Y are Complementary Goods")

#Function for Queriying Income Elsticity Demand
def yED():
	xdq=float(input("Enter Change in quantity demanded of Good :"))
	dyinc=float(input("Enter Change in Income :"))
	xq=float(input("Enter Initial Quantity Demanded of Good :"))
	yinc=float(input("Enter Initial Income :"))
	yedval=calc(xdq,dyinc,xq,yinc)
	print("------------------------------------------------------")
	print("Income Elasticity of Demand is :",round(yedval,2))
	if yedval>0:
		print("Good X and Good Y are Normal Goods")
	else:
		print("Good X and Good Y are Inferior Goods")

#Function for Queriying Price Elsticity Supply
def pes():
	ds=float(input("Enter Change in quantity supplied :"))
	dp=float(input("Enter Change in price :"))
	s=float(input("Enter Initial Quantity supplied :"))
	p=float(input("Enter Initial Price :"))
	pesval=calc(dq,dp,q,p)
	if pesval>0:
		pesval=pesval
	else:
		pesval*=-1
	print("------------------------------------------------------")
	print("Price Elasticity of Supply is :",round(pesval,2))

def rev(a,b,c,d):
	int_rev= c*d
	new_rev= (c+a)*(b+c)
	print("Initial Revenue is: ",int_rev)
	print("New Revenue is: ",int_rev)
	if calc(a,b,c,d)<1:
		print("Decrease in Revenue is: ",int_rev-new_rev)
	elif calc(a,b,c,d)>1:
		print("Decrease in Revenue is: ",int_rev-new_rev)

#Main Function
while True:
	print("Elasticity-Calculator-204216D-IS1020-Assignment-2")
	print("What type of Elasiticity do you want to Calculate ..?")
	print(''' 
			  [1] Price Elasticity Demand
			  [2] Cross Elasticity Demand
			  [3] Income Elasticity of Demand
			  [4] Price Elasticity of Supply
			  [5] Calculate Total Revenue Status
		''')
	ans=int(input("Input Enter the number of the type: "))
	if ans==(1):
		ped()
	elif ans==(2):
		xED()
	elif ans==(3):
		yED()
	elif ans==(4):
		pes()
	print("------------------------------------------------------")
	ans_=str(input("Do you want to calculate again (Y/N) ? "))
	if (ans_=='Y') or (ans_=='y') or (ans_=='Yes') or (ans_=='yes'):
		continue 
	elif (ans_=='N') or (ans_=='n') or (ans_=='no') or (ans_=='No'):
		break
	else:
		print("Incorrect Input")
		print()
		break

