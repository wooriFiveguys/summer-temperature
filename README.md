## 주제🌞
- 22년도 여름 기온 시각화 및 분석(2023.05.15 ~ 2023.05.17)
- 배포 URL: https://woorifiveguys-summer-temperature-group05appmain-page-syorh1.streamlit.app/

## 데이터🌡
- 공공 데이터 사용
- 기상청의 폭염 데이터 셋
- [https://data.kma.go.kr/data/weatherIssue/slthtList.do?pgmNo=690](https://data.kma.go.kr/data/weatherIssue/slthtList.do?pgmNo=690)
- 일시, 지점, 최고 체감온도, 기온(최고/평균/최저),
- 상대 습도, 폭염 특보, 폭염 예보, 열대야, 자외선 지수 제공

## 데이터 전처리👩‍💻
- 일시
- 최고 체감온도
- 기온(최고/평균/최저)

## 작업 과정📈
- 월을 선택하는 selectbox 생성 (6월, 7월, 8월, 9월)
- 선택하는 월에 해당하는 csv파일 읽어오기
- 보고 싶은 그래프를 선택하는 selectbox 생성(최고 체감온도, 최고 온도, 평균 온도, 최저 온도)
- scatter()함수를 사용
    - x는 일시, y는 선택한 온도를 기준으로 그래프 생성
    - streamlit의 pyplot 함수를 이용해 그래프 띄우기
    
## 분석 후 알게 된 점💡
- 7월이 제일 더움!
- 최고 체감온도와 최고 온도 차이가 1~2도로 별로 차이 나지 않음
- 9월의 최저 기온 중 0 도 존재
    - 9월 4일 자의 담양에서 기록
    
## 어려웠던 점😭
- 엑셀 파일의 확장자를 csv로 변경 시 열 들이 띄어쓰기 없이 붙어있었음
    - 데이터에서 열 별로 값을 빼내기 어려움!
    - 해결: 엑셀 파일을 쉼표 구분하기로 다시 저장
- 최근 폭염 예측을 원했으나, 과거 데이터만 존재
    - 단순 데이터 시각 화로 미래 예측 불가
    - 머신 러닝 학습 후 추가로 예측하는 프로그램 진행 예정
- 그래프 생성 시 x축에 년도, 월, 일 모두 출력
    - DateFormatter() 사용하여 일만 가져옴

## 소감❤
- 아쉬운 점
    - 최고, 최저 온도의 지역도 보여주고 싶었지만 구현 못함
- 좋았던 점
    - streamlit 사용해 웹 페이지 꾸미는 실력 향상
    - 수업 시간에 배운 streamlit, maplotlib, pandas 기능 한 번씩 사용하여 복습
