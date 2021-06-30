# Task to implement file exception handling in best way possible by applying DRY - OOP - Python Packaging
### Let's create a file file_exceptions.py to handle file exception handling
```python
class File_Exceptions:
    def file_open(file_name):
        try:
            file = open(file_name)
            print("file found")  # Try block required except or will throw an error
        except FileNotFoundError as errmsg:  # Type of error
            print("file not found {}".format(errmsg))
        finally:  # Finally will execute regardless of try and except block execution
            print("Have a nice Day!")

    def file_write(file_name, file_write):
        try:
            file = open(file_name, "w")  # Open file and overwrite any content
            file.write(file_write)  # Write in file method arg (file_write)
            print("content added")

        except FileNotFoundError as errmsg:  # Type of error
            print("file not found {}".format(errmsg))

        finally:  # Finally will execute regardless of try and except block execution
            print("Thank you for visiting. See you again!")
```
### Let's create the program.py file to implement/use exception handling
```python
from app.file_exceptions import File_Exceptions

file_prompt = input("Enter file name: ")  # Prompt user for file name
file_name = file_prompt + ".text"  # concatenation

prompt = (input("Would you like to add more content?(yes/no) "))

if prompt.lower() == 'yes':
    file_write = (input("what would you like to add? "))
    File_Exceptions.file_write(file_name, file_write)
else:
    File_Exceptions.file_open(file_name)
```
