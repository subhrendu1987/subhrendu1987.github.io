const webAppURL = 'https://script.googleusercontent.com/macros/echo?user_content_key=-nf7HtnAq_0htG1VeTn-eIqjG7DG2zmJVAB9hWC3ghXihLe0aPd4Z5uHfso8dyf3px8_s0aqadWfwTLmhpF3F8T4JLVykrupm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnBgmdpr5BW5TgBjlEPPDofIM2_kNrBC71ajuEfM6JLC4DUaHCjcXJ17FzCh84gbx3gVxNwEBAPUaEcM9aEljYTZS6Ic6skGQNdz9Jw9Md8uu&lib=MiS8nA0IP1S5-p0rxnHc8P-ZNomVPhu3r';

document.addEventListener('DOMContentLoaded', function() {
    // Reference to the table body
    const tableBody = document.querySelector('#data-table tbody');

    // Fetch JSON data from the web app
    fetch(webAppURL)
        .then(response => {
            if (!response.ok) {
                throw new Error('Unable to access JSON');
            }
            return response.json();
        })
        .then(data => {
            for (const key in data) {
                if (data.hasOwnProperty(key)) {
                    const rowData = data[key];
                    const row = document.createElement('tr');

                    // Loop through the object properties and create table cells
                    for (const cellKey in rowData) {
                        const cell = document.createElement('td');
                        if (cellKey === 'URL') {
                            const link = document.createElement('a');
                            link.href = rowData[cellKey];
                            link.textContent = rowData[cellKey];
                            cell.appendChild(link);
                        } else if(cellKey === 'ShortURL'){
                            const link = document.createElement('a');
                            link.href = "https://subhrendu1987.github.io/redir?url="+rowData[cellKey];
                            link.textContent = "https://subhrendu1987.github.io/redir?url="+rowData[cellKey];
                            cell.appendChild(link);
                        } else {
                            cell.textContent = rowData[cellKey];
                        }
                        row.appendChild(cell);
                    }
                    tableBody.appendChild(row);
                }
            }
        })
        .catch(error => {
            alert(error.message); // Display an alert with the error message
        })
        .finally(() => {
            //alert('Code execution is over.'); // Display an alert once code execution is complete
        });
});
