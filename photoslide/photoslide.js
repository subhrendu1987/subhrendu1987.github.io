    function openModal(imageSrc, caption) {
      var modal = document.getElementById("modal");
      var modalImg = document.getElementById("modal-img");
      var modalCaption = document.getElementById("modal-caption");
      
      modal.style.display = "block";
      modalImg.src = imageSrc;
      modalCaption.innerText = caption;
    }
    
    function closeModal() {
      var modal = document.getElementById("modal");
      modal.style.display = "none";
    }
