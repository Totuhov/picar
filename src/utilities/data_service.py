import os
import json

class DataService:
    """
    A class for managing data storage and retrieval in a JSON file.

    Attributes:
        file_path (str): The path to the JSON file for data storage.
        data (list): A list to store data.

    Methods:
        __init__(self, file_path: str = './log/drive_data.json'):
            Initializes a DataService instance with a default or provided file path.

        clear_data(self):
            Clears the data list and saves the changes to the JSON file.

        write_data(self, new_object):
            Appends a new object to the data list.

        read_data(self):
            Reads and returns the data from the JSON file.

        save_to_file(self):
            Creates the necessary directory structure and saves the data to the specified JSON file.
    """

    def __init__(self, file_path: str = './log/drive_data.json'):
        """
        Initializes a DataService instance.

        Args:
            file_path (str): The path to the JSON file for data storage.
        """
        self.file_path = file_path
        self.data = []

    def clear_data(self):
        """
        Clears the data list and saves the changes to the JSON file.
        """
        self.data = []
        self.save_to_file()

    def write_data(self, new_object):
        """
        Appends a new object to the data list.

        Args:
            new_object: The object to be added to the data list.
        """
        self.data.append(new_object)

    def read_data(self):
        """
        Reads and returns the data from the JSON file.

        Returns:
            list: The data read from the JSON file.
        """
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def save_to_file(self):
        """
        Creates the necessary directory structure and saves the data to the specified JSON file.
        """
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=2)