"""
Text files should be stored as:
'random_090000'
or
'counting_130000'
where these two text files should include
the random input-output pairs between
90000 and 99999, and the counting input-output
pairs between 130000 and 139999, respectively.
For 1 million input-output pairs, we get
100 files, each containing 10000 pairs.
Each of the pairs should be separated with a comma and a space:
'hjfskldhfadf, 983rhyioufhsdf'
"""

import os


class Pair_exporter():
    def __init__(self, location='output/random_values'):
        self.dir = location


    def gen_fname(self, base_name):
        """Generate file name/path from base_name and directory."""
        if type(base_name) is not str:
            base_name = str(base_name)
        fname = self.dir + '/' + base_name + '.txt'
        return fname


    def is_num(self, variable):
        """Check if variable is a number.
        * Yes   -> True
        * No    -> False
        """
        try:
            i = float(variable)
            return True
        except:
            return False


    def get_base_name(self, file_name, extension=False):
        for i in range(len(file_name) - 1, 0, -1):
            if file_name[i] == '.':
                if extension is True:
                    return file_name[i+1:]
                else:
                    return file_name[:i]


    def store_to_file(self, text, fname, rewrite=False):
        #full_name = gen_fname(num)
        #full_name = Pair_exporter.self + num
        mode = 'x'
        if rewrite:
            mode = 'w'
        
        f = open(fname, mode, encoding="utf-8")
        f.write(text + '\n')
        f.close()
        return True


    def scan_dir(self):
        """Find all .txt-files in self.dir."""
        files_found = []
        for fil in os.listdir(self.dir):
            #if fil.endswith(".txt"):
            #    files_found.append(os.path.join(self.di, fil))
            files_found.append(self.get_base_name(fil))
        return files_found


    def status_scan(self):
        """Check the existing files
        and find the progress.
        Returns the last number."""
        files = self.scan_dir()
        biggest_number = 0
        for fil in files:
            #print(fil)
            if self.is_num(fil):
                if int(fil) > biggest_number:
                    biggest_number = int(fil)
        return biggest_number


    def check_file(self, name):
        """Checks if a file exists and has 10000 lines."""
        full_name = self.dir + name
        if not os.path.isfile(full_name):
            return False
        
        f = open(full_name, 'r')
        text = f.read()
        f.close()
        if len(text) != 10000:
            return False
        return True


    def update_status_file(self, update):
        """Updated the status file with an update (str)."""
        status_file_path = self.gen_fname('status_file')
        f = open(status_file_path, 'a')
        f.write(update)
        f.write('\n')
        f.close()
        return True
    

    def store(self, text, num):
        """Interface for text and num.
        > Returns False is failed.
        > Returns True if successful or file already checks out."""
        fname = self.gen_fname(num)
        if self.check_file(fname):
            status = 'File "' + fname + '" already exists and checks out!'
            return True

        elif os.path.isfile(fname):
            status = 'File "' + fname + '" exists, but there seems to be an issue with it! Remaking the file...'
            self.update_status_file(status)
            
            self.store_to_file(text, fname, rewrite=True)
            if self.check_file(fname):
                status = 'Attempted remaking of the file "' + fname + '" were successful!'
                self.update_status_file(status)
                return True
            else:
                status = 'Attempted remaking the file "' + fname + '", but it failed.'
                self.update_status_file(status)
                return False
        else:
            self.store_to_file(text, fname)
            status = 'File "' + fname + '" created.'
            self.update_status_file(status)
            return True


if __name__ == '__main__':
    pe = Pair_exporter()
    print(pe.status_scan())
    pe.store('This\nis\nthe\ntext.', '30000')
