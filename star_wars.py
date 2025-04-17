def star_wars_name(name, maiden_name, city):
    cleaned_maiden_name = _clean_maiden_name(maiden_name)
    star_wars_first_name = get_star_wars_first_name(name)
    if not maiden_name and not city:
        return f'{star_wars_first_name}'.title()
    return f'{star_wars_first_name} {cleaned_maiden_name[:2]}{city[:3]}'.title()


def _clean_maiden_name(maiden_name):
    split_name = maiden_name.split()
    if len(split_name) > 0:
        return ''.join(i for i in split_name[-1] if i.isalnum())
    else:
        return ''


def get_star_wars_first_name(name):
    full_name = name.split()
    return f'{get_part_from_last_name(full_name)}{get_part_from_first_name(full_name)}'


def get_part_from_first_name(split_full_name):
    return split_full_name[0][:2] if len(split_full_name) > 0 else ''


def get_part_from_last_name(split_full_name):
    return split_full_name[-1][:3] if len(split_full_name) > 1 else ''
