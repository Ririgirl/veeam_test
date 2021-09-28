from dirsync import sync
import logging
import time


source_path = str(input(r'Введите путь к папке источнику (для примера можете использовать test\first_path): '))
target_path = str(input(r'Введите путь к папке реплике (для примера можете использовать test\second_path): '))
timesleep = int(input(r'Введите интервал: '))
your_log = str(input(r'Введите путь к файлу в котором вы хотите увидеть логи '
                     r'(*.log) (для примера можете использовать your_log.log): '))


def log():
    logging.basicConfig(filename="your_log.log", level=logging.DEBUG)
    my_log = logging.getLogger('dirsync')
    return my_log


def start_program():
    while True:
        sync(source_path, target_path, 'sync', twoway=True, purge=True, logger=log())
        sync(target_path, source_path, 'sync')

        sync(source_path, target_path, 'diff', twoway=True, purge=True, logger=log())
        sync(target_path, source_path, 'diff')

        time.sleep(timesleep)


start_program()


