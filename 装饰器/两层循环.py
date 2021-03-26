def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2015-3-25')


now()

print(11 % 2 == 0)

xx = 54
print(xx is not None)

for i in range(0, 4, 2):
    print(i)
import re

regex = '[A-Z]{2}[0-9]{4}'
print(re.match(regex, 'AD3744'))

import pandas as pd

pf = pd.read_excel('../cc.xlsx')
coluns = pf.columns.values.tolist()
print(coluns)
