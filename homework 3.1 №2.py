def work_with_xml():

  import xml.etree.ElementTree as ET

  def get_description_xml(xml_file):
      description_news = ''
      for item in ET.parse(xml_file).getroot().findall("channel/item/description"):
        description_news += item.text
      return description_news

  with open('newsafr.xml', encoding='utf8') as newsfile:
    xml_str = get_description_xml(newsfile)

  xml_list = xml_str.split()

  long_xml_list = []
  for word in xml_list:
      if len(word) >= 6:
          long_xml_list.append(word)

  xml_list_dict = {}
  for word in long_xml_list:
      xml_list_dict.setdefault(word, 0)
      xml_list_dict[word] += 1

  sorted_words = sorted(xml_list_dict.items(), key=lambda item: -item[1])

  for index, word in enumerate(sorted_words):
    if index > 9:
      break
    print(f'Слово "{word[0]}" встречается {word[1]} раза')

work_with_xml()