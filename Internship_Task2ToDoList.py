# TASK: TO DO LIST Application 

import time
from rich.progress import Progress, BarColumn, TextColumn, MofNCompleteColumn
from rich.console import Console
from rich.table import Table
console = Console()
task = [] 
completed_task = []
status = []
def task_table():
    table = Table(title="TO DO LIST APPLICATION")
    table.add_column("S.no#")
    table.add_column("Tasks")
    table.add_column("Status" , justify="center")
    for i in range(len(task)):
        table.add_row(str(i+1) , f"{task[i]}" , f"{status[i]}")
    console.print(table)
def add_task(name , task_status):
    task.append(name)
    status.append(task_status)
def mark_completed(number):
    status[number-1] = "Completed"
    
def show_progress():
    count = 0
    for i in status: 
        if(i == "Completed"):
            count = count + 1 
    total = len(task) 
    if total == 0:
        console.print("[yellow]Add some tasks first to see progress![/yellow]")
        return
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=40, complete_style="green"),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        MofNCompleteColumn(),
    ) as progress:
        
        p_task = progress.add_task("[cyan]Overall Completion", total=total)
        progress.update(p_task, completed=count)
        time.sleep(1) 

def display(): 
    print("Welcome to the TO DO LIST Application...".title())
    while True: 
        user_input = int(input("1. Add Task \n2. Mark as Completed \n3. Show Task \n4. Show Progress \n"))
        if(user_input == 1):
            name = input("Enter the task: ")
            add_task(name , task_status = "Pending")
        elif user_input == 2: 
            task_table()
            number = int(input("Enter the Task number from the table: "))
            mark_completed(number)
        elif user_input == 3: 
            task_table()
            show_progress()
        elif user_input == 4: 
            show_progress()

if __name__ == "__main__": 
    display()