import pymongo
#Establesemos la conexion con mongodb
MONGO_HOST='localhost'
MONGO_PUERTO='27017'
MONGO_TIEMPO_FUERA=1000

MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"
#Especificamos a que base de datos y coleccion vamos a estableser la conexion 
MONGO_BASEDATOS="BaseM"
MONGO_COLECCION="Enfermedad"
try:
    client=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
    baseDatos=client[MONGO_BASEDATOS]
    coleccion=baseDatos[MONGO_COLECCION]
    #client.server_info()
    #print("conexion a mongo exitosa")
    client.close
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo exedido"+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb"+errorConexion)

