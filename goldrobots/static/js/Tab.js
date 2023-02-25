function openCity(evt, cityName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();

// <!-- /* ///////////////////////////////NEG//////////////////////////////////// */ -->


var header = document.getElementById("myDIV");
var btns = header.getElementsByClassName("branch");
for (var i = 0; i < btns.length; i++) {
btns[i].addEventListener("click", function() {
var current = document.getElementsByClassName("activeBank");
if (current.length > 0) { 
    current[0].className = current[0].className.replace(" activeBank", "");
}
this.className += " activeBank";
});
}

var header = document.getElementById("myDIV2");
var btns = header.getElementsByClassName("branch");
for (var i = 0; i < btns.length; i++) {
btns[i].addEventListener("click", function() {
var current = document.getElementsByClassName("activeBank");
if (current.length > 0) { 
    current[0].className = current[0].className.replace(" activeBank", "");
}
this.className += " activeBank";
});
}

// <!-- /* ///////////////////////////////NEG//////////////////////////////////// */ -->
