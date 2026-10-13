
import json

# Открываем файл для чтения ('r') с указанием кодировки UTF-8
def read_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)



class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class UserRepository:
    def get_all_users(self):
        json_data =  read_json("data.json")
        return [User(name, email) for name, email in json_data.items()]
    
    
  

