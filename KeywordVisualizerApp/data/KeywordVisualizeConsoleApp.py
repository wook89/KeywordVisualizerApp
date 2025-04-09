import lib.myTextMining as tm
import lib.NaverNewsCrawler as nc
from konlpy.tag import Okt
from konlpy.tag import Komoran
# 코퍼스 로딩
# 검색 API 호출, 응답을 JSON 데이터로 return하는 함수 작성
# API 호출 결과에 문제가 있을 경우 exception으로 처리
# exception 발생 시 exception과 호출 url 확인
import urllib.request
import json
        
#input_filename = "daum_movie_review.csv"
title = input("검색어 입력 : ")
# 검색 결과를 저장할 list 초기화
resultAll = []
# 리스트를 csv 파일로 저장
  

# 첫 검색 API 호출
start = 1
display = 10
resultJSON = nc.searchNaverNews(title, start, display) 

while (resultJSON != None) and (resultJSON['display'] > 0):
     # 응답데이터 정리하여 리스트 저장
    nc.setNewsSearchResult(resultAll, resultJSON)
 
    # 다음 검색 API 호출을 위한 파라미터 조정
    start += resultJSON['display']
    # API 호출
    resultJSON = nc.searchNaverNews(title, start, display)
    # API 호출 성공 여부 출력
    if resultJSON != None:
        print(f"{title} [{start}] : Search Request Success")
    else:
        print(f"{title} [{start}] : Error !!")
    if start >= 100:
        break

filename = f"./data/{title}_naver_news.csv"
nc.saveSearchResult_CSV(resultAll, filename)

input_filename = title+"_naver_news.csv"
corpus_list = tm.load_corpus_from_csv("./data/"+input_filename,"description")
print(corpus_list[:10])   

# 빈도수 추출
#Okt
#my_tokenizer = Okt().pos
#my_tags = ['Noun','Adjective','Verb']

#Komoran
my_tokenizer = Komoran().pos
my_tags = ['NNG','NNP','VV','VA']

my_stopwords = ['하며','입','하고','로써','하여','된','한다','제','바','이']
counter = tm.analyze_word_freq(corpus_list, my_tokenizer, my_tags, my_stopwords)

print(list(counter.items())[:20])
#tm.visualize_barchart(counter,"다음 영화 리뷰 분석","빈도수","키워드") #나만 안됨
tm.visualize_wordcloud(counter)
tm.visualize_barchart(counter,title,'빈도','키워드')

 
