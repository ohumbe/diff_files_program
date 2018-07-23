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
    # check for a line in the file
    if len(line1) == 0 or len(line2) == 0:
        idx_indicator = ('=' * idx) + '^'
        if len(line1) == 0:
            formatted = '' + '\n' + idx_indicator + '\n' + line2 + '\n'
        elif len(line2) == 0:
            formatted = line1 + '\n' + idx_indicator + '\n' + '' + '\n'
        return formatted
    # check for newline character or carriage return
    elif ('\n' in line1) or ('\r' in line1) or ('\n' in line2) or ('\r' in line2):
        formatted = ''
        return formatted
    # check for invalid index
    elif (not idx in range(len(line1) + 1)) or (not idx in range(len(line2) + 1)):
        formatted = ''
        return formatted
    else:
        idx_indicator = ('=' * idx) + '^' 
        formatted = line1 + '\n' + idx_indicator + '\n' + line2 + '\n'
        return formatted
    
# tests
line1 = 'a'
line2 = 'ab'
idx = 1
print(singleline_diff_format(line1, line2, idx))