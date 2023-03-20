
#ф-ция выключения ПК пр вводе данных упрощенным образом
import time
import os
def time_off(text):
    while True:

        time.sleep(10)

        time_1 = time.strftime("%H:%M")
        time_sum = []
        for tttt in time_1:
            time_sum.append(tttt)

        time_1 = ''.join(time_sum)
        time_1 = time_1.split()

        b=text

        if time_1 == b:
            print ('время выклбчения ПКЖ',b)
            print ('Текущее время ',time_1)
            os.system('shutdown -s')
            break
        


time_off(['17:40'])

