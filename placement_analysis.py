import pandas as pd

# Load CSV
df = pd.read_csv("placement_data.csv")

# Define roles and their required skills (matching CSV columns)
roles_skills = {
    1: ['Python', 'SQL', 'DSA', 'ML'],           # AI/ML Engineer
    2: ['Python', 'SQL', 'DSA'],                # Data Scientist
    3: ['Python', 'ML', 'DSA'],                 # AI Engineer
    4: ['Python', 'WebDev', 'Projects'],        # Fullstack Developer
    5: ['Python', 'SQL', 'DSA'],                # Backend Developer
    6: ['Python', 'WebDev'],                    # Frontend Developer
    7: ['Python', 'DSA'],                        # ML Engineer
    8: ['Python', 'WebDev', 'Certifications'],  # Data Analyst / BI
    9: ['Python', 'SQL', 'DSA', 'ML']           # AI/ML Researcher
}

# Display roles
roles = [
    "AI/ML Engineer", "Data Scientist", "AI Engineer",
    "Fullstack Developer", "Backend Developer",
    "Frontend Developer", "ML Engineer", "Data Analyst / BI", "AI/ML Researcher"
]

for i, role in enumerate(roles, 1):
    print(f"{i}. {role}")

# User selects role
role_num = int(input("\nSelect your desired role (enter number 1-9): "))
selected_role = roles[role_num - 1]
print(f"\nYou selected: {selected_role}")

# Get relevant skill columns
skill_columns = roles_skills[role_num]

# Filter placed students
placed_students = df[df['Placed'] == 1]

# Calculate average skill scores for placed students
placed_avg = placed_students[skill_columns].mean()

print(f"\nAverage skill scores for placed students in {selected_role}:")
print(placed_avg)
