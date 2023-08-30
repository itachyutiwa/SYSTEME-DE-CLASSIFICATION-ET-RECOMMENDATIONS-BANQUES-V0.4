$("form[name=signup_form").submit(function (e) {
	var $form = $(this);
	var $error = $form.find(".error");
	var data = $form.serialize();

	$.ajax({
		url: "/user/signup",
		type: "POST",
		data: data,
		dataType: "json",
		success: function (resp) {
			window.location.href = "/dashboard/";
		},
		error: function (resp) {
			$error.text(resp.responseJSON.error).removeClass("error--hidden");
		},
	});

	e.preventDefault();
});

$("form[name=login_form").submit(function (e) {
	var $form = $(this);
	var $error = $form.find(".error");
	var data = $form.serialize();

	$.ajax({
		url: "/user/login",
		type: "POST",
		data: data,
		dataType: "json",
		success: function (resp) {
			window.location.href = "/dashboard/";
		},
		error: function (resp) {
			$error.text(resp.responseJSON.error).removeClass("error--hidden");
		},
	});

	e.preventDefault();
});

$("form[name=predictions_form").submit(function (e) {
	var $form = $(this);
	var $error = $form.find(".error");
	var data = $form.serialize();

	$.ajax({
		url: "/predictions/",
		type: "POST",
		data: data,
		dataType: "json",
		success: function (resp) {
			window.location.href = "/predictions/";
		},
		error: function (resp) {
			$error.text(resp.responseJSON.error).removeClass("error--hidden");
		},
	});

	e.preventDefault();
});

document.getElementById("myForm").addEventListener("submit", function (event) {
	event.preventDefault(); // Empêche l'envoi du formulaire par défaut

	// Afficher la boîte modale
	document.getElementById("myModal").style.display = "block";
});

document
	.getElementsByClassName("close")[0]
	.addEventListener("click", function () {
		// Fermer la boîte modale lorsque l'utilisateur clique sur la croix
		document.getElementById("myModal").style.display = "none";
	});
