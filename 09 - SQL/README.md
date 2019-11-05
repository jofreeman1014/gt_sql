# Assignment Background: SQL Databasing

This assignment focused on designing the tables to hold data in the CSVs, importing the CSVs into a SQL database, and answering questions about the data. Essentially, I practiced data modeling, data engineering, and data analysis using only PostgreSQL server and SQL commands. The data that I used was mock employee data.

After I looked through the .csv files, I used the ERD visualization tool [Quick Database Diagrams](http://www.quickdatabasediagrams.com) to develop my schema outside of PostgreSQL, and imported this model into PostgreSQL to start my tables.

![jofschema](JOFschema.PNG)

## Data Analysis

The assignment asked me to query following:

1. List the following details of each employee: employee number, last name, first name, gender, and salary.

2. List employees who were hired in 1986.

3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.

4. List the department of each employee with the following information: employee number, last name, first name, and department name.

5. List all employees whose first name is "Hercules" and last names begin with "B."

6. List all employees in the Sales department, including their employee number, last name, first name, and department name.

7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.

8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.

Each of these questions were answered in my included [queries.sql](queries.sql) file.