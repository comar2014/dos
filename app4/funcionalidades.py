import sqlite3


class Base_Datos:


    def __init__(self):
        
        #yo creo que esto no debe ser
        self.db= sqlite3.connect('Apartamentos.db')
        self.cursor =self.db.cursor()
        print("La base de datos se ha creado correctamente")


    #Creacion de la tabla

    def crea_Tabla_Apartamentos(self):
        self.cursor =self.db.cursor()
        self.db.execute('''CREATE TABLE T_APARTAMENTO(
           id           INTEGER  PRIMARY KEY AUTOINCREMENT,
           titulo       TEXT NOT NULL,
           descripcion  TEXT NOT NULL,
           facilidades   TEXT NOT NULL,
           caracteristicas TEXT NOT NULL,
           ubicacion    TEXT NOT NULL,
           precio       INTEGER NOT NULL,
           longitud       FLOAT,
           latitud       FLOAT,
           tel          TEXT NOT NULL,
           correo       TEXT NOT NULL )''')
        self.db.commit()
        print ("Tabla creada con exito")


    def crea_Tabla_Favoritos(self):
        self.cursor =self.db.cursor()
        self.db.execute('''CREATE TABLE T_FAVORITO(
           id          INTEGER PRIMARY KEY AUTOINCREMENT,
           nombre_usuario     TEXT NOT NULL,
           id_apartamento   TEXT NOT NULL  
          )''')
        self.db.commit()
        print ("Tabla favoritos ha sido creada con exito")

    def inserta_Apartamento(self,pTitulo,pDescripcion,pFacilidades,pCarac,pUbicacion,pPrecio,pLong,pLat,pTel,pCorreo):
        self.cursor.execute('''INSERT INTO T_APARTAMENTO(titulo,descripcion,facilidades,caracteristicas,ubicacion,precio,longitud,latitud,tel,correo)
                       VALUES(?,?,?,?,?,?,?,?,?,?)''', (pTitulo.upper(),pDescripcion.upper(),pFacilidades.upper(),pCarac.upper(),pUbicacion,pPrecio,pLong,pLat,pTel,pCorreo))
        self.db.commit()
        print("Se guardo correctamente")

    def inserta_Favorito(self, pNombre_usuario,pId_apartamento):
        self.cursor.execute('''INSERT INTO T_FAVORITO(correo_usuario,id_apartamento)
                       VALUES(?,?)''', (pNombre_usuario,int(pId_apartamento)))
        self.db.commit()
        print("Se guardo correctamente")


    def cerrar_BaseDatos(self):
        self.db.close()
        
    def busqueda_Apartamentos(self,pFacilidades,pCaracteristicas,pUbicacion,pPrecio,pOrden):
        resultados=[]
        lista_Facilidades=pFacilidades.split(",")
        lista_Caracteristicas=pCaracteristicas.split(",")
        if (pPrecio != ""):
            for facilidad in lista_Facilidades:
                self.cursor.execute('''SELECT id,titulo,descripcion,facilidades,caracteristicas,ubicacion,precio,longitud,latitud,tel,correo FROM T_APARTAMENTO WHERE facilidades LIKE \'%'''
                            + facilidad + '''%\' AND
                            ubicacion LIKE \'%'''
                            + pUbicacion + '''%\' AND
                            precio <= '''
                            + pPrecio + '''  '''  ) # pOrden puede ser ASC o DESC
                resultados = self.cursor.fetchall()
            for caracteristica in lista_Caracteristicas:
                self.cursor.execute('''SELECT id,titulo,descripcion,facilidades,caracteristicas,ubicacion,precio,longitud,latitud,tel,correo FROM T_APARTAMENTO WHERE 
                            caracteristicas LIKE \'%'''
                            + caracteristica+ '''%\' AND
                            ubicacion LIKE \'%'''
                            + pUbicacion + '''%\' AND
                            precio <= '''
                            + pPrecio + ''' ''' ) # pOrden puede ser ASC o DESC
                resultados.extend(self.cursor.fetchall())
        else:
            for facilidad in lista_Facilidades:
                self.cursor.execute('''SELECT id,titulo,descripcion,facilidades,caracteristicas,ubicacion,precio,longitud,latitud,tel,correo FROM T_APARTAMENTO WHERE facilidades LIKE \'%'''
                            + facilidad + '''%\' AND
                            ubicacion LIKE \'%'''
                            + pUbicacion + '''%\' ''')
                resultados = self.cursor.fetchall()
            for caracteristica in lista_Caracteristicas:
                self.cursor.execute('''SELECT id,titulo,descripcion,facilidades,caracteristicas,ubicacion,precio,longitud,latitud,tel,correo FROM T_APARTAMENTO WHERE 
                            caracteristicas LIKE \'%'''
                            + caracteristica+ '''%\' AND
                            ubicacion LIKE \'%'''
                            + pUbicacion + '''%\' ''' ) # pOrden puede ser ASC o DESC
                resultados.extend(self.cursor.fetchall())
        resultados_Final=[]                      
        for aparta in resultados: 
            if resultados_Final==[]:
                resultados_Final.append(aparta)   
            else:
                if aparta  in resultados_Final:
                    print(aparta[0])
                else:
                    resultados_Final.append(aparta)
        #print(resultados_Final)
        if pOrden== 'ASC':
            resultado_Final=sorted(resultados_Final, key=lambda aparta: aparta[6]) 
        else:
            resultado_Final=sorted(resultados_Final, key=lambda aparta: aparta[6],reverse=True)
        return resultados_Final
    

    #recibe el correo (nombre del usuario) y ordenamiento(ASC / DESC)
    def busqueda_Favoritos(self,pNombre):
        self.cursor.execute('''SELECT *
                                FROM (SELECT FA.id, FA.correo_usuario, FA.id_apartamento, AP.titulo, AP.descripcion, AP.facilidades, AP.caracteristicas, AP.ubicacion, AP.precio, AP.longitud, AP.latitud, AP.tel, AP.correo
                                              FROM T_FAVORITO AS FA
                                              JOIN T_APARTAMENTO AS AP
                                              ON FA.id_apartamento = AP.id) AS FAVS
                                WHERE FAVS.nombre_usuario LIKE \'%''' + pNombre + '''%\'''')
        #self.cursor.execute('''SELECT * FROM T_FAVORITO WHERE correo_usuario LIKE \'%''' + pCorreo + '''%\' ''')
        resultado_Final = self.cursor.fetchall() 
        #for aparta in resultado_Final:
        #    print('{0} : {1}, {2}'.format(aparta[0], aparta[1], aparta[2]))
        return resultado_Final

    def verTodo(self):
        self.cursor.execute('''SELECT * FROM T_FAVORITO''')
        favoritos= self.cursor.fetchall()
        self.cursor.execute('''SELECT * FROM T_APARTAMENTO''')
        apartamentos = self.cursor.fetchall()
        print (favoritos)
        print (apartamentos)
        
