import streamlit as st
import pandas as pd
import datetime
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import os
import glob
import matplotlib.dates as mdates
# matplotlib을 이용한 그래프에 한글을 표시하기 위한 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False
# 월 별 최고체감온도
def get_month_highest_sensible_temperature(month_select):
    
    original_title = '<div style = "font-size:50px;display:inline;">날짜 별 전국 </div><div style = "color:#34F9A0;font-size:50px;display:inline;">최고 체감 </div><div style = "font-size:50px;display:inline;">온도🌡</div>'
    st.markdown(original_title, unsafe_allow_html=True)
    folder = '/data/'
    file_path=sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))+folder
    # 파일 읽어오기
    if month_select == '6월':
        df = pd.read_csv(file_path+'ISSUE_HW_DAY_2022-06_2022-06_2022.csv', encoding='EUC-KR')

    elif month_select == '7월':
        df = pd.read_csv(file_path+'ISSUE_HW_DAY_2022-07_2022-07_2022.csv', encoding='EUC-KR')

    elif month_select == '8월':
        df = pd.read_csv(file_path+'ISSUE_HW_DAY_2022-08_2022-08_2022.csv', encoding='EUC-KR')

    elif month_select == '9월':
        df = pd.read_csv(file_path+'ISSUE_HW_DAY_2022-09_2022-09_2022.csv', encoding='EUC-KR')
    
    fig, ax = plt.subplots(figsize=(10,7))
    ax.scatter(x=df['일시'], y=df['최고체감온도(°C)'], color = '#34F9A0')
    dateFmt = mdates.DateFormatter('%d')
    ax.xaxis.set_major_formatter(dateFmt)
    plt.xticks(rotation=45)
    st.pyplot(fig)

    sensible_temperature_mean = df['최고체감온도(°C)'].mean()
    sensible_temperature_max = df['최고체감온도(°C)'].max()
    #max_df = df[(df['최고체감온도(°C)'] == sensible_temperature_max)]
    sensible_temperature_min = df['최고체감온도(°C)'].min()
    st.success(f'평균: {round(sensible_temperature_mean)}°C, 최고: {round(sensible_temperature_max)}°C, 최저: {round(sensible_temperature_min)}°C')

def get_month_highest_temperature(month_select):
    original_title = '<div style = "font-size:50px;display:inline;">날짜 별 전국 </div><div style = "color:red;font-size:50px;display:inline;">최고 </div><div style = "font-size:50px;display:inline;">기온🌡</div>'
    st.markdown(original_title, unsafe_allow_html=True)

    file_path=os.path.dirname(os.path.abspath(__file__))
    # 파일 읽어오기
    if month_select == '6월':
        df = pd.read_csv(file_path+'/ISSUE_HW_DAY_2022-06_2022-06_2022.csv', encoding='EUC-KR')

    elif month_select == '7월':
        df = pd.read_csv(file_path+'/ISSUE_HW_DAY_2022-07_2022-07_2022.csv', encoding='EUC-KR')

    elif month_select == '8월':
        df = pd.read_csv(file_path+'/ISSUE_HW_DAY_2022-08_2022-08_2022.csv', encoding='EUC-KR')

    elif month_select == '9월':
        df = pd.read_csv(file_path+'/ISSUE_HW_DAY_2022-09_2022-09_2022.csv', encoding='EUC-KR')

    fig, ax = plt.subplots(figsize=(10,7))
    ax.scatter(x=df['일시'], y=df['최고기온(°C)'],color = 'red')
    dateFmt = mdates.DateFormatter('%d')
    ax.xaxis.set_major_formatter(dateFmt)
    plt.xticks(rotation=45)
    st.pyplot(fig)

    highest_temperature_mean = df['최고기온(°C)'].mean()
    highest_temperature_max = df['최고기온(°C)'].max()
    highest_temperature_min = df['최고기온(°C)'].min()
    st.success(f'평균: {round(highest_temperature_mean)}°C, 최고: {round(highest_temperature_max)}°C, 최저: {round(highest_temperature_min)}°C')


def get_month_avg_temperature(month_select):
    original_title = '<div style = "font-size:50px;display:inline;">날짜 별 전국 </div><div style = "color:#F182FD;font-size:50px;display:inline;">평균 </div><div style = "font-size:50px;display:inline;">기온🌡</div>'
    st.markdown(original_title, unsafe_allow_html=True)

    file_path=os.path.dirname(os.path.abspath(__file__))
    # 파일 읽어오기
    if month_select == '6월':
        df = pd.read_csv(file_path+'/ISSUE_HW_DAY_2022-06_2022-06_2022.csv', encoding='EUC-KR')

    elif month_select == '7월':
        df = pd.read_csv(file_path+'/ISSUE_HW_DAY_2022-07_2022-07_2022.csv', encoding='EUC-KR')

    elif month_select == '8월':
        df = pd.read_csv(file_path+'/ISSUE_HW_DAY_2022-08_2022-08_2022.csv', encoding='EUC-KR')

    elif month_select == '9월':
        df = pd.read_csv(file_path+'/ISSUE_HW_DAY_2022-09_2022-09_2022.csv', encoding='EUC-KR')

    fig, ax = plt.subplots(figsize=(10,7))
    ax.scatter(x=df['일시'], y=df['평균기온(°C)'], color = '#F182FD')
    dateFmt = mdates.DateFormatter('%d')
    ax.xaxis.set_major_formatter(dateFmt)
    plt.xticks(rotation=45)
    st.pyplot(fig)

    avg_temperature_mean = df['평균기온(°C)'].mean()
    avg_temperature_max = df['평균기온(°C)'].max()
    avg_temperature_min = df['평균기온(°C)'].min()

    st.success(f'평균: {round(avg_temperature_mean)}°C, 최고: {round(avg_temperature_max)}°C, 최저: {round(avg_temperature_min)}°C')




def get_month_lowest_temperature(month_select):

    original_title = '<div style = "font-size:50px;display:inline;">날짜 별 전국 </div><div style = "color:blue;font-size:50px;display:inline;">최저 </div><div style = "font-size:50px;display:inline;">기온🌡</div>'
    st.markdown(original_title, unsafe_allow_html=True)

    file_path=os.path.dirname(os.path.abspath(__file__))
    # 파일 읽어오기
    if month_select == '6월':
        df = pd.read_csv(file_path+'/ISSUE_HW_DAY_2022-06_2022-06_2022.csv', encoding='EUC-KR')

    elif month_select == '7월':
        df = pd.read_csv(file_path+'/ISSUE_HW_DAY_2022-07_2022-07_2022.csv', encoding='EUC-KR')

    elif month_select == '8월':
        df = pd.read_csv(file_path+'/ISSUE_HW_DAY_2022-08_2022-08_2022.csv', encoding='EUC-KR')

    elif month_select == '9월':
        df = pd.read_csv(file_path+'/ISSUE_HW_DAY_2022-09_2022-09_2022.csv', encoding='EUC-KR')

    fig, ax = plt.subplots(figsize=(10,7))
    ax.scatter(x=df['일시'], y=df['최저기온(°C)'], color = 'blue')
    dateFmt = mdates.DateFormatter('%d')
    ax.xaxis.set_major_formatter(dateFmt)
    plt.xticks(rotation=45)
    st.pyplot(fig)

    lowest_temperature_mean = df['최저기온(°C)'].mean()
    lowest_temperature_max = df['최저기온(°C)'].max()
    lowest_temperature_min = df['최저기온(°C)'].min()
    st.success(f'평균: {round(lowest_temperature_mean)}°C, 최고: {round(lowest_temperature_max)}°C, 최저: {round(lowest_temperature_min)}°C')


month_list = ['6월', '7월', '8월', '9월']
month_select = st.sidebar.selectbox("🌞기온을 확인하고 싶은 달을 골라주세요🌞", month_list)
original_month = f'<p style = "color:#55EFDE;font-size:40px;">{month_select}</p>'
st.markdown(original_month, unsafe_allow_html=True)
#st.write(month_select)


func_list = ['최고 체감 온도', '최고 기온', '평균 기온', '최저 기온']
func_select = st.sidebar.selectbox('👉보고 싶은 기능을 선택하세요👈',func_list)

if month_select == '6월':

    if func_select == '최고 체감 온도':
        get_month_highest_sensible_temperature(month_select)
    elif func_select == '최고 기온':
        get_month_highest_temperature(month_select)
    elif func_select == '평균 기온':
        get_month_avg_temperature(month_select)
    elif func_select == '최저 기온':
        get_month_lowest_temperature(month_select)

elif month_select == '7월':
    if func_select == '최고 체감 온도':
        get_month_highest_sensible_temperature(month_select)
    elif func_select == '최고 기온':
        get_month_highest_temperature(month_select)
    elif func_select == '평균 기온':
        get_month_avg_temperature(month_select)
    elif func_select == '최저 기온':
        get_month_lowest_temperature(month_select)

elif month_select == '8월':
    if func_select == '최고 체감 온도':
        get_month_highest_sensible_temperature(month_select)
    elif func_select == '최고 기온':
        get_month_highest_temperature(month_select)
    elif func_select == '평균 기온':
        get_month_avg_temperature(month_select)
    elif func_select == '최저 기온':
        get_month_lowest_temperature(month_select)

elif month_select == '9월':
    if func_select == '최고 체감 온도':
        get_month_highest_sensible_temperature(month_select)
    elif func_select == '최고 기온':
        get_month_highest_temperature(month_select)
    elif func_select == '평균 기온':
        get_month_avg_temperature(month_select)
    elif func_select == '최저 기온':
        get_month_lowest_temperature(month_select)
