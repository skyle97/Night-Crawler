def open_file(file_list):
    with open(file_list, 'r') as file:
        credentials = file.read().split('\n')
    credentials = [x for x in credentials if x != '']
    return credentials
