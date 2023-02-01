# From repo file import repo class
from repo import repo

class service:
    # repo object from repo class in service
    repo1 = repo()

    def addToDB(self):
        print("Adding to DB")
        return self.repo1.addedDB()