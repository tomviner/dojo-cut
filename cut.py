import click

from backend import doCut, Mode


@click.command()
@click.option('-d')
@click.argument('input', type=click.File('r'))
@click.option('-f')
def cut(input, d, f):
    # print(input, d)
    # print(input.read())
    ranges = f.split(',')
    fields = set()
    for rng in ranges:
        start, dash, stop = rng.partition('-')
        # print(start, dash, stop)
        if dash:
            if stop:
                stop = int(stop) + 1
            else:
                stop = None
            fs = range(int(start) or 1, stop)
            fields.update(fs)
            # print(fs)
        else:
            fields.add(int(start))
    # print(sorted(fields))
    doCut(f=input, mode=Mode.DELIM, delim=d, fields=sorted(fields))


if __name__ == '__main__':
    cut()
