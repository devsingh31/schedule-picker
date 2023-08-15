class Class:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty

def calculate_total_difficulty(selected_classes):
    total_difficulty = sum(class_obj.difficulty for class_obj in selected_classes)
    return total_difficulty

def is_schedule_manageable(selected_classes, threshold):
    total_difficulty = calculate_total_difficulty(selected_classes)
    return total_difficulty <= threshold

def main():
    classes = [
        Class("ECS020", 4),
        Class("ECS036A", 4),
        Class("ECS036B", 4),
        Class("ECS036C", 4),
        Class("ECS050", 6),
        Class("ECS122A", 7),
        Class("ECS120", 8),
        Class("ECS140A", 7),
        Class("ECS150", 7),
        Class("ECS154A", 8),
        Class("ECS132", 6),

    ]
    
    class_schedule = input("Enter the classes in your schedule (comma-separated): ").split(", ")
    
    selected_classes = [class_obj for class_obj in classes if class_obj.name in class_schedule]
    threshold = 15
    
    if is_schedule_manageable(selected_classes, threshold):
        print("The selected classes are manageable together.")
    else:
        print("The selected classes are not manageable together.")

if __name__ == "__main__":
    main()
