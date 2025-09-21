

import pandas as pd
from flask import Flask, render_template, request


app = Flask(__name__)

biomarker_data = [
    ("M", "Hemoglobin", 13.5, 17.5, "g/dL"),
    ("F", "Hemoglobin", 12.0, 15.5, "g/dL"),
    ("M", "Total Leucocyte Count (WBC)", 4.0, 11.0, "10^3/uL"),
    ("F", "Total Leucocyte Count (WBC)", 4.0, 11.0, "10^3/uL"),
    ("M", "Platelet Count", 150, 450, "10^3/uL"),
    ("F", "Platelet Count", 150, 450, "10^3/uL"),
    ("M", "Fasting Blood Glucose", 70, 99, "mg/dL"),
    ("F", "Fasting Blood Glucose", 70, 99, "mg/dL"),
    ("M", "Glycated Hemoglobin (HbA1c)", 0, 5.7, "%"),
    ("F", "Glycated Hemoglobin (HbA1c)", 0, 5.7, "%"),
    ("M", "Total Cholesterol", 0, 200, "mg/dL"),
    ("F", "Total Cholesterol", 0, 200, "mg/dL"),
    ("M", "LDL Cholesterol", 0, 100, "mg/dL"),
    ("F", "LDL Cholesterol", 0, 100, "mg/dL"),
    ("M", "HDL Cholesterol", 40, 60, "mg/dL"),
    ("F", "HDL Cholesterol", 50, 60, "mg/dL"), 
    ("M", "Triglycerides", 0, 150, "mg/dL"),
    ("F", "Triglycerides", 0, 150, "mg/dL"),
    ("M", "Serum Creatinine", 0.7, 1.3, "mg/dL"),
    ("F", "Serum Creatinine", 0.6, 1.1, "mg/dL"),
    ("M", "Blood Urea (BUN)", 7, 20, "mg/dL"),
    ("F", "Blood Urea (BUN)", 7, 20, "mg/dL"),
    ("M", "Uric Acid", 3.4, 7.0, "mg/dL"),
    ("F", "Uric Acid", 2.4, 6.0, "mg/dL"),
    ("M", "SGPT (ALT)", 7, 56, "U/L"),
    ("F", "SGPT (ALT)", 7, 56, "U/L"),
    ("M", "SGOT (AST)", 10, 40, "U/L"),
    ("F", "SGOT (AST)", 10, 40, "U/L"),
    ("M", "Alkaline Phosphatase", 44, 147, "U/L"),
    ("F", "Alkaline Phosphatase", 44, 147, "U/L"),
    ("M", "Total Bilirubin", 0.3, 1.2, "mg/dL"),
    ("F", "Total Bilirubin", 0.3, 1.2, "mg/dL"),
    ("M", "Thyroid Stimulating Hormone (TSH)", 0.4, 4.0, "uIU/mL"),
    ("F", "Thyroid Stimulating Hormone (TSH)", 0.4, 4.0, "uIU/mL"),
    ("M", "Vitamin D (25-OH)", 20, 50, "ng/mL"),
    ("F", "Vitamin D (25-OH)", 20, 50, "ng/mL"),
    ("M", "Vitamin B12", 200, 900, "pg/mL"),
    ("F", "Vitamin B12", 200, 900, "pg/mL")
]
biomarkers_df = pd.DataFrame(biomarker_data, columns=["Sex", "Biomarker", "Normal_low", "Normal_high", "Unit"])

# 2. Possible Diseases Data
low_diseases_data = {
    "Hemoglobin": ["Anemia", "Iron deficiency", "Vitamin B12 deficiency"],
    "Total Leucocyte Count (WBC)": ["Leukopenia", "Bone marrow suppression", "Viral infections"],
    "Platelet Count": ["Thrombocytopenia", "Bone marrow disorders", "Viral infections"],
    "Fasting Blood Glucose": ["Hypoglycemia", "Adrenal insufficiency"],
    "HDL Cholesterol": ["Increased cardiovascular risk", "Poor nutrition", "Smoking"],
    "Serum Creatinine": ["Low muscle mass", "Malnutrition"],
    "Blood Urea (BUN)": ["Malnutrition", "Liver disease", "Overhydration"],
    "Thyroid Stimulating Hormone (TSH)": ["Hyperthyroidism", "Pituitary dysfunction"],
    "Vitamin D (25-OH)": ["Vitamin D deficiency", "Malabsorption"],
    "Vitamin B12": ["Vitamin B12 deficiency", "Pernicious anemia", "Malabsorption"]
}
high_diseases_data = {
    "Hemoglobin": ["Polycythemia", "Dehydration", "Heart disease"],
    "Total Leucocyte Count (WBC)": ["Leukocytosis", "Infections", "Inflammation", "Leukemia"],
    "Platelet Count": ["Thrombocytosis", "Bone marrow disorders", "Inflammation"],
    "Fasting Blood Glucose": ["Diabetes", "Cushing syndrome", "Pancreatic disorders"],
    "Glycated Hemoglobin (HbA1c)": ["Poorly controlled diabetes", "Chronic hyperglycemia"],
    "Total Cholesterol": ["Hypercholesterolemia", "Hypothyroidism", "Diabetes"],
    "LDL Cholesterol": ["Atherosclerosis", "Heart disease", "Diabetes"],
    "Triglycerides": ["Hypertriglyceridemia", "Diabetes", "Obesity"],
    "Serum Creatinine": ["Kidney dysfunction", "Dehydration", "Muscle injury"],
    "Blood Urea (BUN)": ["Kidney dysfunction", "Dehydration", "High protein diet"],
    "Uric Acid": ["Gout", "Kidney dysfunction"],
    "SGPT (ALT)": ["Liver damage", "Hepatitis", "Fatty liver"],
    "SGOT (AST)": ["Liver disease", "Heart attack", "Muscle injury"],
    "Alkaline Phosphatase": ["Liver disease", "Bone disorders", "Paget's disease"],
    "Total Bilirubin": ["Liver disease", "Bile duct obstruction", "Hemolytic anemia"],
    "Thyroid Stimulating Hormone (TSH)": ["Hypothyroidism", "Pituitary dysfunction"],
    "Vitamin D (25-OH)": ["Excess supplementation", "Hypercalcemia"],
    "Vitamin B12": ["Excess supplementation", "Liver disease"]
}

# 3. Symptoms Data
low_symptoms_data = {
    "Hemoglobin": ["Fatigue", "Pale skin", "Weakness", "Shortness of breath"],
    "Total Leucocyte Count (WBC)": ["Frequent infections", "Fever", "Mouth sores"],
    "Platelet Count": ["Easy bruising", "Prolonged bleeding", "Petechiae"],
    "Fasting Blood Glucose": ["Shakiness", "Sweating", "Confusion", "Palpitations"],
    "Vitamin D (25-OH)": ["Bone pain", "Muscle weakness", "Fatigue"],
    "Vitamin B12": ["Fatigue", "Numbness or tingling", "Anemia", "Memory problems"]
}
high_symptoms_data = {
    "Hemoglobin": ["Headache", "Dizziness", "Fatigue", "Shortness of Breath"],
    "Total Leucocyte Count (WBC)": ["Fever", "Infections", "Fatigue"],
    "Platelet Count": ["Blood Clots", "Headache", "Weakness"],
    "Fasting Blood Glucose": ["Excessive Thirst", "Frequent Urination", "Fatigue"],
    "Glycated Hemoglobin (HbA1c)": ["Increased Thirst", "Frequent Urination", "Blurred Vision"],
    "Total Cholesterol": ["Chest Pain", "Heart Attack", "Stroke"],
    "LDL Cholesterol": ["Chest Pain", "Heart Attack", "Stroke"],
    "Triglycerides": ["Pancreatitis", "Abdominal Pain", "Fatty Liver"],
    "Serum Creatinine": ["Fatigue", "Swelling", "Nausea", "Decreased Urine Output"],
    "Blood Urea (BUN)": ["Fatigue", "Confusion", "Nausea", "Swelling"],
    "Uric Acid": ["Joint Pain (Gout)", "Swelling", "Redness"],
    "SGPT (ALT)": ["Fatigue", "Nausea", "Abdominal Pain", "Jaundice"],
    "Thyroid Stimulating Hormone (TSH)": ["Fatigue", "Weight Gain", "Cold Intolerance"],
    "Vitamin D (25-OH)": ["Nausea", "Weakness", "Kidney Stones"],
    "Vitamin B12": ["Fatigue", "Weakness", "Numbness", "Cognitive Impairment"]
}

# --- FLASK ROUTES ---

@app.route('/')
def index():
    """Renders the main form page."""
    
    test_names = biomarkers_df['Biomarker'].unique().tolist()
    return render_template('index.html', test_names=test_names)


@app.route('/analyze', methods=['POST'])
def analyze():
    """Processes the form data and displays the analysis results."""
    try:
        # 1. Get user input from the form
        sex = request.form['sex']
        biomarker_name = request.form['test_name']
        result_value = float(request.form['result'])
        unit = request.form['unit']

        user_input = {
            "Sex": "Male" if sex == "M" else "Female",
            "Test": biomarker_name,
            "Result": f"{result_value} {unit}"
        }

        # 2. Find the correct biomarker reference values
        reference = biomarkers_df[(biomarkers_df['Sex'] == sex) & (biomarkers_df['Biomarker'] == biomarker_name)]

        if reference.empty:
            return "Error: Biomarker or Sex not found. Please go back and try again."

        ref_row = reference.iloc[0]
        low_normal = ref_row['Normal_low']
        high_normal = ref_row['Normal_high']

        # 3. Analyze the result
        flag = ""
        analysis_message = ""
        possible_diseases = []
        possible_symptoms = []

        if result_value < low_normal:
            flag = "LOW"
            analysis_message = f"Your result of {result_value} is below the normal range of {low_normal} - {high_normal} {unit}."
            possible_diseases = low_diseases_data.get(biomarker_name, ["No specific diseases listed for this low value."])
            possible_symptoms = low_symptoms_data.get(biomarker_name, ["No specific symptoms listed for this low value."])

        elif result_value > high_normal:
            flag = "HIGH"
            analysis_message = f"Your result of {result_value} is above the normal range of {low_normal} - {high_normal} {unit}."
            possible_diseases = high_diseases_data.get(biomarker_name, ["No specific diseases listed for this high value."])
            possible_symptoms = high_symptoms_data.get(biomarker_name, ["No specific symptoms listed for this high value."])
        
        else:
            flag = "NORMAL"
            mid_point = (low_normal + high_normal) / 2
            deviation = ((result_value - mid_point) / (high_normal - low_normal)) * 100
            
            analysis_message = (f"Your result is within the normal range. "
                                f"It deviates from the ideal midpoint by {deviation:.1f}%.")
            
            if abs(deviation) > 25: # Example threshold for slight concern
                 analysis_message += " While normal, it is on the higher/lower side of the range. Monitoring is advised."
            else:
                 analysis_message += " This is an excellent result, very close to the ideal center of the normal range."


        # 4. Package all results to send to the template
        results = {
            "flag": flag,
            "analysis_message": analysis_message,
            "diseases": possible_diseases,
            "symptoms": possible_symptoms,
            "reference_range": f"{low_normal} - {high_normal} {unit}"
        }

        return render_template('results.html', user_input=user_input, results=results)

    except Exception as e:
        
        return f"An error occurred: {e}. Please ensure you entered a valid number for the result."


if __name__ == '__main__':
    # Runs the Flask app
    app.run(debug=True)