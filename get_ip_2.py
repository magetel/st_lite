import streamlit as st 
from requests import get
import json

loc = get('https://ipapi.co/json/')
st.write(loc.json())

with open('json_data.json', 'w') as outfile:
    json.dump(loc.json(),outfile)