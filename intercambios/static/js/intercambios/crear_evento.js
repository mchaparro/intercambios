$(document).ready(function() {
		
		$('.participantes').keypress(function(e){
			//Checks if keycode is backspace, left-arrow, right-arrow, tab or enter
			if (/^8$|^37$|^39$|^13$|^9$|^46$/.test(e.keyCode) && !e.shiftKey)
				return;
			
		var longitud= $(this).val().length;
		if (e.charCode < 48 || e.charCode > 57)
		        return false;
		if (longitud > 2)
			return false;
		
		});
		$('.precio').keypress(function(e){
			//Checks if keycode is backspace, left-arrow, right-arrow, tab or enter
			if (/^8$|^37$|^39$|^13$|^9$|^46$/.test(e.keyCode) && !e.shiftKey)
				return;
			
		$(this).formatCurrency({ roundToDecimalPlace: -2 });
		var longitud= $(this).val().length;
		if (e.charCode < 48 || e.charCode > 57)
		        return false;
		if (longitud > 8)
			return false;
		});
		
		$('.nombre_evento').keypress(function(e){
		var longitud= $(this).val().length;
		if (longitud > 19)
			return false;
		});
		
		$('.fecha').datepicker({minDate: 0}).attr('readonly', 'readonly');
	    
	    $('#crear_evento').click(function(){
			var evento = $('.nombre_evento').val();
			if (evento.length < 1){
					noty({text: '<h1 class="Diamond">Por favor ingresa nombre</h1>' ,
					 type: 'warning',timeout: 5000,});
				return;
				}
			var fecha = $('.fecha').val();
			if (fecha.length < 1){
					noty({text: '<h1 class="Diamond">Por favor ingresa fecha</h1>' ,
					 type: 'warning',timeout: 5000,});
				return;
				}
			var participantes = $('.participantes').val();
			
			if (parseInt(participantes) < 2){
					noty({text: '<h1 class="Diamond">Tu evento debe tener por lo menos 2 participantes</h1>' ,
					 type: 'warning',timeout: 5000,});
				return;
				}
			var precio = $('.precio').val();
			if (precio.length < 1){
					noty({text: '<h1 class="Diamond">Por favor ingresa precio</h1>' ,
					 type: 'warning',timeout: 5000,});
				return;
				}
					
					
					
				 $.ajax({
					 type:'POST',
					 url: '/crear/evento/',
					 dataType: 'json',
					 data: $('#form_crear').serialize(),
					 success: function(response) {
						 window.location.href = "/detalles/evento/" + response.evento + "/";
					 },
					 error: function(XMLHttpRequest, textStatus, errorThrown) {
					
					 }  
				 }); 
		 
	 });
});


