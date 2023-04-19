## Task
``` bash
1. Make a relationship between companies and employees -> DONE (used ForeignKey).
2. In home page there is a table with company names and an empty link along with each company. 
   clinking on that link, should open up a page to a form with a dropdwon of employees that when choosed 
   should associate that employee with that particular company and redrirect to the table -> DONE (using a view, fetched the company id and employee id, updated the employee).
3. All employee names associated with a company should be displayed comma separated on the second column of the table on the home page -> DONE (using company.employee_set.all|join:', ').
4. Each employee can only be associated with one company only -> DONE (used filter() in views.py to fetch only NOt None Employees).
5. Employee dropdown in the form should be searchable -> DONE (Built-in Djnago Functionality).

```

To Check the admin panel, 

Username: admin
Password: admin
