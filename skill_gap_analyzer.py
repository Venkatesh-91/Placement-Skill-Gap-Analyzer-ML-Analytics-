import pandas as pd

# Load dataset
df = pd.read_csv("placement_data.csv")

# Separate placed and unplaced students
placed_students = df[df["Placed"] == 1]
unplaced_students = df[df["Placed"] == 0]

# Skill columns
skill_columns = ["Python", "SQL", "DSA", "ML", "WebDev"]

# Average skill levels
placed_avg = placed_students[skill_columns].mean()
unplaced_avg = unplaced_students[skill_columns].mean()

# Skill gap calculation
skill_gap = placed_avg - unplaced_avg
skill_gap = skill_gap.sort_values(ascending=False)

print("Skill Gap Analysis (Higher = More Important):")
print(skill_gap)

# ---- Personalized Recommendation ----
student_index = 0  # you can change this value
student = df.iloc[student_index]

missing_skills = []

for skill in skill_columns:
    if student[skill] == 0 and placed_avg[skill] > 0.5:
        missing_skills.append(skill)

print("\nRecommended Skills to Improve:")
print(missing_skills)
