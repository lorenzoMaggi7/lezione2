"""
9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. 
In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.
"""
from esercizilz5 import Privileges
from esercizilz5 import Admin

admin2 = Admin("Danila","Rahoutsu", 21, 187, ["add user", "delete user"])

admin2.privileges.show_privileges()