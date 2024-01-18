def create_table(columns, column_width, rows, row_height):
    # CREATE TOP LINE
    top_line = '╔' + '╦'.join(['═' * column_width for _ in range(columns)]) + '╗'

    # CREATE LINES/LINE CONTENT AND SEPARATOR LINE
    row_lines = []
    for _ in range(rows):
        # CREATE ROW WITH LINE HEIGHT
        for _ in range(row_height):
            row_content = '║' + '║'.join([' ' * column_width for _ in range(columns)]) + '║'
            row_lines.append(row_content)

        # CREATE THE SEPARATOR LINE AFTER EACH LINE
        row_lines.append('╠' + '╬'.join(['═' * column_width for _ in range(columns)]) + '╣')

    # REMOVES THE LAST EXCESS PARTING LINE
    row_lines.pop()

    # ADD BOTTOM LINE
    bottom_line = '╚' + '╩'.join(['═' * column_width for _ in range(columns)]) + '╝'

    # CREATING THE PRINT
    print(top_line)
    for line in row_lines:
        print(line)
    print(bottom_line)

# ENTERING THE VALUES
columns = int(input("Number of columns: "))
column_width = int(input("Column width: "))
rows = int(input("Number of rows: "))
row_height = int(input("Row height: "))

# EXECUTE FUNCTION
create_table(columns, column_width, rows, row_height)