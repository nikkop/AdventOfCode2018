def ask_add_to_cart(cart):
    item = input("Vad vill du lägga till? ")
    cart.append(item)
    show_cart = input("Vill du se din shoppinglista? ")
    if show_cart.lower() == "ja":
        print(cart)
    add_more = input("Vill du lägga till fler varor? ")
    if add_more.lower() == "ja":
        ask_add_to_cart(cart)

cart = list()
ask_add_to_cart(cart)