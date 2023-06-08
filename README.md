# python_tkinter
from pymongo import MongoClient

# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://intelloper:1234@10.150.151.30/?authSource=admin', 27017)

# db = client.test_database
db = client['mydb'] # test-db라는 이름의 데이터베이스에 접속

print(client.list_database_names()) 











