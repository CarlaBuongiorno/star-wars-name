import pytest

from star_wars import star_wars_name


def test_star_wars_name_exists():
    assert star_wars_name


@pytest.mark.parametrize('name, maiden_name, city, expected', [
     ('', '', '',                                       ''),
     ('D', '', '',                                      'D'), # First name
     ('Madona', '', '',                                 'Ma'), # First name
     ('D W', '', '',                                    'Wd'),
     ('Da Wu', '', '',                                  'Wuda'),
     ('Dan Jac', '', '',                                'Jacda'),
     ('John Jac', '', '',                               'Jacjo'),
     ('Dan van der Jackson', '', '',                    'Jacda'),
     ('D W', 'O', '',                                   'Wd O'),
     ('D W', 'Obr', '',                                 'Wd Ob'),
     ('D W', 'O\'br', '',                               'Wd Ob'),
     ('D W', 'O\'Br', '',                               'Wd Ob'),
     ('D W', 'O\'Brien', 'E',                           'Wd Obe'),
     ('D W', 'O\'Br', 'Edinburgh',                      'Wd Obedi'),
     ('D W', '', 'Edinburgh',                           'Wd Edi'),
     ('Dan van der Jackson', 'O\'Brien', 'Edinburgh',   'Jacda Obedi'),
     ('Dan Jackson', 'van der Jackson', 'Edinburgh',    'Jacda Jaedi'),
     ('Dan Jackson', 'van der Jackson', 'Den Hague',    'Jacda Jahag'),
     ('D&n Jackson', 'Jackson', '\'s-Hertogenbosch',    'Jacdn Jaher'),
     ('1', '', '',                                      ''),
     ('1', '2', '3',                                    ''),
     ('D1', '2', '3',                                   'D'),
     ('D1', 'O2', '3',                                  'D O'),
     ('D1', 'O2', 'Ed3',                                'D Oed'),
     ('D1', 'O2', 'Ed3in',                              'D Oedi'),
     ('D1 5', 'O2', 'Ed3in',                            'D Oedi'),
])
def test_star_wars_name(name, maiden_name, city, expected):
    assert star_wars_name(name, maiden_name, city,) == expected
