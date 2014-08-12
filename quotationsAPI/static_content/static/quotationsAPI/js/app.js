$( document ).ready(function() {

	function get_all_authors() {
		get_authors("author_select_1");
		get_authors("author_select_2");			
	}

	function get_all_subjects() {
		get_subjects("subject_select_1");	
		get_subjects("subject_select_2");		
	}

	//GET
	function get_quotations(url) {
		if(arguments.length == 1) {
			url = url;
		} else {
			url = "/quotations/";
		}
		$.get( url, function( data ) {
			results = data['results'];
			$("li").remove();			
			for (var i=0; i<results.length; i++) {
				$( "#quotelist" ).append( '<li>' + results[i]['text'] + '</li>' );	  	
			}
		});		
	}

	function get_authors(selector) {
		$.get( "/authors/", function( data ) {
			results = data['results'];
			$("#" + selector + " option").remove();			
			for (var i=0; i<results.length; i++) {
				$( "#" + selector ).append( '<option value=' + results[i]['id'] + '>' + results[i]['first_name'] + " " + results[i]['last_name'] + '</option>' );	  	
			}
		});		
	}	

	function get_subjects(selector) {
		$.get( "/subjects/", function( data ) {
			results = data['results'];
			$("#" + selector + " option").remove();			
			for (var i=0; i<results.length; i++) {
				$( "#" + selector ).append( '<option value=' + results[i]['id'] + '>' + results[i]['name'] + '</option>' );	  	
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

	$( "#author_form" ).submit(function(e) {
		e.preventDefault(); //prevent submission
		$.ajax({
			type: "POST",
			url: "/authors/",
			data: $( "#author_form" ).serialize(),
			success: function() { get_all_authors(); }
		});
		return false; //avoid redirection
	});		

	$( "#subject_form" ).submit(function(e) {
		e.preventDefault(); //prevent submission
		$.ajax({
			type: "POST",
			url: "/subjects/",
			data: $( "#subject_form" ).serialize(),
			success: function() { get_all_subjects(); }
		});
		return false; //avoid redirection
	});		


	$( "#quote_select_form" ).submit(function(e) {
		e.preventDefault(); //prevent submission
		get_quotations("/quotations/?author=" + $("#author_select_2").val() + "&subject=" + $("#subject_select_2").val());
		return false; //avoid redirection
	});		

	get_quotations();
	get_all_authors();
	get_all_subjects();		

});
