# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.parametrize('a, b, result',
                         [pytest.param(18, 3, 6, marks=pytest.mark.smoke('than_more_0')),
                          pytest.param(-50, 2, -25, marks=pytest.mark.skip('negativ'))
                          ])
def test_than_more_0(a, b, result):
    assert all_division(a, b) == result