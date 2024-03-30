def write_to_file(filename, content):
  """Writes content to a file in write mode ('w').

  Args:
    filename: The name of the file to write to.
    content: A list of strings or lines to write to the file.
  """
  try:
    with open(filename, 'w') as file:
      for line in content:
        file.write(line + "\n")
    print(f"Successfully wrote to {filename}")
  except FileNotFoundError:
    print(f"Error: File '{filename}' does not exist.")
  except PermissionError:
    print(f"Error: Insufficient permissions to write to '{filename}'.")
  finally:
    # Regardless of exceptions, attempt to close the file
    if 'file' in locals():
      file.close()

def read_from_file(filename):
  """Reads the contents of a file and displays them on the console.

  Args:
    filename: The name of the file to read from.
  """
  try:
    with open(filename, 'r') as file:
      contents = file.read()
      print(f"Contents of '{filename}':\n{contents}")
  except FileNotFoundError:
    print(f"Error: File '{filename}' does not exist.")
  except PermissionError:
    print(f"Error: Insufficient permissions to read from '{filename}'.")

def append_to_file(filename, content):
  """Appends content to a file in append mode ('a').

  Args:
    filename: The name of the file to append to.
    content: A list of strings or lines to append to the file.
  """
  try:
    with open(filename, 'a') as file:
      for line in content:
        file.write(line + "\n")
    print(f"Successfully appended to {filename}")
  except PermissionError:
    print(f"Error: Insufficient permissions to append to '{filename}'.")

# Create the file
write_to_file("my_file.txt", [
  "This is the first line of text.\n",
  "Here's some more text with a number: 42\n",
  "And a final line for good measure.\n"
])

# Read and display the file contents
read_from_file("my_file.txt")

# Append additional lines
append_to_file("my_file.txt", [
  "Appending some new content...\n",
  "Line 4 with another number: 100\n",
  "The final appended line.\n"
])

# Read and display the file contents again (including appended data)
read_from_file("my_file.txt")
