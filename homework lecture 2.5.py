from contextlib import contextmanager
from datetime import datetime

@contextmanager
def open_file(file_path, encoding='utf8'):
  try:
    time1 = (datetime.now())
    print('Время запуска кода в менеджере контекста:', time1)
    file = open(file_path)
    yield file
  finally:
    file.close
    time2 = (datetime.now())
    print('Время окончания работы кода:', time2)
    print('Время работы кода:', time2 - time1)

with open_file('test_homework.txt') as file:
  for line in file:
    string = line
    print(string)