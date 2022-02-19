import streamlit as st

def title():
    st.header("설문조사")
    st.caption("선호하는 게임 분야")
    st.title("")
    st.caption("사진 오른쪽의 화살표를 누르시면 사진을 확대하여 보실수 있습니다")

def img_bt():
    col1 , col2 , col3 , col4 , col5 = st.beta_columns(5)
    with col1:
        st.image("https://www.gamehype.co.uk/wp-content/uploads/2017/01/call_of_duty_black_ops_2_video_game-HD-1280x640.jpg" , use_column_width=True)
        st.button("FPS 게임")

    with col2:
        st.image("https://play-lh.googleusercontent.com/SPuYEw87v_Wo1h-4_Y9yMMAfAIWKoyL35bfhZblS4HyhY2itmD74-sj6CrlGdhF_0HNC=w412-h220-rw" , use_column_width=True)
        st.button("퍼즐 게임")

    with col3:
        st.image("https://image.zdnet.co.kr/2012/10/31/5SJnFNYUShQXMiF4xtoL.jpg" , use_column_width=True)
        st.button("슈팅 게임")

    with col4:
        st.image("https://nexus.leagueoflegends.com/wp-content/uploads/2019/10/Banner_Preseason-1_dwfwpnp0byzkpe2hk65v.jpg" , use_column_width=True)
        st.button("AOS 게임")

    with col5:
        st.image("https://pbs.twimg.com/media/EhjvW9EU8AIw1ke.jpg" , use_column_width=True)
        st.button("RPG 게임")
title()
img_bt()
