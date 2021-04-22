import itertools
# pip install itertools


# count()
for el in itertools.count(7):
    if el > 15:
        break
    print(el)

# cycle()
c = 0
for el in itertools.cycle("abcdef"):
    if c > 15:
        break
    print(el)
    c += 1


prog_lang = ["python", "c++", "perl", "java", "javscript"]
iter = itertools.cycle(prog_lang)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
