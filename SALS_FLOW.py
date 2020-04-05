#FLOW, DATA, AND ITERATION Sal's Shipping based on Python Control Flows
def costground(weight):
  if weight <= 2 :
    cost1 = (weight *1.50) + 20
    return cost1
  elif weight > 2 and weight <=6:
    cost2 = (weight *3) + 20
    return cost2
  elif weight > 6 and weight <=10:
    cost3 = (weight *4) + 20
    return cost3
  else:
    cost4 = (weight *4.75) + 20
    return cost4
firstweight = costground(8.4)
print(firstweight)

premiumweight = 125

def droneshipping(weight):
  if weight <= 2 :
    cost5 = (weight *4.50) 
    return cost5
  elif weight > 2 and weight <=6:
    cost6 = (weight *9) 
    return cost6
  elif weight > 6 and weight <=10:
    cost7 = (weight *12) 
    return cost7
  else:
    cost8 = (weight *14.25) 
    return cost8
secondweight = droneshipping(1.5)
print(secondweight)

def cheapshipping(weight):
  if costground(weight) > droneshipping(weight):
    return "drone shipping method and will cost $ " + str(droneshipping(weight))
  elif costground(weight) > droneshipping(weight):
    return "ground shipping method and will cost $ " + str(costground(weight))
  elif premiumweight > costground(weight):
    return "ground shipping method and will cost $ " + str(costground(weight))
  elif premiumweight < costground(weight):
    return "premium shipping method and will cost $ " + str(premiumweight)
  elif premiumweight < droneshipping(weight):
    return "premium shipping method and will cost $ " + str(premiumweight)
  else:
    return "drone shipping method and will cost $ " + str(droneshipping(weight))
  
cheap = cheapshipping(4.8)
print("The shipping of 4.8 pound is " + str(cheap))
cheap = cheapshipping(41.5)
print("The shipping of 41.5 pound is " + str(cheap))

  
   


  