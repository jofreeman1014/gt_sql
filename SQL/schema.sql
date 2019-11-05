drop table if exists departments;
drop table if exists dept_manager;
drop table if exists dept_emp;
drop table if exists titles;
drop table if exists employees;
drop table if exists salaries;

CREATE TABLE departments (
    dept_no varchar   NOT NULL,
    dept_name varchar   NOT NULL;
	primary key (dept_no)
);

CREATE TABLE dept_manager (
    dept_no varchar   NOT NULL,
    emp_no int   NOT NULL,
    from_date varchar   NOT NULL,
    to_date varchar   NOT NULL
);

CREATE TABLE dept_emp (
    emp_no int   NOT NULL,
    dept_no varchar   NOT NULL,
    from_date varchar   NOT NULL,
    to_date varchar   NOT NULL
);

CREATE TABLE titles (
    emp_no int   NOT NULL,
    title varchar   NOT NULL,
    from_date varchar   NOT NULL,
    to_date varchar   NOT NULL
);

CREATE TABLE employees (
    emp_no int   NOT NULL,
    birth_date varchar   NOT NULL,
    first_name varchar   NOT NULL,
    last_name varchar   NOT NULL,
    gender varchar   NOT NULL,
    hire_date varchar   NOT NULL,
	primary key (emp_no)
);

CREATE TABLE salaries (
    emp_no int   NOT NULL,
    salary int   NOT NULL,
    from_date varchar   NOT NULL,
    to_date varchar   NOT NULL
);