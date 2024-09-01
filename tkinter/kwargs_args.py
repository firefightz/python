def add(*args):
    total = 0
    for n in args:
        total = total + n
    return total


print("args: ", add (4, 5, 6))

class SomeOne():
    def __init__(self, **kwargs) -> None:
        self.first = kwargs.get('first')
        self.second = kwargs.get('second')



new_someone = SomeOne(second=5)

print(new_someone.second)
print(new_someone.first)