import json

class DataService:
        
    def __init__(self, file_path):
        self.file_path = file_path
        
        self.data = []

    def clear_data(self):
        self.data = []
        self._save_to_file()

    def write_data(self, new_object):
        self.data.append(new_object)

    def read_data(self):
        with open(self.file_path,'r') as file:
            return json.load(file)

    def _save_to_file(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=2)

