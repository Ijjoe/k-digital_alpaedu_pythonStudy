import streamlit as st 
from langchain.llms import CTransformers

llm =CTransformers(
   model = "llama-2-7b-chat.ggmlv3.q2_K.bin",
   model_type ="llama"
)

st.title('인공지는 시인')

con = st.text_input('시의 주제를 제시해주세요')

if st.button('시 작성 요청하기'):
  with st.spinner('시 작성 중 ...'):
    res = llm.predict("write a poem about " + con + ":")
    st.write(res)