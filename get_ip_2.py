import streamlit as st 
from requests import get
import json
import datetime

loc = get('https://ipapi.co/json/')
st.write(loc.json())
datos = 1

fecha = datetime.datetime.now().strftime('%d/%m/%Y_%H_%M_%S')
with open('json_data' +fecha+'.json', 'w') as outfile:
    json.dump(loc.json(),outfile)