import enum, typing

class Mode(enum.Enum):
    DELIM = 0
    CHAR = 1


def doCut(f, mode: Mode, delim: str, fields: typing.Iterator[int]) -> None:
    
    for line in f:

        if mode == Mode.CHAR:

            newline = ""

            for field in fields:
                if field >= len(line):
                    break
                newline += line[field - 1]

    
        elif mode == Mode.DELIM:

            var = line.split(delim)

            newfields = [field for idx, field in enumerate(var) if idx + 1 in fields]

            newline = delim.join(newfields)

        print(newline)



#def yielder():
#    yield 0
#    n = 2
#    while True:
#        yield n
#        n += 2

#with open("test.csv", "r") as f:
#    doCut(f, Mode.CHAR, None, yielder())


#with open("test.csv", "r") as f:
#    doCut(f, Mode.CHAR, None, [0, 2, 3])

#with open("test.csv", "r") as f:
#    doCut(f, Mode.DELIM, ",", [0, 2, 3])



    
