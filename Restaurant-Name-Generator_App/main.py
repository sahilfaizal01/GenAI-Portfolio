import streamlit as st 
import langchain_helper

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Chinese","Korean","Thai","Japanese","Mediterranean","Indian", "Italian", "Mexican", "Arabic", "American"))
diet_preference = st.sidebar.selectbox("Pick a Diet Preference", ("Vegetarian", "Non-Vegetarian"))

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine, diet_preference)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write(item)
    
