import streamlit as st
import pandas as pd


def obliczenia(df):
    df.dropna(inplace=True)
    return df

def obliczenia2(df):
    for x in df.index:
        if df.loc[x, "Duration"] > 120:
            df.loc[x, "Duration"] = 120
    return df

with st.sidebar:
    st.header("Program testowy")
    st.info(
    f"""
        💡 W tym miejscu znajduje się dostępnę opcje programu
        """
    )

    st.write("Opcje dotyczące tabeli:")
    
    uploaded_file = st.file_uploader("Wybierz plik")

    if uploaded_file is not None :
        st.write(f"""Załadowano plik **{uploaded_file.name}**""")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        przelicz = st.button("Przelicz", help="Po naciśnięciu usnięte zostaną puste wpisy")
    
    with col2:
        view = st.button("Podgląd", help="Podgląd tabeli")
    
    with col3:
        save = st.button("Zapisz", help="zapisz do pliku")

st.write(
    f"""
        💡 W tym miejscu wyświeltana będzie tabelka:
        """
    )

if view:
    st.table(pd.read_csv(uploaded_file))


if przelicz:
    df = pd.read_csv(uploaded_file)
    show = obliczenia(df)
    st.table(show)


