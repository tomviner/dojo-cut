from itertools import count

import click

from backend import doCut, Mode


def parse_fields(f):
    ranges = f.split(',')

    spans = []
    for rng in ranges:
        start, dash, stop = rng.partition('-')
        start = int(start or 1)
        stop = int(stop or 0)
        spans.append((start, dash, stop))

    for start, dash, stop in sorted(spans):
        if dash:
            if not stop:
                yield from count(start)
            else:
                yield from range(start, stop + 1)
        else:
            yield start


def _cut(input, d, f):
    return list(doCut(
        f=input, mode=Mode.DELIM, delim=d,
        fields=parse_fields(f)
    ))


@click.command()
@click.option('-d')
@click.argument('input', type=click.File('r'))
@click.option('-f')
def cut(input, d, f):
    return _cut(input, d, f)


if __name__ == '__main__':
    list(cut())
