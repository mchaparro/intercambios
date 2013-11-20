$(document).ready(function() {
		
		$('#participantes').keypress(function(e){
		var longitud= $(this).val().length;
		console.log(longitud);
		if (e.keyCode < 48 || e.keyCode > 57)
		        return false;
		if (longitud > 2)
			return false;
		
		});
		$('#precio').keypress(function(e){
		$(this).formatCurrency({ roundToDecimalPlace: -2 });
		var longitud= $(this).val().length;
		console.log(longitud);
		if (e.keyCode < 48 || e.keyCode > 57)
		        return false;
		if (longitud > 8)
			return false;
		});
		
		$('#nombre_evento').keypress(function(e){
		var longitud= $(this).val().length;
		if (longitud > 19)
			return false;
		});
		
			
	   $('#fecha').datepicker({
	    });
	    
});


