import requests

api_url = "http://localhost:7000/api/estudiante/"


def listar_estudiantes():
    response = requests.get(api_url)
    estudiantes = response.json()
    for estudiante in estudiantes:
        print(f"{estudiante['matricula']} {estudiante['nombre']}, {estudiante['carrera']}")
    return estudiantes

def buscar_estudiante(matricula):
    response = requests.get(f"{api_url}{matricula}")
    if response.status_code == 200: 
        return response.json()
    else:
        return f"Error: {response.status_code}. No se encontró el estudiante con esa matricula"

def crear_estudiante(matricula, nombre, carrera):
    data = {
        "matricula": matricula,
        "nombre": nombre,
        "carrera": carrera
    }
    response = requests.post(api_url, json=data)
    return response.json()

def borrar_estudiante(matricula):
    response = requests.delete(f"{api_url}{matricula}")
    return response.json()

if __name__ == "__main__":

    lista = listar_estudiantes()
    print ("Estudiantes listados", lista)

    buscar = buscar_estudiante(10141274)
    print ("Estudiante buscado", buscar)

    crear = crear_estudiante(10141274, "Natasha", "ICC")
    crear2 = crear_estudiante(10141415, "Vladimir", "ICC")
    print ("Estudiante creado", crear, crear2)

    borrar= borrar_estudiante(10141274)
    print ("Estudiante borrado", borrar)