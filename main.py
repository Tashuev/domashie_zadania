import threading
from time import sleep, time

# Функция для записи слов в файл
def write_words(word_count, file_name):
    for i in range(1, word_count + 1):
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write(f"Какое-то слово № {i}\n")
        sleep(0.1)  # Задержка 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")

# Взятие текущего времени
start_time = time()

# Запуск функций с аргументами из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени
end_time = time()
print(f"Работа функций {end_time - start_time:.6f} секунд")

# Взятие текущего времени для потоков
start_time_threads = time()

# Создание потоков
threads = []
thread_args = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt')
]

for args in thread_args:
    thread = threading.Thread(target=write_words, args=args)
    threads.append(thread)
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

# Взятие текущего времени после завершения потоков
end_time_threads = time()
print(f"Работа потоков {end_time_threads - start_time_threads:.6f} секунд")
