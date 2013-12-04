$(document).ready(function() {
	
	$('.borrar-evento').click(function(){
			 var evento = $(this).attr('name');
			 var eventoID = $(this).attr('id');
			 bootbox.confirm("<h1 class='Diamond'>Deseas eliminar el evento <span class='rojo'>"+evento+"</span>?</h1>", function(result) {
				  if(result){
					  
							 $.ajax({
								 type:'POST',
								 url: '/cancelar/evento/',
								 dataType: 'json',
								 data: {'evento':eventoID},
								 success: function(response) {
									$('#evento-'+eventoID).remove();
									 noty({text: '<h1 class="Diamond">Se elimino el evento '+evento+'</h1>' , type: 'success',timeout: 5000,});
								 },
								 error: function(XMLHttpRequest, textStatus, errorThrown) {
									 //TODO Place proper error message 
									 console.log(XMLHttpRequest);
								 }  
							 }); 
					  
				  }
				}); 
			 
		 
		 });
		 

});


