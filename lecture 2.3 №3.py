documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

def attachment():
  notice = []
  document_number = input("Введите номер документа:")
  for element in documents:
    if document_number == element['number']:
      notice.append('some_value')
      print(element['name'])
  if len(notice) == 0:
    print('Документ не найден.')
    
def list_of_documents():
  for element in documents:
    print('passport', element['number'], element['name'])
  
def document_shelf_number():
  notice = []
  document_number = input("Введите номер документа:")
  for key, values in directories.items():
    for value in values:
      if document_number == value:
        notice.append('some_value')
        print("Номер полки на которой находится документ:", key)
  if len(notice) == 0:
    print('Документ не найден.')

def new_document():
  notice = []
  document = {} 
  document['type'] = input('Введите тип документа:') 
  document['number'] = input('Введите номер документа:') 
  document['name'] = input('Введите имя:') 
  documents.append(document) 
  shelf_number = input('Введите номер полки на которой будет храниться документ:')
  for key, element in directories.items():
    if shelf_number == key:
      directories[key].append(document['number'])
      notice.append('some_value')            
  if len(notice) == 0:
    print('Полка на которую вы хотите добавить элемент не существует.')
   
def name():
  for element in documents:
    try:
      print(element['name'])
    except KeyError:
      print('У словаря нет ключа "name".')

def list_of_commands():
  instruction = input('Введите команду которую нужно выполнить:')
  if instruction in 'p':
     attachment()
  elif instruction in 'l':
    list_of_documents()
  elif instruction in 's':
    document_shelf_number()
  elif instruction in 'a':
    new_document()
  elif instruction in 'n':
    name()
  else:
    print('Команда не найдена.')

list_of_commands()