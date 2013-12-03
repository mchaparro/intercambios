$(document).ready(function() {
	$("#regalo").wScratchPad();		

	 $('#counter').countdown({
         image: '/static/js/countdown/digits.png',
         startTime: dias+':'+horas+':'+minutos+':'+segundos
         
       });
	 
	 
	 
	 
	 $('#generar-intercambio').click(function(){
		 document.getElementById('main-title').scrollIntoView();
		 var faltan = parseInt($('#faltan').text().trim())
		 if (userID == adminID){
			 if (faltan == 0){
				 
				 $.ajax({
					 type:'POST',
					 url: '/generar/intercambio/evento/'+eventoID+'/',
					 dataType: 'json',
					 beforeSend: function() {
						 // $('#loading-gif').show();
					 },
					 complete: function(){
						 //$('#loading-gif').hide();
					 },
					 data: {  },
					 success: function(response) {
							$('#generar-intercambio').hide();
							$('#invitar-participantes').hide();
							noty({text: '<h1 class="Diamond">El sorteo del intercambio se completo con exito ! <br> Podras encontrar el nombre de la perosna que te toco regalarle en la parte inferior de esta p&aacute;gina</h1>' , type: 'success',timeout: 10000,});
					 },
					 error: function(XMLHttpRequest, textStatus, errorThrown) {
						 //TODO Place proper error message 
						 console.log(XMLHttpRequest);
						 
					 }  
				 }); 
			 }
			 else{
				 noty({text: '<h1 class="Diamond">No se puede generar el intercambio hasta que esten registrados todos los participantes</h1>' , type: 'warning',timeout: 10000,});
			 }
			 
		 }
		 else{
			 noty({text: '<h1 class="Diamond">Solo el creador del evento puede generar el intercambio </h1>' , type: 'warning',timeout: 10000,});
		 }
		 
	 });
});


