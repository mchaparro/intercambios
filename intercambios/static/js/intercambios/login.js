$(document).ready(function() {
		
$('#crear-cuenta').click(function(){
		$('.login-form').html(''+
				'<h2>Crear Cuenta</h2>'+
				'<input name="username" type="text" style="" class="form-control " placeholder="Usuario" value="">'+
				'<input name="nombre" type="text" style="" class="form-control " placeholder="Nombre" value="">'+
				'<input name="password" type="password" class="form-control" placeholder="Clave" value="">'+
				'<button name="submit" id="submit" value="" type="submit" class="btn btn-large btn-danger">Crear Cuenta</button></form>');
		
	});

});


