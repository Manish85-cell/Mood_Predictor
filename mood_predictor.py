import streamlit as st
import pickle
from  joblib import load
from sklearn.preprocessing import LabelEncoder



# Questions dictionary for MCQs
questions = {
    "Q1A": "I found myself getting upset by quite trivial things.",
    "Q2A": "I was aware of dryness of my mouth.",
    "Q3A": "I couldn't seem to experience any positive feeling at all.",
    "Q4A": "I experienced breathing difficulty (eg, excessively rapid breathing, breathlessness in the absence of physical exertion).",
    "Q5A": "I just couldn't seem to get going.",
    "Q6A": "I tended to over-react to situations.",
    "Q7A": "I had a feeling of shakiness (eg, legs going to give way).",
    "Q8A": "I found it difficult to relax.",
    "Q9A": "I found myself in situations that made me so anxious I was most relieved when they ended.",
    "Q10A": "I felt that I had nothing to look forward to.",
    "Q11A": "I found myself getting upset rather easily.",
    "Q12A": "I felt that I was using a lot of nervous energy.",
    "Q13A": "I felt sad and depressed.",
    "Q14A": "I found myself getting impatient when I was delayed in any way (eg, elevators, traffic lights, being kept waiting).",
    "Q15A": "I had a feeling of faintness.",
    "Q16A": "I felt that I had lost interest in just about everything.",
    "Q17A": "I felt I wasn't worth much as a person.",
    "Q18A": "I felt that I was rather touchy.",
    "Q19A": "I perspired noticeably (eg, hands sweaty) in the absence of high temperatures or physical exertion.",
    "Q20A": "I felt scared without any good reason.",
    "Q21A": "I felt that life wasn't worthwhile.",
    "Q22A": "I found it hard to wind down.",
    "Q23A": "I had difficulty in swallowing.",
    "Q24A": "I couldn't seem to get any enjoyment out of the things I did.",
    "Q25A": "I was aware of the action of my heart in the absence of physical exertion (eg, sense of heart rate increase, heart missing a beat).",
    "Q26A": "I felt down-hearted and blue.",
    "Q27A": "I found that I was very irritable.",
    "Q28A": "I felt I was close to panic.",
    "Q29A": "I found it hard to calm down after something upset me.",
    "Q30A": "I feared that I would be 'thrown' by some trivial but unfamiliar task.",
    "Q31A": "I was unable to become enthusiastic about anything.",
    "Q32A": "I found it difficult to tolerate interruptions to what I was doing.",
    "Q33A": "I was in a state of nervous tension.",
    "Q34A": "I felt I was pretty worthless.",
    "Q35A": "I was intolerant of anything that kept me from getting on with what I was doing.",
    "Q36A": "I felt terrified.",
    "Q37A": "I could see nothing in the future to be hopeful about.",
    "Q38A": "I felt that life was meaningless.",
    "Q39A": "I found myself getting agitated.",
    "Q40A": "I was worried about situations in which I might panic and make a fool of myself.",
    "Q41A": "I experienced trembling (eg, in the hands).",
    "Q42A": "I found it difficult to work up the initiative to do things."
}

# Function to display MCQ questions
def display_mcq_questions():
    responses = {}
    response_mapping = {
        "Did not apply to me at all (1)": 1,
        "Applied to me to some degree, or some of the time (2)": 2,
        "Applied to me to a considerable degree, or a good part of the time (3)": 3,
        "Applied to me very much, or most of the time (4)": 4
    }
    
    for question_id, question_text in questions.items():
        response = st.selectbox(
            question_text,
            options=list(response_mapping.keys()),  # Use the keys of the mapping for options
            index=0,  # Default to the first option
            key=question_id
        )
        responses[question_id] = response_mapping[response]  # Get the corresponding score
    return responses

# Display TIPI questions
def display_tipi_questions():
    tipi_responses = {}
    tipi_questions = {
    "TIPI1": "Extraverted, enthusiastic.",
    "TIPI2": "Critical, quarrelsome.",
    "TIPI3": "Dependable, self-disciplined.",
    "TIPI4": "Anxious, easily upset.",
    "TIPI5": "Open to new experiences, complex.",
    "TIPI6": "Reserved, quiet.",
    "TIPI7": "Sympathetic, warm.",
    "TIPI8": "Disorganized, careless.",
    "TIPI9": "Calm, emotionally stable.",
    "TIPI10": "Conventional, uncreative."
    }

    for question_id, question_text in tipi_questions.items():
        response = st.selectbox(
            f"I see myself as: {question_text}",
            options=[
                "Disagree strongly (1)",
                "Disagree moderately (2)",
                "Disagree a little (3)",
                "Neither agree nor disagree (4)",
                "Agree a little (5)",
                "Agree moderately (6)",
                "Agree strongly (7)"
            ],
            index=0,  # Default to the first option
            key=question_id
        )

        # Extracting the numeric value
        # Use the last element in the split result to get the number
        tipi_responses[question_id] = int(response.split('(')[-1].strip(') '))

    return tipi_responses

# Display other questions
import streamlit as st

def encode_education(education):
    if education == "Less than high school (1)":
        return 1
    elif education == "High school (2)":
        return 2
    elif education == "University degree (3)":
        return 3
    elif education == "Graduate degree (4)":
        return 4
    return 0  # Default case

def encode_urban(urban):
    if urban == "Rural (1)":
        return 1
    elif urban == "Suburban (2)":
        return 2
    elif urban == "Urban (3)":
        return 3
    return 0  # Default case

def encode_gender(gender):
    if gender == "Male (1)":
        return 1
    elif gender == "Female (2)":
        return 2
    elif gender == "Other (3)":
        return 3
    return 0  # Default case

def encode_religion(religion):
    religion_map = {
        "Agnostic": 1,
        "Atheist": 2,
        "Buddhist": 3,
        "Christian (Catholic)": 4,
        "Christian (Mormon)": 5,
        "Christian (Protestant)": 6,
        "Christian (Other)": 7,
        "Hindu": 8,
        "Jewish": 9,
        "Muslim": 10,
        "Sikh": 11,
        "Other": 12
    }
    return religion_map.get(religion, 0)  # Default case

def encode_race(race):
    race_map = {
        "Asian": 10,
        "Arab": 20,
        "Black": 30,
        "Indigenous": 40
    }
    return race_map.get(race, 0)  # Default case

def encode_marital_status(married):
    if married == "Never married (1)":
        return 1
    elif married == "Currently married (2)":
        return 2
    elif married == "Previously married (3)":
        return 3
    return 0  # Default case

def encode_major(major_input):
    # Load the saved LabelEncoder
    with open('label_encoder_major.pkl', 'rb') as file:
        le_major = pickle.load(file)



    # Encode the user input using the pre-fitted LabelEncoder
    try:
        encoded_major = le_major.transform([major_input])[0]  # Transform the input to its encoded form
    except ValueError:
        encoded_major = 2950 # Default value for unrecognized inputs
    
    return encoded_major
def display_other_questions():
    other_responses = {}

    # Education
    other_responses['education'] = st.selectbox(
        "How much education have you completed?",
        options=[
            "Less than high school (1)", 
            "High school (2)", 
            "University degree (3)", 
            "Graduate degree (4)"
        ],
        index=0
    )

    # Urban area
    other_responses['urban'] = st.selectbox(
        "What type of area did you live when you were a child?",
        options=[
            "Rural (1)", 
            "Suburban (2)", 
            "Urban (3)"
        ],
        index=0
    )

    # Gender
    other_responses['gender'] = st.selectbox(
        "What is your gender?",
        options=[
            "Male (1)", 
            "Female (2)", 
            "Other (3)"
        ],
        index=0
    )

    # Age
    other_responses['age'] = st.number_input(
        "How many years old are you?",
        min_value=0,
        max_value=120,
        value=25  # Default age
    )

    # Religion
    other_responses['religion'] = st.selectbox(
        "What is your religion?",
        options=[
            "Agnostic", 
            "Atheist", 
            "Buddhist", 
            "Christian (Catholic)", 
            "Christian (Mormon)", 
            "Christian (Protestant)", 
            "Christian (Other)", 
            "Hindu", 
            "Jewish", 
            "Muslim", 
            "Sikh", 
            "Other"
        ],
        index=0
    )

    # Race
    other_responses['race'] = st.selectbox(
        "What is your race?",
        options=[
            "Asian", 
            "Arab", 
            "Black", 
            "Indigenous"
        ],
        index=0
    )

    # Marital Status
    other_responses['married'] = st.selectbox(
        "What is your marital status?",
        options=[
            "Never married (1)", 
            "Currently married (2)", 
            "Previously married (3)"
        ],
        index=0
    )

    # Family Size
    other_responses['familysize'] = st.number_input(
        "Including you, how many children did your mother have?",
        min_value=0,
        value=1  # Default family size
    )

    # Major
    other_responses['major'] = st.text_input("If you attended a university, what was your major (e.g. 'psychology', 'English', 'civil engineering')?")

    # Encode responses
    encoded_responses = {
        'education': encode_education(other_responses['education']),
        'urban': encode_urban(other_responses['urban']),
        'gender': encode_gender(other_responses['gender']),
        'age': other_responses['age'],
        'religion': encode_religion(other_responses['religion']),
        'race': encode_race(other_responses['race']),
        'married': encode_marital_status(other_responses['married']),
        'familysize': other_responses['familysize'],
        'major': encode_major(other_responses['major'])  
    }

    return encoded_responses


# Main Streamlit app
def main():
    st.title("User Input Form")

    # MCQ Questions
    mcq_responses = display_mcq_questions()
 
    # TIPI Questions
    tipi_responses = display_tipi_questions()
    
    
    # Other Questions
    other_responses = display_other_questions()
    combined_responses = list(mcq_responses.values()) + list(tipi_responses.values()) + list(other_responses.values())
    
    # Submit button
    if st.button("Submit"):
        # Process the responses and calculate stress score
        stress_score = sum(mcq_responses.values())
        input_features = combined_responses+[stress_score]
        model_path = r"NB_mood_prediction_model.sav"
        model = load(model_path)
        print(input_features)
        stress_level = model.predict([input_features])[0]
        
        print(stress_level)
        st.write("Thank you for your responses!")
        if stress_level < 1 and stress_level > -1:
          st.write(f"Your predicted stress level is: Moderate")
        elif stress_level < -1:
            st.write(f"Your predicted stress level is: Low")
        elif stress_level > 1:
            st.write(f"Your predicted stress level is: High")
        st.write(f"Your stress score is: {stress_score}")
if __name__ == "__main__":
    main()
