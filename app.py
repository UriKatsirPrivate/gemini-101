import streamlit as st
from initialization import initialize_llm_vertex

REGIONS=["us-central1"]
MODEL_NAMES=['gemini-2.0-flash-001','gemini-2.0-flash-lite-001']

def get_project_id():
    return "landing-zone-demo-341118"

project_id=get_project_id()
region=st.sidebar.selectbox("Region",REGIONS)
model_name = st.sidebar.selectbox('Model Name',MODEL_NAMES)
max_tokens = st.sidebar.slider('Output Token Limit',min_value=1,max_value=8192,step=100,value=8192)
temperature = st.sidebar.slider('Temperature',min_value=0.0,max_value=2.0,step=0.1,value=1.0)
top_p = st.sidebar.slider('Top-P',min_value=0.0,max_value=1.0,step=0.1,value=0.8)

client, safety_settings,generation_config = initialize_llm_vertex(project_id,region,model_name,max_tokens,temperature,top_p)

def run_prompt(prompt):
    response = client.models.generate_content(model=model_name, contents=prompt)
    return response.text 

def display_result(execution_result):
    if execution_result != "":
        st.text_area(label="Execution Result:",value=execution_result,height=400, key=50)
    else:
        st.warning('No result to display.')    

with st.form(key='run-prompt',clear_on_submit=False):
    prompt = st.text_area('Enter your prompt:',height=200, key=1)
        
    if st.form_submit_button('Run Prompt'):
        if prompt:
            with st.spinner('Running prompt...'):
                execution_result = run_prompt(prompt)
                display_result(execution_result)
        else:
            st.warning('Please enter a prompt before executing.')                