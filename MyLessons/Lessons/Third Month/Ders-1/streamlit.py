import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 
st.title("data anliz")
st.header("Csv Faylini yukleyin")
uploaded_file = st.file_uploader("csv fayilini secin",type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("yuklenmis datanin ilk 5 setri")
    st.write(df.head())
    
    st.subheader("datanin statistik gostericileri")
    st.write(df.describe())
    
    st.subheader("datanin sütun analizi")
    columns = df.columns.tolist()
    sel_column = st.selectbox("analiz ucun columu sec:",columns)
    
    if sel_column:
        st.write(f"secilis stun:{sel_column}")
        st.write(df[sel_column].describe())
        
        st.subheader("Vizualizasiya")
        viz_type = st.selectbox("vizualizasiyanin novunu sec:",
                                ["histogram","scatterplot","barchart","barplot"])
        if viz_type == "histogram":
            st.write(f"{sel_column} ucun histogram<---")
            fig, ax = plt.subplots()
            ax.hist(df[sel_column], bins=15,color = "pink")
            plt.xlabel(sel_column)
            plt.ylabel("random")
            st.pyplot(fig)
        elif viz_type == "barchart":
            st.write(f"{sel_column} ucun barchart<---")
            fig,ax = plt.subplots()
            df[sel_column].value_counts().plot(kind="bar",ax=ax,color ="skyblue")
            plt.xlabel(sel_column)
            plt.ylabel("Say")
            st.pyplot(fig)
        elif viz_type == "scatterplot":
            st.write(f"Scatter ucun iki column sec")
            scatter_x = st.selectbox("X oxu ucun column",columns)
            scatter_y = st.selectbox("Y oxu ucun column",columns)
            if scatter_x and scatter_y:
                st.write(f"ilk kolumn:{scatter_x}\nikinci kolumn:{scatter_y}")       
                fig,ax = plt.subplots()
                ax.scatter(df[scatter_x],df[scatter_y],alpha = 0.7,color = "purple")
                plt.xlabel(scatter_x)
                plt.ylabel(scatter_y)
                st.pyplot(fig)
        elif viz_type == "barplot":
            st.write(f"{sel_column} ucun barplot<---")
            fig,ax = plt.subplots()
            cate = df[sel_column].value_counts()
            
            ax.bar(cate.index,cate.values,color="green")
            plt.xlabel(sel_column)
            plt.ylabel("Say")
            st.pyplot(fig)
else:st.write("fayl yoxdu ")



