def print_result(f):
    def wrapper(a):
        print(f.__name__)
        res = f(a)
        if type(res) == list:
            for i in res: 
                print(i)
        elif type(res) == dict:
            for k,v in res.items():
                print(k, '=', v)
        return res
    return wrapper 



#@print_result
#def test_1():
#  return 1


#@print_result
#def test_2():
#  return 'iu5'


#@print_result
#def test_3():
#  return {'a': 1, 'b': 2}


#@print_result
#def test_4():
#  return [1, 2]


#if __name__ == '__main__':
#    print('!!!!!!!!')
#    test_1()
#    test_2()
#    test_3()
#    test_4()