import data
import functions

def show_main_menu():
    current_order = []
    while True:
        print("Saketh Krovvidi's diner")  # Display your name
        print("__________")
        print('N for a new order')
        print("C to change the current order")
        print('X for close orders and print the check')
        print("R to reset the order")
        print('Q for quit')
        user_menu_choice = input('Your input: ')
        
        if user_menu_choice in 'Qq':
            break
        elif user_menu_choice in 'Xx':
            print('This option prints the list of items ordered, extended price, total, Taxes, and Grand total')
            print_check(current_order)
        elif user_menu_choice in 'Cc':
            current_order = change_order(current_order)  # Change items in the order
        elif user_menu_choice in 'Nn':
            print('New order')
            while input('Add a dish? y/n: ') in 'Yy':
                item_code, quantity = input("Enter item code and quantity: ").split()
                if functions.process_customer_request(data.menu_dict, item_code, quantity):
                    current_order.append((item_code, quantity))
                print('your order: ',current_order)
        elif user_menu_choice in 'Rr':
            current_order = []  # Reset the order

def print_check(current_order):
    print("\nYour order:")
    print('your check')

def change_order(current_order):
    print("Change the order:")

if __name__ == '__main__':
    #initialize the lists
    drinks = []
    appetizers = []
    salads = []
    entrees = []
    dessert= []
    #print(functions.get_item_information('D1'))
    show_main_menu()