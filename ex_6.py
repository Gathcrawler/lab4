# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов
import json
from enum import unique
from librip.iterators import Unique as unique

import sys

from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random

path = sys.argv[1]
with open(path, encoding='utf8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    return sorted(unique(field(arg, 'job-name'), ignore_case=True), key=str.lower)


@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith('Программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    salary = list(gen_random(100000, 200000, len(arg)))
    return list('{}, зарплата {} руб'.format(x, y) for x, y in zip(arg, salary))


with timer():
    f4(f3(f2(f1(data))))
