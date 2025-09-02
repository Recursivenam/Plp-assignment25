def read_and_write_file():
    try:
        # Ask the user for a filename
        filename = input("Enter the filename: ")

        # Read the file
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content
        modified_content = content.upper()

        # Write the modified content to a new file
        new_filename = f"modified_{filename}"
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content has been written to {new_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except OSError as e:
        print(f"Error: An error occurred while reading or writing the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_and_write_file()
