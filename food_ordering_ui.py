import data
import functions

def show_main_menu():
    current_order = []
    while True:
        print("Saketh Krovvidi's diner")  # Display your name
        print("__________")
        print('N for a new order')
        print('M for manager menu')
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
        elif user_menu_choice in 'Mm':
            manager_menu()    

def print_check(current_order):
    print("\nYour order:")
    print('your check')

def change_order(current_order):
    print("Change the order:")
    
def manager_menu():
    while True:
        print("\nManager Menu:")
        print("1. Update a menu item")
        print("2. Add a new menu item")
        print("3. Remove a menu item")
        print("4. Display menu")
        print("5. Return to main menu")
        choice = input("Choose an option: ")

        if choice == '1':
            code = input("Enter item code: ")
            field = input("What do you want to update (name/price)? ").lower()
            new_value = input(f"Enter new {field}: ")
            functions.update_menu_item(data.menu_dict, code, field, new_value)
        elif choice == '2':
            code = input("Enter new item code: ")
            name = input("Enter item name: ")
            price = input("Enter item price: ")
            stock = input("Enter item stock: ")
            functions.add_menu_item(data.menu_dict, code, name, price, stock)
        elif choice == '3':
            code = input("Enter item code to remove: ")
            functions.remove_menu_item(data.menu_dict, code)
        elif choice == '4':
            functions.display_menu(data.menu_dict)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    #initialize the lists
    drinks = []
    appetizers = []
    salads = []
    entrees = []
    dessert= []
    #print(functions.get_item_information('D1'))
    show_main_menu()