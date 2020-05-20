var div = document.getElementsByClassName("caminho")[0];
var input = document.getElementById("selecao-arquivo");
var button = document.getElementById("testee");

div.addEventListener("click", function(){
    input.click();
});
input.addEventListener("change", function(){
    var nome = "";
    if(input.files.length > 0) nome = input.files[0].name;
    button.click();
    div.innerHTML = ' ' + nome;
});