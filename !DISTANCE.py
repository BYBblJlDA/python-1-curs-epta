def run():
    # Есть словарь координат городов
    sites = {
        'Moscow': (550, 370),
        'London': (510, 510),
        'Paris': (480, 480),
    }

    # Составим словарь словарей расстояний между ними
    distances = {}

    for city1 in sites:
        distances[city1] = {}
        x1, y1 = sites[city1]
        # Этот цикл должен быть сдвинут вправо (вложен в первый цикл)
        for city2 in sites:
            x2, y2 = sites[city2]
            distances[city1][city2] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    print(distances)

run()
