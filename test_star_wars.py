import pytest

from star_wars import star_wars_name


def test_star_wars_name_exists():
    assert star_wars_name


@pytest.mark.parametrize('name, maiden_name, city, excpected', [
     ('D W', '', '',                        'Wd'),
     ('Da Wu', '', '',                      'Wuda'),
     ('Dan Jac', '', '',                    'Jacda'),
     ('John Jac', '', '',                   'Jacjo'),
     ('Dan van der Jackson', '', '',        'Jacda'),
])
def test_star_wars_name(name, maiden_name, city, excpected):
    assert star_wars_name(name, maiden_name, city,) == excpected
