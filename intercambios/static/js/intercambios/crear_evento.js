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
	    

	   //Validar la forma
	   $('#crear_evento').click(function(e){
		   e.preventDefault();
		  //validar 
		   if($('#nombre_evento').val().length > 20){
			  
			   if($('#nombre_evento').qtip('api'))  $('#nombre_evento').qtip('api').show();
			   // No tooltip present, create it
			   else
			   {
				   $('#nombre_evento').qtip(
			      {
			         content: 'Some basic content for the tooltip', 
			         show: {
			            when: 'click',
			            ready: true
			         }
			      });
			   }
			   
			   
			   
			   console.log('o nopis!!!!');		   
		   
		   }
	   });
});


