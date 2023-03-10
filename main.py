#coding=utf8
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
    print("textnum[-1] = ",textnum[-1])

    if textnum[-1] == "часа":

        # отсекаем словов "часа"
        textnum = ' '.join(textnum[0:len(textnum)-1])
        print(textnum)


    if not numwords:
        units = [
            "ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь",
            "девять", "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
            "шеснадцать", "семнадцать", "восемнадцать", "девятнадцать",         ]

        units_1 = [
            "ноль", "одиу", "две", ]

        hour_1 = ['ноль', 'час' ]

        hour_05 = ['ноль', 'пол' ]

        hour_1_5 = ["ноль", "полтора" ]



        tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]

        numwords["and"] = (1, 0)
        #print(numwords)
        for idx, word in enumerate(units):numwords[word] = (1, idx)
        for idx, word in enumerate(units_1): numwords[word] = (1, idx)
        for idx, word in enumerate(hour_1): numwords[word] = (1, idx)
        for idx, word in enumerate(hour_05):numwords[word] = (1, idx*0.5)
        for idx, word in enumerate(hour_1_5):numwords[word] = (1, idx*1.5)



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
            "ноль", "одну", "две", "три", "четыре", "пять", "шесть", "семь", "восемь",
            "девять", "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
            "шеснадцать", "семнадцать", "восемнадцать", "девятнадцать", ]

        tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
                "девяносто"]

        numwords["and"] = (1, 0)
        # print(numwords)
        for idx, word in enumerate(units):
            numwords[word] = (1, idx)
        for idx, word in enumerate(units_1):
            numwords[word] = (1, idx)

        for idx, word in enumerate(tens):
            numwords[word] = (1, idx * 10)

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
    print('выключение через', rez_minuts, ' минут(от фнкции определения минут)')
    return int(rez_minuts)

def sum_time(rez_minuts, rez_clok):

    time_offsetting = rez_clok + rez_minuts
    print('Итогое время до выключения компьтера: ', time_offsetting)

def clock_1(textnum = str):

    textnum = textnum.split()
    for idx, text in enumerate(textnum):
        if text == 'черерз':
            i = idx
            textnum = ' '.join(textnum[i+1:len(textnum)])
            print('время до выключения: ',textnum)
            textnum = textnum.split()
            print(textnum)
            for ii, hours in enumerate(textnum):
                if hours == 'часа' or hours == 'час':
                    i_1 = ii
                    clocks = ' '.join(textnum[0:i_1+1])
                    print('солько ЧАСОВ до выключения : ', clocks)
                    clocks =str(clocks)
                    minutes = ' '.join(textnum[i_1+1:len(textnum)-1])
                    print('солько минут до выключения : ', minutes)
                    text2int_clock(clocks, numwords={})
                    text2int_minutes(minutes, numwords={})
                    sum_time(rez_minuts, rez_clok)

                else:
                    minutes = ' '.join(textnum[0:len(textnum) - 1])
                    print('солько минут до выключения : ', minutes)
                    text2int_minutes(minutes, numwords={})




clock_1('выключи компьтер черерз двадцать минут ')

