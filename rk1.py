from operator import itemgetter
 
class Composition:
    def __init__(self, id, name, duration, o_id):
        self.id = id
        self.name = name
        self.duration = duration
        self.o_id = o_id
 
class Orchestra:
    def __init__(self, id, name):
        self.id = id
        self.name = name
 
class ComOrc:
    def __init__(self, orc_id, com_id):
        self.orc_id = orc_id
        self.com_id = com_id
 
orchestras = [
    Orchestra(1, 'Оркестр Мариинского театра'),
    Orchestra(2, 'Российский национальный оркестр'),
    Orchestra(3, 'Bavarian Radio Symphony'),
 
    Orchestra(11, 'Vienna Philharmonic Orchestra'),
    Orchestra(22, 'Czech Philharmonic'),
    Orchestra(33, 'Royal Concertgebouw Orchestra'),
]
 
compositions = [
    Composition(1, 'Лунная соната', 4.4, 1),
    Composition(2, 'Симфония Бетховена', 12.2, 2),
    Composition(3, 'Симфония Баха', 3, 3),
    Composition(4, 'Симфония Моцарта', 11, 3),
    Composition(5, 'Симфония Сальери', 5.5, 3),
]
 
comorcs = [
    ComOrc(1,1),
    ComOrc(2,2),
    ComOrc(3,3),
    ComOrc(3,4),
    ComOrc(3,5),
 
    ComOrc(11,1),
    ComOrc(22,2),
    ComOrc(33,3),
    ComOrc(33,4),
    ComOrc(33,5),
]
 
def main():
    """Основная функция"""
 
    # Соединение данных один-ко-многим 
    one_to_many = [(c.name, c.duration, o.name) 
        for o in orchestras 
        for c in compositions 
        if c.o_id==o.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, co.orc_id, co.com_id) 
        for d in orchestras 
        for co in comorcs 
        if d.id==co.orc_id]
    
    many_to_many = [(c.name, c.duration, or_name) 
        for or_name, orc_id, com_id in many_to_many_temp
        for c in compositions if c.id==com_id]
 
    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)
    
    print('\nЗадание А2')
    res_12_unsorted = []
    # Перебираем все оркестры
    for o in orchestras:
        # Список произведений оркестра
        o_com = list(filter(lambda i: i[2]==o.name, one_to_many))
        # Если у оркестра есть произведения    
        if len(o_com) > 0:
            # Длительность произведения
            o_durations = [duration for _,duration,_ in o_com]
            # Суммарная длительность произведений
            o_durations_sum = sum(o_durations)
            res_12_unsorted.append((o.name, o_durations_sum))
 
    # Сортировка по суммарной длительности произведений
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)
 
    print('\nЗадание А3')
    res_13 = {}
    # Перебираем все окестры
    for o in orchestras:
        if 'оркестр' in o.name:
            # Список произведений оркестра
            o_com = list(filter(lambda i: i[2]==o.name, many_to_many))
            # Только названия произведений
            o_com_names = [x for x,_,_ in o_com]
            # Добавляем результат в словарь
            # ключ - оркестр, значение - список произведений
            res_13[o.name] = o_com_names
 
    print(res_13)
 
if __name__ == '__main__':
    main()
