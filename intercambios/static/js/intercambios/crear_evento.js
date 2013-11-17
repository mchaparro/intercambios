$(document).ready(function() {
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


