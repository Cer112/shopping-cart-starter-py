# shopping_cart.py

import datetime 

t = datetime.datetime.now()
print(type()) 
print(t)



products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# TODO: write some Python code here to produce the desired functionality...

print(products)

# an infinite loop! you can press control+c to cancel the program if/when it gets stuck...
while True:
    # capturing user input and storing in a variable
    user_input = input("Please input a product identifier, or 'DONE' if there are no more items: ")
    # demonstrating ability to recognize what the input was, although you might also want to check its datatype
    print("YOUR INPUT WAS: " + user_input)

#starting everything that he shows us in class...need to create environment


#for p in products:
    #print(p)


x = 1

while x < 5:
    y = input("Please input a product id: ")
    print(x)
    x = x + 1 #this is a variable assignment, assigning a value to x



#getting a running total for price

print("STARTED AT: " + t)


x = 1

running_total = 0

while x < 5: #would need to allow this loop to run through infinite times
    #need to ask the user for an input that is the product ID, instead of hardcoding the product
    selected_id = input("Please select a product id (1-20)") 
    #product = 
    #"id":1, 
    #"name": "Chocolate Sandwich Cookies", 
    #"department": "snacks", "aisle": 
    #"cookies cakes", 
    #"price": 3.50
    #}
    matching_products = [p for p in products if p["id"] == selected_id]
    #return some items in a list of items if the item meets a certain criteria (^^^) p is the item in our list of products. 
    product = matching_products[0] #this is the index value lookup within the list that we are returning...and instead of starting at 1, this index starts at 0
    price =  product["price"] 4.95 #need to lookup the actual price of the product instead of hardcoding...do that by using square brackets and identify which part of product we want. 
    running_total = running_total + price
    x = x + 1

print("THE TOTAL PRICE IS: " + str(running_total)) #need to add tax to the total value
 

#new concept...using modules and loading them...can create custom modules...usually do them at top of file 


