def star_wars_name(name, maiden_name, city):
    cleaned_maiden_name = _clean_input(maiden_name)
    full_name = get_star_wars_first_name(name)
    if not maiden_name and not city:
        return f'{full_name}'.title()
    return f'{full_name} {cleaned_maiden_name[:2]}{city[:3]}'.title()


def _clean_input(user_input):
    if len(user_input.split()) > 1:
        user_input = user_input[-1]
        return ''.join(i for i in user_input if i.isalnum())
    return ''.join(i for i in user_input if i.isalnum())



def get_star_wars_first_name(name):
    full_name = name.split()
    if len(full_name) > 1:
        return f'{full_name[-1][:3]}{full_name[0][:2]}'
    return ''.join(full_name)