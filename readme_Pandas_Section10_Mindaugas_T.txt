Section: 10 Deleting


Introduction:
This exercise is a adaptation from the UCI Wine dataset. The only pupose is to practice deleting data with pandas.

Step 1. Import the necessary libraries
lines #3-6
 
Step 2. Import the dataset from this address.
line#8

Step 3. Assign it to a variable called wine
line#10
 
Step 4. Delete the first, fourth, seventh, nineth, eleventh, thirteenth and fourteenth columns
line#12
 
Step 5. Assign the columns as below:
The attributes are (donated by Riccardo Leardi, riclea '@' anchem.unige.it):
1) alcohol
2) malic_acid
3) alcalinity_of_ash
4) magnesium
5) flavanoids
6) proanthocyanins
7) hue

lines #14,15

Step 6. Set the values of the first 3 rows from alcohol as NaN
lines#17-19
 
Step 7. Now set the value of the rows 3 and 4 of magnesium as NaN
lines#21-22
 
Step 8. Fill the value of NaN with the number 10 in alcohol and 100 in magnesium
# in line #25 (but not working)
so I used a very simple solution for this task (lines#26-31)
 
Step 9. Count the number of missing values
line#34 
(0) 

Step 10. Create an array of 10 random numbers up until 10
line#37
 
Step 11. Use random numbers you generated as an index and assign NaN value to each of cell.
-
 
Step 12. How many missing values do we have?
-
 
Step 13. Delete the rows that contain missing values
-

Step 14. Print only the non-null values in alcohol
-
 
Step 15. Reset the index, so it starts with 0 again
-  