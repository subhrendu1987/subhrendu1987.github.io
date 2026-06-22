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
            URI = window.location.href;

            for (const key in data) {
                if (data.hasOwnProperty(key)) {
                    const noteData = data[key];
                    const note = document.createElement('div');
                    note.className = 'note';

                    shortURI = URI + "?url=" + noteData.ShortURL;

                    let comment = !noteData.Comment || noteData.Comment.length === 0
                        ? ""
                        : `<div class="green-box"><p><strong>Note:</strong> ${noteData.Comment}</p></div>`;

                    note.innerHTML = `
                        <h3>${noteData.Description}</h3>
                        <p><strong>Actual URL:</strong> <em>${noteData.URL}</em></p>
                        <p><strong>Short URL:</strong> <em>${shortURI}</em></p>
                        <p><a href="${shortURI}" target="_blank" class="button">Go to Short URL</a></p>
                        ${comment}
                    `;

                    notesContainer.appendChild(note);
                }
            }

            /* ✅ CRITICAL FIX: remove loader AFTER content is ready */
            const loader = document.querySelector('.loading-container');
            if (loader) loader.remove();
        })
        .catch(error => {
            console.log(error.message);

            /* also remove loader on error */
            const loader = document.querySelector('.loading-container');
            if (loader) loader.remove();
        });
});