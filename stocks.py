#Kristina Shaw
#CS-175L
#stocks.py

#declare variables with user input
commission_rate = input("What was the commission rate?: ")
num_shares = input("How many shares did you purchase?: ")
purchase_price = input("What was the purchase price?: ")
selling_price = input("What was the selling price?: ")

#calculations
amountPaidForStock = (float(num_shares) * float(purchase_price))
purchaseCommission = (float(commission_rate) * float(amountPaidForStock))
totalPaid = (float(amountPaidForStock) + float(purchaseCommission))
stockSoldFor = (float(num_shares) * float(selling_price))
sellingCommission = (float(commission_rate) * float(stockSoldFor))
totalReceived = (float(stockSoldFor) - float(sellingCommission))
profitOrLoss = (float(totalReceived) - float(totalPaid))

#display results
print("Amount paid for stock: $", amountPaidForStock)
print("Commission paid on the purchase: $", purchaseCommission)
print("Amount the stock sold for: $", stockSoldFor)
print("Commission paid on the sale: $", sellingCommission)
print("Total commission paid: $", totalReceived)
print("Profit (or loss if negative): $", profitOrLoss)
