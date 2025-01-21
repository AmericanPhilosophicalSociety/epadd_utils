import csv
import click


def write_header(writer):
    writer.writerow(['reference', 'names', 'email_addresses'])


def read_txt_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return lines[1:]


def is_email(email):
    if "@" in email:
        return True
    else:
        return False


def parse_entity(lines, delimiter='|'):
    emails = []
    names = []
    for line in lines:
        if is_email(line):
            line = line.strip()
            emails.append(line)
        else:
            line = line.strip()
            names.append(line)
    if len(names) > 0:
        referent = names[0]
    else:
        referent = emails[0]
    row = [referent, delimiter.join(names), delimiter.join(emails)]
    return row


def process_epadd(lines, delimiter='|'):
    result = []
    chunk = []
    for line in lines:
        if line != '-- \n':
            chunk.append(line)
        else:
            parsed_chunk = parse_entity(chunk, delimiter)
            result.append(parsed_chunk)
            chunk.clear()
    else:
        parsed_chunk = parse_entity(chunk)
        result.append(parsed_chunk)
    return result


def write_to_csv(path, data):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        write_header(writer)
        for row in data:
            writer.writerow(row)


@click.command()
@click.option('--delimiter', default='|', help='Subdelimiter to be used in the CSV')
@click.argument('input', type=click.Path(exists=True))
@click.argument('output', type=click.Path())
def parse_epadd(delimiter, input, output):
    """Convert ePADD text file to CSV

    INPUT is the source TXT file from ePadd.
    OUTPUT is the path to where you want to write the CSV.
    """
    lines = read_txt_file(input)
    click.echo('File read successfully.')
    data = process_epadd(lines, delimiter)
    click.echo('Data parsed successfully.')
    write_to_csv(output, data)
    click.echo('File written successfully.')


if __name__ == '__main__':
    parse_epadd()
