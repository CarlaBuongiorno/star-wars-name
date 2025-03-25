from star_wars import star_wars_name


def test_star_wars_name_exists():
    assert star_wars_name


def test_two_letters_first_name():
    name = star_wars_name(
        'Dan van der Jackson',
        'O\'Brien',
        'Edinburgh'
    )
    assert name == 'Da'
