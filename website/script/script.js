//<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.5/jquery.min.js"></script> //JS values->Python
function sign_in(){
    const e_mail = document.getElementById("str_Email").value;
    const password = document.getElementById("str_Password").value;
    const arr_data = ["E-mail " + e_mail,"Password " + password];

    const str_arr_data = JSON.stringify(arr_data)
    console.log(str_arr_data);
    alert(str_arr_data);

    $.ajax({
        url:"/text",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(str_arr_data)
    });
}