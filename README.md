# Piedra, papel o tijeras

Juego clásico de piedra, papel o tijeras desarrollado en Python con una interfaz gráfica creada con Tkinter.

## Características

- Interfaz gráfica sencilla y fácil de usar.
- Elección entre roca, papel y tijeras.
- Elección aleatoria de la computadora.
- Resultado de cada ronda.
- Marcador para el jugador, la computadora y los empates.
- Botón para reiniciar el marcador.

## Requisitos

- Python 3.10 o superior.
- Tkinter, incluido normalmente en la instalación estándar de Python.

No es necesario instalar paquetes externos.

## Ejecución

Desde la carpeta del proyecto, ejecuta:

```bash
python piedra_papel_tijeras.py
```

En Windows también puedes utilizar:

```bash
py piedra_papel_tijeras.py
```

Se abrirá una ventana con los botones para elegir roca, papel o tijeras.

## Reglas del juego

- La roca gana a las tijeras.
- Las tijeras ganan al papel.
- El papel gana a la roca.
- Si ambos jugadores eligen lo mismo, hay empate.

## Estructura del proyecto

```text
copilot/
├── piedra_papel_tijeras.py  # Código principal del juego y la GUI
├── testDrive.py              # Archivo de pruebas y ejercicios independientes
└── README.md                 # Documentación del proyecto
```

## Tecnologías utilizadas

- Python
- Tkinter
- ttk
- Módulo `random`
