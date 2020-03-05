class Cat():
    name = "mikyi"

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


cat = Cat()

print(Cat.name)
print(cat.name)
print(cat.get_name())

cat.set_name("xiaomaomi")
print(Cat.name)
print(cat.name)
print(cat.get_name())



class Game:
    @staticmethod
    def menu():
        print('.....')
        print('开始[1]')
        print('暂停[2]')
        print('退出[3]')
Game.menu()

