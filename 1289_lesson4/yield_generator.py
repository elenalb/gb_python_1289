# конструкция yield

generator = (param ** 2 for param in range(5))

for el in generator:
    print(el)

# print(next(generator))


def generator_yield():
    for el in (1, 2, 3):
        yield el


g = generator_yield()

print(g)
print(next(g))
print(next(g))
print(next(g))
