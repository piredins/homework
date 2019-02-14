def work_with_json():
  import json

  def get_description_json(json_file):
    description_news = ''
    for item in json.load(json_file)['rss']['channel']['items']:
      description_news += item['description']
    return description_news

  with open('newsafr.json', encoding='cp1251') as newsfile:
    json_str = get_description_json(newsfile)
   
  json_list = json_str.split()

  json_list_sorted = sorted(json_list, reverse=True, key=lambda x: json_list.count(x))
  
  x = 0
  json_result = []
  for el in json_list_sorted:
    while x < 10:
      if el not in json_result:
          json_result.append(el)
          x += 1
    
    print('Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов:', json_result)

work_with_json()

def work_with_xml():
  import xml.etree.ElementTree as ET

  def get_description_xml(xml_file):
    description_news = ''
    for item in ET.parse(xml_file).getroot().findall('channel/item/description'):
      description_news += item.text
    return description_news

    with open('newsafr.xml', encoding='cp1251') as newsfile:
    xml_str = get_description_xml(newsfile)
   
  xml_list = xml_str.split()

  xml_list_sorted = sorted(xml_list, reverse=True, key=lambda x: xml_list.count(x))
  
  x = 0
  xml_result = []
  for el in xml_list_sorted:
    while x < 10:
      if el not in xml_result:
          xml_result.append(el)
          x += 1
    
    print('Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов:', xml_result)

work_with_xml()