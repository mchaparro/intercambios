$(document).ready(function() {
		
$('#crear_cuenta').click(function(){
$('.jumbotron.login').html(' <form class="form-signin" method="post" action="" id="form-signin">{% csrf_token %}<h2>Crear Cuenta</h2><input name="email" type="text" style="" class="form-control " placeholder="E-mail" value="">  <input name="nombre" type="text" style="" class="form-control " placeholder="Nombre" value="">  <input name="password" type="password" class="form-control" placeholder="Clave" value="">  <button name="submit" id="submit" value="" type="submit" class="btn btn-large btn-danger">Crear</button></form>');
});
});


