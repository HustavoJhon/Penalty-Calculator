from flask import Flask, request, jsonify, render_template, Blueprint

app = Flask(__name__)

# Datos iniciales con estructuras avanzadas
class ContactManager:
    def __init__(self):
        # Lista para nombres de los contactos
        self.lista_nombres = []

        # Diccionario con los detalles del contacto {nombre: (nombre, teléfono, email)}
        self.contactos = {}

        # Conjunto para almacenar intereses únicos
        self.intereses = set()

        # Diccionario para grupos de contactos {grupo: [nombres]}
        self.grupos = {}

    def agregar_contacto(self, nombre, telefono, email, intereses):
        """Agrega un nuevo contacto al sistema."""
        if nombre in self.contactos:
            return {"error": f"El contacto '{nombre}' ya existe."}, 400

        # Crear tupla inmutable del contacto
        contacto = (nombre, telefono, email)

        # Actualizar estructuras
        self.lista_nombres.append(nombre)
        self.contactos[nombre] = contacto
        self.intereses.update(intereses)

        return {"mensaje": f"Contacto '{nombre}' agregado exitosamente."}, 201

    def listar_contactos(self):
        """Devuelve todos los contactos y los intereses únicos."""
        return {
            "contactos": self.contactos,
            "intereses": list(self.intereses)
        }

    def eliminar_contacto(self, nombre):
        """Elimina un contacto por su nombre."""
        if nombre in self.contactos:
            self.lista_nombres.remove(nombre)
            del self.contactos[nombre]
            return {"mensaje": f"Contacto '{nombre}' eliminado exitosamente."}, 200
        return {"error": f"Contacto '{nombre}' no encontrado."}, 404

    def crear_grupo(self, nombre_grupo, contactos):
        """Crea un grupo con contactos seleccionados."""
        if nombre_grupo in self.grupos:
            return {"error": f"El grupo '{nombre_grupo}' ya existe."}, 400

        # Validar contactos existentes
        contactos_validos = [c for c in contactos if c in self.contactos]
        self.grupos[nombre_grupo] = contactos_validos

        return {"mensaje": f"Grupo '{nombre_grupo}' creado con {len(contactos_validos)} contactos."}, 201

    def listar_grupos(self):
        """Lista los grupos creados."""
        return self.grupos


# Instancia del gestor
gestor_contactos = ContactManager()

# Rutas para el manejo de contactos
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contactos/agregar', methods=['POST'])
def agregar_contacto():
    """Agrega un contacto."""
    nombre = request.form.get('nombre')
    telefono = request.form.get('telefono')
    email = request.form.get('email')
    intereses = request.form.get('intereses', '').split(',')

    if not nombre or not telefono or not email:
        return jsonify({"error": "Todos los campos son obligatorios"}), 400

    respuesta, estado = gestor_contactos.agregar_contacto(nombre, telefono, email, intereses)
    return jsonify(respuesta), estado

@app.route('/contactos/listar', methods=['GET'])
def listar_contactos():
    """Lista todos los contactos."""
    return jsonify(gestor_contactos.listar_contactos())


@app.route('/contactos/eliminar/<nombre>', methods=['DELETE'])
def eliminar_contacto(nombre):
    """Elimina un contacto."""
    return jsonify(*gestor_contactos.eliminar_contacto(nombre))


@app.route('/grupos/crear', methods=['POST'])
def crear_grupo():
    """Crea un grupo de contactos."""
    nombre_grupo = request.form.get('nombre_grupo')
    contactos = request.form.getlist('contactos')

    return jsonify(*gestor_contactos.crear_grupo(nombre_grupo, contactos))


@app.route('/grupos/listar', methods=['GET'])
def listar_grupos():
    """Lista todos los grupos creados."""
    return jsonify(gestor_contactos.listar_grupos())


if __name__ == '__main__':
    app.run(debug=True)

