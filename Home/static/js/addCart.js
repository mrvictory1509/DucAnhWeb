function cart(id)
{
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			if(this.responseText == "Login")
			{
				location.href = "/sign_in"
			}
		}
	};
	xhttp.open("GET", "/addCart/"+id, true);
	xhttp.send();
}