Section 4: APPLY

Step 1. Import the necessary libraries
in lines #3,4,5
 
Step 2. Import the dataset from this address.
in line  #7

Step 3. Assign it to a variable called crime.
in line #9
 
Step 4. What is the type of the columns?
(64-bit integer) 
in line #10
 
Step 5. Convert the type of the column Year to datetime64
in line #12
 
Step 6. Set the Year column as the index of the dataframe
in line #14
 
Step 7. Delete the Total column
in line #16
 
Step 8. Group the year by decades and sum the values
Pay attention to the Population column number, summing this column is a mistake

Nesugalvojau kaip tai padaryti pitone. Tiksliau, galvojau per daug ilgai, su klaidom pycharme ir be jokio rezultato. 
Tada 'pasivarciau'duomenis programa su kuria dirbu. Susumavau pagal desimtmecius. Atmeciau paskutines keturias eilutes (nes nepilnas desimtmetis). 
Toliau sunormavau rezultatus i kreives plota nes tai leidzia "pagauti" maksimuma kiekvienai kreivei.
Tada normuotus rezultatus isivedziau atgal i pycharma (lines 18-29) kad pagristi atsakyma i 'sekanti' klausima. Gaunasi kad visur isskyrus 'burglary' duomenu maksimumas ties 10 desimtmeciu.     
  
Step 9. What is the most dangerous decade to live in the US?
1991-2000 (10th decade)