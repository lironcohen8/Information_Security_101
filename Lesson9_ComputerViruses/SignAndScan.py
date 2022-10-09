# Implement the function sign so that given a line (in bytes),
# returns a unique signature of that line that is 20 characters long;
# Implement the scan function that, given a list of paths and a signature,
# reads them line by line, and returns a list of all the paths that have a line that matches the static signature.

from hashlib import sha1


def sign(line):
    return sha1(line).digest()


def scan(paths, signature):
    suspected_files = []
    for path in paths:
        with open(path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if sign(line.encode()) == signature:
                    suspected_files.append(path)
                    break
    return suspected_files
