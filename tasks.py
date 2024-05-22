class TaskManager:
    def __init__(self):
        self.tareas_pendientes = {}
        self.tareas_hechas = {}
        self.tareas_borradas = {}

    def crear_tarea(self, id, description):
        self.tareas_pendientes[id] = description

    def modificar_tarea(self, id, nueva_descripcion):
        if id in self.tareas_pendientes:
            self.tareas_pendientes[id] = nueva_descripcion
        elif id in self.tareas_hechas:
            self.tareas_hechas[id] = nueva_descripcion

    def borrar_tarea(self, id):
        if id in self.tareas_pendientes:
            self.tareas_borradas[id] = self.tareas_pendientes.pop(id)
        elif id in self.tareas_hechas:
            self.tareas_borradas[id] = self.tareas_hechas.pop(id)

    def finalizar_tarea(self, id):
        if id in self.tareas_pendientes:
            self.tareas_hechas[id] = self.tareas_pendientes.pop(id)
            
            
            
def main():
    
    # print(f" Ha escogido opción: {input_string}")
    input_string = input("Por favor, introduzca la acción que desear realizar:\n [1]Añadir nueva tarea.\n [2]Modificar tarea.\n [3]Borrar tarea.\n [4]Cerrar tarea.\n ")
    manager = TaskManager()
    tarea_id = 0
    
    while True:
        if (input_string == '1'):
            
            task_name = input("Por favor, introduzca la tarea: ")
            # Crea nueva tarea
            manager.crear_tarea(tarea_id, task_name)
            print(f'La tarea "{manager.tareas_pendientes[tarea_id]}" ha sido añadida.\n')
            
            # Print all tasks in tareas_pendientes
            counter = 1
            print("La lista de tareas pendientes es la siguiente:\n")
            for id, description in manager.tareas_pendientes.items():
                print(f'{counter}. {description}')
                counter +=1
            print("\n")

            tarea_id += 1
            input_string = 0
                    
        elif (input_string == '2'):
            print("¿Qué tarea desea modificar?\n")
            counter = 1
            tareas_list = {}
            for id, description in manager.tareas_pendientes.items():
                print(f'{counter}. {description}')
                tareas_list[counter] = id
                counter +=1
            print("\n")
            opcion = int(input("Elija el número: \n"))
            # Delete a task
            if opcion in tareas_list:
                manager.borrar_tarea(tareas_list[opcion])
            else:
                print("Invalid option")
        
        elif (input_string == '3'):
            print("¿Qué tarea desea borrar?\n")
            counter = 1
            tareas_list = {}
            for id, description in manager.tareas_pendientes.items():
                print(f'{counter}. {description}')
                tareas_list[counter] = id
                counter +=1
            print("\n")
            opcion = int(input("Elija el número: \n"))
            # borra la tarea
            if opcion in tareas_list:
                manager.borrar_tarea(tareas_list[opcion])
            else:
                print("Invalid option")
                
        elif (input_string == '4'):
            print("¿Qué tarea ha sido finalizada?\n")
            counter = 1
            tareas_list = {}
            for id, description in manager.tareas_pendientes.items():
                print(f'{counter}. {description}')
                tareas_list[counter] = id
                counter +=1
            print("\n")
            opcion = int(input("Elija el número: \n"))
            # borra la tarea
            if opcion in tareas_list:
                manager.borrar_tarea(tareas_list[opcion])
            else:
                print("Invalid option")
                
            
        
        else:
            input_string = input("Por favor, que desear realizar a continuación:\n [1]Añadir una nueva tarea.\n [2]Modificar una tarea pendiente.\n [3]Borrar una tarea.\n [4]Cerrar tarea.\n ")
    


if __name__ == "__main__":

  main()