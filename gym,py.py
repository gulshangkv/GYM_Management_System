from IPython.display import clear_output
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sn

def display_menu():
    clear_output(wait=True)
    print("Menu:")
    print("1. Attendance Report")
    print("2. Member's Fitness Goal Distribution Report")
    print("3. Resource Consumption Analysis")
    print("4. Financial Performance Over the Years")
    print("5. User Ratings and Feedback")
    print("6. Workout Plans")
    print("7. Financial Plotting Analysis")
    print("8. Attendance Scatter Report")
    print("9. Diet Plan Tracking")
    print("0. Quit")

def option1():
    fig = plt.figure(figsize=(8, 4), dpi=200)
    dF = pd.read_excel("C:/Users/sahil kumar/OneDrive/Desktop/3rd semester notes and syllabus/python/py/Attendance.xlsx")
    # Extract data for the plot
    x = np.array(dF["Member Name"])
    y = np.array(dF["No. of Days Present"])
    # Define font and label settings
    f1 = {'family': 'sans-serif', 'color': 'black', 'size': 10, 'weight': 'bold'}
    f2 = {'family': 'sans-serif', 'color': 'black', 'size': 10, 'weight': 'bold'}
    f3 = {'family': 'sans-serif', 'color': 'black', 'size': 12, 'weight': 'bold'}
    # Create a custom color map based on the student names
    color_map = {name: plt.cm.tab20c(i % 20) for i, name in enumerate(x)}

    # Create the bar chart with custom colors for each student
    colors = [color_map[name] for name in x]
    plt.bar(x, y, color=colors, label='Attendance')

    # Add labels and title with improved formatting
    plt.xlabel("Student Name", fontdict=f1)
    plt.ylabel("No. of Days Attended", fontdict=f2)
    plt.title("Attendance Report", fontdict=f3)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right', fontsize=8)

    # Show a legend and set its properties
    plt.legend(ncol=3, fontsize=8, loc='upper right')

    # Add grid lines for better reference
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Add a background color to the plot
    plt.gca().set_facecolor('lightgray')

    # Save the plot as an image (optional)
    # plt.savefig('attendance_plot.png', bbox_inches='tight', dpi=200)
    # Show the plot
    plt.tight_layout()
    plt.show()

def option2():
    # Sample data - Fitness goals and their counts
    fitness_goals = ['Weight Loss', 'Muscle Gain', 'General Fitness', 'Endurance', 'Flexibility']
    goal_counts = [30, 20, 25, 15, 10]

    # Create a pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(goal_counts, labels=fitness_goals, autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightgreen', 'lightcoral', 'lightyellow', 'lightpink'])
    plt.title("Member's Fitness Goals Distribution")
    # Display the pie chart
    plt.show()

def option3():
    # Create a figure with a custom size and resolution
    fig = plt.figure(figsize=(10, 6), dpi=200)

    # Read the data from an Excel file
    dF = pd.read_excel("C:/Users/sahil kumar/OneDrive/Desktop/3rd semester notes and syllabus/python/py/Resource_Allocation.xlsx")

    # Extract data for the plot
    x = dF["Resource Name"]
    y1 = dF["Resource Usage"]
    y2 = dF["Condition"]
    y3 = dF["Weight (kg)"]

    # Define font and label settings
    font_title = {'family': 'sans-serif', 'color': 'black', 'size': 16, 'weight': 'bold'}
    font_axes = {'family': 'sans-serif', 'color': 'black', 'size': 12}
    font_legend = {'family': 'sans-serif', 'size': 12}

    # Create the line plot with improved design
    plt.plot(x, y1, color='dodgerblue', linestyle='-', linewidth=2, label='Resource Usage')
    plt.plot(x, y2, color='limegreen', linestyle='--', linewidth=2, label='Condition')
    plt.plot(x, y3, color='tomato', linestyle=':', linewidth=2, label='Weight (kg)')

    # Add labels and title with improved formatting
    plt.xlabel("Resource Name", fontdict=font_axes)
    plt.ylabel("Percentage", fontdict=font_axes)
    plt.title("Resource Consumption Analysis", fontdict=font_title)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right', fontsize=10)

    # Show a legend on the right side and set its properties
    plt.legend(ncol=1, fontsize=12, loc='center right', bbox_to_anchor=(1.15, 0.5))

    # Add grid lines for better reference
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Add a background color to the plot
    plt.gca().set_facecolor('lightgray')

    # Save the plot as an image (optional)
    # plt.savefig('resource_consumption_analysis.png', bbox_inches='tight', dpi=200)

    # Show the plot
    plt.tight_layout()
    plt.show()

def option4():
    # Set the style you want to use
    plt.style.use('ggplot')

    # Sample financial data
    years = ['2020', '2021', '2022', '2023']
    revenue = [1000000, 1200000, 1500000, 1800000]
    expenses = [800000, 900000, 1100000, 1300000]

    # Create a bar chart for financial statement items
    plt.figure(figsize=(10, 6))
    bar_width = 0.35
    index = range(len(years))

    plt.bar(index, revenue, bar_width, label='Revenue', alpha=0.7)
    plt.bar([i + bar_width for i in index], expenses, bar_width, label='Expenses', alpha=0.7)

    plt.title('Financial Performance Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Amount (in lakh rupees)')
    plt.xticks([i + bar_width/2 for i in index], years)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def option5():
    indian_names = ["Aarav", "Aditi", "Arjun", "Diya", "Ishaan", "Kavya", "Neha", "Rohan", "Sanya", "Veer"]
    ratings = [random.randint(1, 5) for _ in indian_names]  # Updated to allow ratings from 1 to 5
    feedbacks = [
        "Great trainer!", 
        "Excellent progress", 
        "Good experience", 
        "Needs improvement", 
        "Highly recommended",
        "Very supportive trainer",
        "Impressive results",
        "A wonderful trainer",
        "Could be better",
        "Best gym experience"
    ]

    # Assign colors based on ratings
    color_map = {
        1: 'red',
        2: 'orange',
        3: 'yellow',
        4: 'limegreen',
        5: 'forestgreen'
    }
    colors = [color_map[rating] for rating in ratings]

    # Create a DataFrame
    data = {'User': indian_names, 'Rating (out of 5)': ratings, 'Feedback': feedbacks, 'Color': colors}
    df = pd.DataFrame(data)

    # Set a custom style
    plt.style.use('ggplot')

    # Create a horizontal bar chart for ratings and feedback
    plt.figure(figsize=(10, 6))

    # Bar chart for ratings
    plt.barh(indian_names, ratings, color=colors, alpha=0.7)
    plt.xlim(0, 5)

    plt.title("User Ratings and Feedback for Gym Trainer & Progress Analysis", fontsize=16)
    plt.xlabel("Rating (out of 5)", fontsize=12)
    plt.grid(axis='x', linestyle='--', alpha=0.7)

    # Display the tabular data
    print("User Feedback and Ratings:")
    print(df)

    # Display the bar chart
    plt.show()

    
def option6():
    # Create a figure with custom size and resolution
    fig = plt.figure(figsize=(10, 6), dpi=200)

    # Read the data from a CSV file
    dF = pd.read_csv("C:/Users/sahil kumar/OneDrive/Desktop/3rd semester notes and syllabus/python/py/ExportCSV.csv")

    # Extract data for the plot
    x = np.array(dF["PlanName"])
    y = np.array(dF["DurationInWeek"])

    # Define font and label settings
    f1 = {'family': 'sans-serif', 'color': 'black', 'size': 16, 'weight': 'bold'}
    f2 = {'family': 'sans-serif', 'color': 'black', 'size': 15, 'weight': 'bold'}
    f3 = {'family': 'sans-serif', 'color': 'black', 'size': 15, 'weight': 'bold'}

    # Create a custom color map with 15 different colors
    colors = plt.cm.tab20c(np.arange(15))

    # Create the bar chart with custom colors
    plt.bar(x, y, color=colors,)

    # Add labels and title with improved formatting
    plt.xlabel("Plan Name", fontdict=f1)  # Increased size and made it bold
    plt.ylabel("Duration in Weeks", fontdict=f2)
    plt.title("Workout Plans", fontdict=f3)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right', fontsize=8)

    # Show a legend and set its properties
    plt.legend(ncol=3, fontsize=8, loc='upper right')

    # Add grid lines for better reference
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Add a background color to the plot
    plt.gca().set_facecolor('lightgray')

    # Save the plot as an image (optional)
    # plt.savefig('workout_plans_plot.png', bbox_inches='tight', dpi=200)

    # Show the plot
    plt.tight_layout()
    plt.show()

def option7():
    # Set the style you want to use
    plt.style.use('ggplot')

    # Sample financial data
    years = ['2020', '2021', '2022', '2023']
    revenue = [1000000, 1200000, 1500000, 1800000]
    expenses = [800000, 900000, 1100000, 1300000]

    f1 = {'family': 'sans-serif', 'color': 'black', 'size': 16, 'weight': 'bold'}
    f2 = {'family': 'sans-serif', 'color': 'black', 'size': 15, 'weight': 'bold'}

    # Create a line chart for financial statement items
    plt.figure(figsize=(10, 6))

    # Plot the revenue as a line
    plt.plot(years, revenue, marker='o', label='Revenue', linestyle='-', markersize=8)

    # Plot the expenses as a line
    plt.plot(years, expenses, marker='o', label='Expenses', linestyle='-', markersize=8)

    plt.title('Financial Performance Over the Years',fontdict=f1)
    plt.xlabel('Year',fontdict=f2)
    plt.ylabel('Amount (in lakh rupees)',fontdict=f2)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.show()

def option8():
    # Create a figure with custom size and resolution
    fig = plt.figure(figsize=(8, 4), dpi=200)

    # Read the data from an Excel file
    dF = pd.read_excel("C:/Users/sahil kumar/OneDrive/Desktop/3rd semester notes and syllabus/python/py/Attendance.xlsx")

    # Extract data for the plot
    x = np.array(dF["Member Name"])
    y = np.array(dF["No. of Days Present"])

    # Define font and label settings
    f1 = {'family': 'sans-serif', 'color': 'black', 'size': 10, 'weight': 'bold'}
    f2 = {'family': 'sans-serif', 'color': 'black', 'size': 10, 'weight': 'bold'}
    f3 = {'family': 'sans-serif', 'color': 'black', 'size': 12, 'weight': 'bold'}

    # Create a custom color map based on the student names
    color_map = {name: plt.cm.tab20c(i % 20) for i, name in enumerate(x)}

    # Create the scatter plot with custom colors for each student
    colors = [color_map[name] for name in x]

    # Add labels and title with improved formatting
    plt.xlabel("Student Name", fontdict=f1)
    plt.ylabel("No. of Days Attended", fontdict=f2)
    plt.title("Attendance Report", fontdict=f3)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right', fontsize=8)

    # Remove the warning by using a single scatter point for the legend
    for name, color in color_map.items():
        plt.scatter([], [], c=[color], label=name, alpha=0.7, edgecolors='k', linewidths=0.5, s=100)

    # Create the scatter plot for the attendance data
    plt.scatter(x, y, c=colors, s=100, alpha=0.7, edgecolors='k', linewidths=0.5)

    # Show a legend and set its properties
    plt.legend(ncol=3, fontsize=8, loc='upper right')

    # Add grid lines for better reference
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Add a background color to the plot
    plt.gca().set_facecolor('lightgray')

    # Save the plot as an image (optional)
    # plt.savefig('attendance_scatter_plot.png', bbox_inches='tight', dpi=200)

    # Show the plot
    plt.tight_layout()
    plt.show()

def option9():
    # Define a dictionary to represent a sample diet plan
    diet_plan = {
        "Breakfast": ["Oatmeal", "Banana", "Milk"],
        "Lunch": ["Grilled Chicken", "Brown Rice", "Broccoli"],
        "Snack": ["Greek Yogurt", "Berries"],
        "Dinner": ["Salmon", "Quinoa", "Asparagus"],
    }

    # Define a custom color palette
    custom_colors = sn.color_palette("pastel")  # Use Seaborn's pastel color palette

    # Function to create a bar chart for the diet plan with custom colors and adjusted legend
    def create_diet_plan_chart(plan, colors):
        meals = list(plan.keys())
        item_counts = [len(items) for items in plan.values()]

        # Create a bar chart with custom colors
        plt.figure(figsize=(8, 6))
        bars = plt.bar(meals, item_counts, color=custom_colors)

        plt.xlabel("Meal")
        plt.ylabel("Number of Items")
        plt.title("Sample Diet Plan")

        # Display a legend with meal categories and corresponding colors
        # Specify the "best" legend position for automatic placement
        plt.legend(bars, meals, title="Meals", loc='best')

        plt.show()

    # Create and display the bar chart with custom colors and "best" legend position
    create_diet_plan_chart(diet_plan, custom_colors)

while True:
    display_menu()
    choice = input("Enter your choice: ")

    match choice:
        case '1':
            option1()
        case '2':
            option2()
        case '3':
            option3()
        case '4':
            option4()
        case '5':
            option5()
        case '6':
            option6()
        case '7':
            option7()
        case '8':
            option8()
        case '9':
            option9()
        case '0':
            print("Goodbye!")
            break
        case _:
            print("Invalid choice. Please select a valid option.")
    
    input("Press Enter to continue...")
