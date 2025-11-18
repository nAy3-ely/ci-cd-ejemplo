 Proyecto de Ejemplo con CI/CD en GitHub Actions

Este proyecto demuestra una implementación completa de un flujo de **Integración Continua (CI)** utilizando **GitHub Actions** en un entorno Python.  
Incluye configuración automática del entorno, ejecución de pruebas, generación de reportes de cobertura, construcción del paquete y publicación de artefactos generados durante el pipeline.

Su objetivo es servir como plantilla o referencia para proyectos Python que requieran automatización, calidad y buenas prácticas desde el inicio.

---

## Badges del Proyecto

![CI](https://img.shields.io/github/actions/workflow/status/nAy3-ely/ci-cd-ejemplo/ci.yml?label=CI)
![Python](https://img.shields.io/badge/Python-3.10_3.11-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Funcionalidades del Proyecto

- Configuración automática del entorno Python.
- Instalación de dependencias desde `requirements.txt`.
- Ejecución de pruebas unitarias con **pytest**.
- Análisis de cobertura de código con **coverage**.
- Construcción del paquete distribuible en formato `.whl` y `.tar.gz`.
- Publicación de artefactos generados durante el pipeline.
- Ejecución simultánea en múltiples versiones de Python mediante matrices.

---

## Pipeline de CI (GitHub Actions)

El archivo `.github/workflows/ci.yml` ejecuta automáticamente:

1. Descarga del repositorio.
2. Configuración de Python (3.10 y 3.11).
3. Instalación de dependencias.
4. Ejecución de pruebas unitarias.
5. Generación del archivo de cobertura `coverage.xml`.
6. Publicación del reporte como artifact.
7. Construcción del paquete (`dist/`).
8. Publicación del paquete como artifact.

Esto garantiza calidad y estabilidad en cada cambio enviado al repositorio.

---

## Estructura del Proyecto

```plaintext
ci-cd-ejemplo/
│── src/
│   └── app/
│       └── calculator.py
│
│── tests/
│   └── test_calculator.py
│
│── .github/
│   └── workflows/
│       └── ci.yml
│
│── pyproject.toml
│── requirements.txt
│── README.md
│── .gitignore
```
