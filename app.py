import streamlit as st
import pickle
import pandas as pd

pipe = pickle.load(open('model_ODI.pkl','rb'))

teams = ['Australia','New Zeland','England', 'South Africa',
       'West Indies', 'Sri Lanka', 'Pakistan', 'India', 'Bangladesh', 'Afghanistan']

st.title("ODI Score Predictor System")

col1,col2, col3 = st.columns(3)

with col1:
    innings = st.selectbox('inning', ['1','2'])
with col2:
    batting_team = st.selectbox('batting team',teams)
with col3:
    bowling_team = st.selectbox('bowling team', teams)

col6,col4,col5 = st.columns(3)

with col6:
    current_score = st.number_input('Current Score', min_value=1, step=1)
with col4:
    overs = st.number_input('Overs done',min_value=10., step=0.1, max_value=50.,format="%.1f")
with col5:
    wickets = st.number_input('Wickets out', min_value=0, step=1, max_value=10)

col7,col8,col9,col10 = st.columns(4)

with col7:
    run_ten = st.number_input('Runs scored in last 10 overs',min_value=0, step=1 )
with col8:
    dot_ten = st.number_input('dot balls in last 10 overs', min_value=0, step=1, max_value=60)
with col9:
    bound_ten = st.number_input('boundries in last 10 overs',min_value=0, step=1)
with col10:
    wkt_ten = st.number_input('wickets in last 10 overs',min_value=0, step=1, max_value=10)


if st.button('Predict Score'):
    ball_bowled = (int(str(overs).split(".")[0])*6) + int(str(overs).split(".")[1])
    ball_left = 300-ball_bowled
    crr = (current_score*6)/ball_bowled
    wickets_left = 10 - wickets

    input_df = pd.DataFrame(
    {'innings':[innings],'batting_team':[batting_team], 'bowling_team':[bowling_team], 'current_score':[current_score], 'ball_bowled':[ball_bowled], 'crr':[crr], 'ball_left': [ball_left], 'wickets_left': [wickets_left], 'last_ten': [run_ten], 'last_ten_dot': [dot_ten], 'last_ten_boundary':[bound_ten], 'last_ten_wkts':[wkt_ten]}
    )

    result =pipe.predict(input_df)
    st.header("Predicted Score - " + str(int(result[0])))

