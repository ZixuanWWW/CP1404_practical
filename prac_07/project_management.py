import datetime
from project import Project


def main():
    MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date" \
           "\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"

    # Load projects from the data file when the program starts
    filename = 'projects.txt'
    projects = load_projects(filename)

    choice = input(f"{MENU}\n>>> ").upper().strip()
    while choice != 'Q':
        if choice == 'L':
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == 'S':
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects_by_date(projects)
        elif choice == 'A':
            add_new_project(projects)
        elif choice == 'U':
            update_project(projects)
        else:
            print("Invalid choice.")
        choice = input(f"{MENU}\n>>> ").upper().strip()
    # save projects to the data file when the user quits.
    save_projects(filename, projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    projects = []
    try:
        in_file = open(filename, 'r')
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            projects.append(Project(parts[0], datetime.datetime.strptime(parts[1], "%d/%m/%Y").date(),
                                    int(parts[2]), float(parts[3]), int(parts[4])))
        print("Projects loaded successfully.")
    except FileNotFoundError:
        print("File not found.")
    return projects


def save_projects(filename, projects):
    try:
        with open(filename, 'w') as file:
            file.write("Name	Start Date	Priority	Cost Estimate	Completion Percentage\n")
            for project in projects:
                file.write(
                    f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}"
                    f"\t{project.priority}\t{project.estimate:.2f}\t{project.completion}\n")
        print("Projects saved successfully.")
    except Exception as exception:
        print(f"Error saving projects: {exception}")


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion < 100]
    completed_projects = [project for project in projects if project.completion == 100]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects, key=lambda x: x.priority):
        print(project)
    print("Completed projects:")
    for project in sorted(completed_projects, key=lambda x: x.priority):
        print(project)


def filter_projects_by_date(projects):
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")

    try:
        filter_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if project.start_date > filter_date]
        for project in sorted(filtered_projects, key=lambda x: x.start_date):
            print(project)
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))

    try:
        start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
        new_project = Project(name, start_date, priority, estimate, completion)
        projects.append(new_project)
        print("New project added successfully.")
    except ValueError:
        print("Invalid date format. Project not added.")


def update_project(projects):
    the_number_of_data = 0
    for data in projects:
        print(f"{the_number_of_data} {data}")
        the_number_of_data += 1

    try:
        choice = int(input("Project choice: "))
        if 0 <= choice < len(projects):
            project = projects[choice]
            new_completion = input(f"New Percentage: ")
            new_priority = input(f"New Priority: ")

            if new_completion:
                project.completion = int(new_completion)
            if new_priority:
                project.priority = int(new_priority)

            print("Project updated successfully.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Project not updated.")


if __name__ == "__main__":
    main()
