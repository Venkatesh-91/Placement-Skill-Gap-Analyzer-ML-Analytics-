import pandas as pd
import random

num_students = 500

# Define all skills required for each role
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

# Flatten all skills into a single list and remove duplicates
all_skills = list(set(skill for skills in role_skills.values() for skill in skills))

# Base features
data = {
    "CGPA": [],
    "Backlogs": [],
    "Internship": [],
    "Projects": [],
    "Certifications": [],
    "Placed": []
}

# Add all skills as columns
for skill in all_skills:
    data[skill] = []

# Generate student data
for _ in range(num_students):
    cgpa = round(random.uniform(5.5, 9.5), 2)
    backlogs = random.choice([0, 0, 0, 1, 1, 2])
    internship = random.choice([0, 1])
    projects = random.randint(0, 5)
    certifications = random.randint(0, 4)

    # Randomly assign skills 0 or 1
    student_skills = {skill: random.choice([0, 1]) for skill in all_skills}

    # Simple placement score calculation (you can adjust weights)
    placement_score = (
        cgpa * 0.4 +
        sum(student_skills[skill] for skill in ['Python', 'SQL', 'DSA', 'ML'] if skill in student_skills) +
        internship * 2 +
        projects * 0.5 -
        backlogs * 1
    )

    placed = 1 if placement_score > 7 else 0

    # Append data
    data["CGPA"].append(cgpa)
    data["Backlogs"].append(backlogs)
    data["Internship"].append(internship)
    data["Projects"].append(projects)
    data["Certifications"].append(certifications)
    data["Placed"].append(placed)

    for skill in all_skills:
        data[skill].append(student_skills[skill])

# Create DataFrame and save
df = pd.DataFrame(data)
df.to_csv("placement_data.csv", index=False)
print("Dataset created successfully with all role-specific skills!")
