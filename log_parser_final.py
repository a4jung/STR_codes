import re

def readline(log_file):
    line = log_file.readline()
    if line == "":
        return None
    else:
        return re.sub(r"[\n\t\s]*", "", line)
    
def is_read_type(line):
    return line.startswith('FLANKING') or line.startswith('SPANNING') or line.startswith('INREPEAT')

# To define name and corresponding sequence
def log_parse(text_file):
    with open(text_file) as log_file:
        dic = {}
        line = readline(log_file)
        while line:
            if line is not None and line != "" and line[0].isdigit():
                repeat_id = line[:-1]
                dic[repeat_id] = {}
                line = readline(log_file)
                while line is not None and (line == "" or not line[0].isdigit()):
                    if is_read_type(line):
                        read_type = line[:-1]
                        dic[repeat_id][read_type] = {}
                        line = readline(log_file)
                        while line is not None and (line == "" or not line[0].isdigit()) and not is_read_type(line):
                            if line.startswith('name'):
                                name_id = line[line.find('"')+1:-1]
                                line = readline(log_file)
                                if read_type.startswith('INREPEAT'):
                                    dic[repeat_id][read_type][name_id] = line[4:]
                                else:

                                    line = readline(log_file)
                                    dic[repeat_id][read_type][name_id] = line
                            line = readline(log_file)
                        continue
                    line = readline(log_file)
                continue
            line = readline(log_file)
        return dic
    
