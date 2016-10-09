import os
def view_dir(path):
    """
    This function prints all files and directories in the given directory.
    :args path: Path to the directory, default is current directory
    """
    names = os.listdir(path)
    names.sort()
    for name in names:
        print(name, end =' ')

if __name__ == '__main':
    view_dir('/')

