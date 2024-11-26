import streamlit as st
from PIL import Image
from datetime import datetime

st.title("My Biography")

col1, col2 = st.columns([3, 1])

with col1:
    st.header("About Me")
    name = st.text_input("Enter your full name", "Marialyn Ramada")
    bio = st.text_area("Write a short bio about yourself", 
                       " I am Marialyn Ramada I live in Albor Libjo Dinagat Islands, I graduate at Albor National High School.")
    birthday = st.text_input("Enter your birthday", "April 04, 2006")
    
    today = datetime.today()
    birth_date = datetime.strptime(birthday, "%B %d, %Y")
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    
    st.write(f"Age: {age}")
             
    gender = st.selectbox("Select your gender", ["Female", "Male", "Other", "Prefer not to say"])

    st.header("Educational Attainment")

    education_options = [
        "College Graduate",
        "College Level",
        "High School Graduate",
        "Middle School Level",
        "Elementary Graduate",
        "Others"
    ]
    
    education_selected  = []
    
    for option in education_options:
        if st.checkbox(option):
            education_selected.append(option)
    
    st.write("Your Selected Educational Attainment:")
    if education_selected:
        for item in education_selected:
            st.write(f"- {item}")
    else:
        st.write("Albor Central Elementary School.")
        st.write("Albor National High School.")
    
    st.header("Parental Information")
    father_name = st.text_input("Father's Name", "Joven Ramada")
    father_occupation = st.text_input("Father's Occupation", "Driver")
    mother_name = st.text_input("Mother's Name", "Marife Ramada")
    mother_occupation = st.text_input("Mother's Occupation", "Housewife")

    st.header("Contact Information")
    email = st.text_input("Email", "ramadamarialyn@gmail.com")
    phone = st.text_input("Phone", "09387610532")
    facebook = st.text_input("Facebook Profile URL", "https://www.facebook.com/marialyn.ramada")


    st.header("Hobbies & Interests")
    hobbies = st.text_area("List your hobbies or interests", 
                           "- Playing Volleyball, Playing Guitar, Dancing and Singing")
with col2:
    st.subheader("Photo")
    st.image('maria.jpg',width=200)


col1, col2 = st.columns([3, 1])

with col1:
    st.header("Your Profile")
    st.subheader(f"Name: {name}")
    st.write(f"Bio: {bio}")
    st.write(f"Age: {age}")
    st.write(f"Gender: {gender}")
    
    st.subheader("Educational Attainment")
    if education_selected:
        for item in education_selected:
            st.write(f"- {item}")
    else:
        st.write("Albor National High School.")

    st.subheader("Parental Information")
    st.write(f"Father's Name: {father_name}  \n**Occupation:** {father_occupation}")
    st.write(f"Mother's Name: {mother_name}  \n**Occupation:** {mother_occupation}")

    st.subheader("Contact Information")
    st.write(f"- Email: {email}  \n- Phone: {phone}")
    st.write(f"- Facebook: [Profile]({facebook})")

    st.subheader("Hobbies & Interests")
    st.write(hobbies)
