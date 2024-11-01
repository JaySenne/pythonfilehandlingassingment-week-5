# File Writing
try:
    # Create a new text file in write mode
    with open("my_file.txt", "w") as file:
        file.write("This is the first line.\n")
        file.write("The second line contains a number: 42.\n")
        file.write("Finally, this is the third line.\n")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred while writing to the file: {e}")
finally:
    print("File writing attempt completed.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print("Contents of 'my_file.txt':")
        print(contents)
except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred while reading the file: {e}")
finally:
    print("File reading attempt completed.")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Appending a new line.\n")
        file.write("Another appended line with a number: 99.\n")
        file.write("Yet another line added to the file.\n")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred while appending to the file: {e}")
finally:
    print("File appending attempt completed.")

# Display Updated Contents
try:
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print("Updated contents of 'my_file.txt':")
        print(contents)
except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred while reading the file: {e}")
finally:
    print("Final file reading attempt completed.")
