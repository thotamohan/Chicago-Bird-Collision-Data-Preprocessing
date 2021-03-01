from pandas.api.types import is_string_dtype
import pandas as pd
import logging
import sys



def stringConversion(df):
  '''
  INPUT: DATAFRAME
  OUTPUT: DATAFRAME
  ALL THE STRING COLUMNS IN THE DATAFRAME ARE
  CONVERTED TO LOWER CASE FOR NO MISMATCH IN UNIQUE COLUMNS
  '''
  for columns in df.columns:
    if is_string_dtype(df[columns]):
      df[columns]=df[columns].str.lower()
  return df




if __name__ == "__main__":
    if len(sys.argv)!=6:
        print("This function needs 6 input arguments <collisionDataPath> <flightCallPath> <lightLevelsPath> <outputPath1> <outputPath2>")
        sys.exit(1)
    collisionDataPath=sys.argv[1]
    flightCallPath=sys.argv[2]
    lightLevelsPath = sys.argv[3]
    outputPath1=sys.argv[4]
    outputPath2=sys.argv[5]


    #READING THE PANDAS DATAFRAMES
    collisionData_df=pd.read_json(collisionDataPath)
    flightCall_df=pd.read_json(flightCallPath)
    lightLevels_df=pd.read_json(lightLevelsPath)

    #DROPPING THE NULL VALUES AS PER THE GIVEN FORMAT
    collisionData_df=collisionData_df.dropna() 
    lightLevels_df=lightLevels_df.dropna()
    flightCall_df=flightCall_df.dropna()

    #RENAMING THE COLUMNS AS PER THE GIVEN FORMAT
    flightCall_df= flightCall_df.rename(columns={"Species":"Genus","Family":"Species","Collisions":"Family","Call":"Flight Call"})

    #WITH NULL VALUES
    df=pd.merge(collisionData_df,lightLevels_df,on='Date',how='left')
    df2=pd.merge(df,flightCall_df,on=['Genus','Species'],how='left')
    df2=stringConversion(df)
    df2['Light Score ']=df2['Light Score '].astype(int)


    #WITHOUT NULL VALUES
    df3=pd.merge(collisionData_df,lightLevels_df,on='Date')
    df4=pd.merge(df3,flightCall_df,on=['Genus','Species'])
    df4=stringConversion(df4)
    df4['Light Score ']=df4['Light Score '].astype(int)

    #OUTPUT DATAFRAMES TO JSON
    df2.to_json(outputPath1)
    df4.to_json(outputPath2)
