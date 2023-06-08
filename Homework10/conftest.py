import pytest
import datetime

@pytest.fixture(scope='class')
def time_start_end(request):
    time_start = datetime.datetime.now()
    print(f'Время начала выполнения {time_start}')

    yield Test1
    time_end = datetime.datetime.now()
    print(f'Время окончания выполнения {time_end}')

@pytest.fixture
def during(test3):
    time_start = datetime.datetime.now()
    yield test3
    time_end = datetime.datetime.now()
    during = time_end - time_start
    print(f'Продолжительность выполнения {during}')
