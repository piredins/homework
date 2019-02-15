def work_with_json():
  import json

  def get_description_json(json_file):
    description_news = ''
    for item in json.load(json_file)['rss']['channel']['items']:
      description_news += item['description']
    return description_news

  with open('newsafr.json', encoding='utf8') as newsfile:
    json_str = get_description_json(newsfile)
   
  json_list = json_str.split()

  long_json_list = []
  for word in json_list:
      if len(word) >= 6:
          long_json_list.append(word)

  json_list_dict = {}
  for word in long_json_list:
      json_list_dict.setdefault(word, 0)
      json_list_dict[word] += 1
  
  sorted_words = sorted(json_list_dict.items(), key=lambda item: -item[1])
    
  for index, word in enumerate(sorted_words):
    if index > 9:
      break
    print(f'Слово "{word[0]}" встречается {word[1]} раза')
          
work_with_json()