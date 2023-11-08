function selecionar_livro(id_livro) {
  $.get({
    url: "selecionarlivro",
    data: { id_livro: id_livro },
    success: (response) => {
      $("#livro_selecionado").html(response);
    },
  });
}

function executar_livro() {
  $("#livro").click(() => {
    $("#pesquisa").html("");
    $("#livro").addClass("bi-book text-bg-dark rounded-2");
    $("#autor").removeClass("bi-book text-bg-dark rounded-2");
    $("#emprestimo").removeClass("bi-book text-bg-dark rounded-2");

    $.get({
      url: "livro",
      success: (response) => {
        $("#cenario").html(response);

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

        $("#id_nome_autor").keyup(() => {
          let nome = $("#id_nome_autor").val();
          $.get({
            url: "pesquisarautor",
            data: { nome: nome },
            success: (response) => {
              $("#pesquisa").html(response);

              // selecionar autor
              let selecionar =
                document.getElementsByClassName("selecionar_autor");
              for (let i = 0; i < selecionar.length; i++) {
                selecionar[i].addEventListener("click", () => {
                  selecionar_autor(selecionar[i].value);
                  $("#id_nome_autor").val("");
                });
              }
            },
          });
        });

        $("#gravar").click(() => {
          let nome = $("#id_nome_livro").val();
          let autor = $("#codigo_autor").html();
          let exemplares = $("#exemplares").val();

          $.get({
            url: "gravarlivro",
            data: { nome: nome, autor: autor, exemplares: exemplares },
            success: (response) => {
              $("#id_nome_livro").val("");
              $("#exemplares").val("");
              alert(response);
            },
          });
        });
      },
    });
  });
}
