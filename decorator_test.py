def start(func):
    print('*********')

    def inner(arg):
        func(arg)
        print('*********')

    def outer(arg):
        func(arg)
        print('%%%%%%%%')


    return outer

def end(func):
    print('######')

    def inner(arg):
        func(arg)
        print('######')


    return inner


@start
@end
def my_name(name):
    print('my name is {}'.format(name))


#s = start(my_name('gupta'))
my_name('Abhishek')