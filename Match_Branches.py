import pandas as pd
#
#   Reads a file, and returns a dataframe. OBS change the delimiter
#


def read_file(source, separator):

    df = pd.read_csv(source, sep=separator, header=0)
    col_names = df.columns
    return df, col_names


def main():
    industries_data_file_name = 'Industries.csv'
    companies_data_file_name = 'Companies.csv'
    data_frame, column_name = read_file(industries_data_file_name, ';')
    print(data_frame)
    for row in data_frame.iterrows():
        pass
    


main()