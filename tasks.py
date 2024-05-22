class TaskManager:
    def __init__(self):
        self.tareas_pendientes = {}
        self.tareas_hechas = {}
        self.tareas_borradas = {}
        self.tarea_id = 0

    def crear_tarea(self):
        task_name = input("Por favor, introduzca la tarea: ")
        self.tareas_pendientes[self.tarea_id] = task_name
        print(f'La tarea "{self.tareas_pendientes[self.tarea_id]}" ha sido añadida.\n')
        self.print_tareas()
        self.tarea_id += 1

    def modificar_tarea(self):
        if not self.tareas_pendientes:
            print("Lista vacia")
        else:
            print("¿Qué tarea desea modificar?\n")
            tasks_list = self.print_tareas()
            opcion = int(input("Elija el número: \n"))
            if opcion in tasks_list:
                self.tareas_pendientes[tasks_list[opcion]] = input("Por favor, introduzca la nueva descripción: ")
            else:
                print("Opción invalida.")
            
    def borrar_tarea(self):
        if not self.tareas_pendientes:
            print("Lista vacia")
        else:
            print("¿Qué tarea desea borrar?\n")
            tasks_list = self.print_tareas()
            opcion = int(input("Elija el número: \n"))
            if opcion in tasks_list:
                self.tareas_borradas[tasks_list[opcion]] = self.tareas_pendientes.pop(tasks_list[opcion])
            else:
                print("Opción invalida. Por favor, selectione un número")

    def finalizar_tarea(self):
        if not self.tareas_pendientes:
            print("Lista vacia")
        else:
            print("¿Qué tarea ha sido finalizada?\n")
            tasks_list = self.print_tareas()
            opcion = int(input("Elija el número: \n"))
            if opcion in tasks_list:
                self.tareas_hechas[tasks_list[opcion]] = self.tareas_pendientes.pop(tasks_list[opcion])
            else:
                print("Opción invalida. Por favor, selectione un número")

    def print_tareas(self):
        counter = 1
        tasks_list = {}
        for id, description in self.tareas_pendientes.items():
            print(f'{counter}. {description}')
            tasks_list[counter] = id
            counter +=1
        print("\n")
        return tasks_list

def handle_input(manager):
    
    while True:
        input_string = input("Por favor, introduzca la acción que desear realizar:\n\n [1]Añadir nueva tarea\n [2]Modificar tarea\n [3]Borrar tarea\n [4]Finalizar tarea\n [5]Abandonar el Taskmanager ")
        if (input_string == '1'):
            manager.crear_tarea()
        elif (input_string == '2'):
            manager.modificar_tarea()
        elif (input_string == '3'):
            manager.borrar_tarea()
        elif (input_string == '4'):
            manager.finalizar_tarea()
        elif (input_string == '5'):
            print("Saliendo de la aplicación." )
            break
        else:
            input_string = input("Por favor, que desear realizar a continuación:\n\n [1]Añadir una nueva tarea\n [2]Modificar una tarea pendiente.\n [3]Borrar una tarea\n [4]Finalizar tarea\n [5]Abandonar el Taskmanager ")

def main():
    manager = TaskManager()
    handle_input(manager)

if __name__ == "__main__":
    main()