function selecionar_autor(id_autor) {
  $.get({
    url: "selecionarautor",
    data: { id_autor: id_autor },
    success: (response) => {
      $("#autor_selecionado").html(response);
    },
  });
}

function resetar_campos() {
  $("#gravar").show();
  $("#atualizar").hide();
  $("#deletar").hide();
  $("#id_nome_autor").val('');
  $("#autor_selecionado").html('');
  $("#pesquisa").html('');
}
function executar_autor() {
  // Autor
  $("#autor").click(() => {
    $("#pesquisa").html("");
    $("#livro").removeClass("bi-book text-bg-dark rounded-2");
    $("#autor").addClass("bi-book text-bg-dark rounded-2");
    $("#emprestimo").removeClass("bi-book text-bg-dark rounded-2");

    $.get({
      url: "autor",
      success: (response) => {
        $("#cenario").html(response);
        $("#atualizar").hide();
        $("#deletar").hide();

        $("#id_nome_autor").keyup(() => {
          let nome = $("#id_nome_autor").val();

          $.get({
            url: "pesquisarautor",
            data: { nome: nome },
            success: (response) => {
              $("#pesquisa").html(response);

              let selecionar =
                document.getElementsByClassName("selecionar_autor");
              for (let i = 0; i < selecionar.length; i++) {
                selecionar[i].addEventListener("click", () => {
                  selecionar_autor(selecionar[i].value);
                  $("#id_nome_autor").val("");
                  $("#gravar").hide();
                  $("#atualizar").show();
                  $("#atualizar").val(selecionar[i].value);
                  $("#deletar").show();
                  $("#deletar").val(selecionar[i].value);
                });
              }
            },
          });
        });

       
        $("#atualizar").click(() => {
          let id_autor = $("#atualizar").val();
          let nome = $("#id_nome_autor").val();

          $.get({
            url: "atualizarautor",
            data: { id_autor: id_autor, nome: nome },
            success: (response) => {
               exibir_mensagem(response);
               resetar_campos();
             
            },
          });
        });


        $("#deletar").click(() => {
          let id_autor = $("#deletar").val();

          $.get({
            url: "deletarautor",
            data: { id_autor: id_autor },
            success: (response) => {
               exibir_mensagem(response);
               resetar_campos();
            },
          });
        });

        $("#gravar").click(() => {
          let nome = $("#id_nome_autor").val();

          $.get({
            url: "gravarautor",
            data: { nome: nome },
            success: (response) => {
              exibir_mensagem(response);
              resetar_campos();
            },
          });
        });
      },
    });
  });
}
