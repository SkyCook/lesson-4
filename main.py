class Pokemon:
    def __init__(self, name, element, stage, hp, energy):
        self._name = name
        self._element = element
        self._stage = stage
        self._hp = hp
        self._energy = energy

    def battle_cry(self):
        print(self._name.upper() + '!!!')

class Pichu(Pokemon):
    def thunder_shock(self, target):
        self._energy -= 15
        target._hp -= 40
        print(self._name + ' использует Thunder shock и наносит 40 урона. у ' + str(target._name) + ' остаётся ' + str(target._hp) + ' HP.')

class Pikachu(Pichu):
    def thunderbolt(self, target):
        self._energy -= 30
        target._hp -= 90
        print(self._name + ' использует Thunderbolt и наносит 90 урона. у '+ str(target._name) + ' остаётся ' + str(target._hp) + ' HP.')

class Raichu(Pikachu):
    def thunder(self, target):
        self._energy -= 45
        target._hp -= 110
        print(self._name + ' использует Thunder и наносит 110 урона. у '+ str(target._name) + ' остаётся ' + str(target._hp) + ' HP.')


pichu = Pichu('Pichu', 'lightning', 1, 200, 200)
pikachu = Pikachu('Pikachu', 'lightning', 2, 350, 400)
raichu = Raichu('Raichu', 'lightning', 3, 600, 800)
pichu.battle_cry()
pikachu.battle_cry()
raichu.battle_cry()
pikachu.thunder_shock(pichu)
pikachu.thunderbolt(pichu)
pichu.thunder_shock(pikachu)
raichu.thunder(pichu)
raichu.thunder(pikachu)

class Student:
    def __init__(self, zel, hist, trav, fig, name):
        self._zel = zel
        self._hist = hist
        self._trav = trav
        self._fig = fig
        self._name = name

    def summ_exam(self):
        s = self._zel+self._hist+self._trav+self._fig
        print(f'Отметки за экзамены учащегося {self._name}:\n'
              f'1. Зельеварение: {self._zel}\n'
              f'2. История магии: {self._hist}\n'
              f'3. Травничество: {self._trav}\n'
              f'4. Трансфигурация: {self._fig}\n'
              f'Итого: {s}')


student1 = Student(9, 4, 8, 9, 'Alex')
student1.summ_exam()


class Game:
    def __init__(self, tex, dif, cor, ask, ans, bal=None):
        self._tex = tex
        self._dif = dif
        self._cor = cor
        self._ask = False
        self._ans = None

    def get_points(self):
        dif_lvl = int(self._dif.split('/')[0])
        return dif_lvl * 10

    def is_correct(self):
        if self._ans is None:
            return False
        return (str(self._ans).strip().lower() ==
                (str(self._cor)).strip().lower())

    def build_question(self):
        return f'Вопрос: {self._tex}\nСложность {self._dif}/5'

    def build_positive_feedback(self):
        points = self.get_points()
        return f'Ответ верный, получено {points} баллов'

    def build_negative_feedback(self):
        return f'Ответ неверный, верный ответ {self._cor}'

    def set_user_answer(self, ans):
        self._ans = ans

    def ask_question(self):
        self._ask = True


questions = [
    Game('Which planet is known as a red planet?',
         '2/5', 'Mars'),
    Game('How many years are there in century?',
         '1/5', '100'),
    Game('who is the first presedent of the USSR(full name)?',
         '3/5','Vladimir Ilich Lenin')
]

total_score = 0
answers = 0








