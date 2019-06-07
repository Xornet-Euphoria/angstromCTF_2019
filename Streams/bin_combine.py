import os


# in default, search current directory
def get_all_files(folder_name='.'):
    all_file_and_directory = os.listdir(folder_name)
    all_file_and_directory.sort()
    all_files = []
    for file in all_file_and_directory:
        file = folder_name + '/' + file
        if os.path.isfile(file):
            all_files.append(file)

    return all_files


def combine_bin_file(folder_name='.', output_name='output'):
    file_list = get_all_files(folder_name)
    with open(output_name, 'wb') as output_file:
        for file in file_list:
            with open(file, 'rb') as input_file:
                output_file.write(input_file.read())

    return True


if __name__ == '__main__':
    print(get_all_files())
    combine_bin_file()
