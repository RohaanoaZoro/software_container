
from pymongo import MongoClient

def MongoDatabaseProperty():
    #client = MongoClient('mongodb://uva-devops-api:Ysl6nuTUn1TTHlskJuGCkBycbYHembMm1fJm1VfrrcHjdYjSYX8co3e7TS2yWkiNrTwOlcLGsl7NACDbRVyvOQ==@uva-devops-api.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@uva-devops-api@')
    client = MongoClient('mongodb-test.default', 27017,  username='admin', password='password')
    db = client.Devops_db
    colz = db.property
    return colz
