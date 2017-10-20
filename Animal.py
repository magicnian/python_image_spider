# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('animal is running……')


class Dog(Animal):
    def run(self):
        print('Dog is running')


class Cat(Animal):
    def run(self):
        print('Cat is running')


def run_twice(a):
    a.run()
    a.run()

if __name__ == '__main__':
    dog = Dog()
    cat = Cat()
    dog.run()
    cat.run()
    print(type(dog))

