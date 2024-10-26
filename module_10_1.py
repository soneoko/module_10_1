from time import sleep, time
from threading import Thread
def  write_words(word_count, file_name):
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(1, word_count + 1):
        file.write(f'Какое-то слово №{i}' + '\n')
        sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start_time = time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
finish_time = time()
print(f'Работа потоков {finish_time - start_time}')

args = [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]
start_time1 = time()
threads = []
for x in args:
    thread = Thread(target=write_words, args= x)
    threads.append(thread)
    thread.start()
for y in threads:
    y.join()
finish_time1 = time()
print(f'Работа потоков {finish_time1 - start_time1}')



