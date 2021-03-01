# Chicago-Bird-Collision-Data-Preprocessing
Creating a summary tabular dataset that can be used to analyze the bird collision data.


## COMMAND TO RUN THE PREPROCESSING SCRPIPT
python run 'collisionDataPath' 'flightCallPath' 'lightLevelsPath' 'outputPath1' 'outputPath2'


## PREPROCESSING TASKS DONE 
* DROPPING THE NULL VALUES AS PER THE GIVEN FORMAT.
* Dropping the null values in the data frames.
* Renaming the columns in the flight call data frame as per the given format.
* {"Species":"Genus","Family":"Species","Collisions":"Family","Call":"Flight Call"}
* Join the data frames based on common columns:
** CHECKING FOR ALL THE COLUMNS TO MAKE JOINS AS WE COULD SEE DATE COLUMNS ARE COMMON IN LIGHT LEVELS DATAFRAME AND COLLISIONS DATA dataframe.
** THE SAME FOR GENUS AND SPECIES IN FLIGHT CALLS DATAFRAME


