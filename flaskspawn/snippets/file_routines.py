import re

def copy_contents_of_file(source_file, destination_file):
    with open(source_file) as f:
        source_contents = f.read()

    with open(destination_file, "w") as f:
        f.write(source_contents)

def append_to_file(file_path, source_file):
    with open(source_file) as f:
        source_contents = f.read()

    with open(file_path, "a") as f:
        f.write(source_contents)

def append_text_to_file(file_path, source_text):
    with open(file_path, "a") as f:
        f.write(source_text)

def add_text_to_file_after_pattern(text, pattern, destination_file):
    with open(destination_file, 'r+') as f:
        contents = f.readlines()
        line_index = None
        for idx, line in enumerate(contents):
            result = re.search(pattern, line)
            if result:
                line_index = idx
                break
        if line_index:
            contents.insert(line_index + 1, text)
            contents = "".join(contents)
            f.seek(0)
            f.write(contents)
            f.truncate()

def add_text_to_top_of_file(destination_file, text):
    with open(destination_file, 'r+') as f:
        contents = f.readlines()
        contents.insert(0, text)
        contents = "".join(contents)
        f.seek(0)
        f.write(contents)
        f.truncate()
