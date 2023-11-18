// This script resizes the weather box text depending on how long the text is

$(document).ready(function () {
  resize_to_fit();
});

function resize_to_fit(){
    var fontsize = $('div#weatherforecastbox p').css('font-size');
    $('div#weatherforecastbox p').css('fontSize', parseFloat(fontsize) - 1);

    if($('div#weatherforecastbox p').height() >= $('div#weatherforecastbox').height()){
        resize_to_fit();
    }
}