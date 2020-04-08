hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Prices and Cuts:

total_price=0
for price in prices:
  total_price+=price

average_price=total_price/len(prices)
print("Average Haricut Price: <${0}".format(round(average_price,2)) +">")
new_prices=[pri-5 for pri in prices]
print(new_prices)

#Revenue:
total_revenue=0
for i in range(0, len(hairstyles)):
  total_revenue+=prices[i] * last_week[i]
print("Total Revenue: <${0}".format(total_revenue)+">")
average_daily_revenue=total_revenue/7
print("Average Daily Revenue: <${0}".format(average_daily_revenue)+">")

cuts_under_30=[hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] <30]

print(cuts_under_30)

  

