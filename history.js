async function loadHistory(){

let response = await fetch("http://127.0.0.1:5000/history");

let data = await response.json();

let historyList = document.getElementById("historyList");

data.forEach(item => {

let li = document.createElement("li");

li.innerText = item.claim + " → " + item.result + " (" + item.confidence + "%)";

historyList.appendChild(li);

});

}

loadHistory();