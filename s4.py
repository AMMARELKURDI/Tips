import streamlit as st
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Tips Dashboard",layout="wide",initial_sidebar_state="auto")

df=pd.read_csv("tips.csv")

#sideBar
st.sidebar.header(":blue[Tips Dashboard]")
st.sidebar.image("images.jpeg")

category=st.sidebar.selectbox("Filter your Data",[None,"sex","day","smoker","time"])
Numerical=st.sidebar.selectbox("Filter your Data",[None,"tip","size","total_bill"])
row_filter=st.sidebar.selectbox("Row Filter",[None,"sex","day","smoker","time"])
col_filter=st.sidebar.selectbox("Col Filter",[None,"sex","day","smoker","time"])


st.sidebar.write(":green[This Dashboard uses Tips dataset from Seaborn for education purpose]")
st.sidebar.write("")
st.sidebar.markdown("Made with :heart_eyes: by Eng [Ammar Elkurdi](www.google.com)")


#body

# Row a

a1,a2,a3,a4=st.columns(4)
a1.metric("Max Total Bill",value=max(df['total_bill']))
a2.metric("Max Tips",value=df['tip'].max())
a3.metric("Min Total Bill",value=min(df['total_bill']))
a4.metric("Min Tips",value=df['tip'].min())

# Row b
st.subheader("Total Bill VS Tips")
fig=px.scatter(data_frame=df,x=df["total_bill"],y=df["tip"],color=category,size=Numerical,facet_col=col_filter,facet_row=row_filter)
st.plotly_chart(fig,use_container_width=True)

# Row C
c1,c2,c3=st.columns((3,4,4))
with c1:
    st.text("Sex Vs Tips")
    fig=px.bar(data_frame=df,x="sex",y="total_bill",color=category)
    st.plotly_chart(fig,use_container_width=True)

with c2:
    if category == None or Numerical==None:
        category,Numerical="sex","tip"
    st.text(f"{category} Vs {Numerical}")
    
    fig=px.pie(data_frame=df,names=category,values=Numerical)
    st.plotly_chart(fig,use_container_width=True)
with c3:
    if category == None or Numerical==None:
        category,Numerical="sex","tip"
    st.text(f"{category} Vs {Numerical}")
    
    #fig=px.pie(data_frame=df,names=category,values=Numerical,hole=0.4)
    ddf=df.groupby(category)[Numerical].mean().reset_index()

    fig = go.Figure()
    fig.add_trace(go.Bar(y=ddf[category], x=ddf[Numerical],
                base=[i*-1  for i  in ddf[Numerical]],
                marker_color='crimson',
                orientation="h",
                name='expenses'))
    fig.add_trace(go.Bar(y=ddf[category], x=ddf[Numerical],
                base=0,
                orientation="h",
                marker_color='lightslategrey',
                name='revenue'
                ))

    fig.update_layout(barmode="stack")
    st.plotly_chart(fig,use_container_width=True)