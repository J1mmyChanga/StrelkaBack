from data import db_session
from data.places import Places
from data.routes import Routes
from data.users import Users
from data.categories import Categories

db_session.global_init('db/strelka.db')
session = db_session.create_session()

pl1 = Places(id=1, title='деревня Борок', description='Круто летом отдыхать', lat=54.767518, long=31.742566, rating=4.8, category='2', image='1.jpg')
pl2 = Places(id=2, title='парк "Реадовка"', description='Главное в озере не купаться', lat=54.760189, long=32.020441, rating=4.2, category='2', image='2.jpg')
pl3 = Places(id=3, title='Бункер "Медвежье Логово"', description='Бункер связистов времен ВОВ', lat=54.783998, long=31.896552, rating=4.4, category='3', image='3.jpg')
pl4 = Places(id=4, title='парк "Лопатинский сад"', description='Самый популярный парк в Смоленске', lat=54.782508, long=32.040862, rating=4.8, category='2', image='4.jpeg')

r1 = Routes(id=1, title='Исток', description='Вдоль реки Днепр. Мы проходим через деревню Борок и Бункер "Медвежье Логово"', category='1', duration=50, rating=4.9)
r2 = Routes(id=2, title='Повторение', description='Вокруг Смоленска. Мы проходим через парк "Реадовка" и парк "Лопатинский сад"', category='2', duration=45, rating=4.6)
r3 = Routes(id=3, title='Путь из варяг в пельмени', description='Стань реальным петушком!. Мы проходим через парк "Лопатинский сад" и Бункер "Медвежье Логово"', category='3', duration=228, rating=4.6)

cat1 = Categories(id=1, title='Еда')
cat2 = Categories(id=2, title='Развлечения')
cat3 = Categories(id=3, title='Туризм')

user = Users(id=1, email='kowlad@aboba.ru')
user.set_password('12345678')
session.add(user)

for i in range(1, 4):
    session.add(eval(f'cat{i}'))

for i in range(1, 4):
    session.add(eval(f'r{i}'))

for i in range(1, 5):
    session.add(eval(f'pl{i}'))
session.commit()