Simple Data Analyzer


Overview of the project

This is a straightforward Python script designed to help you quickly analyze a list of numbers. You don't need to use complex spreadsheet software just to find out basic statistics. You simply type in your numbers, and the script does the math for you.

It calculates the following for any set of numbers you provide:

•	Mean: The average value.

•	Median: The middle number (useful for seeing past outliers).

•	Mode: The number that appears most often (it handles ties if there is more than one).

•	Range: The difference between the largest and smallest number.

Features

•	Friendly Interface: The prompts are written in plain English, not computer jargon.

•	Error Handling: If you accidentally type a letter instead of a number, the program will gently let you know instead of crashing.

•	Smart Mode Calculation: If your list has multiple numbers that appear the most often (a tie), the script will list all of them.

•	Continuous Use: You can analyze as many different datasets as you want without restarting the program.

Technologies/tools used


•	Python 3: The core programming language used for this script.

•	Statistics Module: Uses Python's built-in statistics library for accurate calculations.

•	Standard Library: No external packages or complex installations are required.

Steps to install & run the project

1. Make sure you have Python
You need to have Python installed on your computer to run this script. You can check this by typing python --version in your terminal.

2. Download the script
Save the file named data_analyzer.py to a folder on your computer.

3. Run the command
Open your terminal or command prompt, navigate to the folder where you saved the file, and run:
python data_analyzer.py
Instructions for testing
To ensure the program is working correctly, you can run a simple test using the steps below.
Test Case 1: Standard Data
1.	Start the program.
2.	When asked for numbers, enter: 5, 10, 5, 20
3.	Verify that the output matches the Screenshots section below.
Test Case 2: Error Handling
1.	Start the program.
2.	Enter invalid text like: hello, world
3.	Verify that the program prints a helpful error message asking for numbers, rather than crashing.
Test Case 3: Decimals
1.	Start the program.
2.	Enter decimal numbers: 1.5, 2.5, 3.5
3.	Verify that the script calculates the mean and median correctly as decimals.

