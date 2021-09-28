import os
import psutil
import time
import csv


def open_you_programm():
    t = str(input('Введите путь к файлу (прим. D:/SQLiteStudio/SQLiteStudio.exe): '))
    topen = os.startfile(t)

    PROCNAME = t.split('/')[-1]

    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
            print(proc)
            pid = proc.pid
            print(pid)

    interval = int(input('Введите интервал сбора статистики: '))
    p = psutil.Process(pid=pid)

    try:
        try:
            with open('statistic.csv', "w", newline="") as f:
                fieldnames = ['cpu_percent', 'Resident Set Size, Mb', 'Virtual Memory Size, Mb', 'num_handles']
                thewriter = csv.DictWriter(f, fieldnames=fieldnames)
                thewriter.writeheader()
                while(True):
                    thewriter.writerow({'cpu_percent' : p.cpu_percent(interval=1),
                                        'Resident Set Size, Mb' : p.memory_info().rss/1000000, 'Virtual Memory Size, Mb' :
                                       p.memory_info().vms/1000000, 'num_handles' : p.num_handles()})
                    print()
                    print(p.cpu_percent(interval=1))
                    print(str(p.memory_info().rss/1000000))
                    print(str(p.memory_info().vms/1000000))
                    print(p.num_handles())
                    print('---')
                    time.sleep(interval)
        except Exception as e:
            print(e)
        finally:
            print('close')
    except psutil.NoSuchProcess:
        print('close with exeption')


open_you_programm()