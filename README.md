# Keyword Visualizer App

**Keyword Visualizer App**데이터를 분석하여 핵심 키워드를 시각화하는 텍스트 마이닝 기반 앱입니다.  
Streamlit 웹앱 또는 콘솔 환경에서 실행 가능하며, 워드클라우드, 키워드 빈도 분석, 뉴스 크롤링 기능 등을 제공합니다.

---

## 📌 주요 기능

- 🔍 영화 리뷰 및 뉴스 기사 기반 키워드 분석
- ☁️ 워드클라우드 생성
- 📊 키워드 빈도 그래프 시각화
- 🌐 네이버 뉴스 실시간 크롤링
- 🖥️ 콘솔/웹앱(Streamlit) 양쪽 지원

---

## 🗂️ 디렉토리 구조

├── KeywordVisualizeConsoleApp.py         # 콘솔 실행용 앱
├── keywordVisualizerSTApp.py             # Streamlit 앱 메인
├── data/                                 # 리뷰 및 뉴스 데이터
├── lib/                                  # 기능 모듈
│   ├── myTextMining.py                   # 텍스트 마이닝 기능
│   ├── NaverNewsCrawler.py               # 뉴스 크롤러
│   ├── STVisualizer.py                   # 시각화 처리
│   └── __pycache__/                      # 캐시 파일

## 🚀 실행 방법

### 
✅ 1. 가상환경 생성 (선택)
```bash
conda create -n keyword-env python=3.10 -y
conda activate keyword-env

✅ 2. 의존성 설치
pip install streamlit pandas matplotlib wordcloud konlpy beautifulsoup4 requests

✅ 3. 실행
Streamlit 앱 실행
streamlit run keywordVisualizerSTApp.py

 콘솔 앱 실행
python KeywordVisualizeConsoleApp.py











