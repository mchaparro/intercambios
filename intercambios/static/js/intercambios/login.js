$(document).ready(function() {
    $('.tab1').click(function(){
	    $('#tab2').hide();
	    $('.tab1 a').css({'color':'#D5405B'});
	    $('.tab2 a').css({'color':'#428bca'});
	    $('#tab1').fadeIn();
	    document.getElementById('submit').scrollIntoView();
    });
    
	color:
     $('.tab2').click(function(){
	    $('#tab1').hide();
	    $('#tab2').fadeIn();
	    $('.tab2 a').css({'color':'#D5405B'});
	    $('.tab1 a').css({'color':'#428bca'});
	    document.getElementById('submit2').scrollIntoView();
    });
});


