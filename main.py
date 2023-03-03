import random

great_hotspots = ['New York', 'Los Angeles', 'North Carolina', 'Georgia']
great_spots = ['Ruth Chris', 'Bricktop', 'Slutty Vegan', 'Nusr-Et']
hot_wheels = ['Rolls-Royce', 'Taxi', 'Corevette', 'Uber']
get_me_lit = ['Museum', 'Clubbing', 'Concert', 'Movie']


def pick_random_choice(list):
    select_item = random.choice(list)
    return select_item

def display_trip(destination,restaurant,ride,entertainment):
    print(f"Your trip!!!\nDestination:{destination}\nRestaurant:{restaurant}\nTransportation:{ride}\nEntertainment:{entertainment}")


def day_trip_generator():
    day_trip_run = True
    while day_trip_run == True:
        destination = pick_random_choice(great_hotspots)
        restaurant = pick_random_choice(great_spots)
        transportation = pick_random_choice(hot_wheels)
        entertainment = pick_random_choice(get_me_lit)
        display_trip(destination,restaurant,transportation,entertainment)
        user_input = input("Are you satisfied with your trip y/n?")
        if user_input == 'n':
            print("We will generate a new trip for you!")
        elif user_input == 'y':
            print("Your trip is completed!!!")
            display_trip(destination,restaurant,transportation,entertainment)
            day_trip_run = False

day_trip_generator()




















#def pick_random_places(list_of_places):
 #   select_item = random.choice(list_of_places)
  #  return select_item
#their_city = pick_random_places(great_hotspots) 
#print('The city best for you is',their_city)
#give them option of choice
#choice = input('Are you ok with this choice?')
#if choice == 'no':

    # if user types no they get a new choice
 #   their_city = pick_random_places(great_hotspots)
  #  print('The city best for you is',their_city)
#elif choice == 'yes':
 #   print('Great Choice!!!')

    #if user chooses yes they move on to transportation

#def pick_random_spots(restaurant_list):
 #   choose_item = random.choice(restaurant_list)
  #  return choose_item
#their_restaurant = pick_random_spots(great_spots)
#print('The best restaurant for you is',their_restaurant)
#selection = input('Are you ok with this choice?')
#if selection == 'no':
 #       their_restaurant = pick_random_spots(great_spots)
  #      print('The restaurant best for you is', their_restaurant)
#elif selection == 'yes':
 #       print('Great Choice!!!')
        

#def pick_random_cars(tansportation_list):
 #    make_seletion = random.choice(tansportation_list)
  #   return make_seletion
#their_wheels = pick_random_cars(hot_wheels)
#print('The best transportation for you is',their_wheels)
#answer = input('Are you ok with this choice?')
#if answer == 'no':
 #       their_wheels = pick_random_cars(hot_wheels)
  #      print('The best transportation for you is', their_wheels)
#elif answer == 'yes':
 #   print("Great Choice!!!")


#def pick_random_vibe(vibes_list):
 #   final_pick = random.choice(vibes_list)
  #  return final_pick
#vibe = pick_random_vibe(get_me_lit)
#print('The best vibe for you is',vibe)
#pick = input('Are you ok with this choice?')
#if pick == 'no':
 #   their_vibe = pick_random_vibe(get_me_lit)
  #  print('The best vibe for you is',their_vibe)
#elif pick == 'yes':
 #   print('Great Choice!!!')
#input('Is your trip complete?')
#print('Enjoy your trip!!!')


#nevin  was here