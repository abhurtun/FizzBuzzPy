def process(number):

    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    if number % 5 == 0:
        return 'Buzz'
    if number % 3 == 0:
        return 'Fizz'
    if number % 5 == 0:
        return 'Buzz'

if __name__ == '__main__':
    for i in range(1, 101):
        print(process(i))