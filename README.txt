Hakan Khan - 101237616
https://github.com/hakankhan/studentdatabase

Video tutorial on how to use this tool
    https://youtu.be/cwNatCDVIm8

Text form:
Database setup
    Use pgAdmin4 to create a database and a user with password
    Import the dml.sql file into your database using the query tool 

Tool setup
    Ensure to update the main.py file with your database's information at line 5
    Ensure you have pip3 install'd the necessary packages and have python3 
        prettytable
        psycopg2

How to use tool 
    Run the tool using python3
    Follow the prompts, when prompted to enter in information, ensure it is space separated
        and that the date follows the format YYYY-MM-DD
    For example when adding a student a valid entry would look like this:
        john doe johndoe@email.com 1999-02-25
