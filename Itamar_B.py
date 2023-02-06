import json
#Crear una funció que mostri, per consola, i guardi en un arxiu extern,
# un JSON amb una key de nom book que contindrà titel, cover, year i pages

def jsonString():
    with open('booksFile.json', 'w') as file:
        libros=""" {'Books:
        
             [{"title":"la insoportable levedad del Ser",
                "cover":"verde",
                "year":"1973",
                "pages":"458" },
                
             {"title":"La Republica",
                "cover":"Blanca",
                "year":"237 a.c",
                "pages":"732" },
                
             {"title":"El Quijote",
                "cover":"moñigo",
                "year":"1632",
                "pages":"789" }, 
                
             {"title":"El mercader de Venecia",
                "cover":"Lila",
                "year":"1633",
                "pages":"231" },
              ]}
    """
    with open ("book1",'w') as file:
        json.dump(libros,file)

def printJson():
    with open ("book1", 'r') as file:
        result= json.load(file)
        print(result)

