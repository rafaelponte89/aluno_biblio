from django.shortcuts import render, HttpResponse
from .models import Autor, Livro, Aluno, FichaEmprestimo
from django.db.models.deletion import RestrictedError
# Create your views here.



def padronizar_nome(nome):
    """Eliminar sinais sonoros, acentuações e manter todas maiúsculas"""
    acentuados = {'Á':'A','Ã':'A','Â':'A','É':'E','Ê':'E','Í':'I','Î':'I','Ó':'O','Õ':'O','Ô':'O','Ú':'U','Û':'U','Ç':'C','\'':'','\`':''}   
    #acentuados = {'Á':'A','Ã':'A','Â':'A','É':'E','Ê':'E','Í':'I','Î':'I','Ó':'O','Õ':'O','Ô':'O','Ú':'U','Û':'U'}   

    letra_nova = ''
    for letra in nome:
        if letra in acentuados.keys():
            letra_nova = acentuados[letra]
            nome = nome.replace(letra, letra_nova)
            
    return nome.rstrip(' ').lstrip(' ').upper()
  
def criarMensagem(texto, tipo):
    
    mensagem = HttpResponse(f"<div style='display:block;' class='alert alert-{tipo}' role='alert' >{texto} </div>")
    return  mensagem

def biblio(request):
    total_livros = ""
    livros_emprestados = ""
    livros_disponiveis = ""
    alunos_ativos = ""
    top10 = ""

    context = {
        'livros': total_livros,
        'emprestados': livros_emprestados,
        'disponiveis': livros_disponiveis,
        'alunos_ativos': alunos_ativos,
        'top10': top10

    }
    return render(request, 'biblio.html', context)


def exibir_autor(request):
    tela_autor = """<div id="autor_pesquisa" class="row mt-2 bg-body-secondary rounded-3">
    <input
      type="hidden"
      name="csrfmiddlewaretoken"
    />
    <div id="autor_selecionado" class="row">
     <div class="col-md">
      <span>Selecionado:  </span>
     </div>
    </div>
    
    <div class="col-sm-8 p-3">
      <div class="input-group">
        <div class="input-group-prepend">
          <span class="input-group-text bg-dark text-white" id="basic-addon1"
            ><i class="bi bi-search"></i
          ></span>
        </div>
        <input
          type="text"
          name="nome_autor"
          maxlength="100"
          class="form-control formulario"
          placeholder="Nome do Autor"
          aria-describedby="basic-addon1"
          required=""
          id="id_nome_autor"
        />
      </div>
    </div>
    <div class="col-sm-4 d-flex justify-content-center">
      <button
        id="gravar"
        class="btn btn-outline-dark m-3"
        title="Registrar Autor"
      >
        Gravar
      </button>
       <button
        id="atualizar"
        class="btn btn-primary m-3"
        title="Atualizar Autor"
        class="invisible"
      >
        Atualizar
      </button>
          <button
        id="deletar"
        class="btn btn-danger m-3"
        title="Deletar Autor"
        class="invisible"
        
      >
        Deletar
      </button>
    </div>
  </div>  
  """
    return HttpResponse(tela_autor)


def gravar_autor(request):
    try:
        nome = padronizar_nome(request.GET.get('nome'))
        autor = Autor(nome=nome)
        autor.save()
        return criarMensagem("Autor salvo com sucesso", "success")
    except:
        return criarMensagem("Aconteceu um erro", "danger")

def atualizar_autor(request):
    try:
        codigo_autor = int(request.GET.get("id_autor"))
        nome = padronizar_nome(request.GET.get("nome"))
        autor = Autor.objects.get(pk=codigo_autor)
        autor.nome = nome
        autor.save()
        return criarMensagem("Autor atualizado com Sucesso", "success")
    except Exception:
        return criarMensagem("Aconteceu um erro", "danger")
    

def deletar_autor(request):
    try:
        codigo_autor = request.GET.get("id_autor")
        autor = Autor.objects.get(pk=codigo_autor)
        autor.delete()
        return criarMensagem("Autor deletado com sucesso!", "success")
    except RestrictedError:
        return criarMensagem("Restrição ao Deletar, Autor Vinculado!", "danger")
  
def selecionar_autor(request):
    codigo_autor = request.GET.get("id_autor")
    print(codigo_autor)
    autor = Autor.objects.get(pk=codigo_autor)
    return HttpResponse(f"<div class='col-sd-12'> <strong>Autor Selecionado: </strong> \
                        <span> {autor.nome} </span> \
                         <strong> Código: </strong><span id='codigo_autor'>{autor.codigo}</span> </div>")


def pesquisar_autor(request):
    nome = request.GET.get('nome')
    linhas = ""
    print(nome)
    autor = Autor.objects.filter(nome__contains=nome)[:10]
    if len(autor) == 0:
        tabela = f"""
      <table class="table table-hover mt-3"><tr><td> Nenhum autor encontrado! </td>
       </tr></table>
      """
    else:
        for a in autor:
            linhas += f"<tr><td>{a.nome}</td> <td><button value={a.codigo} class='btn btn-success selecionar_autor' tooltip={a.codigo}> <i class='bi bi-check-lg'></i> </button> </td></tr>"
        tabela = f"""
        
        <div class="col-md-12">
        <table class="table table-hover mt-3">
        
          <tr><th>Nome do Autor</th> <th>Selecionar</th></tr>
         
          {linhas}       
        </table>
        </div>
    
    """
    return HttpResponse(tabela)


def excluir_autor(request):
    pass


def exibir_livro(request):
    livro = """<div class="row mt-2 bg-body-secondary rounded-3">
    <input
      type="hidden"
      name="csrfmiddlewaretoken"
    />
         <div class="row">
     
     <div id="autor_selecionado" class="col-md-6">
     <div class="col-md">
      <span>Selecionado: <span id="selecionado"> </span>  </span>
     </div>
    </div>
    <div id="livro_selecionado" class="col-md-6">
     <div class="col-md">
      <span>Selecionado: <span id="selecionado"> </span>  </span>
     </div>
    </div>
    </div>
    
     <div class="col-sm-5 p-3">
      <div class="input-group">
        <div class="input-group-prepend">
          <span class="input-group-text bg-dark text-white" id="basic-addon1"
            ><i class="bi bi-search"></i
          ></span>
        </div>
        <input
          type="text"
          name="nome_autor"
          maxlength="100"
          class="form-control formulario"
          placeholder="Nome do Autor"
          aria-describedby="basic-addon1"
          required=""
          id="id_nome_autor"
        />
      </div>
    </div>
    
    <div class="col-sm-5 p-3">
      <div class="input-group">
        <div class="input-group-prepend">
          <span class="input-group-text bg-dark text-white" id="basic-addon1"
            ><i class="bi bi-search"></i
          ></span>
        </div>
        <input
          type="text"
          name="nome_livro"
          maxlength="100"
          class="form-control formulario"
          placeholder="Nome do Livro"
          aria-describedby="basic-addon1"
          required=""
          id="id_nome_livro"
        />
      </div>
      </div>
      <div class="col-sm-1 p-3">
        <input
          type="number"
          name="exemplares"
          maxlength="100"
          class="form-control formulario"
          placeholder="Exemplares"
          aria-describedby="basic-addon1"
          required=""
          value=0
          id="exemplares"
        />
      </div>
    <div class="col-sm-1 d-flex justify-content-center">
      <button
        id="gravar"
        class="btn btn-outline-dark m-3"
        title="Registrar Livro"
      >
        Gravar
      </button>
    </div>
  </div>  
  """
    return HttpResponse(livro)


def gravar_livro(request):
    nome_livro = padronizar_nome(request.GET.get("nome"))
    codigo_autor = request.GET.get("autor")
    exemplares = request.GET.get("exemplares")

    autor = Autor.objects.get(pk=codigo_autor)

    livro = Livro(titulo=nome_livro, autor=autor, exemplares=exemplares)
    livro.save()

    return HttpResponse("Livro Salvo Com Sucesso")


def pesquisar_livro(request):

    nome_livro = request.GET.get('nome_livro')
    linhas = ""

    livro = Livro.objects.filter(titulo__contains=nome_livro)[:10]
    if len(livro) == 0:
        tabela = f"""
      <table class="table table-hover mt-3"><tr><td> Nenhum livro encontrado! </td>
       </tr></table>
      """
    else:
        for l in livro:
            linhas += f"<tr><td>{l.titulo}</td> <td>{l.autor}</td> <td>{l.exemplares}</td> <td><button value={l.codigo} class='btn btn-success selecionar_livro'> <i class='bi bi-check-lg'></i></button> </td></tr>"
        tabela = f"""
        
        <div class="col-md-12">
        <table class="table table-hover mt-3">
        
          <tr><th>Nome do Livro</th> <th>Autor</th><th>Exemplares</th> <th>Selecionar</th></tr>
         
          {linhas}       
        </table>
        </div>
    
    """
    return HttpResponse(tabela)


def excluir_livro(request):
    pass


def exibir_emprestimo(request):
    import datetime
    tela_emprestimo = f"""<div class="row mt-2 bg-body-secondary rounded-3">
    <input
      type="hidden"
      name="csrfmiddlewaretoken"
    />
    <div class="row">
     <div id="livro_selecionado" class="col-md-6">
     <div class="col-md">
      <span>Selecionado: <span id="selecionado"> </span>  </span>
     </div>
    </div>
     <div id="aluno_selecionado" class="col-md-6">
     <div class="col-md">
      <span>Selecionado: <span id="selecionado"> </span>  </span>
     </div>
    </div>
    </div>
    
     <div class="col-sm-4 p-3">
      <div class="input-group">
        <div class="input-group-prepend">
          <span class="input-group-text bg-dark text-white" id="basic-addon1"
            ><i class="bi bi-search"></i
          ></span>
        </div>
        <input
          type="text"
          name="nome_livro"
          maxlength="100"
          class="form-control formulario"
          placeholder="Nome do Livro"
          aria-describedby="basic-addon1"
          required=""
          id="id_nome_livro"
        />
      </div>
    </div>
    
    <div class="col-sm-4 p-3">
      <div class="input-group">
        <div class="input-group-prepend">
          <span class="input-group-text bg-dark text-white" id="basic-addon1"
            ><i class="bi bi-search"></i
          ></span>
        </div>
        <input
          type="text"
          name="nome_aluno"
          maxlength="100"
          class="form-control formulario"
          placeholder="Nome do Aluno"
          aria-describedby="basic-addon1"
          required=""
          id="id_nome_aluno"
        />
      </div>
      </div>
      <div class="col-sm-3 p-3">
        <input
          type="date"
          name="data_emprestimo"
          maxlength="100"
          class="form-control formulario"
          aria-describedby="basic-addon1"
          required=""
          value={datetime.datetime.today()}
          id="data_emprestimo"
        />
      </div>
    <div class="col-sm-1 d-flex justify-content-center">
      <button
        id="gravar"
        class="btn btn-outline-dark m-3"
        title="Registrar Empréstimo"
      >
        Gravar
      </button>
    </div>
  </div>  
  """
    return HttpResponse(tela_emprestimo)


def pesquisar_emprestimo(request):
    pass


def cancelar_emprestimo(request):
    pass


def gravar_emprestimo(request):
    codigo_livro = request.GET.get("livro")
    codigo_aluno = request.GET.get("aluno")
    retirada = request.GET.get("retirada")
    livro = Livro.objects.get(pk=codigo_livro)
    aluno = Aluno.objects.get(pk=codigo_aluno)
    emprestimo = FichaEmprestimo(
        livro=livro, aluno=aluno, retirada=retirada, devolucao='2023-11-30')
    emprestimo.save()

    return HttpResponse("Emprestimo Salvo")


def selecionar_livro(request):
    codigo_livro = request.GET.get("id_livro")
    print(codigo_livro)
    livro = Livro.objects.get(pk=codigo_livro)
    return HttpResponse(f"<div > <strong>Livro Selecionado: </strong> \
                        <span> {livro.titulo} </span> \
                         <strong> Código: </strong><span id='codigo_livro'>{livro.codigo}</span> </div>")


def pesquisar_aluno(request):

    nome_aluno = request.GET.get('nome_aluno')
    linhas = ""
    aluno = Aluno.objects.filter(nome__contains=nome_aluno)[:10]
    if len(aluno) == 0:
        tabela = f"""
      <table class="table table-hover mt-3"><tr><td> Nenhum aluno encontrado! </td>
       </tr></table>
      """
    else:
        for a in aluno:
            linhas += f"<tr><td>{a.rm}</td> <td>{a.nome}</td> <td>{a.serie} - {a.turma}</td> <td><button value={a.rm} class='btn btn-success selecionar_aluno'> <i class='bi bi-check-lg'></i></button> </td></tr>"
        tabela = f"""
        
        <div class="col-md-12">
        <table class="table table-hover mt-3">
        
          <tr><th>Registro de Matrícula</th> <th>Nome do Aluno</th><th>Ano/Turma</th> <th>Selecionar</th></tr>
         
          {linhas}       
        </table>
        </div>
    
    """
    return HttpResponse(tabela)


def selecionar_aluno(request):
    codigo_aluno = request.GET.get("id_aluno")
    print(codigo_aluno)
    aluno = Aluno.objects.get(pk=codigo_aluno)
    return HttpResponse(f"<div> <strong>Aluno Selecionado: </strong> \
                        <span> {aluno.nome} </span> \
                         <strong> Código: </strong><span id='codigo_aluno'>{aluno.rm}</span> </div>")
