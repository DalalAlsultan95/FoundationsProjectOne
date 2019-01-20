####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Sprinckles"
signature_flavors = "Birthday cake", "Bubble gum"
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    for key,value in menu.items():
        print (key,value)


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for cupcake in original_flavors:
        print (cupcake)


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for cupcake in signature_flavors:
        print (cupcake)


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    if order in signature_flavors:
        return True
    elif order in original_flavors:
        return True
    elif order in menu:
            return True
    else:
            return False


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here
    user_input = input("what is your order? exit to checkout\n")
    while user_input.lower() != "exit":
        if is_valid_order(user_input) == True:
            order_list.append(user_input)
        print("[%s] has been added" % user_input)
        user_input = input("what else? \n")
    else:
        print("Not on the menu")
        user_input = input ("please enter a valid flavor \n")
        return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total >= 5:
        print ("we can put that on a card")
    else:
        print ("cash only")


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for order in order_list:
        if order in original_flavors:
            totaal += original_price
        elif order in signature_flavors:
            total += signature_price
        elif order in menu:
            total += menu[order]
    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    print("This is your order %s" % order_list)
    x= get_total_price(order_list)
    print ("%0.3f KWD" % x)
