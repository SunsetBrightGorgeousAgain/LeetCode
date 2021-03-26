# coding=utf-8
import time
from functools import wraps


class RetryException(Exception):
    def __init__(self):
        err = 'this func need retry'
        Exception.__init__(self, err)


def retry_func(retry=3, time_wait=0.1, return_value=None):
    def decorate(func):
        local_retry = retry
        local_time_wait = time_wait
        default_return = return_value

        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(local_retry):
                try:
                    res = func(*args, **kwargs)
                    return res
                except RetryException:
                    time.sleep(local_time_wait)
                    continue

            # 达到重试次数后仍然没有获得期望的结果则返回默认值
            return default_return

        return wrapper

    return decorate


@retry_func(return_value=0)
def first_test(name):
    print(123)
    return 'hello {name}'.format(name=name)


print(first_test('lili'))


@retry_func(return_value=0)
def second_name(name):
    print(123)
    raise RetryException()
    return 'hello {name}'.format(name=name)


print(second_name('lili'))


@retry_func(return_value=0)
def third_name(name):
    print(123)
    0 / 0
    return 'hello {name}'.format(name=name)


print(third_name('lili'))








print(11/2)



















