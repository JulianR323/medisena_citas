from src.cita import CitaMedica
from src.gestion_datos import cargar_citas, guardar_citas

def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN DE CITAS MEDISENA ---")
    print("1. Listar citas")
    print("2. Registrar nueva cita")
    print("3. Consultar total de ingresos proyectados")
    print("4. Salir")

def main():
    citas_guardadas = cargar_citas()

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-4): ").strip()

        if opcion == "1":
            print("\n--- LISTADO DE CITAS MÉDICAS ---")
            if not citas_guardadas:
                print("No hay citas registradas.")
            else:
                for c in citas_guardadas:
                    tipo = "Urgencia" if c["es_urgencia"] else "Programada (15% desc.)"
                    print(f"ID: {c['id_cita']} | Paciente: {c['paciente']} | Especialidad: {c['especialidad']} | Médico: {c['medico_asignado']} | Tipo: {tipo} | Costo Final: ${c['costo_final']}")

        elif opcion == "2":
            print("\n--- REGISTRAR NUEVA CITA ---")
            id_cita = input("Ingrese el ID de la cita (ej: CIT-2026-01): ").strip()
            
            # Validar duplicados de id_cita
            if any(c["id_cita"] == id_cita for c in citas_guardadas):
                print("Error: Ya existe una cita registrada con ese ID.")
                continue

            paciente = input("Nombre completo del paciente: ").strip()
            especialidad = input("Especialidad médica (ej: Medicina General): ").strip()
            medico_asignado = input("Nombre del médico: ").strip()
            
            try:
                costo_consulta = float(input("Costo de la consulta ($): "))
            except ValueError:
                print("Error: El costo debe ser un valor numérico.")
                continue

            urgencia_input = input("¿Es una urgencia? (s/n): ").strip().lower()
            es_urgencia = True if urgencia_input == 's' else False

            nueva_cita = CitaMedica(id_cita, paciente, especialidad, medico_asignado, costo_consulta, es_urgencia)
            citas_guardadas.append(nueva_cita.a_diccionario())
            guardar_citas(citas_guardadas)
            print("¡Cita registrada y guardada exitosamente!")

        elif opcion == "3":
            total_ingresos = sum(c["costo_final"] for c in citas_guardadas)
            print(f"\n--- INGRESOS PROYECTADOS ---")
            print(f"El total de ingresos proyectados es: ${total_ingresos:.2f}")

        elif opcion == "4":
            print("\nSaliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elija un número entre 1 y 4.")

if __name__ == "__main__":
    main()