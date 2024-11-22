def main():
    contacts = {}

    def display_menu():
        print("\nAgenda de Contactos:")
        print("1. Buscar un contacto")
        print("2. Insertar un contacto")
        print("3. Actualizar un contacto")
        print("4. Eliminar un contacto")
        print("5. Salir")

    def is_valid_phone(phone):
        return phone.isdigit() and len(phone) <= 11

    while True:
        display_menu()
        try:
            choice = int(input("\nSeleccione una opción: "))
        except ValueError:
            print("Opción inválida. Intente de nuevo.")
            continue

        if choice == 1:  # Buscar un contacto
            name = input("Ingrese el nombre del contacto a buscar: ").strip()
            if name in contacts:
                print(f"\n{name}: {contacts[name]}")
            else:
                print("\nEl contacto no existe.")

        elif choice == 2:  # Insertar un contacto
            name = input("Ingrese el nombre del nuevo contacto: ").strip()
            if name in contacts:
                print("\nEl contacto ya existe.")
            else:
                phone = input("Ingrese el número de teléfono: ").strip()
                if is_valid_phone(phone):
                    contacts[name] = phone
                    print("\nContacto agregado exitosamente.")
                else:
                    print("\nNúmero de teléfono inválido. Asegúrese de que sea numérico y tenga como máximo 11 dígitos.")

        elif choice == 3:  # Actualizar un contacto
            name = input("Ingrese el nombre del contacto a actualizar: ").strip()
            if name in contacts:
                phone = input("Ingrese el nuevo número de teléfono: ").strip()
                if is_valid_phone(phone):
                    contacts[name] = phone
                    print("\nContacto actualizado exitosamente.")
                else:
                    print("\nNúmero de teléfono inválido. Asegúrese de que sea numérico y tenga como máximo 11 dígitos.")
            else:
                print("\nEl contacto no existe.")

        elif choice == 4:  # Eliminar un contacto
            name = input("Ingrese el nombre del contacto a eliminar: ").strip()
            if name in contacts:
                del contacts[name]
                print("\nContacto eliminado exitosamente.")
            else:
                print("\nEl contacto no existe.")

        elif choice == 5:  # Salir
            print("\nGracias por usar la agenda de contactos. ¡Hasta luego!")
            break

        else:
            print("\nOpción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()