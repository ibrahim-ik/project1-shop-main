####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["Vanilla", "Chocolate", "Strawberry", "Caramel", "Raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Ebraheem cupcakes shop."
signature_flavors = ["Mango","Orange","Apple","Peppsi","Banana"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    print("Welcome to %s, let me show you the menu...") % (cupcake_shop_name)
    for key, value in menu.items():

        print("- %s %s KD.") % (key, value)


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each and the flavors are):" % original_price)
    for item in original_flavors:
        print("- %s.") % (item)



def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Also, we have signature flavor cupcake (KD %s each and the flavors are):" % signature_price)
    for item in signature_flavors:
        print("- %s.") % (item)


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    if order == "original cupcake" or order == "Vanilla" or order == "Chocolate" or order == "Strawberry" or order == "Caramel" or order == "Raspberry" or order == "signature cupcake" or order == "Mango" or order == "Orange" or order == "Apple" or order == "Peppsi" or order == "Banana" or order == "coffee" or order == "tea" or order == "bottled water":
        return True

    else:
        return False

def get_order():

    order_list = []
    new_order = raw_input("what is your order?...: \t\t")
    while new_order != "Exit":
        if is_valid_order(new_order) == True:
            order_list.append(new_order)
            new_order = raw_input("and ?...\t\t")
        else:
            new_order = raw_input("you entered an invalid order, please re order...")


    return order_list


def accept_credit_card(total):
    if total >= 5:
        return True
    else:
        return False



def get_total_price(order_list):
    total = 0
    for i in range(0,len(order_list)):
        for j in range(0,len(original_flavors)):
            if order_list[i] == original_flavors[j]:
                total = total + 2.000

        for j in range(0,len(signature_flavors)):
            if order_list[i] ==signature_flavors[j]:
                total = total + 2.750

        if order_list[i] == "coffee":
            total = total + 1.000

        elif order_list[i] == "tea":
            total = total + 0.900

        elif order_list[i] == "bottled water":
            total = total + 0.750

    return total


def print_order(order_list):

    
    print("Your order is: \n")
    for item in order_list:
        print("- %s.") % (item)

    print("and your total price is: %s ") % (get_total_price(order_list))
    
    if accept_credit_card(get_total_price(order_list)) == True:
        print("BTW you can pay by your credit card")
    else:
        print("we are sorry you cannot pay with you credit card")

    print("\nthanks for bying from %s, hope to see you again.") % (cupcake_shop_name)
    # your code goes here!
