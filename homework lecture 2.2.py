class Animal:
  
  def __init__(self, name, weight, voice, max_weight):
    self.name = name
    self.weight = weight # вес измеряется в кг
    self.voice = voice
    self.max_weight = max_weight # теоритический максимальный вес
    
  
  def feed(self):
    print('Ням-ням-ням')
    if self.weight + self.food > self.max_weight:
      print('Мне кажется ей на сегодня хватит.')
    elif self.weight + self.food <= self.max_weight:
      self.weight += self.food 

  def collect(self):
    pass

class Bird(Animal):

  food = 0.5
  
  eggs = 10 # яйца которые снесла птица, но мы не собрали.

  def collect(self):
    sum_eggs = input('Введите сколько яиц вы хотите собрать у {}:'.format(self.name))
    if self.eggs >= int(sum_eggs):
      self.eggs = self.eggs - int(sum_eggs)
    else:
      print('Но тут только:', self.eggs)

goose = Bird('Серый', 2, 'га-га-га', 3)

goose_1 = Bird('Белый', 2, 'га-га-га', 3)

chicken = Bird('Ко-ко', 1, 'ко-ко-ко', 3)

chicken_1 = Bird('Кукареку', 1, 'ко-ко-ко', 3)

duck = Bird('Кряква', 1, 'кря-кря-кря', 3)

class ClovenFooted(Animal):

  food = 7
  
  milk = 0 # кол-во молока, которое нам дало определенное животное.

  def collect(self):
    self.milk += 5 # 5л в среднем может нам дать корова и коза за раз.

cow = ClovenFooted('Манька', 600, 'мууу', 800)

goat = ClovenFooted('Рога', 55, 'бе-е-е', 65)

goat_1 = ClovenFooted('Копыта', 55, 'бе-е-е', 65)

class Sheep(Animal):

  food = 7
  
  wool = 100 # измеряется в процентах

  def collect(self):
    clip = input('Введите на сколько процентов хотите стричь шерсть у {}:'.format(self.name))
    if int(clip) <= 100:
      self.wool = self.wool % int(clip) 
    elif int(clip) > 100:
      print('У вас не получится стричь шерсть больше чем на 100%')

sheep = Sheep('Барашек', 50, 'ме-е-е', 70)

sheep_1 = Sheep('Кудрявый', 50, 'ме-е-е', 70)

animals = [goose, goose_1, chicken, chicken_1, duck, cow, goat, goat_1, sheep, sheep_1]

def the_hardest():
  weight_animals = []
  for animal in animals:
    weight_animals.append(animal.weight)
  for animal in animals:
    if max(weight_animals) == animal.weight:
      print('Самое тяжелое животное:', max(weight_animals), animal.name)
  
def weight_of_all_animals():
  weight_animals = []
  for animal in animals:
    weight_animals.append(animal.weight)
  print(sum(weight_animals), 'вес всех животных')

def feeding():
  for animal in animals:
    animal.feed()

def collecting():
  for animal in animals:
    animal.collect()

feeding()

collecting()

the_hardest()

weight_of_all_animals()