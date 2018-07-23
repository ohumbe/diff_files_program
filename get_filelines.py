def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    
    # open the file
    open_file = open(filename, 'rt')
#    file_lines = ''
    # check for empty file
#    print(len(open_file.read()))
    if len(open_file.read()) < 1:
        return file_lines
    # remove newline characters or '\r'
    else:
        file_lines = []
        for line in open_file.read():
            print(line)
            line = line.replace('\n', '')
            line = line.replace('\r', '')
            file_lines.append(line)
    return file_lines
    open_file.close()

# tests
print(get_file_lines('file8.txt'))