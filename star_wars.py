def star_wars_name(name, maiden_name, city):
    starwars_f_name = get_star_wars_first_name(name)
    starwars_l_name = get_star_wars_last_name(maiden_name, city)
    return f'{starwars_f_name} {starwars_l_name}'


def get_star_wars_first_name(name):
    first_name = name.split()
    return f'{first_name[-1][:3]}{first_name[0][:2].lower()}'


def get_star_wars_last_name(maiden_name, city):
    return f'{maiden_name}'