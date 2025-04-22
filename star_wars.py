def star_wars_name(name, maiden_name, city):
    star_wars_first_name = _get_star_wars_first_name(name)
    star_wars_last_name = _get_star_wars_last_name(maiden_name, city)
    if not maiden_name and not city:
        return f'{star_wars_first_name}'.title()
    return f'{star_wars_first_name} {star_wars_last_name}'.title()


def _get_star_wars_first_name(name):
    full_name = name.split()
    return f'{_get_part_from_last_name(full_name)}{_get_part_from_first_name(full_name)}'


def _get_part_from_last_name(split_full_name):
    return split_full_name[-1][:3] if len(split_full_name) > 1 else ''


def _get_part_from_first_name(split_full_name):
    return split_full_name[0][:2] if len(split_full_name) > 0 else ''


def _get_star_wars_last_name(maiden_name, city):
    split_maiden_name = maiden_name.split()
    return f'{_get_part_from_maiden_name(split_maiden_name)}{_get_part_from_city(city)}'


def _get_part_from_maiden_name(split_maiden_name):
    return (''.join(i for i in split_maiden_name[-1] if i.isalnum()))[:2] if len(split_maiden_name) > 0 else ''


def _get_part_from_city(city):
    return city[:3]