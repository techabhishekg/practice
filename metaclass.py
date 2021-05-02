class Myclass():
    pass


class Mymeta(type):
    pass


class Mymetaclass(Mymeta):
    pass


class Mymetasubclass(Mymetaclass):
    pass


print(type(Myclass))
print(type(Mymeta))
print(type(Mymetaclass))
print(type(Mymetasubclass))


class DataCamp():
    pass


DataCampClass = type('DataCamp', (), {})


class DataSampClass(DataCamp):
    pass


print(DataCamp)
print(DataCampClass)
print(DataSampClass)
print(eval('DataSampClass'))

artilce = 'metaclass'
print(type(artilce))
print(type(artilce.__class__.__class__.__class__))







###########

