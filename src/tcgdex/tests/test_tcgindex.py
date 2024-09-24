from tcgdex import TCGDex

test = TCGDex('en')
print(test.fetch("hp", "100"))