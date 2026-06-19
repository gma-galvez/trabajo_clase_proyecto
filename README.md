TAREA 3.0 - Pipeline de CI/CD con GitHub Actions y Docker
🚀 Resumen del Proyecto
Este repositorio alberga una aplicación web dinámica desarrollada con el micro-framework Flask (Python 3.12) y diseñada con una interfaz responsiva basada en Bootstrap 5. La funcionalidad central del sistema es un Conversor de Temperatura Inteligente (Celsius a Fahrenheit), el cual sirve como base para implementar un ecosistema moderno de Integración y Despliegue Continuos (CI/CD).

El enfoque principal de la práctica es la automatización del ciclo de vida del software: validación del código mediante pruebas unitarias con pytest, empaquetado de la aplicación en un contenedor optimizado con Docker y la distribución automática del artefacto hacia GitHub Container Registry (GHCR) mediante flujos de trabajo automatizados.

💻 Stack Tecnológico
Core: Python 3.12 & Flask (procesamiento y renderizado del lado del servidor)

Frontend: Bootstrap 5 (interfaz fluida con componentes visuales modernos y estilizados)

Testing: Pytest 8.x (aseguramiento de calidad y validación de lógica de negocio)

DevOps & Entornos: Docker (python:3.12-alpine para garantizar imágenes ligeras y seguras)

Automatización: GitHub Actions (Pipeline de CI/CD) & GHCR (Almacenamiento de imágenes de contenedor)

📂 Organización del Código
El proyecto sigue una estructura limpia y estandarizada para facilitar el mantenimiento y la ejecución de los pipelines:

Plaintext
Tarea3.0/
├── .github/
│   └── workflows/
│       └── python-application.yml     # Configuración del pipeline de integración y despliegue continuo
├── app.py                             # Servidor web y lógica principal de la aplicación Flask
├── test_app.py                        # Pruebas unitarias para la validación del conversor
├── requirements.txt                   # Manifiesto de dependencias del entorno Python
├── Dockerfile                         # Configuración y pasos para compilar la imagen del contenedor
└── README.md                          # Documentación técnica del repositorio