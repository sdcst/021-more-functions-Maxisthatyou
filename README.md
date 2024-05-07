## SDSS Computing Studies Python Assignment
### Assignment #005c More Functions (Total Marks 12)

Objectives:
* Understand the structure for creating and defining a function
* Use return statements to control the flow of information from the function to the calling block
* Make use of input parameters to control the flow of information from the calling block to the function


### 4 Tasks 2 Problems

##### Task 1
Create a function that converts the price of Bitcoin into Canadian Dollars .  
The function will require 2 input parameters:  
float: amount of currency being converted  

return: float value in Canadian Dollars  
You will make use of a local variable called "currBTC"  
currBTC shows that the conversion is 1 btc = 45000 cad  

Sample assertions:

assert btcTocad(1) == 45000  
(2 points) 


##### Task 2
Create a function that determines the largest number in a list of values and returns it.  
1 input parameter:  
list: the numbers to be checked for the largest value  

return: float value of the largest number  

Sample assertions:  
assert largest([3,10,3]) == 10  
(2 points)

##### Task 3
Create a function that determines the length of a hypotenuse given the lengths of 2 shorter sides  
2 input parameters  
float: the length of one side of a right triangle  
float: the length of the other side of a right triangle  
  
return: float value for the length of the hypotenuse  
  
Sample assertions:  
assert hypotenuse(6,8) == 10  
(2 points)


##### Task 4
Create a function that determines the area of a circle if given the radius  
1 input parameter  
float: radius  

return: float area for the circle  

note: Area of a circle is given by A = pi*(square of the radius)  
You may want to use the math module to complete this problem  

##### Problem 1
Create a function that converts from degrees F to degrees C or vice versa, depending on which initial unit is given
2 input parameters:  
float: the number of degrees  
string: the unit that you currently have: may be 'C' of 'F'  

return: float the number of degrees of the other unit  

Sample assertions:  
assert convertTemp(10,'C') == 50  
assert converTemp(32,'F') == 0  
(2 points)

##### Problem 2
Create a function that determines if a triangle is scalene, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is scalene
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert hypotenuse(12,5,13) == 2     
assert hypotenuse(5,3,3) == 1  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
