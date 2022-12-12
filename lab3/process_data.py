import json
from print_result import print_result
from cm_timer import cm_timer_1
from unigue import Unique
from field import field
from gen_random import gen_random
from operator import concat


def f1(a):
    return Unique([i['job-name'] for i in field(data, 'job-name')], ignore_case=True)
def f2(a):
    return filter(lambda a: a.startswith('программист'), a)
def f3(a):
    return list(map(lambda x: concat(x, ' c опытом Python'), a))
def f4(a):
    return zip(a, gen_random(len(a),137287, 200000))

with open('data_light.json','r',encoding='utf-8') as f:
    data = json.load(f)
    for i in f4(f3(f2(f1(data)))):
        print(i)