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


def _get_part_from_last_name(split_full_name):
    return (''.join(i for i in split_full_name[-1] if i.isalpha()))[:3] if len(split_full_name) > 1 else ''


def _get_part_from_first_name(split_full_name):
    return (''.join(i for i in split_full_name[0] if i.isalpha()))[:2] if len(split_full_name) > 0 else ''


def _get_part_from_maiden_name(split_maiden_name):
    return (''.join(i for i in split_maiden_name[-1] if i.isalpha()))[:2] if len(split_maiden_name) > 0 else ''


def _get_part_from_city(split_city):
    return (''.join(i for i in split_city[-1] if i.isalpha()))[:3] if len(split_city) > 0 else ''
