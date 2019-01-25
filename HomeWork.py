class animals:
  
  def __init__(self, name, weight, voice, max_weight, max_amount_of_food):
    self.name = name
    self.weight = weight # вес измеряется в кг
    self.voice = voice
    self.max_weight = max_weight # теоритический максимальный вес
    self.max_amount_of_food = max_amount_of_food # максимальное кол-во еды, которое животное может съесть за раз.
  
  def feeding(self, food):
    print('Ням-ням-ням')
    if self.weight + food > self.max_weight:
      print('Мне кажется ей на сегодня хватит.')
    elif self.weight + food <= self.max_weight:
      if food > self.max_amount_of_food:
        print('Думаю за раз она столько не съест.')
      else:
        self.weight += food 

class birds(animals):
  
  eggs = 10 # яйца которые снесла птица, но мы не собрали.

  def collecting_eggs(self):
    sum_eggs = input('Введите сколько яиц вы хотите собрать:')
    if self.eggs >= int(sum_eggs):
      self.eggs = self.eggs - int(sum_eggs)
    else:
      print('Но тут только:', self.eggs)

goose = birds('Серый', 2, 'га-га-га', 3, 0.5)

goose_1 = birds('Белый', 2, 'га-га-га', 3, 0.5)

chicken = birds('Ко-ко', 1, 'ко-ко-ко', 3, 0.5)

chicken_1 = birds('Кукареку', 1, 'ко-ко-ко', 3, 0.5)

duck = birds('Кряква', 1, 'кря-кря-кря', 3, 0.5)

class cloven_footed(animals):
  
  milk = 0 # кол-во молока, которое нам дало определенное животное.

  def milking(self):
    self.milk += 5 # 5л в среднем может нам дать корова и коза за раз.

cow = cloven_footed('Манька', 600, 'мууу', 800, 12)

goat = cloven_footed('Рога', 55, 'бе-е-е', 65, 7)

goat_1 = cloven_footed('Копыта', 55, 'бе-е-е', 65, 7)

class sheeps(animals):
  
  wool = 100 # измеряется в процентах

  def clip_wool(self):
    clip = input('Введите на сколько процентов хотите стричь шерсть:')
    self.wool = self.wool % int(clip) 

sheep = sheeps('Барашек', 50, 'ме-е-е', 70, 7)

sheep_1 = sheeps('Кудрявый', 50, 'ме-е-е', 70, 7)

def weight_of_all_animals():
  print('Вес всех животных:', sum([goose.weight, goose_1.weight, chicken.weight, chicken_1.weight, duck.weight, cow.weight, goat.weight, goat_1.weight, sheep.weight, sheep_1.weight]), 'кг')

def the_hardest():  
  print('Самое тяжелое животное:', max([(goose.weight, goose.name), (goose_1.weight, goose_1.name), (chicken.weight, chicken.name), (chicken_1.weight, chicken_1.name), (duck.weight, duck.name), (cow.weight, cow.name), (goat.weight, goat.name), (goat_1.weight, goat_1.name), (sheep.weight, sheep.name), (sheep_1.weight, sheep_1.name)]))

weight_of_all_animals()

the_hardest()