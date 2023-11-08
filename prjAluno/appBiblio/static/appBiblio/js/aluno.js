function selecionar_aluno(id_aluno) {
  $.get({
    url: "selecionaraluno",
    data: { id_aluno: id_aluno },
    success: (response) => {
      $("#aluno_selecionado").html(response);
    },
  });
}
