# Sistema de Gestión para Bodega «Luinto»
**Curso:** Fundamentos de Programación
**Universidad:** UPN Universidad Privada del Norte  
**Autor:** Pedro Jesus Becerra Mucha  
**Docente:** José Carlos García La Riva  

---

Sistema de gestión por consola para la bodega «Luinto». Permite registrar ventas, controlar el stock e inventario y generar reportes diarios, reemplazando el registro manual en cuadernos.

---

## Requisitos

- Python 3.x

---

## Cómo ejecutar

```bash
python main.py
```

---

## Archivos generados

- `bodega.txt` — catálogo de productos (al guardar se crea el archivo txt)
- `ventas_YYYY-MM-DD.txt` — reporte de ventas del día con fecha en el nombre

---

## Generar el ejecutable (.exe)

1. Instalar PyInstaller:
```bash
pip install pyinstaller
```

2. Generar el .exe:
```bash
python -m PyInstaller --onefile --console main.py
```