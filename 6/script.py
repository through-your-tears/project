import csv


FIRST_PATH = '7.csv'
SECOND_PATH = '17.csv'


def main():
    with open(FIRST_PATH, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data_first = list(reader)
    with open(SECOND_PATH, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data_second = list(reader)

    answers = []

    for row in data_first:
        mark = row["Оценка/10,00"]
        mark = mark.replace(',', '.')
        if mark != '-':
            k = 0
            if row["В. 1 /1,00"] == '1,00' and row["В. 2 /1,00"] == '1,00':
                k += 1
            if row["В. 3 /1,00"] == '1,00':
                k += 1
            if row["В. 4 /1,00"] == '1,00' and row["В. 5 /1,00"] == '1,00':
                k += 1
            if row["В. 6 /1,00"] == '1,00' and row["В. 7 /1,00"] == '1,00':
                k += 1
            if row["В. 8 /1,00"] == '1,00' and row["В. 9 /1,00"] == '1,00' and row["В. 10 /1,00"] == '1,00':
                k += 1
            if k > 1:
                answers.append(row)

    for row in data_second:
        mark = row["Оценка/100,00"]
        mark = mark.replace(',', '.')
        if mark != '-':
            k = 0
            if row["В. 1 /10,00"] == '10,00' and row["В. 2 /10,00"] == '10,00':
                k += 1
            if row["В. 3 /10,00"] == '10,00':
                k += 1
            if row["В. 4 /10,00"] == '10,00' and row["В. 5 /10,00"] == '10,00':
                k += 1
            if row["В. 6 /10,00"] == '10,00' and row["В. 7 /10,00"] == '10,00':
                k += 1
            if row["В. 8 /10,00"] == '10,00' and row["В. 9 /10,00"] == '10,00' and row["В. 10 /10,00"] == '10,00':
                k += 1
            if k > 1:
                answers.append(row)

    print(*answers, sep='\n')


if __name__ == '__main__':
    main()
