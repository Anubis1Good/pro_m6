
def parent(name):
    def helper(func):
        def wrapper(n):
            print('start')
            func(n)
            print(name)
            print('end')
        return wrapper
    return helper

@parent(name='Ivan')
def test(n):
    print('work', n)


test(10)