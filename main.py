from app.io.input import read, read_file, read_file_with_pandas
from app.io.output import to_console, write


def main():

    input = read()
    fileInput = read_file('assets/somefile')
    csvFileInput = read_file_with_pandas('assets/somefile.csv')

    to_console(input)
    to_console(fileInput)
    write('assets/somefile-outputted.csv', csvFileInput)



if __name__ == '__main__':
    main()
