import sys
import pandas as pd
from os import listdir
from os.path import isfile, join
from pandas.api.types import is_string_dtype


def string_conversion(df):
    """
    All the string columns in the dataframe are converted to lower case
    :param df: dataframe
    :return: dataframe
    """
    for columns in df.columns:
        if is_string_dtype(df[columns]):
            df[columns] = df[columns].str.lower()
    return df


def flight_call_column_renaming(df):
    """
    column names of the flight column dataframe is renamed to as per the data
    :param df: flight call dataframe
    :return: renamed dataframe
    """
    # RENAMING THE COLUMNS AS PER THE GIVEN FORMAT
    df = df.rename(
        columns={"Species": "Genus", "Family": "Species", "Collisions": "Family", "Call": "Flight Call"})
    return df


def data_preprocess(data_path):
    """
    input json file is read, and null values are removed
    :param data_path: json file path
    :return: read dataframe
    """
    temp_df = pd.read_json(data_path)
    temp_df = temp_df.dropna()
    temp_df = temp_df.drop_duplicates()
    return temp_df


def joining_dataframe_null(df_1, df_2, df_3, outputPath1):
    """
    All the three dataframes are joined with no loss of any data and the dataframe output is printed to json file
    light score column in the dataframe is converted to int from float type
    :param df_1: Collision data dataframe
    :param outputPath1: json file output path
    :param df_2: lightLevels_df
    :param df_3: flightCall_df
    :return: None
    """
    df_3 = flight_call_column_renaming(df_3)
    temp_df = pd.merge(df_1, df_2, on='Date', how='left')
    final_df = pd.merge(temp_df, df_3, on=['Genus', 'Species'], how='left')
    final_df = string_conversion(final_df)
    final_df['Light Score '] = final_df['Light Score '].astype('Int64')
    final_df.to_json(outputPath1)


def joining_dataframe_not_null(df_1, df_2, df_3, outputPath2):
    """
    All the three dataframes are joined with no loss of any data and the dataframe output is printed to json file
    light score column in the dataframe is converted to int from float type
    :type outputPath2: json file path for output
    :param df_1: Collision data dataframe
    :param outputPath2: json file output path
    :param df_2: lightLevels_df
    :param df_3: flightCall_df
    :return: None
    """
    df_3 = flight_call_column_renaming(df_3)
    temp_df = pd.merge(df_1, df_2, on='Date')
    final_df = pd.merge(temp_df, df_3, on=['Genus', 'Species'])
    final_df = string_conversion(final_df)

    final_df['Light Score '] = final_df['Light Score '].astype('Int64')
    final_df.to_json(outputPath2)


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("""
        This function needs 2 input arguments
        <Input file folder>
        <outputPath>
             """)
    filepath = sys.argv[1]
    outputPath1 = sys.argv[2]
    outputPath2 = "final_output2.json"

    onlyfiles = [f for f in listdir(filepath) if isfile(join(filepath, f))]

    for _file in onlyfiles:
        if _file.endswith('.json'):
            if _file.startswith('chicago'):
                collisionData_df = data_preprocess(_file)
            elif _file.startswith('flight'):
                flightCall_df = data_preprocess(_file)
            elif _file.startswith('light'):
                lightLevels_df = data_preprocess(_file)

    joining_dataframe_null(collisionData_df, lightLevels_df, flightCall_df, outputPath1)
    joining_dataframe_not_null(collisionData_df, lightLevels_df, flightCall_df, outputPath2)
