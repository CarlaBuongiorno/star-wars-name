from star_wars import star_wars_name


def test_star_wars_name_exists():
    assert star_wars_name


def test_one_letter_name():
    name = star_wars_name(
        'D W',
        '',
        ''
    )
    assert name == 'Wd'


def test_two_letter_name():
    name = star_wars_name(
        'Da Wu',
        '',
        ''
    )
    assert name == 'Wuda'


def test_three_letter_first_name():
    name = star_wars_name(
        'Dan Jac',
        '',
        ''
    )
    assert name == 'Jacda'


def test_four_letter_first_name():
    name = star_wars_name(
        'John Jac',
        '',
        ''
    )
    assert name == 'Jacjo'


def test_four_letter_last_name():
    name = star_wars_name(
        'John Jack',
        '',
        ''
    )
    assert name == 'Jacjo'
