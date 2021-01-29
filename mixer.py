import csv

data_path = "data/lifter-data_social-instagram.csv"
negative_result_path = "results/defunct_accounts"
mixed_path = "results/mixed"


def load_negatives(file):
    with open(file, encoding="UTF-8") as csvfile:
        reader = csv.reader(csvfile)
        data = [row[0] for row in reader]
        return data


def load_data(file):
    with open(file, encoding="UTF-8") as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
        return data


def write_mixed(data, negs):
    with open(mixed_path, mode="w+", encoding="UTF-8") as mixed_file:
        mixed_file.write("{},{}\n".format(data[0][0], data[0][1]))
        for elem in data[1:]:
            if elem[1] not in negs:
                mixed_file.write("{},{}\n".format(elem[0], elem[1]))


if __name__ == "__main__":
    negatives = load_negatives(negative_result_path)
    original_data = load_data(data_path)
    write_mixed(original_data, negatives)
