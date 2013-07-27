########################################
import sys
from pymongo import MongoClient
from pymongo import Connection
from pymongo.errors import ConnectionFailure

def main():
#Connect to MongoDB
    try:
        c = Connection(host="localhost", port=27017)
        print ("Connected sucessfully")
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    # Get a Database handle to a database named "mydb -> juntadb"
    dbh = c["juntadb"]
    # Demonstrate the db.connection property to retrieve a reference to the
    # Connection object should it go out of scope. In most cases, keeping a
    # reference to the Database object for the lifetime of your program should
    # be sufficient.
    assert dbh.connection == c
    print "Successfully set up a database handle"

 #Busca Todas as empresas
    companies = dbh.companies.find()
    #Imprime todas as empresas
    for company in companies:
        print (company)
    # Contar quantas empresas existem cadastradas
    countCompanies = dbh.companies.find().count()
    print "There are %d companies" % countCompanies

    searchComp = raw_input("Empresa: ")
    company = dbh.Data.find_one({"nome": searchComp})
    print (company)
if __name__ == "__main__":
        main()