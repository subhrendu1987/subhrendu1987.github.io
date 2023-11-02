document.addEventListener('DOMContentLoaded', function() {
    // URL of your web app that serves JSON data
    const webAppURL = 'https://script.googleusercontent.com/macros/echo?user_content_key=-nf7HtnAq_0htG1VeTn-eIqjG7DG2zmJVAB9hWC3ghXihLe0aPd4Z5uHfso8dyf3px8_s0aqadWfwTLmhpF3F8T4JLVykrupm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnBgmdpr5BW5TgBjlEPPDofIM2_kNrBC71ajuEfM6JLC4DUaHCjcXJ17FzCh84gbx3gVxNwEBAPUaEcM9aEljYTZS6Ic6skGQNdz9Jw9Md8uu&lib=MiS8nA0IP1S5-p0rxnHc8P-ZNomVPhu3r';

    // Reference to the table body
    const tableBody = document.querySelector('#data-table tbody');

    // Fetch JSON data from the web app
    fetch(webAppURL)
        .then(response => response.json())
        .then(data => {
            // Loop through the JSON data and create table rows
            data.forEach(rowData => {
                const row = document.createElement('tr');

                // Loop through the object properties and create table cells
                for (const key in rowData) {
                    const cell = document.createElement('td');
                    cell.textContent = rowData[key];
                    row.appendChild(cell);
                }

                tableBody.appendChild(row);
            });
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
});
