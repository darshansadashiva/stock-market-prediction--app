// register
$("#btn_createAccount").click(function () {
    debugger;
    var name = document.getElementById('name').value;
    var username = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var gender = document.getElementById('gender').value;
    var pswd = document.getElementById('pswd').value;
    var cfpswd = document.getElementById('cfpswd').value;

    var namePattern = /^[a-zA-Z]+(?: [a-zA-Z]+)*$/;
    var emailPatten = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    var pswdPattern = /^[^\s]{1,10}$/;


    if (!namePattern.test(name)) {
        alert("Invalid Name!");
        return false;
    }

    if (!emailPatten.test(email)) {
        alert("Invalid Email!");
        return false;
    }

    if (gender == "Gender") {
        alert("Please Select Gender!");
        return false;
    }

    if (!pswdPattern.test(pswd)){
        alert("Max 10 character with no space");
        return false;
    }

    if (cfpswd != pswd ){
        alert("Password does't match!");
        return false;
    }

    $.ajax({
        type: "GET",
        url: "/regdata",
        contentType: "application/json;charset=UTF-8",
        data: {
            "username": username,
            "name": name,
            "email": email,
            "gender": gender,
            "pswd": pswd,
            "cfpswd": cfpswd
        },
        dataType: "json",
        success: function (result) {
            alert('Data Saved Successfully');
            window.location = "register";
        },
        failure: function (result) {
            alert('Data Saving Failed');
        }
    });

});

// login
$("#btn_acceseAccount").click(function () {
    var username = document.getElementById('username').value;
    var pswd = document.getElementById('pswd').value;

    $.ajax({
        type: "GET",
        url: "/logdata",
        contentType: "application/json;charset=UTF-8",
        data: {
            "username": username,
            "pswd": pswd
        },
        dataType: "json",
        success: function (result) {
            if (result == "Success") {
                alert('Logged in Successfully');
                window.location = "\streamlit_app.py";
            }
            else {
                alert('Credentials not found');
                window.location = "register";
            }
        },
        failure: function (result) {
            alert('Data Saving Failed');
        }
    });
});