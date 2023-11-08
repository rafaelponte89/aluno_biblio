function executar_emprestimo() {
  $("#emprestimo").click(() => {
    $("#pesquisa").html("");
    $("#cenario").html("");
    $("#livro").removeClass("bi-book text-bg-dark rounded-2");
    $("#autor").removeClass("bi-book text-bg-dark rounded-2");
    $("#emprestimo").addClass("bi-book text-bg-dark rounded-2");
    $.get({
      url: "emprestimo",
      success: (response) => {
        $("#pesquisa").html("");
        $("#cenario").html(response);

        $("#gravar").click(() => {
          let livro = $("#codigo_livro").html();
          let aluno = $("#codigo_aluno").html();
          let retirada = $("#data_emprestimo").val();

          $.get({
            url: "gravaremprestimo",
            data: { livro: livro, aluno: aluno, retirada: retirada },
            success: (response) => {
              $("#id_nome_livro").val("");
              $("#id_nome_aluno").val("");
              alert(response);
            },
          });
        });

        $("#id_nome_livro").keyup(() => {
          let nome_livro = $("#id_nome_livro").val();
          $.get({
            url: "pesquisarlivro",
            data: { nome_livro: nome_livro },
            success: (response) => {
              $("#pesquisa").html(response);
              let selecionar =
                document.getElementsByClassName("selecionar_livro");
              for (let i = 0; i < selecionar.length; i++) {
                selecionar[i].addEventListener("click", () => {
                  selecionar_livro(selecionar[i].value);
                  $("#id_nome_livro").val("");
                });
              }
            },
          });
        });

        $("#id_nome_aluno").keyup(() => {
          let nome_aluno = $("#id_nome_aluno").val();
          $.get({
            url: "pesquisaraluno",
            data: { nome_aluno: nome_aluno },
            success: (response) => {
              $("#pesquisa").html(response);
              let selecionar =
                document.getElementsByClassName("selecionar_aluno");
              for (let i = 0; i < selecionar.length; i++) {
                selecionar[i].addEventListener("click", () => {
                  selecionar_aluno(selecionar[i].value);
                  $("#id_nome_aluno").val("");
                });
              }
            },
          });
        });
      },
    });
  });
}
