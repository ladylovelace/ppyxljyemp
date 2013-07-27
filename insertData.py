#Leitura do arquivo data.dat
arq = open("data.dat","r")
f = arq.readlines()
# Todo o conteudo colocado em text[]
text = []
for line in f :
    line = line.split("\t")
    try: 
        line[4]
        text.append(line)
    except IndexError: 
        print("Erro na linha\n",line)
arq.close()
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

    #Insere dados de data no bando juntadb
    i  = 0
    while i < len(text) :
        company = {
            "cnpj" : text[i][0],
            "nome" : text[i][1],
            "status" : text[i][2],
            "uf" : text[i][3],
            "fantasia" : text[i][4]
        }
        dbh.companies.insert(company,safe=True)
        i+=1
    print ("Successfully insert on database")
if __name__ == "__main__":
        main()