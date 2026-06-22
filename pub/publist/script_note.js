document.addEventListener('DOMContentLoaded', function () {

    const notesContainer = document.getElementById('notes-container');
    const sideNav = document.getElementById('sidenav');

    fetch(webAppURL)
        .then(response => {
            if (!response.ok) {
                throw new Error('Unable to access JSON');
            }
            return response.json();
        })
        .then(data => {

            /*
              Supports both:
              1. JSON array:
              [
                {"ID":"1","Name":"Paper title", ...}
              ]

              2. JSON dictionary:
              {
                "1":{"ID":"1","Name":"Paper title", ...}
              }
            */

            let papers = Array.isArray(data) ? data : Object.values(data);

            papers.forEach(paperData => {

                const note = document.createElement('div');
                note.className = 'note';

                note.innerHTML = `

                    <h3>
                        ${paperData.Name || "Untitled Paper"}
                    </h3>

                    <div class="details">
                        ${paperData.Authors || ""}
                    </div>

                    <div class="abstract">
                        <b>Abstract—</b>
                        ${paperData.Abstract || ""}
                    </div>

                    <div class="link">
                        <a href="${paperData.Link}" 
                           target="_blank">
                           View Paper
                        </a>
                    </div>

                    <div class="info">
                        ${paperData.Info || ""}
                    </div>

                `;

                notesContainer.appendChild(note);

            });


            // Remove loading animation after rendering
            const loader = document.querySelector('.loading-container');
            if (loader) {
                loader.remove();
            }

        })
        .catch(error => {

            console.log(error.message);

            const loader = document.querySelector('.loading-container');
            if (loader) {
                loader.remove();
            }

            notesContainer.innerHTML =
                `<div class="note">
                    <h3>Error</h3>
                    <p>${error.message}</p>
                 </div>`;

        });

});