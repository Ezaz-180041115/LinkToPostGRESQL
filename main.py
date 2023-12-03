from DB_connection import connection, cursor
from read_files import file_list
from DB_table_creation import create_tables
from DB_data_insertion import insert_data


if __name__ == '__main__':

    if connection:
        for file in file_list:
            if create_tables(file):
                insert_data(file)

    connection.commit()
    cursor.close()
    connection.close()
