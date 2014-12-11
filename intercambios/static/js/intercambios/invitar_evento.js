$(document).ready(function(){
	$.fn.modal.Constructor.prototype.enforceFocus = function() {};
	$("#usuarios").select2({placeholder: "Selecciona un usuario:"});
	
	$(".select2-input").focus(function(){
		$('#enviado').html('');
		
	});
	$('#enviar-invitacion').click(function(){
		var usuarios_invitacion = $('#usuarios').val();
		$.ajax({
			type:'POST',
			url: '/invitacion/evento/'+eventoID+'/',
			dataType: 'json',
			beforeSend: function() {
			    // $('#loading-gif').show();
			},
		    complete: function(){
			     //$('#loading-gif').hide();
			},
			data: { usuarios : JSON.stringify(usuarios_invitacion) },
			success: function(response) {
				$('#enviado').html('Se envio la invitaci&oacute;n a los usuarios seleccionados <span style="color:green" class="glyphicon glyphicon-ok"></span>');
			},
			error: function(XMLHttpRequest, textStatus, errorThrown) {
				//TODO Place proper error message 
           		alert(':(');
       		}  
		});
		
		
	});
});