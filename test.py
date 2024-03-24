from data import db_session
from data.places import Places
from data.routes import Routes
from data.categories import Categories

db_session.global_init('db/strelka.db')
session = db_session.create_session()

pl1 = Places(id=1, title='деревня Борок', description='Круто летом отдыхать', lat=54.6669, long=35.4664, rating=4.8, category='1', image='1.jpg')
pl2 = Places(id=2, title='парк Реадовка', description='Главное в озере не купаться', lat=54.3467, long=35.789, rating=4.2, category='2', image='2.jpg')
pl3 = Places(id=3, title='Бункер Гитлера', description='Там вроде Гитлер застрелился', lat=54.3267, long=35.9053, rating=4.4, category='3', image='3.jpg')

r1 = Routes(id=1, title='Исток', description='Вдоль реки Днепр', duration=50, rating=4.9)
r2 = Routes(id=2, title='Повторение', description='Вокруг Смоленска', duration=45, rating=4.6)

cat1 = Categories(id=1, title='Еда')
cat2 = Categories(id=2, title='Развлечения')
cat3 = Categories(id=3, title='Туризм')

for i in range(1, 4):
    session.add(eval(f'cat{i}'))

for i in range(1, 3):
    session.add(eval(f'r{i}'))

for i in range(1, 4):
    session.add(eval(f'pl{i}'))
session.commit()