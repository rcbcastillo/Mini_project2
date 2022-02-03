# add some product names, create list
product_names = ['Americano', 'Black Coffee','Cappuccino', 'Espresso', 'Latte']

# print(product_names)
Main_menu= '''
       * MAIN MENU *
0. Exit the app 
1. See the product's menu
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
            ** SUBMENU **
        0. RETURN to main menu
        1. SEE product's list
        2. ADD a new product
        3. UPDATE an existing product
        4. DELETE an existing product
        
        '''
        print(product_menu_options) #products menu
        ## get user input for product menu option
        product_menu_option = int(input('Select a product from the submenu option: '))
        
        if product_menu_option == 0:
            print(Main_menu)
        elif product_menu_option == 1:
        #Updating the printing format, and printing the index of each product
            print("Available products  and their index, are: ")
            for num in range(0, len(product_names)):
                print(f'Product at position {num} = {product_names[num]}')
        
        elif product_menu_option == 2:
            list_added_product = list(product_names)
            new_product = input('Enter a new product: ')
            list_added_product.append(new_product)
            print('Updated list of available products')
            for item in range(len(list_added_product)):
                print(f'Product at position {item} = {list_added_product[item]}')
            product_update_asnwer= input('Would you like to add another product?: ') #products menu
            # get user input for product options again
            if product_update_asnwer == 'No':
                print(product_menu_options)
                continue
                print ('Select an option from the submenu: ')
            if product_update_asnwer == 'Yes':
                product_menu_option = input('Select a product from avalaible options: ')
        
        elif product_menu_option == 3:
            new_product_names = []
            print("Available products  and their index, are: ")
            for num in range(0, len(product_names)):
                product_names.append(product_names[num])
                print(f'Product at position {num} = {product_names[num]}')
                product_index = int(input('Enter the index of the product to update:'))
                product_to_add = input('Enter the name of new product: ') 
                product_names[product_index] = product_to_add
                print("Now the available products  and their index, are: ")
            for num in range(0, len(new_product_names)):
                print(f'Product at position {num} = {new_product_names[num]}')
                product_update_asnwer= input('Would you like to update another product?: ') #products menu
                # get user input for product options again
                if product_update_asnwer == 'No':
                    print(product_menu_options)
                    continue
                    print ('Select an option from the submenu: ')
                elif product_update_asnwer == 'Yes':
                    product_menu_option = int(input('Select a product from the menu option: '))
