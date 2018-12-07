import enum, typing

class Mode(enum.Enum):
    DELIM = 0
    CHAR = 1


def doCut(f, mode: Mode, delim: str, fields: typing.Iterator[int]) -> None:
    
    seen = []

    def isIn(index):
        if index in seen:
            return True

        for f in fields:
            seen.append(f)
            if f == index:
                return True
            if f >= index:
                return False

        return False

    for line in f:

        line = line.rstrip('\n')

        if mode == Mode.CHAR:
            var = line
            delim = ""

        elif mode == Mode.DELIM:
            var = line.split(delim)

        newfields = [field for idx, field in enumerate(var) if isIn(idx + 1)]

        newline = delim.join(newfields)

        print(newline)
        yield newline



def yielder():
    yield 1
    n = 2 
    while True:
        n += 1
        yield n



#for mode in [Mode.CHAR, Mode.DELIM]:
#    for fields in [yielder(), [1, 3, 4]]:
#
#        with open("test.csv", "r") as f:
#            doCut(f, mode, ",", fields)
        
