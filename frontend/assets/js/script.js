function falbak(lang) {
	cupImg = document.getElementById("fileField").files[0];
	var reader = new FileReader();
	var tempImg = document.createElement("img");
	reader.addEventListener(
		"load",
		() => {
			// convert image file to base64 string
      			tempImg.src = reader.result;
    		},
    		false,
  	);
	reader.readAsDataURL(cupImg);

	var formdata = new FormData();
	formdata.append('file', cupImg);

	var xhr = new XMLHttpRequest();
	xhr.open('POST', 'https://kahvefalcim.com/api/fal/' + lang);
	err = false
	xhr.onreadystatechange = function(){
	if (xhr.readyState != 4) return;
		if (xhr.status != 200) {
  			alert("Status: " + xhr.status);
		} else {
			var jsonResp = JSON.parse(xhr.responseText)
			if (jsonResp.hasOwnProperty("error_msg")) {
				if (lang == "en") {
					document.getElementById("result").
						innerHTML = '<p>Something went wrong! Try again later.</p>'
				}
				else {
					document.getElementById("result").
						innerHTML = '<p>Bir şeyler yanlış gitti! Daha sonra tekrar deneyin.</p>'
				}
				err = true
			}
			if (!err) {
				var dataUrl = imgResult(tempImg, jsonResp)
				var list = makelist(jsonResp.defs)
				document.getElementById("result").innerHTML = '<img src="' + dataUrl + '">' + list
			}
		}
	};

	if (lang == "en") {
		document.getElementById("result").innerHTML = '<p>Loading...</p>'
	}
	else {
		document.getElementById("result").innerHTML = '<p>Yükleniyor...</p>'
	}
	xhr.send(formdata);
}

function imgResult(img, res) {
	var imgCanvas = document.createElement("canvas"),
        ctx = imgCanvas.getContext("2d");

	imgCanvas.width = res.cup_boundaries[2] - res.cup_boundaries[0];
	imgCanvas.height = res.cup_boundaries[3] - res.cup_boundaries[1];

	ctx.drawImage(img, res.cup_boundaries[0], res.cup_boundaries[1], imgCanvas.width, imgCanvas.height,
		0, 0, imgCanvas.width, imgCanvas.height);
	
	for (i = 0; i < res.annotations.length; i++) {
		var anno = res.annotations[i]

		ctx.beginPath();	
		ctx.lineWidth = "4";
		ctx.strokeStyle = "black";
		ctx.rect(anno.pos[0], anno.pos[1], anno.pos[2] - anno.pos[0], anno.pos[3] - anno.pos[1]);
		ctx.stroke();

		ctx.beginPath();
		ctx.strokeStyle = "#eb99a1";
		ctx.lineWidth = "2";
		ctx.rect(anno.pos[0], anno.pos[1], anno.pos[2] - anno.pos[0], anno.pos[3] - anno.pos[1]);
		ctx.stroke();
    		
		ctx.beginPath();
		ctx.strokeStyle = 'black';
    		ctx.lineWidth = "3";
    		ctx.lineJoin="round";
      		ctx.miterLimit = 2;
		ctx.font='bold 1.8rem -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif'
		
		ctx.fillStyle = "#eb99a1";
		ctx.strokeText(anno.obj, anno.pos[0], anno.pos[1] - 7);
		ctx.fillText(anno.obj, anno.pos[0], anno.pos[1] - 7);
		ctx.stroke();
	}
	return imgCanvas.toDataURL("image/png");
}

function makelist(defs) {
	list = "<ul>"
	console.log(defs)
	for (i = 0; i < defs.length; i++) {
		list += "<li><b>" + defs[i].name + ":</b> " + defs[i].meaning + "</li>"
	}
	list += "</ul>"
	return list
}
