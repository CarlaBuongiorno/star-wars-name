def star_wars_name(name, maiden_name, city):
    f_name = get_two_letters_of_first_name(name)
    l_name = get_three_letters_of_last_name(name)
    return f'{l_name}{f_name}'


def get_two_letters_of_first_name(name):
    return name[:2].lower()


def get_three_letters_of_last_name(name):
    return name.split()[-1][:3]
