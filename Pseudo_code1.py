# add some product names, create list
product_names =['Fruits', 'Vegetables', 'Meat', 'Baking', 'Pasta and Rice', 'Seasoning','Paper products', 'Seafood','Baking', 'Cleaning products', 'Frozen products','Snacks', 'Bakery','Personal products', 'Drinks', 'Refrigerated', 'Cans and jars' ]

'''product_names =['Fruits', 'Vegetables', 'Meat']
# Fruits=['Melon','Kiwi','Mangos','Pear','Royal gala apple','Bananas','Mandarine','Grapes','Lemons','Avocados','Organic bananas','Pineapple','Figs']
# Vegetables =['Potatoes','Carrots','Sweet potatoes','Broccoli','Cabbage','Pepper','Mushrooms','Tomatoes','Spinach', 'Kale', 'Asparagus', 'Onions', 'Courgette','Aubergine','Squash']
# Meat=['Lean beef','Beef mince', 'Pork loin medallions','lamb', 'Chicken breast']'''

# print(product_names)
print('Main menu')
# give a list of options===print('Select 0')????
# Printing main menu options
# Get user input for main menu option
while True:
    user_input= int(input('Select the menu options: '))
    # IF user input is 0:EXIT app
    if user_input == 0:
        break
    # products menu
    elif user_input == 1:
        print(product_names) #products menu
        # get user input for product menu option
        product_menu_option = int(input('Select a an option from the menu option:'))
        
        if user_input == 0:
            print(product_names)
        
        


    


    
