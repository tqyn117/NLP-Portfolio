import sys
import pathlib
import re
import pickle


class Person:
    def __init__(self, last, first, mi, id, phone):
        self.id = id
        self.first = first
        self.mi = mi
        self.last = last
        self.phone = phone

    # Print out person object in a specific format
    def display(self):
        print('Employee id: ' + self.id)
        print('\t\t' + self.first + ' ' + self.mi + ' ' + self.last)
        print('\t\t' + self.phone + '\n')


def processor(filepath):
    # Access the file to read from the given filepath
    with open(pathlib.Path.cwd().joinpath(filepath), encoding='utf-8-sig', mode='r') as f:
        # Skip first line
        next(f)
        # Declare dictionary
        dict = {}
        # Access file line by line
        for line in f:
            # Remove \n at the end of each line
            person = line.rstrip('\n').split(',')

            # Capitalize the first letter of last name, first name, and middle name
            person[0] = person[0].title()
            person[1] = person[1].title()
            if not person[2]:
                person[2] = 'X'
            else:
                person[2] = person[2].title()

            # Validate Id format
            idMatch = re.compile("^[A-Z]{2}[0-9]{4}$")
            while not idMatch.match(person[3]):
                print('ID invalid: ' + person[3])
                print('ID is two letters followed by 4 digits')
                id = input('Please enter a valid id: ')

                # Allow user to input the id in lowercase and format to proper uppercase
                id = id[0].upper() + id[1].upper() + id[2:]
                person[3] = id;

            # Validate phone number format
            numberMatch = re.compile("^\d{10}$")
            # Check if the special characters matches to convert to '-'
            if len(person[4]) == 12 and person[4][3] == person[4][7]:
                person[4] = person[4].replace(person[4][3], '-')
            # Check if there is no special character to add '-'
            elif len(person[4]) == 10 and numberMatch.match(person[4]):
                person[4] = person[4][0:3] + '-' + person[4][3:6] + '-' + person[4][6:10]
            # Ask for input in case the special characters do not match
            phoneMatch = re.compile("^\d{3}-\d{3}-\d{4}$")
            while not phoneMatch.match(person[4]):
                print('Phone ' + person[4] + ' is invalid')
                print('Enter phone number in form 123-456-7890')
                phone = input('Enter phone number: ')
                person[4] = phone

            # Check for duplicate key or Id in dictionary
            if dict.get(person[3]):
                raise ValueError("Duplicate Key")
            # Initialize Person object
            person = Person(
                person[0],
                person[1],
                person[2],
                person[3],
                person[4]
            )
            # Adding Person object to dict
            dict[person.id] = person
        return dict


if __name__ == '__main__':
    # Check if a filename is passed in as a system arg
    if len(sys.argv) < 2:
        print('Please enter a filename as a system arg')
    else:
        fp = sys.argv[1]
        # Pickle file to test if dictionary unpickle properly
        pickle.dump(processor(fp), open('dict.p', 'wb'))
        dict_in = pickle.load(open('dict.p', 'rb'))
        # Access dictionary values to print out using object Person display() func
        print('\nEmployee list: \n')
        for person in dict_in.values():
            person.display()
