$( document ).ready(function() {

	function get_quotations(params) {
		$.get( "/quotations/", params, function( data ) {
			results = data['results'];
			$("li").remove();			
			for (var i=0; i < results.length; i++) {
				$( "#quotelist" ).append( '<li>' + results[i]['text'] + '</li>' );	  	
			}
		});		
	}

	function get_authors() {
		$.get( "/authors/", function( data ) {
			results = data['results'];
			$("select[id^='author_select']").find('option').remove();
			for (var i=0; i < results.length; i++) {
				$( "select[id^='author_select']" ).append( '<option value=' + results[i]['id'] + '>' + results[i]['first_name'] + " " + results[i]['last_name'] + '</option>' );	  						
			}
		});		
	}	

	function get_subjects() {
		$.get( "/subjects/", function( data ) {
			results = data['results'];
			$("select[id^='subject_select']").find('option').remove();
			for (var i=0; i < results.length; i++) {
				$( "select[id^='subject_select']" ).append( '<option value=' + results[i]['id'] + '>' + results[i]['name'] + '</option>' );
			}
		});		
	}	

	/* setup CSRF token for posts */
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
			url: "/subjects/", //this is how we add quote to subject manytomany
			data: {text: $("#add_quote_text").val(), name: $("#subject_select_1").val(), author: $("#author_select_1").val()},
			success: function() { get_quotations({
				author: $("#author_select_2").val(),
				subject: $("#subject_select_2").val()
			});
		}});	

		return false; //avoid redirection
	});	

	$( "#author_form" ).submit(function(e) {
		e.preventDefault(); //prevent submission
		$.ajax({
			type: "POST",
			url: "/authors/",
			data: $( "#author_form" ).serialize(),
			success: function() { get_authors(); }
		});
		return false; //avoid redirection
	});		

	$( "#subject_form" ).submit(function(e) {
		e.preventDefault(); //prevent submission
		$.ajax({
			type: "POST",
			url: "/subjects/",
			data: $( "#subject_form" ).serialize(),
			success: function() { get_subjects(); }
		});
		return false; //avoid redirection
	});		


	$( "#quote_select_form" ).submit(function(e) {
		e.preventDefault(); //prevent submission
		get_quotations({
			author: $("#author_select_2").val(),
			subject: $("#subject_select_2").val()
		});
		return false; //avoid redirection
	});		

	get_quotations();
	get_authors();
	get_subjects();		

});
