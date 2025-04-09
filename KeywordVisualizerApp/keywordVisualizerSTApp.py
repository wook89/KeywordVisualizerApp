import streamlit as st
import lib.myTextMining as tm
import pandas as pd
import numpy as np
import lib.STVisualizer as STV
from konlpy.tag import Komoran

def process_file(file):
    # 파일 처리 로직을 여기에 작성
    st.write(f"파일 처리 중: {file.name}")
    
uploaded_files = st.sidebar.file_uploader("파일 선택")
    
keyword = st.sidebar.text_input("데이터가 있는 컬럼명")
first_btn = st.sidebar.button("데이터 파일 확인")

if first_btn:
    if uploaded_files:
        process_file(uploaded_files)
    else:
        st.sidebar.write("파일이 업로드되지 않았습니다.")

st.sidebar.subheader("설정")
##여기부터 컨테이너 안쪽
container = st.sidebar.container(border=True)

graph_cb = container.checkbox("빈도수 그래프")#그래프 체크박스
wordNum1 = container.slider("단어 수", 10, 50, 20)

wordCloud_cb = container.checkbox("워드클라우드")#워드클라우드 체크박스
wordNum2 = container.slider("단어 수", 20, 500, 50)
second_btn = container.button("분석 시작")##분석시작 버튼


if second_btn :
    
    corpus_list = tm.load_corpus_from_csv("./data/"+uploaded_files.name,"description")
    my_tokenizer = Komoran().pos
    my_tags = ['NNG','NNP','VV','VA']
    my_stopwords = ['하며','입','하고','로써','하여','된','한다','제','바','이']
    counter = tm.analyze_word_freq(corpus_list, my_tokenizer, my_tags, my_stopwords)
    
    if graph_cb and wordCloud_cb:
        graph = STV.visualize_barchart(counter,keyword,"빈도","키워드",wordNum1)
        st.pyplot(graph)
        wordCloud_fig = STV.visualize_wordcloud(counter,wordNum2)
        st.pyplot(wordCloud_fig)
    elif graph_cb:
        graph = STV.visualize_barchart(counter,keyword,"빈도","키워드",wordNum1)
        st.pyplot(graph)
    elif wordCloud_cb:
        wordCloud_fig = STV.visualize_wordcloud(counter,wordNum2)
        st.pyplot(wordCloud_fig)
    
