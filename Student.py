# -*- coding: utf-8 -*-

class Student(object):
    name = 'Student'

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        try:
            pass
        except Exception as e:
            pass
        finally:
            pass
        return self.__score


if __name__ == '__main__':
    a = Student('a', '97')
    b = Student('b', '89')
    print(a.get_name())
    a.print_score()
    b.print_score()

    print(hasattr(a, '__name'))
