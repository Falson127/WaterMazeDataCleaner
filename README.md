# WaterMazeDataCleaner
Automated Cleaner for WaterMaze data
###############################################################################################################
                Automatic Water Maze data cleaner for excel files produced in AnyMaze!
###############################################################################################################
											Author: Ben Landon
###############################################################################################################

How to use:
>Place your excel files (.xlsx) containing your raw data in the "Uncleaned Data Files" Folder.
	The data should be in a sheet titled "RAW".
>Run the WaterMazeDataCleaner.exe file
>Retrieve your cleaned excel files from "Cleaned Data Files" Folder

###############################################################################################################
Notes: This program extracts based on column names, so they need to be 
correctly named, but they don't have to be in a specific order. Below
are the names you should give to the fields in your excel file. They
should be the default in AnyMaze, but if you have changed them from 
the default it will not be able to detect the correct columns.

These columns are case sensitive and need to include the spaces as shown:
'Animal'
'Stage'
'Trial'
'Duration'
'Distance (cm)'
'Speed (cm/s)'
'Target Site : entries'
'%Time in Target Quadrant'
'%Time in Ann40cm'
'%Time in Ann20cm'
'%Time in Target Site'

Let me know if you have any issues! Currently it will clean up to 7 stages.
It assumes that stages: 2,4,5, and 7 will be probe days. All other stages are assumed to be normal. 
