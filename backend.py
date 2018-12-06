import enum, typing

class Mode(enum.Enum):
    DELIM = 0
    CHAR = 1


def doCut(mode: Mode, delim: str, fields: typing.List[int]) -> None:
    pass


