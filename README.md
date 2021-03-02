# Chicago-Bird-Collision-Data-Preprocessing
Creating a summary tabular dataset that can be used to analyze the bird collision data.


## COMMAND TO RUN THE PREPROCESSING SCRPIPT
python DataPreprocessing.py InputFileFolder outputpath


## PREPROCESSING TASKS DONE 
* Dropping the null values in the three dataframes. 
* Renaming the columns in the flight call data frame as per the given format.
 {"Species":"Genus","Family":"Species","Collisions":"Family","Call":"Flight Call"}
* the light level values in the dataframe are converted to integer values from float as given in the requirement.
* Then dataframes are joined based on common columns:
* Here joining is done between light levels data frame and collisions data frame based on the DATE column.
* then join combined new data frame with Flight calls data frame based on genus and species.
* then the combined dataframe is printed on to json output file.

Here the output is given as json file as it has 
* a smaller message size
* it can easily represent null values.
* More structural information in the document. Can easily distinguish between the number 1 and the string "1" as numbers, strings (and Booleans) are represented differently in JSON.


# REQUIREMENTS
numpy==1.20.1
pandas==1.2.2
python-dateutil==2.8.1
pytz==2021.1
six==1.15.0

