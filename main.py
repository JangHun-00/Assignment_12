from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    lines = open(path, 'r').read().split('\n') # read file and split line into list, change variable name 'lines'
    return lines

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    # Preprocess unwanted characters
    def process_file(file):
        if '\\' in file:
            file = file.replace('\\', '\\\\') # \\ should be replaced to \\\\
        if '/' or '"' in file:
            file = file.replace('/', '\\/')
            file = file.replace('"', '\\"')
        return file

    # Template for json file
    template_start = '{\"English\":\"' # template starts with English
    template_mid = '\",\"German\":\"'
    template_end = '\"}'

    # Can this be working?
    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        english_file = process_file(english_file)
        german_file = process_file(german_file) # change variable name to german_file

        # result should be {"English": "(english_file)", "German": "(german_file)"}
        processed_file_list.append(template_start + english_file + template_mid + german_file + template_end)
    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    with open(path, 'w') as f: # open file with write mode to write file
        for file in file_list:
            f.write(file + '\n') # for concatenate files, each file variable should be written in each loop
            
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path) # change function to read german file

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list) # change function to make english and german file to json

    write_file_list(processed_file_list, path+'concated.json')
