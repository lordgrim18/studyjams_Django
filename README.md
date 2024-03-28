## Welcome to day 4.2 of the Django Study Jams Session

### How to follow along
- Look at the commit history of this repository to see the changes made in each step. 
- Only the commands used in the command line will be mentioned in the README.
- The code changes will be visible in the commit history.
- The commit messages are self-explanatory and will help you understand the changes made in each step.
- The commit messages follows the flow and can therefore be used as a guide to follow along.

### Today's Agenda
- Setting up custom Register and Login views for a normal user.
- Adding flash messages to templates.
- Adding a custom logout view.
- Restricting access to certain views for authenticated and unauthenticated users.
- Redirecting users from editing database entries that do not belong to them.

### Django Register, Login and Logout Views
Django provides built-in functions for user authentication, login, logout, etc. We will be using these functions to create custom views for Register, Login and Logout.

### Flash Messages
Flash messages are messages that are displayed to the user for a short period of time. Flash messages are used to give feedback to the user after an action has been performed. We will be adding flash messages to our templates.

### Restricting Access to Views
login_required decorator is used to restrict access to certain views for authenticated users. We will be using this decorator to restrict access to certain views for unauthenticated users. So unauthenticated users won't be able to access certain views such as the ones that is used for entering data into the database.

### Restricting Access to Editing Database Entries
We will be restricting access to editing database entries that do not belong to the user. So a user can only edit the entries that they have created. In order to do this, we will be checking if the user is the owner of the entry before allowing them to edit the entry.