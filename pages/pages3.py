import streamlit as st

st.set_page_config(page_title="우리나라 MBTI 비율", page_icon="🇰🇷")

st.title("🇰🇷 우리나라 친구들은 어떤 유형이 많을까?")
st.markdown("우리나라 사람들은 어떤 성격 유형을 가장 많이 가지고 있을까요? 재미로 보는 통계 그래프랍니다! 📊")

st.divider()

# 추가 라이브러리 없이 딕셔너리로 데이터 구현
korea_mbti_data = {
    "비율(%)": {
        "INFP": 13.3, "ENFP": 12.6, "ESFJ": 8.3, "ISFJ": 7.6,
        "ISFP": 6.7, "ESTJ": 5.8, "INTP": 5.5, "INFJ": 5.4,
        "ENFJ": 5.1, "ENTP": 4.8, "ESTP": 4.7, "ISTJ": 4.5,
        "ENTJ": 4.2, "ISTP": 4.1, "INTJ": 3.9, "ESFP": 3.5
    }
}

st.subheader("📊 대한민국 MBTI TOP 16")
st.bar_chart(korea_mbti_data)

st.info("""
💡 **상담가 쌤의 포인트:**  
그래프를 보면 우리나라에는 **INFP**와 **ENFP** 친구들이 꽤 많다는 걸 알 수 있어요! 
나와 같은 유형이 얼마나 되는지 확인해 보는 것도 쏠쏠한 재미죠? 😆
""")