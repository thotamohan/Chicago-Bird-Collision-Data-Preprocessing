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
* join light levels data frame and collisions data frame based on the DATE column.
* then join combined data frame with Flight calls data frame based on genus and species.


