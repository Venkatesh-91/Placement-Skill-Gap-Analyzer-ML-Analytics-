import pandas as pd

# Load CSV
df = pd.read_csv("placement_data.csv")

# Define roles and required skills
role_skills = {
    "AI/ML Engineer": ['Python', 'SQL', 'DSA', 'ML'],
    "Data Analyst": ['Power BI', 'Excel', 'Statistics'],
    "Web Developer": ['HTML', 'CSS', 'JavaScript'],
    "Fullstack Developer": ['Python', 'SQL', 'HTML', 'CSS', 'JavaScript'],
    "Data Scientist": ['Python', 'SQL', 'ML', 'Statistics'],
    "AI Engineer": ['Python', 'ML', 'DL', 'NLP'],
    "ML Engineer": ['Python', 'ML', 'DSA', 'Statistics'],
    "Backend Developer": ['Python', 'SQL', 'API', 'Database'],
    "Frontend Developer": ['HTML', 'CSS', 'JavaScript', 'React']
}

# Display roles
roles = list(role_skills.keys())
for i, role in enumerate(roles, 1):
    print(f"{i}. {role}")

# User selects role
role_num = int(input("\nSelect your desired role (enter number 1-9): "))
selected_role = roles[role_num - 1]
print(f"\nYou selected: {selected_role}")

# Get required skills for this role
skill_columns = role_skills[selected_role]

# Filter placed students
placed_students = df[df['Placed'] == 1]

# Calculate average skill scores for placed students
placed_avg = placed_students[skill_columns].mean()
print(f"\nAverage skill scores for placed students in {selected_role}:")
print(placed_avg)

# Function to get user profile
def get_user_profile(required_skills):
    cgpa = float(input("\nEnter your CGPA (out of 10): "))
    certifications = int(input("Enter number of certifications: "))
    projects = int(input("Enter number of projects: "))
    internships = int(input("Enter number of internships: "))

    skills_known = []
    print("\nAnswer the following skills questions with y/n:")
    for skill in required_skills:
        while True:
            ans = input(f"Do you know {skill}? (y/n): ").strip().lower()
            if ans in ['y', 'yes']:
                skills_known.append(skill)
                break
            elif ans in ['n', 'no']:
                break
            else:
                print("Please enter y or n")

    return {
        "cgpa": cgpa,
        "certifications": certifications,
        "projects": projects,
        "internships": internships,
        "skills": skills_known
    }

# Function to calculate skill gaps
def skill_gap_analysis(selected_role, user_skills):
    required_skills = role_skills[selected_role]
    missing_skills = [skill for skill in required_skills if skill not in user_skills]
    return required_skills, missing_skills

# Function to calculate placement probability
def placement_probability(user_profile, required_skills):
    cgpa_score = (user_profile['cgpa'] / 10) * 100
    skill_score = (len(user_profile['skills']) / len(required_skills)) * 100
    proj_intern_score = ((user_profile['projects'] + user_profile['internships']) / 7) * 100  # max 7
    cert_score = (user_profile['certifications'] / 5) * 100  # max 5
    
    # Weighted sum
    probability = (0.4 * cgpa_score +
                   0.3 * skill_score +
                   0.2 * proj_intern_score +
                   0.1 * cert_score)
    
    return round(probability, 2)

# Get user input
user_profile = get_user_profile(skill_columns)

# Analyze skill gaps
required, missing = skill_gap_analysis(selected_role, user_profile['skills'])

# Show summary
print("\n=== Profile Summary ===")
for key, value in user_profile.items():
    print(f"{key.capitalize()}: {value}")

print("\nRequired Skills for this role:", required)
print("Your Skills:", user_profile['skills'])
print("Missing Skills:", missing)

# Calculate placement probability
prob = placement_probability(user_profile, required)
print(f"\nEstimated Placement Probability: {prob}%")

