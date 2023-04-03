class Human:
    default_name = 'Кузя'
    default_age = 20
    def __init__(self, house, money, name=default_name, age=default_age):
        self.__house = None
        self.__house = house
        self.__money = 0
        self.__money = money
        self.name = name
        self.age = age
    def earn_money(self, money, name):
        money += 100
        print('{} заработал денег'.format(self.name))
    def info(self, house, name, age, money):
        print(str(f'дом {house}, имя {name}, возраст {age}, баланс {money}'))
    @staticmethod
    def default_info(default_name, default_age):
        return default_name, default_age
    def __make_deal(self, money, House, House_cost):
            money -= House_cost
            House = self.__house
    def buy_house(self, House_cost, money, House):
        if self.money >= House_cost:
            self.__make_deal(money=self.money, House= House, House_cost=House_cost)
        elif self.money < House_cost:
            print('Ошибка, недостаточно средств')
            self.earn_money()