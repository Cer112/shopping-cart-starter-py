 # shopping_cart.py

import datetime

tax rate = .06

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
@ -27,9 +31,33 @@ products = [

print(products)

# an infinite loop! you can press control+c to cancel the program if/when it gets stuck...
total_price = 0
selected_ids = []
running_total = 0
matching_product = []


while True:
    # capturing user input and storing in a variable
    user_input = input("Please input a product identifier, or 'DONE' if there are no more items: ")
    # demonstrating ability to recognize what the input was, although you might also want to check its datatype
    print("YOUR INPUT WAS: " + user_input)
    selected_id = input("Please input a product identifier: ") #> "9" (string)
    if selected_id == "Done": 
        break
    else:
        selected_ids.append(selected_id) 

for selected_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    total_price = total_price + matching_product["price"]
    print("SELECTED_PRODUCT: " + matching_product["name"] + "" + str(matching_product["price"]


#print("total price: ") + str(running_total))
#running_total = running_total + total_price
#add tax to thi

t = 0

t = datetime.datetime.now()
print(type()) 
print(t)
print(t.strftime("%Y-%m-%d"))


print("hello")