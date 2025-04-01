def star_wars_name(name, maiden_name, city):
    cleaned_maiden_name = _clean_input(maiden_name)
    starwars_f_name = get_star_wars_first_name(name)
    starwars_l_name = get_star_wars_last_name(cleaned_maiden_name, city)
    return f'{starwars_f_name} {starwars_l_name}'.title()


def _clean_input(user_input):
    return ''.join(i for i in user_input if i.isalnum() or '')


def get_star_wars_first_name(name):
    if name:
        full_name = name.split()
        return f'{full_name[-1][:3]}{full_name[0][:2]}'
    return name

def get_star_wars_last_name(maiden_name, city):
    return f'{maiden_name[:2]}{city[:3]}'