$(document).ready(function() {
    $("input#btn_translate").click(function() {
        let val = $('input#language_code').val();
        $.ajax({
            type: "GET",
            url: "https://hellosalut.stefanbohacek.dev/?lang="  +  val,
            success: function(data) {
                $('div#hello').html(data.hello);
            }
        });
    });
});
