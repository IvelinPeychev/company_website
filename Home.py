import pandas
import streamlit as st

st.set_page_config(layout='wide')


st.title('The Best Company')
st.write(' This is a test description about the company and so on.\n' + '\n' +
         ' This is a test description about the company and so on.\n' + '\n' +
         ' This is a test description about the company and so on.\n')

st.write("""


""")

st.header('Our Team')


data_file = pandas.read_csv('data (1).csv')

col1, empty_col, col2, empty_col2,  col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

# Content for the first column

with col1:
    # Iterate over rows from 1 to 4
    for index, row in data_file[:4].iterrows():
        # Add member first and last names
        st.header(row['first name'].title() + ' ' + row['last name'].title())
        # Add member role for the company
        st.write(row['role'])
        # Add member's photo
        st.image('images (1)/' + row['image'])


# Content for the second column

with col2:
    # Iterate over rows from 4 to 7
    for index, row in data_file[4:8].iterrows():
        # Add member first and last names
        st.header(row['first name'].title() + ' ' + row['last name'].title())
        # Add member role for the company
        st.write(row['role'])
        # Add member's photo
        st.image('images (1)/' + row['image'])


# Content for the third column

with col3:
    # Iterate over rows 8 to 12
    for index, row in data_file[8:].iterrows():
        # Add member first and last names
        st.header(row['first name'].title() + ' ' + row['last name'].title())
        # Add member role for the company
        st.write(row['role'])
        # Add member's photo
        st.image('images (1)/' + row['image'])
