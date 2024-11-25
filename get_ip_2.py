import streamlit as st 
from requests import get
import json
import datetime

loc = get('https://ipapi.co/json/?key=1Ns8Sx9LNPSbVY8J5DS5XTA7jSbX3OXKvbj08JpXNS47lqJ35B')
st.write(loc.json())

with open('json_data.json', 'w') as outfile:
    json.dump(loc.json(),outfile)
