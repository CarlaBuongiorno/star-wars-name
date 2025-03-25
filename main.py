'''
There was a popular thing going around the internet a while ago; 
how to find out your Star Wars name! For the first part, 
you take the first three letters of your last name, 
and the first two letters of your first name. For the second part, 
you take the first two letters of your mother's maiden name, 
and the first three letters of the city where you were born.

So, let's say my name is Dan van der Jackson, my mother's maiden name 
is O'Brien, and I was born in Edinburgh. In that case, my Star Wars name
would be Jacda Obedi. Notice that punctuation is ignored, 
it's capitalized correctly, etc.

Write a function to generate Star Wars Names. It should take a whole 
name, a maiden name, and a city name, and it should return a string 
containing the Star Wars Name. Call your module star_wars.py, and 
use this function signature:

def star_wars_name(name, maiden_name, city):
    pass # should return string

Your code should not throw exceptions. 
In error conditions, (e.g. a maiden_name is not provided, the last name 
is 'Wu', etc) the function should use the largest portion of the name 
it can (so, empty string for no maiden name, and just the first two 
letters of 'Wu'.)'''

from star_wars import star_wars_name


def main():
    name = input('Please enter your full name: ')
    maiden_name = input('Please enter your mother\'s maiden name: ')
    city = input('Please enter the name of the city where you were born: ')
    generated_name = star_wars_name(name, maiden_name, city)
    print(generated_name)


if __name__ == '__main__':
    main()
