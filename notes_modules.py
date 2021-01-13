def say_hi():
    print('Hi')

def main():
    print('Main')
    say_hi()

if __name__ == '__main__':
    print('__name__ == __main__')
    main()
else:
    print('__name__ != __main__')