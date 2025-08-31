import itertools
import re

def solicitarNombre(mensaje):
    """Solicita un nombre válido, mínimo 3 y máximo 50 caracteres, solo letras y espacios"""
    while True:
        nombre = input(mensaje).strip()
        nombre = " ".join(nombre.split())  # elimina espacios extras
        if len(nombre) < 3:
            print("⚠️ Nombre muy corto, mínimo 3 caracteres.")
        elif len(nombre) > 50:
            print("⚠️ Nombre muy largo, máximo 50 caracteres.")
        elif not all(c.isalpha() or c.isspace() for c in nombre):
            print("⚠️ Nombre inválido. Solo letras y espacios.")
        else:
            # Normalizar: poner mayúscula inicial en cada palabra
            nombreNormalizado = " ".join(word.capitalize() for word in nombre.split())
            return nombreNormalizado

def solicitarTelefono(mensaje):
    """Solicita un teléfono válido para Colombia (celular de 10 dígitos que empieza con 3)"""
    while True:
        telefono = input(mensaje).strip()
        telefono = re.sub(r'\D', '', telefono)  # elimina cualquier carácter que no sea número
        if len(telefono) != 10:
            print("⚠️ Teléfono inválido. Debe tener 10 dígitos.")
        elif not telefono.startswith("3"):
            print("⚠️ Teléfono inválido para Colombia. Debe empezar con 3.")
        else:
            return telefono

def solicitarEmail(mensaje):
    """Solicita un email válido con mínimo 6 caracteres y formato correcto"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    while True:
        email = input(mensaje).strip()
        if len(email) < 6:
            print("⚠️ Email muy corto, mínimo 6 caracteres.")
        elif not re.match(pattern, email):
            print("⚠️ Email inválido. Debe tener formato ejemplo@dominio.com y solo caracteres válidos.")
        else:
            return email.lower()

# Generador automático de IDs
idClienteGenerator = itertools.count(1)

# Solicitar datos del cliente
nombreCliente = solicitarNombre("Nombre del cliente: ")
telefonoCliente = solicitarTelefono("Teléfono del cliente: ")
emailCliente = solicitarEmail("Email del cliente: ")


def solicitarEntero(mensaje, minimo=None):
    """Solicita un número entero con validación"""
    while True:
        try:
            numero = int(input(mensaje))
            if minimo is not None and numero < minimo:
                print(f"⚠️ El valor debe ser al menos {minimo}.")
                continue
            return numero
        except ValueError:
            print("⚠️ Debes ingresar un número válido.")

def solicitarOpcion():
    """Solicita la opción de alquiler"""
    opciones = {
        1: "En el local físico (-5%)",
        2: "Dentro de la ciudad (normal)",
        3: "Fuera de la ciudad (+5%)"
    }

    print("\nOpciones de alquiler:")
    for key, value in opciones.items():
        print(f"{key}. {value}")

    while True:
        try:
            opcion = int(input("Selecciona una opción (1-3): "))
            if opcion in opciones:
                return opcion, opciones[opcion]
            else:
                print("⚠️ Opción no válida, intenta de nuevo.")
        except ValueError:
            print("⚠️ Debes ingresar un número válido (1-3).")

# Valor base por día
valorDia = 35000

# Programa principal con ciclo
if __name__ == "__main__":
    while True:
        idCliente = next(idClienteGenerator)
        print(f"\n🧾 ID del cliente: {idCliente}")

        equipos = solicitarEntero("Cantidad de equipos a alquilar (mínimo 2): ", minimo=2)
        diasIniciales = solicitarEntero("Número de días iniciales de alquiler: ", minimo=1)
        opcion, descripcion = solicitarOpcion()

        # Cálculo subtotal inicial
        subtotalInicial = equipos * diasIniciales * valorDia

        # Ajustes según opción
        if opcion == 1:  # Local físico
            subtotalInicial *= 0.95
            ajuste = "-5% (alquiler en local físico)"
        elif opcion == 2:  # Dentro de la ciudad
            ajuste = "0% (alquiler dentro de la ciudad)"
        elif opcion == 3:  # Fuera de la ciudad
            subtotalInicial *= 1.05
            ajuste = "+5% (fuera de la ciudad, domicilio)"

        # Días adicionales
        diasAdicionales = solicitarEntero("¿Cuántos días adicionales deseas agregar? (0 si ninguno): ", minimo=0)
        subtotalAdicional = 0
        descuentoAplicado = 0

        if diasAdicionales > 0:
            # Calcular porcentaje acumulativo, máximo 20%
            descuentoAplicado = min(diasAdicionales * 2, 20)

                # Mensaje si se alcanza el descuento máximo
            if descuentoAplicado == 20:
                print("\n⚠️ Se alcanzó el descuento máximo del 20% en días adicionales.")
                if diasAdicionales * 2 > 20:
                    print("👉 Para más días adicionales con descuento deberás iniciar un nuevo alquiler.")

            # Subtotal días adicionales
            precioBaseAdicional = equipos * diasAdicionales * valorDia
            subtotalAdicional = precioBaseAdicional * (1 - descuentoAplicado / 100)

        # Total final
        total = subtotalInicial + subtotalAdicional

        # Mostrar factura completa
        print("\n===== FACTURA COMPLETA =====")
        print(f"Nombre: {nombreCliente}")
        print(f"Teléfono: {telefonoCliente}")
        print(f"Email: {emailCliente}")
        print(f"ID Cliente: {idCliente}")
        print(f"Cantidad de equipos: {equipos}")
        print(f"Días iniciales: {diasIniciales}")
        print(f"Días adicionales: {diasAdicionales}")
        print(f"Opción de alquiler: {descripcion}")
        print(f"Ajuste aplicado: {ajuste}")
        if diasAdicionales > 0:
            print(f"Descuento aplicado en días adicionales: {descuentoAplicado}%")
        print(f"Subtotal inicial: ${subtotalInicial:,.0f}")
        print(f"Subtotal días adicionales: ${subtotalAdicional:,.0f}")
        print(f"TOTAL A PAGAR: ${total:,.0f}")
        print("=============================")

        # Preguntar si desea registrar otro cliente
        continuar = input("\n¿Deseas registrar otra factura? (s/n): ").lower()
        if continuar != "s":
            print("✅ Gracias por usar el sistema de facturación.")
            break
input("\nPresiona ENTER para cerrar el programa...")
