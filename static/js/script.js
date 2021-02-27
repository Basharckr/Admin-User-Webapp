//  ===========================================================================================
//  ================================Register===================================================
$("#s_button").click(function () {
    console.log("here");
    var fname = $("#idfname").val()
    var fname_len = $("#idfname").val().length
    var lname = $("#idlname").val()
    var uname = $("#iduname").val()
    var uname_len = $("#iduname").val().length
    var email = $("#idemail").val()
    var pass1 = $("#idpass1").val()
    var pass1_len = $("#idpass1").val().length
    var pass2 = $("#idpass2").val()
    var at = email.indexOf("@")
    var dot = email.lastIndexOf(".")
    
    var data = {
         'csrfmiddlewaretoken': '{{csrf_token}}',
        'fname1': fname,
        'lname1':lname,
        'uname1': uname,
        'email1': email,
        'pass_1': pass1,      
    }

    if(fname_len < 3){
        $("#error1").html('First name must be more than 3 characters')
    }
    
    else if (lname === '') {
        $('#error1').html('Pease enter your last_name')

    }
    else if (uname_len < 3) {
        $('#error1').html('Username must be more than 3 characters')

    }
    else if (at<1 || dot<at+2 || dot+2>=email.length) {
        $('#error1').html('Email must be Email format eg:abc@yahoo.com')

    }
    else if (pass1_len < 6) {
        $('#error1').html('Password must be more than 6 characters')

    }
    else if (pass2 === '') {
        $('#error1').html('Please enter your confirm password')

    }
    else if (pass1 !== pass2) {
        $('#error1').html('Your password and confirm passowrd are not same!!!')
    }
    else {
        console.log("hai")
        // create an AJAX call
        $.ajax({
            url: "/",
            method: "POST",
            data: data,
            dataType: 'json',

            // on success
            success: function (data) {
                if (data == 'true') {
                    window.location.replace("login")
                }
                if (data == 'false1') {
                    $('#error1').html(" Username already taken!!!!")
                }
                if (data == 'false2') {
                    $('#error1').html(" Email already taken!!!!")
                }
            }
        })

    }
})

//  ===========================================================================================
//  ================================User-Login===================================================

$("#l_button").click(function(){
    console.log('hii')
    var uname = $("#iduname").val()
    var passw = $("#idpassw").val()
    var data = {
        'csrfmiddlewaretoken': '{{csrf_token}}',
        'name1': uname,
        'pass1': passw,
    }
    console.log('hoo')
    if(uname === ''){
        $("#error1").html("Please enter your username")
    }
    else if(passw === ''){
        $('#error1').html("Please enter your password")
    }
    else{
         // create an AJAX call
        $.ajax({
            url: 'login',
            method: 'POST',
            data: data,
            dataType: 'json',
             // on success

            success: function (data) {
                if(data == 'true'){
                    window.location.replace('home')
                }
                if(data == 'false'){
                    $("#error1").html("Incorrect Username or Password!!!!")
                }
                 
            }
        })
    }
})

//  ===========================================================================================
//  ================================Admin-Login===================================================
$("#a_button").click(function(){
    console.log('hii')
    var uname = $("#iduname").val()
    var passw = $("#idpassw").val()
    var data = {
        'csrfmiddlewaretoken': '{{csrf_token}}',
        'name1': uname,
        'pass1': passw,
    }
    console.log('hoo')
    if(uname === ''){
        $("#error1").html("Please enter your username")
    }
    else if(passw === ''){
        $('#error1').html("Please enter your password")
    }
    else{
         // create an AJAX call
        $.ajax({
            url: '/adminpanel/',
            method: 'POST',
            data: data,
            dataType: 'json',
             // on success

            success: function (data) {
                if(data == 'true'){
                    window.location.replace('home')
                }
                if(data == 'false'){
                    $("#error1").html("Incorrect Username or Password!!!!")
                }
                 
            }
        })
    }
})

//  ===========================================================================================
//  ================================Admin-create user===================================================
$("#ar_button").click(function () {
    console.log("here");
    var fname = $("#idfname").val()
    var fname_len = $("#idfname").val().length
    var lname = $("#idlname").val()
    var uname = $("#iduname").val()
    var uname_len = $("#iduname").val().length
    var email = $("#idemail").val()
    var pass1 = $("#idpass1").val()
    var pass1_len = $("#idpass1").val().length
    var pass2 = $("#idpass2").val()
    var at = email.indexOf("@")
    var dot = email.lastIndexOf(".")

    var data = {
        'csrfmiddlewaretoken': '{{ csrf_token }}',
        'fname1': fname,
        'lname1':lname,
        'uname1': uname,
        'email1': email,
        'pass_1': pass1,      
    }
    if(fname_len < 3){
        $("#error1").html('First name must be more than 3 characters')
    }
    
    else if (lname === '') {
        $('#error1').html('Pease enter your last_name')

    }
    else if (uname_len < 3) {
        $('#error1').html('Username must be more than 3 characters')

    }
    else if (at<1 || dot<at+2 || dot+2>=email.length) {
        $('#error1').html('Email must be Email format eg:abc@yahoo.com')

    }
    else if (pass1_len < 6) {
        $('#error1').html('Password must be more than 6 characters')

    }
    else if (pass2 === '') {
        $('#error1').html('Please enter your confirm password')

    }
    else if (pass1 !== pass2) {
        $('#error1').html('Your password and confirm passowrd are not same!!!')
    }
    else {
        console.log("hai")
        // create an AJAX call
        $.ajax({
            url: "/adminpanel/create/",
            method: "POST",
            data: data,
            dataType: 'json',

            // on success
            success: function (data) {
                if (data == 'true') {
                    window.location.replace("home")
                }
                if (data == 'false1') {
                    $('#error1').html(" Username already taken!!!!")
                }
                if (data == 'false2') {
                    $('#error1').html(" Email already taken!!!!")
                }
            }
        })

    }
})
