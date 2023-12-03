import os


def read_files(directory):
    return os.listdir(directory)


def get_filename(file):
    return os.path.splitext(file)[0]


# Set the directory where the CSV files are located
directory = "C:/Users/IT Support/Downloads/Sample_task/test/"

# Get a list of files in the directory
file_list = read_files(directory)
