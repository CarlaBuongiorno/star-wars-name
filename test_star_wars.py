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