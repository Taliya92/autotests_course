# Напишите 5 тестов на функцию all_division.
# Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest

def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.smoke
def test_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(4, 0)

def test_than_more_0():
    assert all_division(18, 3) == 6

def test_than_less_0():
    assert all_division(-20, 5) == -4

def test_float():
    assert all_division(6, 1.2) == 5

@pytest.mark.acceptance
def test_accept():
    assert all_division(54, 9) == 6
