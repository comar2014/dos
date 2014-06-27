import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import unicodedata
import funcionalidades

from flask import Flask, redirect, url_for, request, render_template


app = Flask(__name__)
#funcionalidades.crea_Tabla_Apartamentos()

@app.route('/')
def registrarse(methods=['POST']):
       
	return render_template('face.html')	

@app.route('/mapa')
def mapa():
	return render_template('geocoging.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')
 
@app.route('/consultar/apartamento')
def consulta_apartamentos():
    return render_template('consultas.html')

@app.route('/agregar/apartamento')
def agregar():
    return render_template('agregar.html')

#en este metodo se almacenan los datos del apartamento que se publico
@app.route('/agregar_apartamento', methods=['POST'])
def agregar_apartamento():

    titulo_local = 'Apartamentos'
    mensaje_insercion= ''
    nombre = request.form['inputNombre_aparta']
    descripcion = request.form['inputDescripcion']
    facilidades = request.form['inputFacilidades']
    caracteristicas = request.form['inputCaracteristicas']
    ubicacion = request.form['inputUbicacion']
    precio = request.form['inputPrecio']
    telefono = request.form['inputTelefono']
    correo = request.form['inputCorreo']
    lat="hol"
    longitud="hola"
    lista=[]
    funciona= funcionalidades.Base_Datos() 
    #funciona.crea_Tabla_Apartamentos()
    #funciona.crea_Tabla_Favoritos()


    funciona.inserta_Apartamento(nombre,descripcion,facilidades,caracteristicas,ubicacion,precio,lat,longitud,telefono,correo)
    funciona.verTodo()
    
    #base.inserta_Apartamento("Titulo","Descripcion","facilidades","caracteristicas", "ubicacion","precio","longitud","latitud","tel","correo")
  
    lista.append("Nombre del apartamento: " + nombre)
    lista.append("Descripcion: "+ descripcion)
    lista.append("Caracteristicas: " + caracteristicas)
    lista.append("Facilidades: " + facilidades)
    lista.append("Ubicacion: " + ubicacion)
    lista.append("Precio: " + precio)
    lista.append("Telefono: " +telefono)
    lista.append("Correo:" + correo)
    mensaje_insercion = 'El apartamento ha sido ingresado con exito'
    return render_template('resultado_insercion.html', titulo = titulo_local, lista = lista)

@app.route('/consultas', methods=['POST'])
def consultas():

	funciona= funcionalidades.Base_Datos()
	titulo_local= "Consultas"
	mensaje_insercion = 'La consulta ha sido realizada con exito'
	facilidades = request.form['inputFacilidades']
	caracteristicas = request.form['inputCaracteristicas']
	precio = request.form['inputPrecio']
	ubicacion = request.form['inputUbicacion']
	pOrden= request.form['inputMayor_menor']
	
	
	
	print (facilidades)
	print(caracteristicas)

	resu=funciona.busqueda_Apartamentos(facilidades,caracteristicas,ubicacion,precio,pOrden)
	print(funciona.busqueda_Apartamentos(facilidades,caracteristicas,ubicacion,precio,pOrden))
	funciona.verTodo()
       
	contador=0
	lista=[]
	
	
		
	
	
	return render_template('resultado_insercion.1.html', titulo = titulo_local, mensaje = mensaje_insercion,lista=resu)
	
	#return "hola"

if __name__ == '__main__':
	app.run(debug=True)
    


