# From repo file import repo class
from repo import repo

class Service:
    # repo object from repo class in service
    repo1 = repo()

    def addToDB(self):
        print("Adding to DB")
        return self.repo1.addedDB()

    def getAllData(self):
        query = "SELECT * FROM orders"
        return self.repo1.runQuery(query)