$(document).ready(function() {
    $('input').hover(function() {
        $(".tooltip").hide()
        var tooltip = $('div#'+$(this).attr('id')+'_tooltip.tooltip')
        tooltip.show();
    },function() {
        $(".tooltip").hide()
        var tooltip = $('div#'+$(this).attr('id')+'_tooltip.tooltip')
        tooltip.hide();
    }).keyup(function() {
        $(".tooltip").hide()
        var tooltip = $('div#'+$(this).attr('id')+'_tooltip.tooltip')
        tooltip.show();
    }).focus(function() {
        $(".tooltip").hide()
        var tooltip = $('div#'+$(this).attr('id')+'_tooltip.tooltip')
        tooltip.show();
    }).blur(function() {
        $(".tooltip").hide()
        var tooltip = $('div#'+$(this).attr('id')+'_tooltip.tooltip')
        tooltip.hide();
    });
    $('.tooltip').hover(function() {
        $(this).hide();
    });

    var updatematch = function() {
        var newpass = $("input#newpassword").val();
        var conpass = $("input#conpassword").val();
        if (newpass == conpass) {
            $('#conpassword_tooltip #match').removeClass('invalid').addClass('valid');
        } else {
            $('#conpassword_tooltip #match').removeClass('valid').addClass('invalid');
        }
    }

    $('input#newpassword').keyup(function() {
        var pswd = $(this).val();
        //validate the length
        if ( pswd.length < 8 ) {
            $('#newpassword_tooltip #length').removeClass('valid').addClass('invalid');
        } else {
            $('#newpassword_tooltip #length').removeClass('invalid').addClass('valid');
        }
        //validate letter
        if ( pswd.match(/[a-z]/) ) {
            $('#newpassword_tooltip #letter').removeClass('invalid').addClass('valid');
        } else {
            $('#newpassword_tooltip #letter').removeClass('valid').addClass('invalid');
        }
        //validate capital letter
        if ( pswd.match(/[A-Z]/) ) {
            $('#newpassword_tooltip #capital').removeClass('invalid').addClass('valid');
        } else {
            $('#newpassword_tooltip #capital').removeClass('valid').addClass('invalid');
        }
        //validate number
        if ( pswd.match(/\d/) ) {
            $('#newpassword_tooltip #number').removeClass('invalid').addClass('valid');
        } else {
            $('#newpassword_tooltip #number').removeClass('valid').addClass('invalid');
        }
        //validate symbols
        if ( pswd.match(/[^A-z0-9]/) ) {
            $('#newpassword_tooltip #symbol').removeClass('invalid').addClass('valid');
        } else {
            $('#newpassword_tooltip #symbol').removeClass('valid').addClass('invalid');
        }
        //password meter
        var result = zxcvbn(pswd);
        $("meter").val(result.score);
        updatematch();
    });
    $('input#conpassword').keyup(updatematch);
});
