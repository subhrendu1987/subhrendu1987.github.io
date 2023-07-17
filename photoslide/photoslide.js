function findFigures() {
  var figures = document.getElementsByTagName('figure');
  for (var i = 0; i < figures.length; i++) {
    var figure = figures[i];
    var img = figure.querySelector('img');
    var figcaption = figure.querySelector('figcaption');
    figcaption.textContent = img.alt; 
  }
}


function openFrame(imgElement) {
  var modal = document.getElementById("modal");
  var modalImg = document.getElementById("modal-img");
  var modalCaption = document.getElementById("modal-caption");
  modal.style.display = "block";
  modalImg.src =imgElement.src;
  modalCaption.innerText = imgElement.alt;
}

function closeFrame() {
  var modal = document.getElementById("modal");
  modal.style.display = "none";
}