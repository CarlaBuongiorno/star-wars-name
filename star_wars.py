def star_wars_name(name, maiden_name, city):
    f_name = get_star_wars_first_name(name)
    # l_name = get_three_letters_of_last_name(name)
    return f'{f_name}'


def get_star_wars_first_name(name):
    full_name = name.split()
    starwars_f_name = f'{full_name[-1]}{full_name[0].lower()}'
    return starwars_f_name


# def get_three_letters_of_last_name(name):
    # return name.split()[-1][:3]
