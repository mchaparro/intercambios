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
	    
});


