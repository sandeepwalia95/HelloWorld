from random import choice


class Person:

    x = 0
    
    def __init__(self):
        self.id = Person.x
        Person.x += 14
        eg=999

    def getId(self):
        return self.id




def main():
    
    people = [
        Person(),
        Person(),
        Person()
    ]
    
    for p in people:
        num = p.getId()
        print(p.id)


if __name__ == '__main__':
    main()
