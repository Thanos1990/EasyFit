def generate_fibonacci_under(max):
    a, b = 0, 1
    while a<max:
        yield a
        a, b = b, a+b


# Generator function for an infinite generator of Fibonacci numbers
def generate_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


if __name__ == '__main__':

    # finite loop using generator expressions
    # generator = (n for n in [0,1,1,2,3,5,8,13,21,34,55,89])
    # for f in generator:
    #     print(f)

    generator = generate_fibonacci_under(100)
    for f in generator:
        print(f)

    # generator = generate_fibonacci()
    # while True:
    #     print(next(generator))
