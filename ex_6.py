for a1 in "123456789":  # первая цифра (Х не может быть 0)
    for a2 in "0123456789":  # вторая цифра (О может быть 0)
        for a3 in "0123456789":  # третья цифра (Д может быть 0)
            number_set = {a1, a2, a3}
            number_int = int(a1) * 100 + int(a2) * 10 + int(a3) # формируем число ХОД

            if len(number_set) == 3 and number_int * 3 < 1000:
                summ_set = set(str(number_int * 3))# множество цифр результата МАТ
                if len(summ_set) == 3 and len(summ_set & number_set) == 0:
                    print(number_int, " + ", number_int, " + ", number_int, " = ", number_int * 3)
