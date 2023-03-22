def find_all_hobbyists(hobby, hobbies):
    # Loop through hobbies and add every name whos hobby-list has the supplied hobby in it.
    return [ person for person in hobbies.keys() if hobby in hobbies[person] ]

if __name__ == "__main__":
    hobbies = { 
        "Steve": ['Fashion', 'Piano', 'Reading'],
        "Patty": ['Drama', 'Magic', 'Pets'],
        "Chad": ['Puzzles', 'Pets', 'Yoga'],
        "Nils": ['Programming', 'biking', 'Yoga'],
    }
    
print(find_all_hobbyists('Yoga', hobbies)); # -> ['Chad', 'Nils']
input() # Prevent the program from exiting right away when run on the console