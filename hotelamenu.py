menu = {
    "Pizza":500,
    "Pasta": 80,
    "Coffee":90,
    "Tea":30,
    'Burger':50,
    'Salad':80
}

#Greet
print("Welcome to my first python Restaurand project menu !")
print("1) Pizza : Rs500\n2) Pasta : Rs80\n3) Coffee : Rs90 \n4) Tea : Rs30\n5) Burger : Rs50\n6) Salad : Rs80\n")


order_total = 0

item1 = input("Enter the name of item you want to order :")
if item1 in menu :
    order_total += menu[item1]
    print(f'you item {item1} has been added your order !')

else :
    print(f'item {item1} has not avaialable yet')

another_order = input("Do you want to add another item ? (Yes/No) ")

if another_order == "Yes":
    item2 = input("Enter the name of second item :")
    if item2 in menu :
        order_total += menu[item2]
        print(f"item {item2} has been added your order !")

    else :
        print(f"item {item2} is not avaialable !")
print(f"Total order amount of item to pay is {order_total} ")