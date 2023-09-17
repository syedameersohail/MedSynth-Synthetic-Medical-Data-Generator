from faker import Faker
import numpy as np
import pandas as pd


def get_exercise_frequency_adjusted(age, smoking, alcohol):
    # Base probabilities
    if age < 30:
        freq_probs = [0.1, 0.15, 0.15, 0.15, 0.15, 0.15, 0.1, 0.05]  # More active
    elif 30 <= age < 60:
        freq_probs = [0.15, 0.15, 0.15, 0.15, 0.15, 0.1, 0.1, 0.05]  # Moderately active
    else:
        freq_probs = [0.2, 0.2, 0.2, 0.15, 0.1, 0.05, 0.05, 0.05]  # Less active

    # Adjustments for smoking and alcohol consumption
    if smoking == "Regular":
        freq_probs = [prob * 1.2 for prob in freq_probs]  # Decrease exercise frequency for regular smokers
    if alcohol == "Regular":
        freq_probs = [prob * 1.2 for prob in freq_probs]  # Decrease exercise frequency for regular drinkers
    
    # Normalize the probabilities to ensure they sum to 1
    freq_probs = [prob / sum(freq_probs) for prob in freq_probs]
    
    return np.random.choice(np.arange(0, 8), p=freq_probs)  # 0 to 7 days a week


# Instantiate a faker generator
fake = Faker()

# Adjusting the sample size to 100,000 records
sample_size = 100000

# Generating realistic patient names using faker
names_faker = [fake.name() for _ in range(sample_size)]

# Regenerate other attributes to match the new sample size
age_mean = 45
age_std = 15

# Age
ages = np.random.normal(age_mean, age_std, sample_size).astype(int)
ages = np.clip(ages, 0, 100)

gender_choices = ['Male', 'Female', 'Non-Binary', 'Others']
gender_probs = [0.48, 0.50, 0.01, 0.01]

# Gender
genders = np.random.choice(gender_choices, sample_size, p=gender_probs)

ethnicity_choices = ['Caucasian', 'African', 'Asian', 'Hispanic', 'Others']
ethnicity_probs = [0.4, 0.2, 0.25, 0.1, 0.05]

# Ethnicity
ethnicities = np.random.choice(ethnicity_choices, sample_size, p=ethnicity_probs)

# Using a list of sample city names to generate the location field
city_names = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", 
    "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", 
    "Fort Worth", "Columbus", "Charlotte", "San Francisco", "Indianapolis", "Seattle", 
    "Denver", "Washington", "Boston", "El Paso", "Nashville", "Detroit", "Oklahoma City", 
    "Portland", "Las Vegas", "Memphis", "Louisville", "Baltimore", "Milwaukee", "Albuquerque", 
    "Tucson", "Fresno", "Sacramento", "Mesa", "Kansas City", "Atlanta", "Omaha", "Raleigh", 
    "Miami", "Long Beach", "Virginia Beach", "Oakland", "Minneapolis", "Tulsa", "Arlington", 
    "Tampa", "New Orleans"
]

# Location (using real city names)
locations_realistic = np.random.choice(city_names, sample_size)

# Smoking Status
smoking_choices = ["Non-smoker", "Occasional", "Regular"]
smoking_probs = [0.6, 0.25, 0.15]
smoking_status = np.random.choice(smoking_choices, sample_size, p=smoking_probs)

# Alcohol Consumption
alcohol_choices = ["Non-drinker", "Occasional", "Regular"]
alcohol_probs = [0.5, 0.3, 0.2]
alcohol_consumption = np.random.choice(alcohol_choices, sample_size, p=alcohol_probs)

# Generate exercise frequency based on age, smoking status, and alcohol consumption
exercise_frequencies_final = [get_exercise_frequency_adjusted(age, smoking, alcohol) 
                              for age, smoking, alcohol in zip(ages, 
                                                               smoking_status, 
                                                               alcohol_consumption)]

# Patient IDs
patient_ids = np.arange(1, sample_size + 1)

# Creating the new DataFrame
patient_profiles_df_faker = pd.DataFrame({
    "patient_id": patient_ids,
    "name": names_faker,
    "age": ages,
    "gender": genders,
    "ethnicity": ethnicities,
    "location": locations_realistic,
    "smoking_status": smoking_status,
    "alcohol_consumption": alcohol_consumption,
    "exercise_frequency": exercise_frequencies_final
})

patient_profiles_df_faker.to_csv('patient_profiles.csv',index=False)
print('data created')