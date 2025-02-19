# Gauss-Jordan-Solver
Resuelve sistemas de ecuaciones lineales utilizando el método de Gauss-Jordan.

# Cómo Usar
## Configuración del Entorno
Antes de ejecutar la aplicación, es recomendable crear un entorno virtual de Python e instalar las dependencias necesarias. Sigue estos pasos:

1. **Crear un entorno virtual** (Ejecuta en la terminal, dentro de la carpeta del proyecto):
   ```sh
   python -m venv .venv
   ```
   ó
   ```sh
   python3 -m venv .venv
   ```
2. **Activar el entorno virtual**:
   - En Windows:
     ```sh
     .venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```sh
     . .venv/bin/activate
     ```
3. **Instalar las dependencias**:
   ```sh
   pip install -r requirements.txt
   ```
   ó
   ```sh
   pip3 install -r requirements.txt
   ```
4. **Ejecutar la aplicación**:
   ```sh
   python app.py
   ```
   ó
   ```sh
   python3 app.py
   ```

## Uso de la Aplicación
En la página de inicio, debes ingresar cuántas variables tiene el sistema que deseas resolver.  
![Página de inicio](static/index.png)

Una vez que hayas ingresado el número de variables, debes llenar el sistema o presionar el botón de "Valores Aleatorios" para llenarlo con números aleatorios.  
![Página de entrada](static/input.png)

Después de completar el sistema y presionar el botón "Resolver", el algoritmo procesará el sistema y mostrará todos los pasos realizados para obtener la solución. Finalmente, mostrará la conclusión con los valores de las variables encontradas.  
![Página de solución](static/result.png)

En caso de que el sistema no tenga solución, el algoritmo lo indicará.  
![Página sin solución](static/noResult.png)