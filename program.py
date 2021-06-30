from app.file_exceptions import File_Exceptions

file_prompt = input("Enter file name: ")  # Prompt user for file name
file_name = file_prompt + ".text"  # concatenation

prompt = (input("Would you like to add more content?(yes/no) "))

if prompt.lower() == 'yes':
    file_write = (input("what would you like to add? "))
    File_Exceptions.file_write(file_name, file_write)
else:
    File_Exceptions.file_open(file_name)