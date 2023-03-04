import csv
import pathlib

if __name__ == '__main__':
    target = pathlib.Path('from_lists.csv').resolve()
    column_names = ['name','surname', 'country', 'email']
    row_data = [
        ['thanos','alev','GR','thanos.alev@gmail.com'],
        ['than','alev','GR','than.alev@outlook.com'],
        ['th','al','UK','th.al@outlook.com']
    ]
    with open(str(target), 'w') as f:
        writer = csv.writer(f)
        writer.writerow(column_names)
        for row in row_data:
            writer.writerow(row)

    # write dicts as CSV rows
    target = pathlib.Path('from_dicts.csv')
    dict_data = map(lambda values: dict(zip(column_names, values)), row_data)
    with open(str(target), 'w') as f:
        writer = csv.DictWriter(f, fieldnames=column_names)
        writer.writeheader()
        for _dict in dict_data:
            writer.writerow(_dict)


