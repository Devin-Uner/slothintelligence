// the function called by the button press
function get_output() {
	get_request('output_generator.py', draw_output, draw_error);
	return false;
}

// what to do if theres an error
// note that until it is succsessful, it assumes theres an error, so while its loading it assumes it just didnt work
// but it will update if it succsessfully recieves a reply
function draw_error() {
	document.getElementById("changeme").innerHTML = "ERROR!";
}

// what do do if its succsessful
function draw_output(response_text) {
	document.getElementById("changeme").innerHTML = response_text;
}

// get the request from the python CGI page
function get_request(url, success, error) {
	var req = new XMLHttpRequest();
	req.onreadystatechange = function () {
		return req.status == 200 ? success(req.responseText) : error(req.status);
	}
	req.open("POST", url, true);
	req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	var data = document.getElementById("symptoms").value;
	req.send("symptoms="+data); // TODO: add the symptoms as test
	return req;

}




