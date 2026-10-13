
print("****** Welcome to Task Manager ******")

tasks = int(input("How many tasks you want to add: "))

while tasks <= 0:
    tasks = int(input("Tasks must be in positive values. Enter again: "))

task_names = []
task_priorities = []

for i in range(tasks):
    task = input("Enter the name of task: ")

    priority = int(input("Assign a priority (1=High, 2=Medium, 3=Low): "))

    while priority > 3 or priority <= 0:
        priority = int(input("You can only assign priority using 1, 2, 3: "))

    task_names.append(task)
    task_priorities.append(priority)


def label(priority):
    if priority == 1:
        return "High"
    elif priority == 2:
        return "Medium"
    elif priority == 3:
        return "Low"


print("****** Your Task Summary ******")

for i in range(tasks):
    print("Task:", task_names[i], "| Priority:", label(task_priorities[i]))


    


                        
        

        
        


