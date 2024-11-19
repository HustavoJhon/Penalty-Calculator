# Proyecto de Calculadora de Penalidades

Este proyecto es una aplicación web desarrollada con Flask que permite realizar cálculos de penalidades en función de una categoría específica y un monto base en dólares. Es útil para situaciones donde se necesite convertir montos en dólares a soles y aplicar penalidades según distintas categorías.

## Características

- **Interfaz Web Intuitiva**: Un formulario sencillo en la página principal que permite ingresar datos rápidamente.
- **Cálculo Automático**: La aplicación calcula automáticamente la penalidad y el monto total en soles.
- **Conversión de Moneda**: Convierte montos de dólares a soles utilizando un tipo de cambio por defecto o uno proporcionado por el usuario.
- **Soporte para Múltiples Categorías**: Cinco categorías (A, B, C, D, E) con porcentajes de penalidad predefinidos.

## Estructura del Proyecto

- **app.py**: Archivo principal donde se definen las rutas y la lógica de negocio.
- **templates/index.html**: Archivo HTML que contiene el diseño de la interfaz web del usuario.
- **static/**: Carpeta para recursos estáticos como CSS o JavaScript (si es necesario en futuras versiones).

## Cómo Funciona

1. El usuario ingresa una categoría (A, B, C, D o E) y un monto base en dólares en el formulario.
2. La aplicación convierte el monto en dólares a soles utilizando el tipo de cambio especificado (por defecto es 3.77).
3. Se aplica un porcentaje de penalidad según la categoría elegida.
4. El monto total a pagar en soles se muestra en la misma página, junto con la penalidad aplicada.

## Requisitos

- Python 3.7 o superior
- Flask

## Instalación

1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd nombre_del_proyecto
   ```

3. Crea un entorno virtual:
   ```bash
   python -m venv venv
   ```

4. Activa el entorno virtual:
   * En Windows:
     ```bash
     venv\Scripts\activate
     ```
   * En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Instala las dependencias:
   ```bash
   pip install Flask
   ```

## Ejecución

1. Corre la aplicación:
   ```bash
   python app.py
   ```

2. Abre un navegador y ve a `http://127.0.0.1:5000` para usar la aplicación.

## Uso

1. **Ingresar Datos**: Introduce la categoría (A, B, C, D o E) y el monto base en dólares en el formulario.

2. **Calcular**: Presiona "Calcular" para obtener la penalidad y el monto total a pagar en soles.

3. **Resultados**: La aplicación muestra:
   * El monto base convertido a soles.
   * La penalidad calculada en soles.
   * El monto total a pagar en soles.

4. **Manejo de Errores**: Si se ingresa una categoría inválida o un monto base negativo, se mostrará un mensaje de error apropiado.

## Ejemplo de Uso

* **Entrada**: 
  * Categoría = B
  * Monto Base en USD = 100
  * Tipo de Cambio = 3.77
* **Salida**:
  * Monto Base en Soles = 377.0
  * Penalidad = 26.39
  * Monto Total a Pagar = 403.39

## Contribución

Si deseas contribuir, por favor abre un issue o envía un pull request. Todas las contribuciones son bienvenidas.

## Licencia

Este proyecto se distribuye bajo la licencia MIT.
