$(document).ready(function() {
	
	$('#csrf').val(getCookie('csrftoken'));
	
	
	//Make table links use colorbox plugin to display admin features
	$('a.colorbox-link').colorbox({
		trapFocus:false,
		onComplete:function(){
			$("#crud-table-title").text($("#cboxTitle").text());
			
			$('.close-colorbox').click(function(){
				$.colorbox.close();
			});
			
		},
		onCleanup:function(){
			$('.select2-drop').hide();
		}
	});
	
//format int into digits separeted with commas
	Number.prototype.formatMoney = function(c, d, t){
		var n = this, 
		c = isNaN(c = Math.abs(c)) ? 2 : c, 
				d = d == undefined ? "." : d, 
						t = t == undefined ? "," : t, 
								s = n < 0 ? "-" : "", 
										i = parseInt(n = Math.abs(+n || 0).toFixed(c)) + "", 
										j = (j = i.length) > 3 ? j % 3 : 0;
										return s + (j ? i.substr(0, j) + t : "") + i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + t) + (c ? d + Math.abs(n - i).toFixed(c).slice(2) : "");
	};
});


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({
    headers: { "X-CSRFToken": getCookie("csrftoken") }


});


