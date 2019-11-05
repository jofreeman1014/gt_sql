-- List the following details of each employee: 
--   employee number, last name, first name, gender, and salary.
select e.emp_no, e.last_name, e.first_name, e.gender, s.salary
	from employees e
	join salaries s
	on (e.emp_no = s.emp_no);
	
-- List employees who were hired in 1986.
select last_name, first_name, hire_date
	from employees
	where hire_date like '1986%';

-- List the manager of each department with the following information: 
--   department number, department name, the manager's employee number, 
--   last name, first name, and start and end employment dates.
select m.dept_no, d.dept_name, m.emp_no, e.last_name, e.first_name, m.from_date, m.to_date
	from dept_manager m
	join departments d on (d.dept_no = m.dept_no)
	join employees e on (e.emp_no = m.emp_no);

-- List the department of each employee with the following information: 
--   employee number, last name, first name, and department name.
select e.emp_no, e.last_name, e.first_name, d.dept_name
	from dept_emp m
	join departments d on (d.dept_no = m.dept_no)
	join employees e on (e.emp_no = m.emp_no);

-- List all employees whose first name is "Hercules" and last names begin with "B."
select first_name, last_name
	from employees
	where first_name = 'Hercules'
	and last_name like 'B%';

-- List all employees in the Sales department, including 
--   their employee number, last name, first name, and department name.
select e.emp_no, e.last_name, e.first_name, d.dept_name
	from dept_emp m
	join departments d on (d.dept_no = m.dept_no)
	join employees e on (e.emp_no = m.emp_no)
	where dept_name = 'Sales';

-- List all employees in the Sales and Development departments, including 
--   their employee number, last name, first name, and department name.
select e.emp_no, e.last_name, e.first_name, d.dept_name
	from dept_emp m
	join departments d on (d.dept_no = m.dept_no)
	join employees e on (e.emp_no = m.emp_no)
	where dept_name = 'Sales'
	or dept_name = 'Development';

-- In descending order, list the frequency count of 
--   employee last names, i.e., how many employees share each last name.
select last_name, count(last_name) as "name_count"
	from employees
	group by last_name
	order by count(last_name) desc;
	