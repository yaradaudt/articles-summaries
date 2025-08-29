import streamlit as st
from main import generate_url_summary

# Adding a title
st.title("Resumidor de Artigos com IA")

# Adding a description
st.write("Cole a URL de algum artigo para um resumo rápido e conciso!")

# Adding an input field where the url should be pasted
article_url = st.text_input("Cole a URL aqui: ")

if st.button("Gerar resumo"):
    st.write(f"Você clicou no botão para a URL: {article_url}")

    if article_url:
        with st.spinner("Extraindo e resumindo o texto..."):
            summary_generated = generate_url_summary(article_url)

            if summary_generated:
                st.subheader("Resumo Gerado")
                st.success("Resumo gerado com sucesso!")
                st.write(summary_generated)
            else:
                st.warning("Não foi possível extrair o texto da URL. Tente outra URL.")
    else:
        st.warning("Por favor, insira uma URL válida.")
