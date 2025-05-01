def star_wars_name(name, maiden_name, city):
    if (maiden_name and not maiden_name.isdigit()) or (city and not city.isdigit()):
        return f'{_get_star_wars_first_name(name)} {_get_star_wars_last_name(maiden_name, city)}'.title()
    return f'{_get_star_wars_first_name(name)}'.title()


def _get_star_wars_first_name(name):
    full_name = _split_user_input(name)
    return f'{_get_part_from_last_name(full_name)}{_get_part_from_first_name(full_name)}'


def _get_star_wars_last_name(maiden_name, city):
    two_part_city = ''.join([i.replace('-', ' ') if '-' in i else i for i in city])
    return f'{_get_part_from_maiden_name(_split_user_input(maiden_name))}{_get_part_from_city(_split_user_input(two_part_city))}'


def _split_user_input(user_input):
    return user_input.split()


# There has to be at least 2 parts (1st and last name) 
def _get_part_from_last_name(full_name):
    return _get_part(split_input=full_name, part_to_use=-1, amout_of_letters=3, min_word_size=1)


def _get_part_from_first_name(full_name):
    return _get_part(split_input=full_name, part_to_use=0, amout_of_letters=2, min_word_size=0)


def _get_part_from_maiden_name(maiden_name):
    return _get_part(split_input=maiden_name, part_to_use=-1, amout_of_letters=2, min_word_size=0)


def _get_part_from_city(city):
    return _get_part(split_input=city, part_to_use=-1, amout_of_letters=3, min_word_size=0)


def _get_part(split_input, part_to_use, amout_of_letters, min_word_size):
    return (''.join(i for i in split_input[part_to_use] if i.isalpha()))[:amout_of_letters] if len(split_input) > min_word_size else ''
