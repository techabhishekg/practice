class Birds(object):
    def fly(self):
        print('bird can fly')

    def jump(self):
        print('bird can jump')

    def swim(self):
        print('bird can swim')

    def hetch(self):
        print('bird can hetcheggs')


class Duck(Birds):
    def test(self):
        pass

    def __getattribute__(self, item):
        if item == 'jump':
            print('help')
            raise AttributeError('can not jump')
        return super(Duck, self).__getattribute__(item)


duck = Duck()
duck.fly()
duck.jump()
duck.swim()
duck.hetch()