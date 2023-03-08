import random

def template_1():
    '''
    The first template
    :return:
    '''
    print('You got MadLib N1')
    num_1 = input('Input a number: ')
    measure_of_time = input('Input a measure of time: ')
    mode_of_transport = input('Input a mode of transportation: ')
    adj_1 = input('Input an adjective: ')
    adj_2 = input('Input another adjective: ')
    noun_1 = input('Input a noun: ')
    color = input('Input a color: ')
    body_part = input('Input a part of body: ')
    verb = input('Input a verb: ')
    num_2 = input('Input a number: ')
    noun_2 = input('Input a noun: ')
    noun_3 = input('Input a noun: ')
    body_part_2 = input('input a body bart')
    noun_4 = input('input a noun')
    adj_3 = input('input an adj')
    silly_word = input('input a sillyword')

    return f'''
      It was about {num_1} {measure_of_time} ago when I arrived at the hospital in a {mode_of_transport}. 
      The hospital is a/an {adj_1} place, there are a lot of {adj_2} {noun_1} here. 
      There are nurses here who have {color} {body_part}. If someone wants to come into my room I told them 
      that they have to {verb} first. I’ve decorated my room with {num_2} {noun_2}. Today I talked to a doctor and 
      they were wearing a {noun_3} on their {body_part_2}. I heard that all doctors {verb} {noun_4} every day for 
      breakfast. The most {adj_3} thing about being in the hospital is the {silly_word} {noun_1} ! 
           '''

def template_2():
    '''
    The second template
    :return:
    '''
    print('You got MadLib N2')
    name = input(
        'Input person\'s name: ')
    noun_1 = input('Input a noun: ')
    adj_1 = input('Input an adjective(feeling): ')
    verb_1 = input('Input a verb: ')
    adj_2 = input('Input another adjective: ')
    animal = input('Input an animal: ')
    verb_2 = input('Input a verb: ')
    color_1 = input('Input a color: ')
    verb_3 = input('Input another verb: ')
    adverb = input('Input an adverb ending in ly: ')
    num_1 = input('Input a number: ')
    measure_of_time = input('Input a measure of time: ')
    color_2 = input('Input a color: ')
    animal_2 = input('Input an animal: ')
    num_2 = input('Input a number: ')
    sillyword = input('Input a silly word')
    noun_2 = input('Input a noun: ')

    return f'''
     This weekend I am going camping with {name}. I packed my lantern, sleeping bag, and {noun_1}.
      I am so {adj_1} to {verb_1} in a tent. I am {adj_2} we might see a(n) {animal}, 
      I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and 
      {verb_2}. I have heard that the {color_1} lake is great for {verb_3}ing. Then we will {adverb} hike through 
      the forest for {num_1} {measure_of_time}. If I see a {color_2} {animal_2} while hiking, 
      I am going to bring it home as a pet! At night we will tell {num_2} {sillyword} 
      stories and roast {noun_2} around the campfire!!
            '''
def template_3():
    '''
    The third template
    :return:
    '''
    print('You got MadLib N3')
    person_name = input("Input person\'s name: ")
    adj_1 = input("Input adjective (feeling): ")
    color = input("Input a color: ")
    animal = input("Input an animal: ")
    place = input("Input a place: ")
    adj_2 = input("Input adjective again (feeling): ")
    magical_creature = input("Input magical creature (plural): ")
    adj_3 = input("Input adjective again (feeling): ")
    magical_creature_2 = input("Input magical creature again (plural): ")
    room_in_a_house = input("Input room in a house: ")
    noun = input("Input noun: ")
    noun_2 = input("Input noun again: ")
    noun_3 = input("Input noun again (plural): ")
    adj_4 = input("Input adjective again (feeling): ")
    noun_4 = input("Input noun again (plural): ")
    number = input("Input a number: ")
    measure_of_time = input("Input measure of time: ")
    verb = input("Input verb (ending in ing): ")
    adj_5 = input("Input adjective again (feeling): ")
    noun_5 = input("Input noun again (plural): ")

    return f'''
     Dear {person_name}, I am writing to you from a {adj_1} castle in an 
     enchanted forest. I found myself here one day 
     after going for a ride on a {color} {animal} in {place}. 
     There are {adj_2} {magical_creature} and {adj_3} 
     {magical_creature_2} here! In the {room_in_a_house} 
     there is a pool full of {noun}. I fall asleep each night on a {noun_2} of 
     {noun_3} and dream of {adj_4} {noun_4}. 
     It feels as though I have lived here for {number} {measure_of_time}. 
     I hope one day you can visit, although the only way to get here 
     now is {verb} on a {adj_5} {noun_5}!!
        '''

