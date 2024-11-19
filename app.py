from flask import Flask, Blueprint, render_template, request, jsonify

app = Flask(__name__)

calculadora_bp = Blueprint('calculadora_bp', __name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@calculadora_bp.route('/calcular', methods=['POST'])
def calcular():
    try:
        categoria = request.form.get("categoria").lower()
        monto_base_usd = float(request.form.get("monto_base_usd"))
        tipo_cambio = float(request.form.get("tipo_cambio", 3.77))

        porcentaje_penalidad = {
            'a': 5,
            'b': 7,
            'c': 9,
            'd': 12,
            'e': 15
        }

        if categoria not in ['a', 'b', 'c', 'd', 'e']:
            return render_template('index.html', error="Categoría inválida")

        if monto_base_usd <= 0:
            return render_template('index.html', error="Monto base en dólares inválido")

        monto_soles = monto_base_usd * tipo_cambio
        penalidad = monto_soles * porcentaje_penalidad.get(categoria, 0) / 100
        monto_a_pagar = monto_soles + penalidad

        return render_template('index.html', categoria=categoria.upper(), monto_soles=round(monto_soles, 2),
                             penalidad=round(penalidad, 2), monto_a_pagar=round(monto_a_pagar, 2))

    except Exception as e:
        return render_template('index.html', error="Ocurrió un error: " + str(e))

app.register_blueprint(calculadora_bp)

if __name__ == '__main__':
    app.run(debug=True)
