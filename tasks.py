class TaskManager:
    def __init__(self):
        self.tareas_pendientes = {}
        self.tareas_finalizadas = {}
        self.tareas_borradas = {}
        self.tarea_id = 0

    def crear_tarea(self):
        task_name = input("\nPor favor, introduzca una nueva tarea (o 'exit' para salir): ")
        if task_name.lower() == 'exit':
            print("Operación cancelada.\n")
            return
        self.tareas_pendientes[self.tarea_id] = task_name
        print(f'\nLa tarea "{self.tareas_pendientes[self.tarea_id]}" ha sido añadida.\n')
        self.tarea_id += 1

    def modificar_tarea(self):
        if not self.tareas_pendientes:
            print("\n¡Lista vacia!\n")
        else:
            print("\n¿Qué tarea desea modificar?\n")
            tasks_list = self.print_tareas()
            while True:
                option = input("\nElija un número (o 'exit' para salir): ")
                if option.lower() == 'exit':
                    print("Operación cancelada.\n")
                    return
                elif option.isdigit() and int(option) in tasks_list:
                    opcion = int(option)
                    self.tareas_pendientes[tasks_list[opcion]] = input("Por favor, introduzca la nueva descripción: ")
                    print(f'\nLa tarea ha sido modificada: "{self.tareas_pendientes[tasks_list[opcion]]}" .\n')
                    break
                else:
                    print("\nOpción invalida. Por favor, seleccione un número") 
            
            
            
    def borrar_tarea(self):
        if not self.tareas_pendientes:
            print("\n¡Lista vacia!\n")
        else:
            print("\n¿Qué tarea desea borrar?\n")
            tasks_list = self.print_tareas()
            while True:
                option = input("\nElija un número (o 'exit' para salir): ")
                if option.lower() == 'exit':
                    print("Operación cancelada.\n")
                    return
                elif option.isdigit() and int(option) in tasks_list:
                    opcion = int(option)
                    self.tareas_borradas[tasks_list[opcion]] = self.tareas_pendientes.pop(tasks_list[opcion])
                    print(f'\nLa tarea ha sido eliminada.\n')
                    break
                else:
                    print("\nOpción invalida. Por favor, seleccione un número")
            
            

    def finalizar_tarea(self):
        if not self.tareas_pendientes:
            print("\n¡Lista vacia!\n")
        else:
            print("\n¿Qué tarea desea completar?")
            tasks_list = self.print_tareas()
            while True:
                option = input("\nElija un número (o 'exit' para salir): ")
                if option.lower() == 'exit':
                    print("Operación cancelada.\n")
                    return
                elif option.isdigit() and int(option) in tasks_list:
                    opcion = int(option)
                    self.tareas_finalizadas[tasks_list[opcion]] = self.tareas_pendientes.pop(tasks_list[opcion])
                    print(f'\nLa tarea ha sido modificada: "{self.tareas_finalizadas[tasks_list[opcion]]}" .\n')
                    break
                else:
                    print("\nOpción invalida. Por favor, seleccione un número")

    def print_tareas(self):
        counter = 1
        tasks_list = {}
        print("\n")
        for id, description in self.tareas_pendientes.items():
            print(f'{counter}. {description}')
            tasks_list[counter] = id
            counter +=1
        print("\n")
        return tasks_list
    
    def visualizar_tareas(self):
        if not self.tareas_pendientes and not self.tareas_finalizadas:
            print('\n¡Lista vacia!')
        else:
            if self.tareas_pendientes:
                counter = 1
                print('\nTareas pendientes:')
                for tarea_desc in self.tareas_pendientes.items():
                    print(f'{counter} - {tarea_desc[1]}')
                    counter +=1
            if self.tareas_finalizadas:
                counter = 1
                print('\nTareas finalizadas:')
                for tarea_desc in self.tareas_finalizadas.items():
                    print(f'{counter} - {tarea_desc[1]}')
                    counter +=1
        print("\n")           
                
                
def procesar_input(manager):
    
    while True:
        input_string = input("Por favor, seleccione la acción que desea realizar:\n\n [1]Añadir nueva tarea\n [2]Modificar tarea\n [3]Borrar tarea\n [4]Finalizar tarea\n [5]Visualizar tareas\n [6]Abandonar el Taskmanager\n\n Introducir opción: ")
        if (input_string == '1'):
            manager.crear_tarea()
        elif (input_string == '2'):
            manager.modificar_tarea()
        elif (input_string == '3'):
            manager.borrar_tarea()
        elif (input_string == '4'):
            manager.finalizar_tarea()
        elif (input_string == '5'):
            manager.visualizar_tareas()
        elif (input_string == '6'):
            print("Saliendo de la aplicación." )
            break
        else:
            print("\nPor favor, introduzca una opción válida.")
            #input_string = input("Elija un número:\n\n [1]Añadir una nueva tarea\n [2]Modificar una tarea pendiente.\n [3]Borrar una tarea\n [4]Finalizar tarea\n [5]Visualizar tareas\n [6]Abandonar el Taskmanager\n\nIntroducir opción: ")
   
def main():
    manager = TaskManager()
    procesar_input(manager)

if __name__ == "__main__":
    main()