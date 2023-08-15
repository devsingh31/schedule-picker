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
        Class("math", 7),
        Class("English", 6),
        Class("chemistry", 8),
        Class("sociology", 3),
        Class("psychology", 4),
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
