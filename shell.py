import datetime

from kfc.models import *

client_1 = Client(user=User.objects.create(email='nikname21@gmail.com', password='defender42'), name='Азат Соколов',
                  card_number=4147_5657_9878_9009)
client_1.save()

worker_1 = Worker(user=User.objects.create(email='altywa1998@gmail.com', password='nono34'), name='Алтынай Алиева',
                  position='Оператор кассы')
worker_1.save()

cheese = Ingredient.objects.create(name='Сыр', extra_price=10)
cheese.save()

chicken = Ingredient.objects.create(name='Курица', extra_price=70)
chicken.save()

beef = Ingredient.objects.create(name='Говядина', extra_price=80)
beef.save()

salad = Ingredient.objects.create(name='Салат', extra_price=15)
salad.save()

free = Ingredient.objects.create(name='Фри', extra_price=15)
free.save()

shaurma = Food(name='Шаурма', start_price=50)
shaurma.save()

gamburger = Food(name='Гамбургер', start_price=25)
gamburger.save()

shaurma.ingredient.set([cheese, chicken, beef],
                       through_defaults={'client': client_1, 'worker': worker_1, 'order_date_time': '2022-12-12'})

sum_1 = shaurma.start_price + cheese.extra_price + chicken.extra_price + beef.extra_price
print(sum_1)

gamburger.ingredient.set([chicken, salad],
                         through_defaults={'client': client_1, 'worker': worker_1, 'order_date_time': '2022-12-12'})

sum_2 = gamburger.start_price + chicken.extra_price + salad.extra_price
print(sum_2)

print(sum_1 + sum_2)
