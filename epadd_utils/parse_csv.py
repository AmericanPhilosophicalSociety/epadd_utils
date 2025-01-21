import csv
from typing import Literal
import click


def parse_csv(file):
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        # drop first row containing reference text
        data = [r[1:] for r in reader][1:]

    return data


MODES = Literal['strict', 'verbose', 'mixed']


def parse_row(row, delimiter, mode: MODES = 'mixed'):
    output = []
    if mode != 'mixed':
        # implement non-default methods here
        pass
    else:
        for r in row:
            if r == '':
                continue
            elif delimiter in r:
                entries = r.split(delimiter)
                output = output + entries
            else:
                output.append(r)

        return output


def process_csv_data(data, delimiter, mode: MODES = 'mixed'):
    '''Returns a list of lists of parsed CSV data'''
    output = []
    for row in data:
        processed = parse_row(row, delimiter, mode)
        output.append(processed)

    return output


def generate_textfile(data, path):
    '''Generate ePadd compatible textfile from processed data'''
    # sanity check for path
    if not path.endswith('.txt'):
        raise ValueError('Invalid file path for output TXT file.')
    with open(path, 'w', encoding='utf-8') as f:
        for i in data:
            f.writelines('-- \n')
            for j in i:
                f.writelines(f'{j}\n')
    click.echo('Text file generated successfully.')


@click.command()
@click.option('--delimiter', default='|', help='Subdelimiter used in the CSV')
@click.option('--mode', default='mixed', help='CSV type: strict, verbose or mixed')
@click.argument('input', type=click.Path(exists=True))
@click.argument('output', type=click.Path())
def generate_epadd(delimiter, mode, input, output):
    data = parse_csv(input)
    processed = process_csv_data(data, delimiter, mode)
    generate_textfile(processed, output)


if __name__ == '__main__':
    generate_epadd()
