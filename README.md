Un pequeño script que estoy haciendo para ver más rápido las notas de mi U.

## Tabla de Contenidos
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)

## Requisitos
Para poder ejecutar este script, asegúrese de tener instalados los siguientes componentes:
- Python 3.8 o superior
- Google Chrome (o el navegador que vaya a utilizar con Selenium)
- ChromeDriver (o el controlador del navegador correspondiente)
- Poetry para la gestión del entorno y las dependencias

## Instalación
1. **Instalar Python**:
   - Asegúrese de tener Python 3.8 o superior instalado. Puede verificarlo ejecutando:
     ```bash
     python --version
     ```
   - Si no está instalado, descárguelo e instálelo desde [python.org](https://www.python.org/downloads/).

2. **Instalar Poetry**:
   - Ejecuta el siguiente comando para instalar `Poetry`:
     ```bash ( si instaló python desde Microsoft Store cambiar py- por python-)
     (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py - 
                                                                                      
     ```                
   - Agrega `Poetry` a la variable de entorno `PATH`

3. **Configurar el Entorno Virtual con Poetry**:
   - Ejecutar en la consola el comando:
     ```bash
     poetry install

## Uso

1. **Ejecución del script con el Archivo Principal (`main.py`)**:
   - Para ejecutar el script principal verificar que en consola se encuentre la ruta que corresponde al archivo main.py y escribir el siguiente comando:
     
     python main.py  