$( document ).ready(function() {

	function get_quotations() {
		$.get( "/quotations/", function( data ) {
			results = data['results'];
			$("li").remove();			
			for (var i=0; i<results.length; i++) {
				$( "#quotelist" ).append( '<li>' + results[i]['text'] + '</li>' );	  	
			}
		});		
	}

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

	//POST
	$( "#quote_form" ).submit(function(e) {

		//prevent submission
		e.preventDefault();

		$.ajax({
			type: "POST",
			url: "/quotations/",
			data: $( "#quote_form" ).serialize(),
			success: function() { get_quotations(); }
		});

		//avoid redirection
		return false;
	});	

	get_quotations();

});
