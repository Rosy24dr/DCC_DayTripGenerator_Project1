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

def random_selection():
    print(f'We have selected {random_destination}. You will be traveling by {random_transportation}, then you will eat at {random_restaurant} and enjoy yourself while {random_entertainment}.')

def input_from_user( ):
    user_input = input('Does this work for you? Please enter yes or no:')
    while (user_input != True):
        if (user_input == 'yes'):
            print("Congrats! We have completed generating your day trip. Now let's just confirm that this is the trip you wanted. The trip we have generated for you is:")
            return
        elif (user_input == 'no'):
            random_destination = random.choice(destinations)
            random_transportation = random.choice(transportations)
            random_restaurant = random.choice(restaurants)
            random_entertainment = random.choice(entertainments)
            user_input = input(f"I am sorry this didn't work for you. Does {random_destination}, traveling by {random_transportation}, eating at {random_restaurant} and having fun by {random_entertainment} work for you? Please enter yes or no:")
            continue

def trip_results():
    print("Destination: " + random_destination)
    print("Restaurant: " + random_restaurant)
    print("Transportation: " + random_transportation)
    print("Entertainment: " + random_entertainment)

def finalized_trip():
    user_input_finalize_trip = (input('Would you like to finalize this trip? Please enter yes or no:'))
    if (user_input_finalize_trip == 'yes'):
        print(f'We have selected {random_destination}. You will be traveling by {random_transportation}, then you will eat at {random_restaurant} and enjoy yourself while {random_entertainment}.')
    elif(user_input_finalize_trip == 'no'):
        user_input_finalize_trip = input("I am sorry you did not like the choices. Let's start the process again.")
        
welcome_msg()
random_selection()
input_from_user()
trip_results()
finalized_trip()






