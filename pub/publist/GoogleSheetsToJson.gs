/*
Create Google Sheet with "Anyone can View" priviledge
Update the variable named "SPREADSHEET_URL" with the spreadsheet URL 

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
    Use the same URL in index.html variable named "webAppURL" and "jsonURL"; Use the URL of the spreadsheet in the variable named "sheetURL"
*/
SPREADSHEET_URL="https://docs.google.com/spreadsheets/d/1POh9C2N0DXVjNn21y0lxoQvFoCulFeFTmC5hsrMcPbo/"

function convertArrayToDict(arrayOfDicts){
 var dict = {};

  // Convert the array into a dictionary
  for (var i = 0; i < arrayOfDicts.length; i++) {
    var element = arrayOfDicts[i];
    var shortURL = element.ShortURL;
    dict[shortURL] = element;
  }
  Logger.log(dict); //// Log the entire dictionary for debugging purpose 
  return(dict);
}


function doGet() {
  var sheet = SpreadsheetApp.openByUrl(SPREADSHEET_URL).getSheets()[0]; // Use the first sheet
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
  var mapdict = convertArrayToDict(jsonData);

  //return ContentService.createTextOutput(JSON.stringify(jsonData))
  //  .setMimeType(ContentService.MimeType.JSON);
  return ContentService.createTextOutput(JSON.stringify(mapdict))
    .setMimeType(ContentService.MimeType.JSON);
}
