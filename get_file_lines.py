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
    
    # initiate a list and open the file
    file_lines = []
    open_file = open(filename, 'r')
    # remove newline characters or '\r'
    for line in open_file:
        line = line.replace('\n', '')
        line = line.replace('\r', '')
        file_lines.append(line)
    open_file.close()
    return file_lines

print(get_file_lines('file1.txt'))
print(get_file_lines('file9.txt'))