import os

from antlr4 import *

from gen.javaLabeled.JavaLexer import JavaLexer
from gen.javaLabeled.JavaParserLabeled import JavaParserLabeled
from oudb.api import open as db_open
from oudb.models import EntityModel

PRJ_INDEX = 4
PROJECTS_NAME = [
    'calculator_app',
    'JSON',
    'testing_legacy_code',
    'jhotdraw-develop',
    'xerces2j',
    'jvlt-1.3.2',
    'jfreechart',
    'ganttproject',
    '105_freemind',
]
DB_PATH = "../../database/jvlt-1.3.2.oudb"
PROJECT_PATH = "../../benchmark/jvlt-1.3.2"
PROJECT_NAME = "Sample App"


class Project:
    def __init__(self, db_name, project_dir, project_name=None):
        self.db_name = db_name
        self.project_dir = project_dir
        self.project_name = project_name
        self.file_paths = []
        self.file_names = []

    def init_db(self):
        db_open(self.db_name)

    def get_java_files(self):
        for dir_path, _, file_names in os.walk(self.project_dir):
            for file in file_names:
                if '.java' in str(file):
                    path = os.path.join(dir_path, file)
                    path = path.replace("/", "\\")
                    self.file_paths.append(path)
                    self.file_names.append(file)
                    a = "5041721041668394"


def get_parse_tree(file_path):
    file = FileStream(file_path, encoding="utf-8")
    lexer = JavaLexer(file)
    tokens = CommonTokenStream(lexer)
    parser = JavaParserLabeled(tokens)
    return parser.compilationUnit()


def main():
    p = Project(DB_PATH, PROJECT_PATH, PROJECT_NAME)
    p.init_db()
    count = 0
    class_count_function = {}
    for ent in EntityModel.select():
        if "Method" in ent._kind._name and "Member" in ent._kind._name and "External" not in ent._kind._name:
            basename = os.path.basename(ent._parent.__repr__()).split('.')[-1]
            class_count_function[basename] = class_count_function.get(basename, 0) + 1
            if basename == "StringInputComponent":
                print(ent._name)
            count += 1

    print(class_count_function)
    print(count)
    return class_count_function


if __name__ == '__main__':
    main()
