import consts
import data_service as dts
import active_user


def main():
    while True:
        try:
            print_header(consts.header)
            register_or_login()
        except KeyboardInterrupt:
            return


def register_or_login():
    ans = input("press [L] to login or [R] to register, "
                "[W] to login as a restaurant worker or [X] to exit: ").upper().strip()

    if ans == 'L':
        login_user()
    elif ans == 'R':
        register_user()
    elif ans == 'W':
        login_worker()
        show_options_for_logged_workers()
    elif ans == 'X' or 'EXIT':
        exit_app()
    else:
        print("Please enter a valid input ", end='\n\n')
        register_or_login()


# Functions for users:

# show menu of options after login
def show_options_user():
    chosen_option = input(consts.options).upper()
    if chosen_option == 'O':
        order = order_a_meal()
        dts.add_order(active_user.active_email_account, order)
    elif chosen_option == 'R':
        add_review()
    elif chosen_option == 'C':
        change_address()
    elif chosen_option == 'X':
        exit_app()
    else:
        print("Please enter a valid input")
        show_options_user()


def login_user():
    print('****************LOGIN****************')
    print("(press X to exit)")
    email = input("Email: ")
    if email.upper() == 'X':
        exit_app()
    if not dts.search_email_db(email):
        print("Plesae enter an existing email!")
        login_user()
    password = str(input("Password: "))
    current_user = dts.login_user(email, password)
    if not current_user:
        print("wrong password! ")
        exit_app()
    active_user.active_email_account = current_user["email"]
    show_options_user()


def register_user():
    print('****************REGISTER****************')
    name = str(input("Whats your name? ").capitalize())
    email = str(input("Whats your email? "))
    if dts.search_email_db(email):  # check if user already exists
        print("This e-mail already exists! ")
        exit_app()
    valid_email = dts.validate_email(email)
    if not valid_email:
        print("Invalid email! ")
        register_or_login()
    password = str(input("choose a password: "))
    address = str(input("whats your address? "))
    dts.register_user(name, email, password, address)
    exit_app()


def show_menu(menu):
    list_burgers = ', '.join(burger for burger in menu["burgers"])
    list_doneness = ', '.join(stage for stage in menu["stages of doneness"])
    list_toppings = ', '.join(top for top in menu["toppings"])
    list_drinks = ', '.join(drink for drink in menu["drinks"])
    list_sides = ', '.join(side for side in menu["sides"])
    return {'burgers': list_burgers, 'donness': list_doneness, 'toppings': list_toppings, 'drinks': list_drinks,
            'sides': list_sides}


def order_a_meal():
    menu = show_menu(consts.original_menu)
    burger_weight = str(input(f"choose the weight of your burger (in grams){menu.get('burgers')}: "))
    stages_of_doneness = input(f"choose the stages of doneness {menu.get('donness')}: ")
    toppings = input(f"choose one topping {menu.get('toppings')}: ")
    drink = input(f"choose a drink {menu.get('drinks')}: ")
    side = input(f"choose a side {menu.get('sides')}")
    order = f"a {stages_of_doneness} {burger_weight} gram hamburger with {toppings}, " \
            f"some {side} on the side and a {drink}"
    return order


def add_review():
    review = input("please write your unanimous review: ")
    dts.add_review(review)
    print("Thank you for your honest review")


def change_address():
    new_address = input("What is your new address? ")
    email = active_user.active_email_account
    dts.change_address(new_address, email)
    print("Address changed successfully!")


# Functions for workers:
def show_options_for_logged_workers():
    ans = input(consts.options_for_worker).upper()
    if ans == 'S':
        dts.show_orders_worker()
    elif ans == 'D':
        delete_order()
    elif ans == 'R':
        dts.show_reviews()
    elif ans == 'N':
        # only logged in worker can register a new one
        register_new_worker()
    elif ans == 'X':
        exit_app()
    else:
        print("Please enter a valid input")
        show_options_for_logged_workers()


def login_worker():
    print('****************WELCOME TO WORK****************')
    name = str(input("Name: "))
    password = str(input("Password: "))
    is_worker = dts.login_worker(name, password)
    if not is_worker:
        print("wrong name or password")
        exit_app()


def delete_order():
    _id = str(input("what is the order id: "))
    dts.delete_order(_id)
    print(f"order with id '{_id}' was deleted successfully!")


def register_new_worker():
    name = input("Name: ")
    password = input("Choose a password: ")
    dts.register_worker(name, password)


# System functions

def print_header(header):
    print(header)


def exit_app():
    print("please login again to continue")
    print('Goodbye!')
    raise KeyboardInterrupt()


if __name__ == '__main__':
    main()
