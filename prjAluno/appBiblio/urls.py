
from django.urls import path, re_path
from .views import biblio
from .views import exibir_autor, gravar_autor, pesquisar_autor, selecionar_autor, atualizar_autor, deletar_autor
from .views import gravar_livro, pesquisar_livro, exibir_livro, selecionar_livro
from .views import exibir_emprestimo, gravar_emprestimo
from .views import selecionar_aluno, pesquisar_aluno

urlpatterns = [
    path("biblio", biblio , name="biblio"),
    path("autor", exibir_autor, name="autor"),
    path("gravarautor", gravar_autor, name="gravarautor"),
    path("pesquisarautor", pesquisar_autor, name="pesquisarautor"),
    path("selecionarautor", selecionar_autor, name="selecionarautor"),
    path("atualizarautor", atualizar_autor, name="atualizarautor"),
     path("deletarautor", deletar_autor, name="deletarautor"),
    
    path("livro", exibir_livro, name="livro"),
    path("gravarlivro", gravar_livro, name="gravarlivro"),
    path("pesquisarlivro", pesquisar_livro, name="pesquisarlivro"),
    path("selecionarlivro", selecionar_livro, name="selecionarlivro"),

    
    path("emprestimo", exibir_emprestimo, name="emprestimo"),
    
    path("selecionaraluno", selecionar_aluno, name="selecionaraluno"),
    path("pesquisaraluno", pesquisar_aluno, name="pesquisaraluno"),
    
    path("gravaremprestimo", gravar_emprestimo, name="gravaremprestimo"),

    
    
]