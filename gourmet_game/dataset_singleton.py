import random
class GameDataSet:
    def __init__(self):
        self.foods = {
            'massas': ['macarrão',
                       'Lasanha',
                       'Nhoque',
                       'Pizza',
                       'Calzone',
                       ],
            'churrasco': ['Costela',
                          'Fraldinha',
                          'Picanha',
                          ],
            'doce':['Rocambole',
                    'Brownie',
                    'Cookie',
                    'Torta de Limão',
                    'Mousse de Maracujá',
                    'Rapadura',
                    'Paçoquinha',
                    ]
        }

    def get_afood_type(self):
        return random.choice(list(self.foods.keys()))

    def get_afood_from_atype(self, type):
        foods = self.foods[type]
        return random.choice(list(foods))

    def get_afood_from_another_type(self, type):
        all_foods = []
        for food_type in self.foods:
            if food_type is not type:
                for food in self.foods[food_type]:
                    all_foods.append(food)
        return random.choice(all_foods)

if __name__ == "__main__":
    app = GameDataSet()
    print(app.get_afood_from_another_type('doce'))