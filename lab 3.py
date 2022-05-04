def one(*args):
    return list(args)


print(one(88, 54, "kak-to tak"))


def second(lst):
    lst.sort(key=lambda x: abs(x), reverse=True)
    return lst


print(second([-33, -0.05, -4.18, 11.2, 13.12]))


def third(First_name, Second_name, Weight, Hight, Age):
    data = {'Age': Age, 'Weight': Weight, 'Hight': Hight, 'First_name': First_name}
    Sex = input('Укажите пол: ')
    data['Sex'] = Sex
    return print(data)


third(First_name="dsadas", Second_name="wda", Weight="70", Hight="182", Age="20")


def four_max():
    dict_one = {'a': 1, 'b': 5, 'c': 9}
    dict_two = {'a': 4, 'b': 2}
    dict_max = {}
    dicts = [dict_one, dict_two]
    for key_1, value_1 in dict_one.items():
        for key_2, value_2 in dict_two.items():
            if key_1 == key_2:
                dict_max[key_1] = max(value_1, value_2)
    print(dict_max)




def four_sum():
    dict_one = {'a': 1, 'b': 5, 'c': 9}
    dict_two = {'a': 4, 'b': 2}
    dict_sum = {}
    dicts = [dict_one, dict_two]
    for key_1, value_1 in dict_one.items():
        for key_2, value_2 in dict_two.items():
            if key_1 == key_2:
                dict_sum[key_1] = value_1 + value_2
    print(dict_sum)




def five(tpl):
    for element in tpl:
        if not isinstance(element, int):
            return tpl
    return tuple(sorted(tpl))


#print(five((5, 5, 3, 1, 9)))


def six(dict, elem):
    if elem in dict:
        dict = dict.replace(elem, '', 1)
        return dict
    else:
        return dict
