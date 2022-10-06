mongo_uri = 'mongodb://localhost:27017/'
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

original_menu = {
    "burgers": ['100', '350', '400'],
    "stages of doneness": ["rare", "medium rare", "medium", "medium well", "well done", "vegan"],
    "toppings": ["mushrooms", "egg", "avocado", "onions", "no toppings"],
    "drinks": ["coca cola", "coca cola zero", "orange juice", "water", "without a drink"],
    "sides": ["onion rings", "salad", " french fries", "sweet potato fries", "wings", "nothing"]
}
options = "To order from a menu press [O]\n" \
          "To leave a review press [R]\n" \
          "To change your address press [C]\n" \
          "To exit press [X]\n"
options_for_worker = "To see orders press [S]\n" \
                     "To delete an order press [D]\n" \
                     "To register new worker press[N]\n" \
                     "To see reviews press [R]\n" \
                     "To Exit press [X]"


header = """"
┌┐ ┬ ┬┬─┐┌─┐┌─┐┬─┐  ┌─┐┬ ┬┌─┐┌─┐
├┴┐│ │├┬┘│ ┬├┤ ├┬┘  └─┐├─┤│ │├─┘
└─┘└─┘┴└─└─┘└─┘┴└─  └─┘┴ ┴└─┘┴  
                                
          _..----.._       
        .'     o    '.     
       /   o       o  \    
      |o        o     o|             
      /'-.._o     __.-'\   
      \      `````     /   
      |``--........--'`|    
       \              /
        `'----------'`

"""
