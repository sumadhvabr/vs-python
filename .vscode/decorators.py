# wrapper fun


def wrap(f):
    def inner():
        print('Got Decorated')
        f()
    return inner  


# normalfunction
def func():
    print('This is an ordinary output')
df=wrap(func)
print(type(df))
df()


# syntatic decorators


def split_val(f):
    def val():
        func=f()
        s_s=func.split()
        return s_s
    return val



def upper_val(f):
    def val():
        func=f()
        u_v=func.upper()
        return u_v
    return val



@upper_val
def input_val():
    return 'This is python programming'
print(input_val())

        

