import csv
import os
from read_files import file_list, directory, get_filename
from DB_connection import connection, cursor


def create_tables(file):

    # Creating the local file path
    file_directory = directory + file

    # Extract the file name by splitting the name part
    table_name = get_filename(file)

    with open(file_directory, 'r') as file:

        csv_reader = csv.reader(file)

        # Read the header row
        columns = next(csv_reader)

        # Begin construction of the SQL command to create a table
        create_table_command = f'DROP TABLE IF EXISTS {table_name};\n'

        create_table_command += f'CREATE TABLE {table_name} (\n'

        sql_type = 'VARCHAR(100)'

        # Loop through each header to add it to the SQL command
        for col in columns:
            # Set SQL data type for each column
            create_table_command += f'    "{col}" {sql_type},\n'

        # Remove the trailing comma from the last column definition
        create_table_command = create_table_command.rstrip(',\n') + '\n);'

        # print(create_table_command)

        # Execute the SQL command to create the table
        cursor.execute(create_table_command)

    print(f"Table {table_name} is created!")

    return True
