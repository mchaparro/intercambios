$(document).ready(function() {
	$("#regalo").wScratchPad();		

	 $('#counter').countdown({
         image: '/static/js/countdown/digits.png',
         startTime: dias+':'+horas+':'+minutos+':'+segundos
       });
	 
	 
	 $('.borrar-participante').click(function(){
		 var participante = $(this).attr('name');
		 var participanteID = $(this).attr('id');
		 var faltan = $('#faltan').text();
		 faltan = parseInt(faltan);
		 var total = $('#total-participantes').text();
		 total = parseInt(total);
		 bootbox.confirm("<h1 class='Diamond'>Deseas eliminar a <span class='rojo'>"+participante+"</span></br> de tu intercambio?</h1>", function(result) {
			  if(result){
				  
				  if (parseInt(userID) == parseInt(adminID)){
					  if (parseInt(participanteadminID) != parseInt(participanteID)){
						 $.ajax({
							 type:'POST',
							 url: '/borrar/participante/',
							 dataType: 'json',
							 data: {'participante':participanteID,'evento':eventoID},
							 success: function(response) {
								 var faltan = $('#faltan').text();
								 var total = $('#total-participantes').text();
								 faltan = parseInt(faltan);
								 total = parseInt(total); 
								$('#total-participantes').text(total-1);
								$('#faltan').text(faltan+1);
								
								$('.participante-'+participanteID).remove();
								 noty({text: '<h1 class="Diamond">Se elimino '+participante+' del intercambio </h1>' , type: 'success',timeout: 5000,});
							 },
							 error: function(XMLHttpRequest, textStatus, errorThrown) {
								 //TODO Place proper error message 
								 console.log(XMLHttpRequest);
							 }  
						 }); 
					  }
					  else
						  noty({text: '<h1 class="Diamond">No puedes eliminarte a ti mismo del intercambio </h1>' , type: 'warning',timeout: 5000,});
				  }
				  else{
					  noty({text: '<h1 class="Diamond">Solo el creador del evento puede eliminar participantes </h1>' , type: 'warning',timeout: 5000,});
				  }
				  
			  }
			}); 
		 
	 
	 });
	 
	 
	 $('#generar-intercambio').click(function(){
		 document.getElementById('main-title').scrollIntoView();
		 var faltan = parseInt($('#faltan').text().trim())
		 if (userID == adminID){
			 if (faltan == 0)
				 window.location = '/generar/intercambio/evento/'+eventoID+'/';
			 else
				 noty({text: '<h1 class="Diamond">No se puede generar el intercambio hasta que esten registrados todos los participantes</h1>' , type: 'warning',timeout: 10000,});
		 }
		 else{
			 noty({text: '<h1 class="Diamond">Solo el creador del evento puede generar el intercambio </h1>' , type: 'warning',timeout: 10000,});
		 }
	 });
});


