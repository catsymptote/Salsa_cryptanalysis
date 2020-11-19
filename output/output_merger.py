import os


def is_num(variable):
        """Check if variable is a number.
        * Yes   -> True
        * No    -> False
        """
        try:
            i = float(variable)
            return True
        except:
            return False


def scan_dir(dir):
    """Find all .txt-files in self.dir."""
    files_found = []
    for fil in os.listdir():
        #if fil.endswith(".txt"):
        #    files_found.append(os.path.join(self.di, fil))
        files_found.append(fil)
    return files_found


def sort_files(files:list):
    accepted_files = []
    for fil in files:
        if fil[-4:] == '.txt':
            if is_num(fil[:-4]):
                accepted_files.append(fil)
    return accepted_files


def combine_files(file_list, output_file):
    file_contents = []
    counter = 0
    print('Reading:')
    for fil in file_list:
        counter += 1
        if counter % 50 == 0:
            print(end='.', flush=True)
        with open(fil) as current_file:
            text = current_file.read() + '\n'
            file_contents.append(text)
    
    print('\nWriting:')
    counter = 0
    for content in file_contents:
        counter += 1
        if counter % 50 == 0:
            print(end='.', flush=True)
        with open(output_file, 'a') as write_file:
            write_file.write(content)


if __name__ == "__main__":
    files = scan_dir('/')
    relevant_files = sort_files(files)
    print('Found and updated files.', flush=True)
    combine_files(relevant_files, 'random_compiled_list.txt')
