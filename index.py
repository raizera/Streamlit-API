import requests
import streamlit as st

base_url = "https://api.github.com"

def selecionarUsuario(username):
    url = f'{base_url}/users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
#UI/UX-Streamlit:

def ui():
    st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">', unsafe_allow_html=True)
    st.title('Pesquisa dos usuários do GitHub !')
    username = st.text_input('busque por um usuário para ver as suas informações')

    if st.button('buscar'):
        infoUsuario = selecionarUsuario(username)
        if infoUsuario is not None:
            #st.write(infoUsuario)
            st.markdown(f'''
                        <div class="card" style="width: 18rem;">
                        <img src="{infoUsuario['avatar_url']}" class="card-img-top" alt="avatar">
                        <div class="card-body">
                            <h5 class="card-title">usuário: {infoUsuario['login']}</h5>
                            <p class="card-text">Bio: {infoUsuario['bio']}</p>
                            <a href="{infoUsuario['html_url']}" class="btn">visualizar perfil</a>
                        </div>
                        </div>
                        ''', unsafe_allow_html=True)
        else:
            st.write('usuário não encontrado!')


ui()