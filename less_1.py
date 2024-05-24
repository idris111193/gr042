class SuperHero:
    nindja = 'nindja'

    def __init__(self, name, nickname, superpower, health, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health = health
        self.catchphrase = catchphrase

    def print_name(self, name):
        print('name hero is', self.name)

    def double_health(self):
        self.health *= 2
        print('health is', self.health)

    def __str__(self):
        return f'{self.nickname}, {self.superpower}, {self.health}, {self.catchphrase}'



    def __len__(self):
         return len (self.catchphrase)




hero = SuperHero('Hanzo Hasashi', 'Scorpion', 'firekatana', 500, 'SubZero must die')
hero.print_name('Hanzo Hasashi')
hero.double_health()
print(hero)
catchphrase_lenth = len(hero.catchphrase)
print('catchphrase lenth is',catchphrase_lenth )


