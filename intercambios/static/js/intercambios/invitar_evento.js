$(document).ready(function(){
	$.fn.modal.Constructor.prototype.enforceFocus = function() {};
	$("#usuarios").select2({placeholder: "Selecciona un usuario:"});
	
	
	$('#enviar-invitacion').click(function(){
		$.ajax({
			type:'POST',
			url: '/invitar/evento/'+eventoID+'/',
			dataType: 'json',
			beforeSend: function() {
			    // $('#loading-gif').show();
			},
		    complete: function(){
			     //$('#loading-gif').hide();
			},
			data: { 'invitarUsuarios' : $('#usuarios').val()},
			success: function(response) {
				
			},
			error: function(XMLHttpRequest, textStatus, errorThrown) {
				//TODO Place proper error message 
           		alert(':(');
       		}  
		});
		
		
	});
});