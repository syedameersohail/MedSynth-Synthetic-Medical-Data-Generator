import pandas as pd
import numpy as np
from time import time

t1 = time()

def get_illnesses(age, gender):
    # Detailed Age Grouping for illnesses
    if age < 5:
        common_illnesses = illnesses_child
    elif 5 <= age < 12:
        common_illnesses = illnesses_preteen
    elif 12 <= age < 18:
        common_illnesses = illnesses_teen
    elif 18 <= age < 40:
        common_illnesses = illnesses_young_adult
    elif 40 <= age < 60:
        common_illnesses = illnesses_middle_aged
    else:
        common_illnesses = illnesses_elderly

    # Gender-specific illnesses
    if gender == "Male":
        gender_illnesses = illnesses_male
    elif gender == "Female":
        gender_illnesses = illnesses_female
    else:
        gender_illnesses = []  # For simplicity, not assigning gender-specific illnesses for non-binary

    # Combine lists and sample illnesses
    all_illnesses = common_illnesses + gender_illnesses
    num_illnesses = np.random.randint(0, 4)
    sampled_illnesses = np.random.choice(all_illnesses, num_illnesses, replace=False)

    return list(sampled_illnesses)


def get_surgeries(age, gender):
    # Get common surgeries based on age
    if age < 5:
        common_surgeries = illnesses_child
    elif 5 <= age < 12:
        common_surgeries = illnesses_preteen
    elif 12 <= age < 18:
        common_surgeries = illnesses_teen
    elif 18 <= age < 40:
        common_surgeries = illnesses_young_adult
    elif 40 <= age < 60:
        common_surgeries = illnesses_middle_aged
    else:
        common_surgeries = illnesses_elderly

    # Get gender-specific surgeries
    if gender == "Male":
        gender_surgeries = surgeries_male
    elif gender == "Female":
        gender_surgeries = surgeries_female
    else:  # For Non-Binary or Others, we won't assign gender-specific surgeries
        gender_surgeries = []

    # Combine the lists and sample a few surgeries for the patient
    all_surgeries = common_surgeries + gender_surgeries
    num_surgeries = np.random.randint(0, 3)  # 0 to 2 surgeries
    sampled_surgeries = np.random.choice(all_surgeries, num_surgeries, replace=False)

    return list(sampled_surgeries)


def get_medications(illnesses):
    meds = []
    for illness in illnesses:
        meds += medications_for_illnesses.get(illness, [])
    # Remove duplicates
    meds = list(set(meds))
    if not meds:  # Check if meds list is empty
        return []
    num_meds = np.random.randint(1, len(meds) + 1)
    chosen_meds = np.random.choice(meds, num_meds, replace=False)
    return list(chosen_meds)

illnesses_child = ["Colic", "Roseola", "Hand foot mouth disease"]
illnesses_preteen = ["Chickenpox", "Measles", "Mumps", "Asthma"]
illnesses_teen = ["Acne", "Mono", "Bronchitis"]
illnesses_young_adult = ["Type 1 Diabetes", "Hypertension", "Anxiety"]
illnesses_middle_aged = ["Type 2 Diabetes", "Chronic pain", "Arthritis"]
illnesses_elderly = ["Osteoporosis", "Alzheimer's", "Glaucoma", "Parkinson's"]
illnesses_male = ["Prostate cancer", "Testicular cancer", "Male pattern baldness"]
illnesses_female = ["Breast cancer", "Ovarian cancer", "Endometriosis", "Polycystic ovary syndrome"]


# Sample surgeries segregated by age and gender
surgeries_young = ["Tonsillectomy", "Appendectomy", "Hernia repair"]
surgeries_adult_common = ["Gallbladder removal", "C-Section", "Joint replacement", "Laser eye surgery"]
surgeries_elderly = ["Hip replacement", "Knee replacement", "Pacemaker placement"]
surgeries_male = ["Vasectomy"]
surgeries_female = ["Hysterectomy", "Mastectomy", "Tubal ligation"]

# Sample medications aligned with illnesses
medications_for_illnesses = {
    "Chickenpox": ["Acyclovir", "Calamine lotion"],
    "Measles": ["Ribavirin"],
    "Mumps": ["Pain relievers"],
    "Asthma": ["Albuterol", "Levalbuterol", "Prednisone"],
    "Acne": ["Isotretinoin", "Tretinoin"],
    "Hypertension": ["Lisinopril", "Amlodipine", "Losartan"],
    "Type 2 Diabetes": ["Metformin", "Glyburide", "Insulin"],
    "Depression": ["Fluoxetine", "Citalopram", "Sertraline"],
    "Anxiety": ["Diazepam", "Lorazepam", "Clonazepam"],
    "Chronic pain": ["Ibuprofen", "Naproxen", "Acetaminophen"],
    "Arthritis": ["Celecoxib", "Ibuprofen"],
    "Osteoporosis": ["Alendronate", "Ibandronate"],
    "Alzheimer's": ["Donepezil", "Rivastigmine"],
    "Glaucoma": ["Timolol", "Brimonidine"],
    "Parkinson's": ["Levodopa", "Pramipexole"],
    "Prostate cancer": ["Abiraterone", "Enzalutamide"],
    "Testicular cancer": ["Bleomycin", "Etoposide"],
    "Breast cancer": ["Tamoxifen", "Anastrozole"],
    "Ovarian cancer": ["Bevacizumab", "Olaparib"],
    "Endometriosis": ["Leuprorelin", "Danazol"],
    "Polycystic ovary syndrome": ["Clomiphene", "Metformin"],
    "Male pattern baldness": ["Minoxidil", "Finasteride"]
}

# Sample allergies
allergies_list = ["Pollen", "Dust mites", "Mold", "Pet dander", "Insect stings", "Latex", "Medications", "Foods (e.g., peanuts, shellfish)"]

# Generate allergies for patients
def get_allergies():
    num_allergies = np.random.randint(0, 4)  # 0 to 3 allergies
    sampled_allergies = np.random.choice(allergies_list, num_allergies, replace=False)
    return list(sampled_allergies)

#--------------------------------------------------------------------------
sample_size = 100000
patient_profiles_df_faker = pd.read_csv('patient_profiles.csv')

# Generate illnesses for all patients
previous_illnesses_list = [get_illnesses(age, gender) for age, gender in zip(patient_profiles_df_faker["age"], patient_profiles_df_faker["gender"])]


# Generate surgeries for all patients
surgeries_list = [get_surgeries(age, gender) for age, gender in zip(patient_profiles_df_faker["age"], patient_profiles_df_faker["gender"])]


# Generate medications based on illnesses
medications_list = [get_medications(illnesses) for illnesses in previous_illnesses_list]


allergies_data = [get_allergies() for _ in range(sample_size)]

patient_ids = list(patient_profiles_df_faker["patient_id"])

# Creating the Medical History DataFrame
medical_history_df = pd.DataFrame({
    "patient_id": patient_ids,
    "previous_illnesses": previous_illnesses_list,
    "surgeries": surgeries_list,
    "medications": medications_list,
    "allergies": allergies_data
})

# Displaying the first few rows of the Medical History DataFrame
medical_history_df.to_csv('medical_history.csv', index=False)

t2 = time()
print(f"Dataframe saved, python took {t2-t1} seconds for execution of scripts")

