import lib.myTextMining as tm
import lib.NaverNewsCrawler as nc
from konlpy.tag import Okt
from konlpy.tag import Komoran
# 코퍼스 로딩
# 검색 API 호출, 응답을 JSON 데이터로 return하는 함수 작성
# API 호출 결과에 문제가 있을 경우 exception으로 처리
# exception 발생 시 exception과 호출 url 확인

def visualize_barchart(counter,title,xlabel,ylabel,wordNum):
    #데이터 준비
    counter.most_common(wordNum)
    word_list = [word for word, count in counter.most_common(wordNum)]
    count_list = [count for word, count in counter.most_common(wordNum)]
    
    #한글폰트 설정
    from matplotlib import font_manager, rc
    font_path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font_name)

    import matplotlib.pyplot as plt

    # 수평 막대그래프
    fig, ax = plt.subplots() 
    ax.barh(word_list[::-1], count_list[::-1])
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return fig
   
def visualize_wordcloud(counter,wordNum):
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt

    # 한글 폰트 path 지정
    font_path = "c:/Windows/fonts/malgun.ttf"

    # WordCloud 객체 생성
    wordcloud = WordCloud(font_path,
                    width=600,
                    height=600,
                    max_words=wordNum,
                    background_color='ivory')
    wordcloud = wordcloud.generate_from_frequencies(counter)
    fig, ax = plt.subplots(figsize=(8, 4))  # matplotlib figure 생성
    ax.imshow(wordcloud, interpolation='bilinear')  # WordCloud 이미지를 ax에 그리기
    ax.axis('off') 
    return fig
   
