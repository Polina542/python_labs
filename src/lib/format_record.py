def format_record(rec):
    '''возвращает строку вида: Фамилия И.О., гр. <группа>, GPA <оценка>. При некорректной записи возвращает ValueError'''

    s = ''
    if len(rec) != 3:
        raise ValueError('Неверно введены данные в кортеже')

    str_without_whitespace = rec[0].replace(' ', '')

    # преобразование имени
    if type(rec[0]) == str and str_without_whitespace.isalpha():
        if len(rec[0].split()) == 2:
            name_list = rec[0].title().split()
            name_str = name_list[0] + ' ' + name_list[1][0] + '., '
            s = s + name_str
        elif len(rec[0].split()) == 3:
            name_list = rec[0].title().split()
            name_str = name_list[0] + ' ' + \
                name_list[1][0] + '.' + name_list[2][0] + '., '
            s = s + name_str
        else:
            raise ValueError('Неверно введено имя!')
    else:
        raise ValueError(
            'Имя не является строкой либо есть символы, не являющиеся буквой или пробелом')

    # преобразование группы
    gr_without_whitespace = rec[1].replace(' ', '')

    if len(gr_without_whitespace) > 0:
        s = s + 'гр. ' + gr_without_whitespace + ', '
    else:
        raise ValueError('Группа введена неверно')

    # преобразование оценки
    if (type(rec[2]) == float or type(rec[2]) == int) and (0 <= rec[2] <= 5):
        s = s+'GPA ' + f'{rec[2]:.2f}'
    else:
        raise ValueError('неверно введена оценка')

    return s
