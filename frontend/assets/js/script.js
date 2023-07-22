function falbak() {
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
	xhr.open('POST', 'http://127.0.0.1:5000/fal');
	xhr.onreadystatechange = function(){
	if (xhr.readyState != 4) return;
		if (xhr.status != 200) {
  			alert("Status: " + xhr.status);
		} else {
			var jsonResp = JSON.parse(xhr.responseText)
			var dataUrl = imgResult(tempImg, jsonResp)
			document.getElementById("result").innerHTML = /*'<p>' + xhr.responseText + '</p>' +*/ '<img src="' + dataUrl + '">'
		}
	};

	document.getElementById("result").innerHTML = '<p>Loading...</p>'
	xhr.send(formdata);
}

// Big thanks to etham https://stackoverflow.com/a/42769683
function convertRemToPixels(rem) {
    return rem * parseFloat(getComputedStyle(document.documentElement).fontSize);
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
		//pxVal = convertRemToPixels(1.8)
		//ctx.font='bold ' + pxVal + 'px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif'
		ctx.fillText(anno.obj, anno.pos[0], anno.pos[1] - 7);
		ctx.stroke();


	}
	return imgCanvas.toDataURL("image/png");
}
