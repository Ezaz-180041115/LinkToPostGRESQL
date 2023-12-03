import csv
from read_files import file_list, directory, get_filename
from DB_connection import connection, cursor


def insert_data(file):

    # Creating the local file path
    file_directory = directory + file

    # Extract the file name by splitting the name part
    table_name = get_filename(file)

    with open(file_directory, 'r') as file:
        csv_reader = csv.reader(file)

        # Skip the header row
        columns = next(csv_reader)

        # Start constructing the SQL query to insert data
        basic_query = f'INSERT INTO {table_name} \n    ('

        # Add column names to the INSERT INTO part of the query
        basic_query += ', '.join([f'"{col}"' for col in columns])

        # Add the VALUES part of the query
        basic_query += ') \nVALUES\n    ('

        for row in csv_reader:
            insert_query = basic_query
            for cell in row:
                insert_query += f"'{cell}', "
            insert_query = insert_query.rstrip(", ") + ");"

            # print(insert_query)

            # Execute the INSERT query with the data
            cursor.execute(insert_query)

    print(f"Data of table {table_name} is inserted!")

