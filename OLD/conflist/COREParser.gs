/********************************************************************/
/********************************************************************/
/********************************************************************/
function matchString(strA,strB){
  for(var result = 0, i = strA.length; i--;){
    if(typeof strB[i] == 'undefined' || strA[i] == strB[i]);
    else if(strA[i].toLowerCase() == strB[i].toLowerCase())
    result++;
    else
      result += 4;
  }
  var ret=1 - (result + 4*Math.abs(strA.length - strB.length))/(2*(strA.length+strB.length)); 
  Logger.log(strA+":"+strB+"("+ret+")");
  return(ret) ;
}
/********************************************************************/
function main(){
  //Fill up URLs
  var confsheet=SpreadsheetApp.getActiveSpreadsheet().getSheetByName("ConfName");
  var sheet  =SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Garbage");
  var coresheet=SpreadsheetApp.getActiveSpreadsheet().getSheetByName("CORE");
  

  MaxRow=5;
  row=10;
  //for(row=2;row<MaxRow;row++){
  acronym=confsheet.getRange(row, 1).getValue();
  title=confsheet.getRange(row, 2).getValue();
  COREURL="http://portal.core.edu.au/conf-ranks/?search="+acronym+"&by=all&source=all&sort=atitle&page=1";
  
  coresheet.getRange(row, 1).setValue(acronym); // acronym
  coresheet.getRange(row, 2).setValue(title);   // title
  coresheet.getRange(row, 3).setValue(COREURL); // URL
  
    //SpreadsheetApp.getActiveSpreadsheet().getSheetByName("CORE").getRange(row, 2).setValue(parseWikiCFP(COREURL));
  /// Start parsing of CORE page
  sheet.clearContents();
  sheet.getRange(1, 1).setValue("=importHTML(\""+COREURL+"\",\"table\")");
  parseWikiCFP(acronym,title) ;
  
  coresheet.getRange(row, 4).setValue(sheet.getRange(2, 1,1,10).getValues()); // page data
  
  sheet.clearContents();
  /// Start parsing of WikiCFP page
  //}
  return;
}
/********************************************************************/
function getRegExp(pattern){
  var start = new RegExp(pattern,"ig");
  return(start);
}
/********************************************************************/
function getTag(text,tag){
  Logger.log(text.indexOf("<"+tag));
  pattern="(<"+tag+")(\\s|$|[0-9]|[a-b]|[A-Z]|\\W)*>(\\s)*<(\\S)"+tag+">"
  var start = new RegExp(pattern,"igm");
  if (start.test(text)) {
    Logger.log("Pattern: Found");
  }else{
    Logger.log("Pattern: Not Found");
  }
  return(text.match(start));
  //var end=new RegExp("<"+tag+">");
}
/********************************************************************/
function parseWikiCFP(acronym,title) {
  var sheet=SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Garbage");
      var numRows=sheet.getLastRow();
  sheet.getRange(1, 20).setValue(numRows);
  for(i=2;i<=numRows;i++){
   parsedTitle=sheet.getRange(i, 1).getValue();
   sheet.getRange(i, 10).setValue(matchString(""+parsedTitle,title));
  }
  table=sheet.getRange(2, 1, sheet.getLastRow() - 1, sheet.getLastColumn());
  table.sort({column: 10, ascending: false});
  return;
}
/********************************************************************/
