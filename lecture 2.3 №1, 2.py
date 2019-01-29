operation = input('Введите операцию:')
operation = operation.split()
value = input('Вы хотите провести операции над строками? Введите "да" или "нет":')
try:  
  if value in 'да':
    sum1 = str(operation[1])
    sum2 = str(operation[2])
  elif value in 'нет':
    sum1 = int(operation[1])
    sum2 = int(operation[2])
except IndexError:
  print('Передано необходимое количество аргументов')    
try:
  assert operation[0] in ['+', '-', '*', '/']
except AssertionError:
  print('Операция не поддерживается')
if operation[0] in '+':
  result = sum1 + sum2
  print(result)
elif operation[0] in '-':
  result1 = sum1 - sum2
  print(result1)
elif operation[0] in '*':
  result2 = sum1 * sum2
  print(result2)  
elif operation[0] in '/':
  try:
    try:
      result3 = sum1 / sum2
      print(result3)
    except ZeroDivisionError:
      print('Деление на ноль не поддерживается')
  except TypeError:
    print('Деление строк не поддерживается')