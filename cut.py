from itertools import count

import click

from backend import doCut, Mode


def get_fields(ranges):
    spans = []
    for rng in ranges:
        start, dash, stop = rng.partition('-')
        start = int(start or 1)
        stop = int(stop or 0)
        spans.append((start, dash, stop))

    for start, dash, stop in sorted(spans):
        # print(start, dash, stop)
        if dash:
            if not stop:
                yield from count(start)
            else:
                yield from range(start, stop + 1)
        else:
            yield start


@click.command()
@click.option('-d')
@click.argument('input', type=click.File('r'))
@click.option('-f')
def cut(input, d, f):
    # print(input, d)
    # print(input.read())
    ranges = f.split(',')
    # fields = set()

    # print(sorted(fields))
    # for i, fld in enumerate(get_fields(ranges)):
    #     if i > 10:
    #         break
    #     print(fld)

    doCut(f=input, mode=Mode.DELIM, delim=d, fields=get_fields(ranges))


if __name__ == '__main__':
    cut()
