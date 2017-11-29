import pandas as pd
#
#   Reads a file, and returns a dataframe. OBS change the delimiter
#


def get_file_path(file_name):
    file_path = "/Users/carlhasselskog/PycharmProjects/HittaPunktSe/Data/" + file_name
    return file_path


def read_file(source, separator):

    df = pd.read_csv(source, sep=separator, header=0)
    col_names = df.columns
    return df, col_names


def write_file(output_file, label, info, pair1, source, m, kind):
    filename = output_file + "/" + label + " " + kind + "_out.txt"
    f = open(filename, 'w+')
    f.write("Info                 : " + info + "\n")
    f.write("Source                                    : " + source + "\n")
    f.write("Classifier                                : " + label + "\n")
    f.write("Simply the best                           : " + label + " " + str(m) + "\n")
    f.write("Best TEST Classifier OF ALL is : " + str(pair1) + "\n")


def main():
    branch_path = get_file_path('Branscher.csv')
    data_frame, column_name = read_file(branch_path, ';')
    print(data_frame)
    branch_set = []
    for row in data_frame.iterrows():
        set(row).add('key')

main()