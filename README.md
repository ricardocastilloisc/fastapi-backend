# FastAPI Shape API

Esta es una aplicación FastAPI que proporciona un endpoint para servir archivos `.obj` de modelos 3D. La API permite a los usuarios acceder a diferentes formas mediante un tipo de forma especificado en la solicitud.

## Descripción

El script principal (`app/main.py`) define una API que:
- Utiliza **CORS** para permitir solicitudes de diferentes orígenes.
- Permite obtener archivos `.obj` de una carpeta específica en el servidor.
- Retorna un error 404 si el archivo solicitado no se encuentra.

## Requisitos

Asegúrate de tener instalado Python 3.7 o superior. También necesitarás tener `pip` para instalar las dependencias.

1. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   ```
2. Activa el entorno virtual:

  En Windows:

   ```bash
   venv\Scripts\activate
   ```
  En macOS/Linux:

   ```bash
   source venv/bin/activate
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

 4. Uso:
   ```bash
   uvicorn app.main:app --reload
   ```
