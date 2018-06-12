"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    shorter_line = None
    longer_line = None
    
    # check for differences
    diff_index = None
    added_content = None
    
    # if line1 or line2 are empty
    if (len(line1) == 0) or (len(line2) == 0):
        diff_index = 0
        return diff_index
    # if line1 and line2 are different
    elif line1 != line2:
        # if lines are same length
        if len(line1) == len(line2):
            for index in range(len(line1)):
                    if line1[index] != line2[index]:
                        diff_index = index
                        break
            return diff_index
        # if lines are different length
        elif len(line1) != len(line2):
            # determine shorter/longer line
            if len(line1) < len(line2):
                shorter_line = line1
                longer_line = line2
            elif len(line2) < len(line1):
                shorter_line = line2
                longer_line = line1
                
            # check to make sure shorter_line is not in longer_line    
            if shorter_line[:] == longer_line[:len(shorter_line)]:
                    diff_index = len(shorter_line)
                    added_content = 'everything starting at this point was added'
                    return diff_index
            # if there are differences between shorter_line and longer_line
            # within the range of shorter_line, return the diff_index
            elif shorter_line[:] != longer_line[:len(shorter_line)]:
                for index in range(len(shorter_line)):
                    if shorter_line[index] != longer_line[index]:
                        diff_index = index
                        break
                return diff_index
    # return result if lines are identical
    else: return IDENTICAL

# tests
line1 = 'what did you do?'
line2 = 'what did you do? '
line3 = 'what did your do?'
#print(singleline_diff(line1, line2))
#print(singleline_diff(line1, line3))

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    formatted = ''
    # check for newline character or carriage return
    if ('\n' in line1) or ('\r' in line1) or ('\n' in line2) or ('\r' in line2):
        return formatted
    # check for invalid index
    elif (not idx in range(len(line1))) or (not idx in range(len(line2))):
        return formatted
    else:
        idx_indicator = ('=' * idx) + '^' 
        formatted = line1 + '\n' + idx_indicator + '\n' + line2 + '\n'
        return formatted

# tests
line1 = 'where did you go?'
line2 = 'where did your go?'
line3 = 'where did you go?'
line4 = 'where did your go?'
line5 = 'where 3did yours go?'
line6 = 'where did yours go?'
#print(singleline_diff_format(line1, line2, 12))
#print(singleline_diff_format(line3, line4, 13))


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    shorter_list = None
    longer_list = None
    diff_list = None
    diff_index = None
    
    # check if lines are equivalent    
    if lines1 == lines2:
        return (IDENTICAL, IDENTICAL)
    
    # check for an empty line
    elif (len(lines1) == 0) or (len(lines2) == 0):
        diff_list = 0
        diff_index = 0
    
    # check what differences there are
    elif lines1 != lines2:
        # if lines are the same length
        if len(lines1) == len(lines2):
            for index in range(len(lines1)):
                if lines1[index] != lines2[index]:
                    # determine the index using singleline_diff
                    diff_list = index
                    diff_index = singleline_diff(lines1[diff_list], lines2[diff_list])
                    #print(shorter_list[index], longer_list[index], 'first')
                    break
                    
        # if lines are different length, determine which line is shorter
        elif len(lines1) != len(lines2):
            if len(lines1) < len(lines2):
                shorter_list = lines1
                longer_list = lines2
            elif len(lines2) < len(lines1):
                shorter_list = lines2
                longer_list = lines1
#            print('shorter list is ' + shorter_list)
    
            # check for differences
            # in the case that the shorter_list is not in longer_list
            if shorter_list[:len(shorter_list)] != longer_list[:len(shorter_list)]:
                for index in range(len(shorter_list)):
                    if shorter_list[index] != longer_list[index]:
                        diff_list = index
                        # determine the index using singleline_diff
                        diff_index = singleline_diff(shorter_list[diff_list], longer_list[diff_list])
#                        print(shorter_list[index], longer_list[index], 'first')
                        break
            # in the case that all of the shorter_list is in the longer_list        
            elif shorter_list[:len(shorter_list)] == longer_list[:len(shorter_list)]:
#                print(longer_list[:len(shorter_list)], 'second')
                diff_list = len(shorter_list)        
            
    return (diff_list, diff_index)
 
# tests
line1 = 'where did you go?'
line2 = 'where did your go?'
line3 = 'where did you go?'
line4 = 'where did your go?'
line5 = 'where did yours go?'
line6 = 'where did yours go?'
lines1 = [line1, line2, line5]
lines2 = [line3, line4, line6]
#print(multiline_diff(lines1, lines2))

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
    open_file = open(filename, 'rt')
    # remove newline characters or '\r'
    for line in open_file:
        line = line.replace('\n', '')
        line = line.replace('\r', '')
        file_lines.append(line)
    open_file.close()
    return file_lines

def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    # return lists from file using get_file_lines()
    file1 = get_file_lines(filename1)
    file2 = get_file_lines(filename2)
    line_no = None
    index_no = None
    
    # check if files are the same
    if multiline_diff(file1, file2) == (-1, -1):
        return "No differences\n"
    
    # if lines are different:
    elif multiline_diff(file1, file2) != (-1, -1):
        # if there is an empty file
        if (len(get_file_lines(file1)) == 0) or (len(get_file_lines(file2)) == 0):
            line_no = 0
            index_no = 0
        # check the rest of the cases                     
        else:
            line_no = multiline_diff(file1, file2)[0]
            index_no = multiline_diff(file1, file2)[1]
#            print(file1[line_no], file2[line_no])
            first_format = singleline_diff_format(file1[line_no], file2[line_no], index_no)
#            print(first_format)
        return 'Line {0}\n'.format(line_no) + first_format + '\n'

# tests
print(file_diff_format('file8.txt', 'file9.txt'))