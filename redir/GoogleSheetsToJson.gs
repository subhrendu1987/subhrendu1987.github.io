/*
Create Google Sheet

In the first sheet 
    add three columns "Description", "URL", "ShortURLID"
    Sample entry "Homepage", "https://subhrendu1987.github.io/", "home"

Write app script
    "Extention" -> "App Script" -> Add this text in the IDE provided
    Save script    

Publish the Web App:

    Click on the "Publish" menu, select "Deploy as web app," and configure it as follows:
        Project Version: New
        Execute the app as: Me
        Who has access to the app: Anyone, even anonymous
Deploy the Web App:
    Click "Deploy" and review and accept the permissions.
Access the JSON Data:
    After deploying the web app, you'll receive a URL. Open this URL in your web browser, and it will return the JSON data.
*/

function doGet() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0]; // Use the first sheet
  var data = sheet.getDataRange().getValues();
  var headers = data[0];
  var jsonData = [];

  for (var i = 1; i < data.length; i++) {
    var row = data[i];
    var rowObject = {};

    for (var j = 0; j < headers.length; j++) {
      rowObject[headers[j]] = row[j];
    }

    jsonData.push(rowObject);
  }

  return ContentService.createTextOutput(JSON.stringify(jsonData))
    .setMimeType(ContentService.MimeType.JSON);
}
