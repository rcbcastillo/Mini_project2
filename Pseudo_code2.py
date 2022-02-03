# add some product names, create list
product_names = ['Americano', 'Black Coffee','Cappuccino', 'Espresso', 'Latte']

# print(product_names)
Main_menu= '''
0. Press zero to exit the app 
1. Press one to see the product's menu
'''
print(Main_menu)
# Printing main menu options
# Get user input for main menu option
while True:
    main_menu_option = int(input('Select an option from the main menu: '))
    # If user input is 0:EXIT app
    if main_menu_option == 0:
        break
    # products menu
    elif main_menu_option == 1:
        product_menu_options = '''
        0. RETURN to main menu
        1. PRINT products list
        2. CREATE new product
        '''
        print(product_menu_options) #products menu
        # get user input for product menu option
        product_menu_option = int(input('Select a product from the menu option:'))
        # for product in range(0,len(product_names)+1):
        if product_menu_option == 0:
            print(Main_menu)
        elif product_menu_option == 1:
            print(product_names)
        elif product_menu_option == 2:
            new_product = input('Enter a new product: ')
            print(new_product)
            product_names.append(new_product)
        
        


    


    
