# Homework 2

_disclaimer: Manrique Vargas helped me a bit with Assignment 3 and 4. More on this below!_

__Part 1__
In this assignment, I was supposed to remove files from a GitHub repo in the right way. 
The right way is really to use the following commands in the terminal: 
>   git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch HW2_tm1722/test2.csv 
> --prune-empty --tag-name-filter cat -- --all 
>
>   git push origin --force --all

I first misunderstood the instructions and at first created test.csv file on the
local machine. Only then I followed the directions and created a file on GitHub.
So the file called test2.csv is what we really want to pay attention here. 


Creating the file in the GitHub interface and commiting it the master branch: 
![alt text](https://github.com/timurmukhtarov/PUI2018_tm1722/blob/master/HW2_tm1722/screenShots/1.png?raw=true) 

Checking the history of the folder right after creating the file:
![alt text](https://github.com/timurmukhtarov/PUI2018_tm1722/blob/master/HW2_tm1722/screenShots/2.png?raw=true) 

Checking the directory right after deleting the file using provided command: 
![alt text](https://github.com/timurmukhtarov/PUI2018_tm1722/blob/master/HW2_tm1722/screenShots/3.png?raw=true) 

__Part 2__ 
Here I needed to choose a file in CSV format from NYC Open Data portal and use _pandas_ to read the file, mangle it 
and do a visualization. The extra credit assignment was to do the same assignment using API and JSON in stead of a CSV file

See the jupyter notebook _HW2_Assignment2_tm1722.ipynb_ for my solution

__Part 3. Assignment 3__ 
For this problem, I needed to taccess MTA's Bus Time interface through their API and write a script to stream bus data.

Manrique Vargas told me that we need to use sys.argv[] arguments to do the assignment right. Thanks, Manrique!

__Part 3. Assignment 4__
Here, I needed to write a Python script that displays information on the next stop location of all 
busses of a given line.

Once again, Manrique Vargas pulled through and helped me with the for loop to get the data in the proper format 
from the JSON file.

_**update: I was just informed by Manrique that he himself got a lot of help from Tanya Nabila
another update Amber (Yushi) Chen walked me through her solution (and she did it diferently!) 
which helped me conceptualize this even better! Thanks, everyone!**_