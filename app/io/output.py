def to_console(str):
    """
      print text
       str: str to print
    """
    print(str)


def write(file, str):
    """
      write to file
        file_path: str, path to file
        text: str, string to be written to file
    """
    with open(file, 'w') as file:
        file.write(str)
