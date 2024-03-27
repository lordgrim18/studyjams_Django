## Welcome to Day 3 of the Django Study Jams Session

### How to follow along
- Look at the commit history of this repository to see the changes made in each step. 
- Only the commands used in the command line will be mentioned in the README.
- The code changes will be visible in the commit history.
- The commit messages are self-explanatory and will help you understand the changes made in each step.
- The commit messages follows the flow and can therefore be used as a guide to follow along.

### Today's Agenda
- Form creation
- Template for form
- Ordering objects read from the database
- CRUD (Create Read Update Delete)
- Search 
- Function based vs Class based

### Forms
Forms are used to take input from the user. Django provides a Form class which is used to create forms. 

### Ordering objects read from the database
The objects read from the database can be ordered using the `order_by` method.
Or meta class can be used to order the objects by default.

### CRUD
CRUD stands for Create, Read, Update and Delete. These are the basic operations that can be performed on a database. Create and Update operations are done using forms. Read operation is done using the ORM. Delete operation is done using the `delete` method. These operations can be performed using function based views or class based views. These operations are found in all dynamic websites in some form.

### Search
Search is a common feature in websites. It is used to search for objects in the database. The search can be done using the `filter` method of the ORM. 

### Function based views vs Class based views
Function based views are simple functions that take a request and return a response. Class based views are classes that have methods for different HTTP methods. They are more powerful and can be used to create complex views. 