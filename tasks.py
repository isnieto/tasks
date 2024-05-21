class TaskManager:
    def __init__(self):
        self.pending_tasks = {}
        self.done_tasks = {}
        self.deleted_tasks = {}

    def add_task(self, id, description):
        self.pending_tasks[id] = description

    def modify_task(self, id, new_description):
        if id in self.pending_tasks:
            self.pending_tasks[id] = new_description
        elif id in self.done_tasks:
            self.done_tasks[id] = new_description

    def delete_task(self, id):
        if id in self.pending_tasks:
            self.deleted_tasks[id] = self.pending_tasks.pop(id)
        elif id in self.done_tasks:
            self.deleted_tasks[id] = self.done_tasks.pop(id)

    def mark_task_done(self, id):
        if id in self.pending_tasks:
            self.done_tasks[id] = self.pending_tasks.pop(id)
            
            
            
def main():
    
    # print(f" Ha escogido opción: {input_string}")
    input_string = input("Por favor, introduzca la acción que desear realizar:\n [1]Añadir nueva tarea.\n [2]Modificar tarea.\n [3]Borrar Tarea.\n")
    manager = TaskManager()
    task_id = 0
    
    while True:
        if (input_string == '1'):
            
            task_name = input("Por favor, introduzca la tarea: ")
            # Crea nueva tarea
            manager.add_task(task_id, task_name)
            print(f'La tarea {manager.pending_tasks[task_id]} ha sido añadida.\n')
            
            # Print all tasks in pending_tasks
            contador = 1
            print("La lista de tareas pendientes es la siguiente:|n")
            for id, description in manager.pending_tasks.items():
                print(f'{contador}. {description}')
                contador +=1
            print("\n")

            task_id += 1
            input_string = 0
                    
        elif (input_string == '2'):
            name = input("¿Qué tarea desea modificar?\n")
        
        elif (input_string == '3'):
            name = input("¿Qué tarea desea borrar?\n")
        
        else:
            input_string = input("Por favor, que desear realizar a continuación:\n [1]Añadir una nueva tarea.\n [2]Modificar una tarea pendiente.\n [3]Borrar una tarea.\n")
    


if __name__ == "__main__":

  main()