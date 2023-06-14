# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import time
import pytest
import datetime

@pytest.fixture(autouse=True)
def test_time1():
    start = datetime.datetime.now()
    print(f'Начало выполнения {start}')
    yield
    end = datetime.datetime.now()
    print(f'Окончание выполнения {end}')


@pytest.fixture()
def test_time2():
    start = datetime.datetime.now()
    yield
    end = datetime.datetime.now()
    time_all = end - start
    print(f'Время выполнения метода {time_all}')