from flask import Flask, Blueprint, render_template, request, jsonify

# Crear la app Flask
app = Flask(__name__)

# Definir el Blueprint
calculator_bp = Blueprint('calculator_bp', __name__)

# Ruta para la raíz (con formulario HTML)
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para procesar el cálculo (POST request)
@calculator_bp.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Obtener datos del formulario
        category = request.form.get("category").lower()
        base_amount_usd = float(request.form.get("base_amount_usd"))
        exchange_rate = float(request.form.get("exchange_rate", 3.77))  # Default exchange rate

        penalty_percentage = {
            'a': 5,
            'b': 7,
            'c': 9,
            'd': 12,
            'e': 15
        }

        # Validar categoría
        if category not in ['a', 'b', 'c', 'd', 'e']:
            return render_template('index.html', error="Invalid category")

        # Validar monto base
        if base_amount_usd <= 0:
            return render_template('index.html', error="Invalid base amount in dollars")

        # Convertir monto base a soles
        amount_soles = base_amount_usd * exchange_rate

        # Calcular la penalidad
        penalty = amount_soles * penalty_percentage.get(category, 0) / 100

        # Calcular monto total a pagar
        amount_to_pay = amount_soles + penalty

        # Mostrar los resultados en el HTML
        return render_template('index.html', category=category.upper(), amount_soles=round(amount_soles, 2),
                               penalty=round(penalty, 2), amount_to_pay=round(amount_to_pay, 2))

    except Exception as e:
        return render_template('index.html', error="An error occurred: " + str(e))

# Registrar el blueprint
app.register_blueprint(calculator_bp)

if __name__ == '__main__':
    # Correr la app
    app.run(debug=True)
