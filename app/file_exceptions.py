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