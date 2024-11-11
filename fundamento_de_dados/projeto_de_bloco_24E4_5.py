import uuid
import datetime as dt
from enum import Enum

class Status(Enum):
    """Enumeração dos possíveis estados de uma tarefa."""
    TODO = 1    # Tarefa a ser feita
    DOING = 2   # Tarefa em andamento
    DONE = 3    # Tarefa concluída

class Urgency(Enum):
    """Enumeração dos níveis de urgência de uma tarefa."""
    LOW = 1     # Baixa urgência
    MEDIUM = 2  # Média urgência
    HIGH = 3    # Alta urgência

class Task: 
    """
    Classe que representa uma tarefa individual no sistema.
    
    Atributos:
        id (uuid): Identificador único da tarefa
        description (str): Descrição detalhada da tarefa
        status (Status): Estado atual da tarefa (TODO, DOING, DONE)
        urgency (Urgency): Nível de urgência da tarefa (LOW, MEDIUM, HIGH)
        created_at (datetime): Data e hora de criação da tarefa
    """
    
    def __init__(self, description: str = "", status: Status = Status.TODO, urgency: Urgency = Urgency.LOW):
        """
        Inicializa uma nova tarefa com os atributos fornecidos.
        
        Args:
            description (str): Descrição da tarefa (padrão: "")
            status (Status): Estado inicial da tarefa (padrão: Status.TODO)
            urgency (Urgency): Nível de urgência da tarefa (padrão: Urgency.LOW)
        """
        self.id = uuid.uuid1()
        self.description = description
        self.status = status
        self.urgency = urgency
        self.created_at = dt.datetime.now()    
        return

    def update_Status(self, newStatus: Status) -> None:
        """
        Atualiza o status de uma tarefa.
        
        Args:
            newStatus (Status): Novo status a ser atribuído à tarefa
        """
        self.status = newStatus
        return

    def __str__(self) -> str:
        """
        Retorna uma representação em string formatada da tarefa.
        
        Returns:
            str: String formatada contendo os detalhes da tarefa
        """
        status_symbols = {
            Status.TODO: "[ ]",
            Status.DOING: "[~]",
            Status.DONE: "[x]"
        }
        
        return (
            f"{status_symbols[self.status]} "
            f"[{self.urgency.name}] "
            f"ID: {self.id} "
            f"{self.description:<50} "
            f"(Created: {self.created_at.strftime('%Y-%m-%d %H:%M')})"
        )

class TaskList:
    """
    Classe que gerencia uma lista de tarefas.
    
    Atributos:
        tasks (list): Lista contendo objetos do tipo Task
    """
    
    def __init__(self, tasks = None):
        """
        Inicializa uma nova lista de tarefas.
        
        Args:
            tasks (list, opcional): Lista inicial de tarefas. Se None, cria uma lista vazia.
        """
        if tasks:
            self.tasks = tasks
        else: 
            self.tasks = []
        return 

    def filter_on_status(self, status: Status):
        """
        Filtra as tarefas com base no status fornecido.
        
        Args:
            status (Status): Status pelo qual filtrar as tarefas
            
        Returns:
            list: Lista de tarefas que correspondem ao status especificado
        """
        return list(filter(lambda t: t.status == status, self.tasks))
    
    def remove_task_by_id(self, id: uuid) -> None:
        """
        Remove uma tarefa da lista com base em seu ID.
        
        Args:
            id (uuid): ID da tarefa a ser removida
        """
        self.tasks = list(filter(lambda t: t.id != id, self.tasks))
        return
    
    def add_task(self, task: Task) -> None:
        """
        Adiciona uma nova tarefa à lista.
        
        Args:
            task (Task): Objeto Task a ser adicionado à lista
        """
        self.tasks.append(task)
        return

    def __str__(self) -> str:
        """
        Retorna uma representação em string formatada da lista de tarefas.
        
        Returns:
            str: String formatada contendo todas as tarefas organizadas por status
        """
        if not self.tasks:
            return "No tasks found!"
        
        output = [
            "\n" + "=" * 100,
            "Task Management System".center(100),
            f"Total Tasks: {len(self.tasks)}".center(100),
            "=" * 100 + "\n"
        ]
        
        for status in Status:
            status_tasks = self.filter_on_status(status)
            if status_tasks:
                output.append(f"\n{status.name} ({len(status_tasks)} tasks)")
                output.append("-" * 100)
                for i, task in enumerate(status_tasks, 1):
                    output.append(f"{i:2d}. {task}")
        
        return "\n".join(output)


def print_menu():
    """
    Exibe o menu de opções disponíveis para o usuário.
    """

    print(''' 
    \n=== Menu de Opções ===
    \r1. Adicionar Nova Tarefa
    \r2. Listar Tarefas
    \r3. Marcar Tarefa como Concluída
    \r4. Remover Tarefa
    \r0. Sair
    \r====================
    ''')


def get_task_info():
    """
    Solicita informações ao usuário para criar uma nova tarefa.
    
    Returns:
        tuple: Descrição, status e urgência da tarefa
    """
    description = input("Digite a descrição da tarefa: ")
    
    print("\nSelecione o status inicial:")
    for status in Status:
        print(f"{status.value}. {status.name}")
    status = Status(int(input("Status: ")))
    
    print("\nSelecione a urgência:")
    for urgency in Urgency:
        print(f"{urgency.value}. {urgency.name}")
    urgency = Urgency(int(input("Urgência: ")))
    
    return description, status, urgency


def main():
    """
    Função principal que executa o loop do programa e gerencia as operações.
    """
    task_list = TaskList()
    
    while True:
        print_menu()
        option = input("Escolha uma opção: ")
        
        if option == "1":
            # Adicionar tarefa
            desc, status, urg = get_task_info()
            task_list.add_task(Task(desc, status, urg))
            print("Tarefa adicionada com sucesso!")
            
        elif option == "2":
            # Listar tarefas
            print(task_list)
            
        elif option == "3":
            # Marcar como concluída
            print(task_list)
            task_id = input("Digite o ID da tarefa a ser concluída: ")
            for task in task_list.tasks:
                if str(task.id) == task_id:
                    task.update_Status(Status.DONE)
                    print("Tarefa marcada como concluída!")
                    break
            
        elif option == "4":
            # Remover tarefa
            print(task_list)
            task_id = input("Digite o ID da tarefa a ser removida: ")
            task_list.remove_task_by_id(uuid.UUID(task_id))
            print("Tarefa removida com sucesso!")
            
        elif option == "0":
            print("Programa finalizado!")
            break
            
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()