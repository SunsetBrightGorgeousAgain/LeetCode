# coding=utf-8
import time
from functools import wraps


class RetryException(Exception):
    def __init__(self):
        err = 'this func need retry'
        Exception.__init__(self, err)


def decorate(func):
    local_retry = 3
    local_time_wait = 0.1
    default_return = None

    @wraps(func)
    def wrapper(*args, **kwargs):
        for i in range(local_retry):
            try:
                res = func(*args, **kwargs)
                return res
            except Exception:
                time.sleep(local_time_wait)
                continue

        # 达到重试次数后仍然没有获得期望的结果则返回默认值
        return default_return

    return wrapper


@decorate
def first_test(name):
    print(123)
    return 'hello {name}'.format(name=name)


print(first_test('lili'))

print('--------------------------')


@decorate
def second_name(name):
    print(123)
    raise Exception()
    return 'hello {name}'.format(name=name)


second_name('lili')

print('*************************')


@decorate
def third_name(name):
    print(123)
    0 / 0
    return 'hello {name}'.format(name=name)


third_name(1)
