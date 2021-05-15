class Title:
    def __init__(self, name):
        self.name = name

    def get_date(self):
        return self.name

    @staticmethod
    def add_title(name):
        return 'Mr.' + name


class Honorname(Title):

    def full_name(self):
        return Title.add_title(self.name)


h_name = Honorname('abhishek')
print(h_name.full_name())
