"""Неправильные горы
  > При путешествии по планете марсоход постоянно замеряет высоту рельефа и сохраняет результаты замеров в массив.
  
  Одна из задач марсохода - поиск «правильных гор». «Правильной» считается та гора, у которой на пути от подножия до вершины высота постоянно растёт, а на пути от вершины к подножию - постоянно уменьшается. Если у горы есть несколько вершин или в каком-то месте встречается горизонтальный участок - это «неправильная гора».
  
  Напишите функцию valid_mountain_array, которая будет принимать на вход массив с высотами и возвращать True или False в зависимости от того, «правильная» это гора или не
  Если в массиве менее трёх элементов, такой массив не может описывать «правильную» гору.
  
  Формат ввода:
    Массив целых чисел через пробел - отметки о высоте точек рельефа.
  Формат вывода:
    Булево значение: True - если гора «правильная», False - если гора «неправильная».
"""


HEIGHTS: str = '9 10 6 5 5'

def is_valid_mountain_array(heights: str) -> bool:

    HEIGHTS_DATA: list = list(map(int, heights.split()))

    if len(HEIGHTS_DATA) > 3:

        MAX_ID_HEIGHTS_DATA: int = HEIGHTS_DATA.index(max(HEIGHTS_DATA))
        LEFT_HEIGHTS_DATA: list = HEIGHTS_DATA[:MAX_ID_HEIGHTS_DATA][::-1]
        RIGHT_HEIGHTS_DATA: list = HEIGHTS_DATA[MAX_ID_HEIGHTS_DATA + 1:]


        if len(LEFT_HEIGHTS_DATA) == 0:
            return False

        if len(RIGHT_HEIGHTS_DATA) == 0:
            return False

        if HEIGHTS_DATA[MAX_ID_HEIGHTS_DATA] == RIGHT_HEIGHTS_DATA[0]:
            return False

        # Проверка на дупликаты
        if len(LEFT_HEIGHTS_DATA) != len(set(LEFT_HEIGHTS_DATA)):
            return False

        if len(RIGHT_HEIGHTS_DATA) != len(set(RIGHT_HEIGHTS_DATA)):
            return False

        #TODO: Если переписать на итераторы, возможно будет быстрее
        if LEFT_HEIGHTS_DATA != sorted(LEFT_HEIGHTS_DATA):
            return False

        if RIGHT_HEIGHTS_DATA != sorted(RIGHT_HEIGHTS_DATA, reverse=True):
            return False

        return True

    return False


print(is_valid_mountain_array(HEIGHTS))


