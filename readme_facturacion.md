# README - Sistema de Facturación de Alquiler de Equipos

## Descripción
Sistema de facturación en consola desarrollado en Python para **alquiler de equipos por días**, con validaciones, descuentos, ajustes según ubicación y registro de múltiples clientes.

---

## Funcionalidades

- Registro automático de **ID de cliente**.
- Solicita **nombre, teléfono y email** con validaciones.
- Alquiler por **días iniciales** y opción de **días adicionales** con descuento acumulativo hasta 20%.
- Ajustes según ubicación del alquiler:
  - Local físico: **-5%**
  - Dentro de la ciudad: precio normal
  - Fuera de la ciudad: **+5%**
- Muestra **factura completa** en pantalla.
- Permite registrar **varios clientes consecutivos**.
- Mantiene la consola abierta hasta que el usuario presione ENTER.

---

## Validaciones

| Campo               | Restricciones |
|---------------------|---------------|
| Nombre              | Letras y espacios, 3–30 caracteres, normalizado con mayúscula inicial |
| Teléfono            | 10 dígitos, empieza con 3, solo números (Colombia) |
| Email               | Min 6 caracteres, formato `algo@dominio.com`, dominio mínimo 2 letras |
| Cantidad de equipos | Mínimo 2 |
| Días iniciales      | Mínimo 1 |
| Días adicionales    | Descuento 2% por día, máximo acumulado 20% |

---

## Cómo usar

### Con Python
```bash
python app.py
```

### Como ejecutable `.exe`
1. Instalar PyInstaller:  
```bash
pip install pyinstaller
```

2. Generar `.exe` desde la carpeta del proyecto:  
```bash
pyinstaller --onefile --console app.py
```

3. Ejecutable generado en `dist\app.exe`.

> La consola se mantendrá abierta hasta presionar ENTER.

---

##  Autor
**Diego Quevedo** – Sistema de facturación de alquiler de equipos en Python.

