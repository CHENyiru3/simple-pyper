# This file is for reading the inputs (also parameters) and outputs

import re

class pyReader(object):
    def __init__(self, file_path):
        self.file = open(file_path, "r")

    def print_file(self):
        print(self.file.read())


    def count_pattern_in_def(self, pattern):
        self.file.seek(0)
        content = self.file.read()
        defs = re.findall(r'def.*\)',content)
        count = 0
        for parameter in defs:
            matches = re.findall(pattern, parameter)
            count += len(matches)

        return (len(defs),count)

# 创建一个pyReader对象
reader = pyReader(file_path='/Users/chen_yiru/PycharmProjects/simple-pyper/example_pipeline/tsv2csv.py')

# 调用print_file方法
reader.print_file()


count = reader.count_pattern_in_def('inputas')
print(f" {count} 次")

