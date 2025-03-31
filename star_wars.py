def star_wars_name(name, maiden_name, city):
    starwars_name = get_star_wars_first_name(name)
    return f'{starwars_name}'


def get_star_wars_first_name(name):
    full_name = name.split()
    return f'{full_name[-1][:3]}{full_name[0][:2].lower()}'
