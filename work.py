import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


# Тесты с обработкой исключений и логированием
def test_walk():
    try:
        runner = Runner("Боб", speed=-5)  # Передаем отрицательное значение скорости
    except ValueError as e:
        logging.warning("Неверная скорость для Runner: %s", e)
    else:
        logging.info('"test_walk" выполнен успешно')


def test_run():
    try:
        runner = Runner(12345, speed=10)  # Передаем некорректный тип для имени
    except TypeError as e:
        logging.warning("Неверный тип данных для объекта Runner: %s", e)
    else:
        logging.info('"test_run" выполнен успешно')


if __name__ == "__main__":
    test_walk()
    test_run()

