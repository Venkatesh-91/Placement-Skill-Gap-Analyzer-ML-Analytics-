import pandas as pd
import random
num_students = 500
data = {
    "CGPA": [],
    "Backlogs": [],
    "Python": [],
    "SQL": [],
    "DSA": [],
    "ML": [],
    "WebDev": [],
    "Internship": [],
    "Projects": [],
    "Certifications": [],
    "Placed": []
}
for _ in range(num_students):

    cgpa = round(random.uniform(5.5, 9.5), 2)
    backlogs = random.choice([0, 0, 0, 1, 1, 2])
    python_skill = random.choice([0, 1])
    sql_skill = random.choice([0, 1])
    dsa_skill = random.choice([0, 1])
    ml_skill = random.choice([0, 1])
    web_skill = random.choice([0, 1])
    internship = random.choice([0, 1])
    projects = random.randint(0, 5)
    certifications = random.randint(0, 4)
    placement_score = (
        cgpa * 0.4 +
        python_skill * 1 +
        sql_skill * 1 +
        dsa_skill * 1.5 +
        ml_skill * 1 +
        internship * 2 +
        projects * 0.5 -
        backlogs * 1
    )
    placed = 1 if placement_score > 7 else 0
    data["CGPA"].append(cgpa)
    data["Backlogs"].append(backlogs)
    data["Python"].append(python_skill)
    data["SQL"].append(sql_skill)
    data["DSA"].append(dsa_skill)
    data["ML"].append(ml_skill)
    data["WebDev"].append(web_skill)
    data["Internship"].append(internship)
    data["Projects"].append(projects)
    data["Certifications"].append(certifications)
    data["Placed"].append(placed)
df = pd.DataFrame(data)
df.to_csv("placement_data.csv", index=False)

print("Dataset created successfully!")
