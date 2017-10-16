# aip

Library Management( using python, django)

Whether you have 20 items or 2000 items, your library is precious. The library management application caters for both the institutional and small organisation. Our online web application lets the user to create multiple catalogues, view the book information and other features enabled with the administration zone for the admin to perform some superlative actions that cannot be done by the ordinary users.

Scope

The different areas where we can use our application are:
•	Any educational institutions can make use of it by providing the information about the author, book content available in the library.
•	Modifications can be done easily based on the requirements when necessary.

Requirement specification
Functional requirements:

•	Librarian login (Admin Zone): Admin can login and access the required information.
•	Security: No other users can login except the admin.
•	Update details: Admin can add and remove books and users also change the status of the book (available/ Unavailable)


Non-functional requirements:

•	Secure access to user’s data with own login name and password.
•	Better component design to get better performance.
•	Flexible service based architecture desirable for further extension.

Getting started
Installation

pip install python 3.6.1

python version must be more than 3.0 in order the run this web application.

It is possible that pip does not get installed by default. So use the command (only when pip not installed )

python -m ensurepip --default-pip 

pip install django 1.11.4

To clone and run this application, you need to install Github and Django in your computer.
Django version must be greater than 1.11.

To clone the repository

Use Git or checkout with SVN using the web URL.
https://github.com/bandana-khadka/aip.git

Salient features:

•	Sing up, Login, Logout
o	Users need to create an account and log in to create book catalogue.
•	Create, View, Search, Edit and Delete
o	Registered users can create their book info.
o	Administrator can edit and delete book based on availability.
o	Everyone can search for book information.

Coding Standards

COMMENTS
-> TODOs should include the string. TODO in all caps, followed by the name, e-mail address, or other identifier of the person who can best provide context about the problem referenced by the TODO, in parentheses. A comment explaining what there is to do is required. 
-> Have a comment on every function that describes its purpose.



INDENTATION
-> Spaces are the preferred indentation method.
-> Tabs should be used only to remain consistent with the codes already indented with the tabs.
-> Since, we need python version more than 3.6 it disallows mixing of tabs and spaces.

NAMING

-> Use Capitals for class names, but lower_with_under.py for module names.
 -> Use of underscores in names, not using any dashes.
 -> Not using any single character names except for counters and iterators.
 -> Prepending a single underscore (_) has some support for protecting module variables and functions (not included with import * from). 
-> Prepending a double underscore (__) to an instance variable or method effectively serves to make the variable or method private to its class (using name mangling). 
-> Don't abbreviate local variables (e.g., 'total' not 'tot')

STATEMENTS
 -> only one statement in a line.	

WHITE SPACING 

-> No whitespace inside parentheses, brackets or braces.
 -> No whitespace before a comma, semicolon, or colon. Do use whitespace after a comma, semicolon, or colon except at the end of the line. 
-> No whitespace before the open parenthesis/bracket that starts an argument list, indexing or slicing.

IMPORTS

 -> Imports should be usually on separate lines so that it will be clear and precise if followed conventions.
For example,
Yes: Import django
         Import sys
No: Import django, sys


PYTHON STYLE RULES

-> Do not terminate your lines with semi-colons and do not use semi-colons to put two commands on the same line.
 -> Indent your code blocks with 4 spaces.
 -> Two blank lines between top-level definitions, one blank line between method definitions.

AUTHORS

Students of UTS- Bandana, Yoonhye, Sachin

REFERENCES

https://docs.djangoproject.com/en/1.11/
https://github.com/buckyroberts/Viberr
https://simpleisbetterthancomplex.com/tutorial/2016/08/29/how-to-work-with-ajax-request-with-django.html
https://developers.google.com/maps/documentation/javascript/tutorial
https://www.youtube.com/watch?v=qgGIqRFvFFk&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK
