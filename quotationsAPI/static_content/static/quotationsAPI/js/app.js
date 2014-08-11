$( document ).ready(function() {

	//GET
	function get_quotations() {
		$.get( "/quotations/", function( data ) {
			results = data['results'];
			$("li").remove();			
			for (var i=0; i<results.length; i++) {
				$( "#quotelist" ).append( '<li>' + results[i]['text'] + '</li>' );	  	
			}
		});		
	}

	//POST
	var csrftoken = $.cookie('csrftoken');
	function csrfSafeMethod(method) {
	    // these HTTP methods do not require CSRF protection
	    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    }
	});

	$( "#quote_form" ).submit(function(e) {
		e.preventDefault(); //prevent submission
		$.ajax({
			type: "POST",
			url: "/quotations/",
			data: $( "#quote_form" ).serialize(),
			success: function() { get_quotations(); }
		});
		return false; //avoid redirection
	});	

	get_quotations();

});
