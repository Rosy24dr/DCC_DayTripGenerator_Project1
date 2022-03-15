import random

destinations = ['Dominican Republic','Puerto Rico','Mexico','Colombia']
restaurants = ['El Mesón de la Cava','Raices','Pujol','Andrés Carne de Res']
transportations = ['plane', 'train','walking','swimming']
entertainments = ['dancing','kareoking','doing an escape room', 'horseback riding at the beach']

random_destination = random.choice(destinations)
random_restaurant = random.choice(restaurants)
random_transportation = random.choice(transportations)
random_entertainment = random.choice(entertainments)

def welcome_msg():
    print('Hello, welcome to the day trip calculator where we can help you choose your destination.')
    print(f'We have selected {random_destination}. You will be traveling by {random_transportation}, then you will eat at {random_restaurant} and enjoy yourself while {random_entertainment}.')

def input_from_user_destination():
    user_input_destination = input('Does this destination work for you? Please enter yes or no:')
    
    while (user_input_destination != True):
        if (user_input_destination == 'yes'):
            print("Great, glad this destination works. Now let's move on.")
            return
        elif (user_input_destination == 'no'):
            random_destination = random.choice(destinations)
            user_input_destination = input(f"I am sorry this destination didn't work for you. Does {random_destination}  work for you? Please enter yes or no:")
            continue

def input_from_user_transportation():
    user_input_transportation = input('Does this way of transportation work for you? Please enter yes or no:')
    
    while (user_input_transportation != True):
        if (user_input_transportation == 'yes'):
            print("Great, glad this way of transportation works. Now let's move on.")
            return
        elif (user_input_transportation == 'no'):
            random_transportation = random.choice(transportations)
            user_input_transportation = input(f"I am sorry this way of transportation didn't work for you. Does {random_transportation}  work for you? Please enter yes or no:")
            continue
        
def input_from_user_restaurant():
    user_input_restaurant = input('Does this restaurant work for you? Please enter yes or no:')
    
    while (user_input_restaurant != True):
        if (user_input_restaurant == 'yes'):
            print("Great, glad this restaurant works. Now let's move on.")
            return
        elif (user_input_restaurant == 'no'):
            random_restaurant = random.choice(restaurants)
            user_input_restaurant = input(f"I am sorry this restaurant didn't work for you. Does {random_restaurant}  work for you? Please enter yes or no:")
            continue

def input_from_user_entertainment():
    user_input_entertainment = input('Does this form of entertainment work for you? Please enter yes or no:')
    
    while (user_input_entertainment != True):
        if (user_input_entertainment == 'yes'):
            print("Great, glad this form of entertainment works. Now let's move on.")
            return
        elif (user_input_entertainment== 'no'):
            random_entertainment = random.choice(entertainments)
            user_input_entertainment = input(f"I am sorry this form of entertainment didn't work for you. Does {random_entertainment}  work for you? Please enter yes or no:")
            continue

welcome_msg()
input_from_user_destination()
input_from_user_restaurant()
input_from_user_transportation()
input_from_user_entertainment()

print("Congrats! We have completed generating your day trip. Now let's just confirm that this is the trip you wanted. The trip we have generated for you is:")

def trip_results():
    print(random_destination)
    print(random_restaurant)
    print(random_transportation)
    print(random_entertainment)

trip_results()



            