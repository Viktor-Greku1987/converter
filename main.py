#coding=utf8
# ф-ция определения часа в который необходимо выключить ПК
def clock_in(textnum = str, numwords={}):

    #print("textnum : ", textnum)
    global rez_clok_in
    #textnum = textnum.split()
    # выполняем проверку на наличие в выражении о времни выключения.
    # Если нет данных, значит выключение будет только в минутах

    if textnum == '':
        rez_clok_in = '00'
        print("выключение ПК в: ", rez_clok_in)
        return rez_clok_in
    #print(textnum[-1])
    textnum = textnum.split()
    #print("textnum[-1] = ",textnum[-1])

    if textnum[-1] == "часов" or textnum[-1] == 'часов' or textnum[-1] == 'час':
        if len(textnum)> 1:

            # отсекаем словов "часа"
            textnum = ' '.join(textnum[0:len(textnum)-1])
            textnum=textnum.split()
        #print(textnum)
        else:
            textnum = ' '.join(textnum[0:len(textnum)])
            textnum = textnum.split()


    if not numwords:
        units = [
            "ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь",
            "девять", "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
            "шеснадцать", "семнадцать", "восемнадцать", "девятнадцать", "двадцать"        ]

        units_n = []
        for i in range(0, 16):
            units_n.append(str(i))

        units_1 = ["ноль", "одиу", "две"]

        hour_1 = ['ноль', 'час' ]

        #hour_05 = ['ноль', 'пол' ]

        #hour_1_5 = ["ноль", "полтора" ]



        #tens = ["", "", "двадцать"]

        numwords["and"] = (1, 0)
        #print(numwords)
        for idx, word in enumerate(units):
            numwords[word] = (1, idx)
        for idx, word in enumerate(units_n):
            numwords[word] = (1, idx)
        for idx, word in enumerate(units_1):
            numwords[word] = (1, idx)
        for idx, word in enumerate(hour_1):
            numwords[word] = (1, idx)
        #for idx, word in enumerate(hour_05):
            #numwords[word] = (1, idx*0.5)
        #for idx, word in enumerate(hour_1_5):
            #numwords[word] = (1, idx*1.5)

        #for idx, word in enumerate(tens):
            #numwords[word] = (1, idx * 10)

            #numwords[hour[i]] = (10 ** (i * 3 or 2), 0)
    current = result = 0
    textnum = ' '.join(textnum)
    for word in textnum.split():
        if word not in numwords:
            raise Exception("Незаконное слово: " + word)

        scale, increment = numwords[word]

        print('scale :',scale, 'increment : ',increment )
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0


    #global rez_clok
    rez_clok_in = (result + current)
    if int(rez_clok_in) < 10:
        rez_clok_in = str(rez_clok_in)
        rez_clok_in = "0" +rez_clok_in
        print('выключение через в ', rez_clok_in, ' часов (от фнкции определения часа)')
        return rez_clok_in
    else:
        rez_clok_in = str(rez_clok_in)
        print('выключение через в ',rez_clok_in, ' часов (от фнкции определения часа)')
        return rez_clok_in

#clock_in('15 часов', numwords={})

def minutes_in(textnum=str, numwords={}):
    global rez_minuts_in
    if textnum == '':
        rez_minuts_in = '00'
        return rez_minuts_in
    if not numwords:
        units = [
            "ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь",
            "девять", "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
            "шеснадцать", "семнадцать", "восемнадцать", "девятнадцать", ]
        units_1 = [
            "ноль", "одну", "две",  ]

        minut_05 = ['ноль', 'пол']

        minut_1_5 = ["ноль", "полтора"]

        units_n = []
        for i in range(0, 40):
            units_n.append(str(i))

        tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
                "девяносто"]

        numwords["and"] = (1, 0)
        # print(numwords)
        for idx, word in enumerate(units):
            numwords[word] = (1, idx)

        for idx, word in enumerate(units_n):
            numwords[word] = (1, idx)

        for idx, word in enumerate(units_1):
            numwords[word] = (1, idx)

        for idx, word in enumerate(tens):
            numwords[word] = (1, idx * 10)
        for idx, word in enumerate(minut_05):
            numwords[word] = (1, idx * 0.5)
        for idx, word in enumerate(minut_1_5):
            numwords[word] = (1, idx * 1.5)

            # numwords[hour[i]] = (10 ** (i * 3 or 2), 0)
    current = result = rez = 0
    for word in textnum.split():
        if word not in numwords:
            raise Exception("Незаконное слово: " + word)

        scale, increment = numwords[word]
        # print('scale :',scale, 'increment : ',increment )
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

        rez_minuts_in = result + current

    if rez_minuts_in < 10:
        rez_minuts_in = str(rez_minuts_in)
        rez_minuts_in = '0' + rez_minuts_in
        print('выключение в', rez_minuts_in, ' минуту(ы)(от фнкции определения минут)')
        return rez_minuts_in
    else:
        print('выключение в', rez_minuts_in, ' минуту(ы)(от фнкции определения минут)')
        return str(rez_minuts_in)

#minutes_in('5', numwords={})

def sum_time_in(rez_minuts_in, rez_clok_in):

    time_offsetting_in = str(rez_clok_in)+":" + str(rez_minuts_in)
    print('Итогое время до выключения компьтера: ', time_offsetting_in)

def text2int_clock(textnum = str, numwords={}):

    #print("textnum : ", textnum)
    global rez_clok
    #textnum = textnum.split()
    # выполняем проверку на наличие в выражении о времни выключения.
    # Если нет данных, значит выключение будет только в минутах

    if textnum == []:
        rez_clok = 0
        return rez_clok
    #print(textnum[-1])
    textnum = textnum.split()
    #print("textnum[-1] = ",textnum[-1])

    if textnum[-1] == "часа":

        # отсекаем словов "часа"
        textnum = ' '.join(textnum[0:len(textnum)-1])
        #print(textnum)


    if not numwords:
        units = [
            "ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь",
            "девять", "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
            "шеснадцать", "семнадцать", "восемнадцать", "девятнадцать"         ]

        units_n = []
        for i in range(0, 1000):
            units_n.append(str(i))

        units_1 = ["ноль", "одиу", "две"]

        hour_1 = ['ноль', 'час' ]

        hour_05 = ['ноль', 'пол' ]

        hour_1_5 = ["ноль", "полтора" ]



        tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]

        numwords["and"] = (1, 0)
        #print(numwords)
        for idx, word in enumerate(units):
            numwords[word] = (1, idx)
        for idx, word in enumerate(units_n):
            numwords[word] = (1, idx)
        for idx, word in enumerate(units_1):
            numwords[word] = (1, idx)
        for idx, word in enumerate(hour_1):
            numwords[word] = (1, idx)
        for idx, word in enumerate(hour_05):
            numwords[word] = (1, idx*0.5)
        for idx, word in enumerate(hour_1_5):
            numwords[word] = (1, idx*1.5)



        for idx, word in enumerate(tens):
            numwords[word] = (1, idx * 10)

            #numwords[hour[i]] = (10 ** (i * 3 or 2), 0)
    current = result =  rez= 0
    textnum = ' '.join(textnum)
    for word in textnum.split():
        if word not in numwords:
            raise Exception("Незаконное слово: " + word)

        scale, increment = numwords[word]
        #print('scale :',scale, 'increment : ',increment )
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0


    #global rez_clok
    rez_clok = (result + current)*60

    print('выключение через',rez_clok, ' минут(от фнкции определения часа)')
    return int(rez_clok)


def text2int_minutes(textnum=str, numwords={}):
    global rez_minuts
    if textnum == '':
        rez_minuts = 0
        return rez_minuts
    if not numwords:
        units = [
            "ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь",
            "девять", "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
            "шеснадцать", "семнадцать", "восемнадцать", "девятнадцать", ]
        units_1 = [
            "ноль", "одну", "две",  ]

        minut_05 = ['ноль', 'пол']

        minut_1_5 = ["ноль", "полтора"]

        units_n = []
        for i in range(0, 1000):
            units_n.append(str(i))

        tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
                "девяносто"]

        numwords["and"] = (1, 0)
        # print(numwords)
        for idx, word in enumerate(units):
            numwords[word] = (1, idx)

        for idx, word in enumerate(units_n):
            numwords[word] = (1, idx)

        for idx, word in enumerate(units_1):
            numwords[word] = (1, idx)

        for idx, word in enumerate(tens):
            numwords[word] = (1, idx * 10)
        for idx, word in enumerate(minut_05):
            numwords[word] = (1, idx * 0.5)
        for idx, word in enumerate(minut_1_5):
            numwords[word] = (1, idx * 1.5)

            # numwords[hour[i]] = (10 ** (i * 3 or 2), 0)
    current = result = rez = 0
    for word in textnum.split():
        if word not in numwords:
            raise Exception("Незаконное слово: " + word)

        scale, increment = numwords[word]
        # print('scale :',scale, 'increment : ',increment )
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

        rez_minuts = result + current
    #print('выключение через', rez_minuts, ' минут(от фнкции определения минут)')
    return int(rez_minuts)

def sum_time(rez_minuts, rez_clok):

    time_offsetting = rez_clok + rez_minuts
    print('Итогое время до выключения компьтера: ', time_offsetting)

def clock_1(textnum = str):

    textnum = textnum.split()
    textnum_1 = [] # список , покоторому будет проверяться условие
    # по какой ветке пойти опредления времени либо "в" либо "через"
    through = ['через'] #клчевое слово выбора поределения сколько времени осталось до выключения
    in_v = ['в']

    for idx, text_3 in enumerate(textnum):
        textnum_1.append(str(text_3))
    rezult_th = list(set(through) & set(textnum_1))
    rezult_in_v = list(set(in_v) & set(textnum_1))
    if rezult_th != []:
        for i_i, text_5 in enumerate(textnum):
            if text_5 == 'через':
                u = i_i
                textnum = ' '.join(textnum[u+1:len(textnum)])
                #print('время до выключения: ',textnum)
                textnum = textnum.split()
                #print(textnum)
                hours_2 = ['часа', 'час']
                hours_3 = []
                for ii, hours_1 in enumerate(textnum):
                    hours_3.append(str(hours_1))
                #print('hours_3 = ', hours_3)
                rez_1 =list(set(hours_3) & set(hours_2))
                #print("rez_1 = ", rez_1)

                if rez_1 != [] :
                    for ii_1, hours_4 in enumerate(textnum):
                        if hours_4 == 'час' or hours_4 == 'часа':
                            i_1 = ii_1
                            clocks = ' '.join(textnum[0:i_1+1])
                            #print('солько ЧАСОВ до выключения : ', clocks)
                            clocks =str(clocks)
                            minutes = ' '.join(textnum[i_1+1:len(textnum)-1])
                            #print('солько минут до выключения : ', minutes)
                            text2int_clock(clocks, numwords={})
                            text2int_minutes(minutes, numwords={})
                            sum_time(rez_minuts, rez_clok)

                else:
                    minutes = ' '.join(textnum[0:len(textnum) - 1])
                    #print('солько минут до выключения : ', minutes)
                    text2int_minutes(minutes, numwords={})
                    sum_time(rez_minuts, 0)
    elif rezult_in_v != []:

        for yy, checking_v in enumerate(textnum):
            if checking_v == 'в':
                stop_yy = yy
                textnum = ' '.join(textnum[stop_yy+1: len(textnum)])
                textnum = textnum.split()
                print("textnum : ", textnum)
                hours_2 = ['часа', 'час', 'часов']
                checking_hour = list(set(textnum) & set(hours_2))
                if checking_hour !=[]:
                    for y, checking_h  in enumerate(textnum):
                        if checking_h == 'часа' or checking_h == 'час' or checking_h == 'часов':
                            y_stop = y
                            print("y", y)
                            hour_h = ' '.join(textnum[0:y_stop+1])
                            minut_h = ' '.join(textnum[y_stop+1:len(textnum)-1])
                            clock_in(hour_h, numwords={})
                            minutes_in(minut_h, numwords={})
                            sum_time_in(rez_minuts_in, rez_clok_in)















clock_1('выключи компьтер в 15 часов 12 минут ')

