$(document).ready(function() {
    console.log($("#id_temVarejo").val());
    if ($('#id_temVarejo').prop('checked')) {
        $("div.divBtnVarejo button:contains('SIM')").addClass("btnGreen")
        console.log("verd");
    }
    else {
        $("div.divBtnVarejo button:contains('NÃO')").addClass("btnRed")
        console.log("redous");
    }
})

$("div.divBtnVarejo button").click(function () {

    let temVarejo = $("#id_temVarejo").val()

    if ($(this).html() == "SIM") {
        $(this).addClass("btnGreen")
        $(this).siblings().removeClass("btnRed")
        $("#id_temVarejo").prop('checked', true)
    }
    
    else if ($(this).html() == "NÃO") {
        $(this).addClass("btnRed")
        $(this).siblings().removeClass("btnGreen")
        $("#id_temVarejo").prop('checked', false)
    }
})