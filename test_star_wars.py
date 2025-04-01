import pytest

from star_wars import star_wars_name


def test_star_wars_name_exists():
    assert star_wars_name


@pytest.mark.parametrize('name, maiden_name, city, excpected', [
     ('', '', '',                           ' '),
     ('D W', '', '',                        'Wd '),
     ('Da Wu', '', '',                      'Wuda '),
     ('Dan Jac', '', '',                    'Jacda '),
     ('John Jac', '', '',                   'Jacjo '),
     ('Dan van der Jackson', '', '',        'Jacda '),
     ('D W', 'O', '',                       'Wd O'),
     ('D W', 'Obr', '',                     'Wd Ob'),
     ('D W', 'O\'br', '',                   'Wd Ob'),
     ('D W', 'O\'Br', '',                   'Wd Ob'),
     ('D W', 'O\'Brien', 'E',               'Wd Obe'),
     ('D W', 'O\'Br', 'Edinburgh',          'Wd Obedi'),
     ('D W', '', 'Edinburgh',               'Wd Edi'),
     ('Dan van der Jackson', 'O\'Brien', 'Edinburgh','Jacda Obedi'),
])
def test_star_wars_name(name, maiden_name, city, excpected):
    assert star_wars_name(name, maiden_name, city,) == excpected
