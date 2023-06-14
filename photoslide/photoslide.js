    function openModal(imageSrc, caption) {
      var modal = document.getElementById("modal");
      var modalImage = document.getElementById("modal-image");
      var modalCaption = document.getElementById("modal-caption");
      
      modal.style.display = "block";
      modalImage.src = imageSrc;
      modalCaption.innerText = caption;
    }
    /********************************/
   function closeModal() {
      var modal = document.getElementById("modal");
      
      modal.style.display = "none";
    }
    /********************************/
    window.onclick = function(event) {
      var modal = document.getElementById("modal");
      
      if (event.target == modal) {
        closeModal();
      }
    }

