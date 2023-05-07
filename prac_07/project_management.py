import datetime

"""4:22pm 5/7/2023"""
FILE = 'project.txt'


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, '%d/%m/%Y')
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        return f"{self.name}, start: {self.start_date.date()}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"


class ProjectManage:
    def __init__(self):
        self.projects = []

    def load_file(self):
        with open(FILE, 'r') as in_file:
            first_line = in_file.readline()
            for line in in_file:
                name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
                self.projects.append(Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage)))
    def save_projects(self):
        with open(FILE, 'w') as out_file:
            out_file.write("Name	Start Date	Priority	Cost Estimate	Completion Percentage")
            for project in self.projects:
                out_file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.percent_complete}\n")

    def display_projects(self):
        incomplete_projects = []
        for project in self.projects:
            if project.completion_percentage < 100:
                incomplete_projects.append(project)
        completed_projects = []
        for project in self.projects:
            if project.completion_percentage == 100:
                completed_projects.append(project)
        print("Incomplete projects:")
        for project in incomplete_projects:
            print(repr(project))
        print("Completed projects:")
        for project in completed_projects:
            print(repr(project))

    def update_projects(self):
        for i, project in enumerate(self.projects):
            print(f"{i} {repr(project)}")
        try:
            project_choice = int(input("Project choice: "))
            if 0 <= project_choice <= len(self.projects):
                selected_project = self.projects[project_choice]
                print(repr(selected_project))
                new_percent_complete = int(input("New Percentage: "))
                new_priority = int(input("New Priority: "))
                selected_project.completion_percentage = new_percent_complete
                selected_project.priority = new_priority
            else:
                print("Invalid Input")
        except ValueError:
            print("Invalid Input")
        finally:
            project_choice = int(input("Project choice: "))


if __name__ == '__main__':
    user_project = ProjectManage()
    menu = " - (L)oad projects\n - (S)ave projects\n - (D)isplay projects\n - (F)ilter projects by date" \
           "\n - (A)dd new project\n - (U)pdate project\n - (Q)uit"
    print(menu)
    user_choice = input(">>> ").upper()
    while user_choice != "Q":
        if user_choice == "L":
            user_project.load_file()
            print("Projects loaded.")

        elif user_choice == "S":
            user_project.save_projects()

        elif user_choice == "D":
            user_project.display_projects()

        elif user_choice == "F":
            date_str = input("Show projects that start after date (dd/mm/yy): ")
            try:
                date = datetime.datetime.strptime(date_str, '%d/%m/%Y')
                filtered_projects = []
                for project in user_project.projects:
                    if project.start_date.date() == date.date():
                        filtered_projects.append(project)
                for project in filtered_projects:
                    print(repr(project))
            except ValueError:
                print("Invalid date format. Please enter a date in dd/mm/yyyy format.")

        elif user_choice == "A":
            print("Let's add a new project")
            name = input("Name: ")
            start_date = input("Start date (dd/mm/yyyy): ")
            priority = int(input("Priority: "))
            cost_estimate = float(input("Cost estimate: $"))
            completion_percentage = int(input("Percent complete: "))
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            user_project.projects.append(project)

        elif user_choice == "U":
            user_project.update_projects()

        else:
            print("Invalid Input")

        print(menu)
        user_choice = input(">>> ").upper()

    print("Thank you for using custom-built project management software.")
    user_project.save_projects()
