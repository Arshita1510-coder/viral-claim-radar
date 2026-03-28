// Toggle "How it works" section
function toggleHow(){

let section = document.getElementById("howSection");

if(section.style.display === "block"){
section.style.display = "none";
}else{
section.style.display = "block";
}

}


// Theme switcher
function setTheme(theme){

document.body.classList.remove("purple-theme","white-theme");

if(theme === "purple"){
document.body.classList.add("purple-theme");
}

if(theme === "white"){
document.body.classList.add("white-theme");
}

}


// Analyze Claim
async function analyzeClaim(){

let claim = document.getElementById("claimText").value.trim();

if(!claim){
alert("Enter a claim first");
return;
}

try{

let response = await fetch("http://127.0.0.1:5000/analyze",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({claim:claim})
});

let data = await response.json();

// Show result card
document.getElementById("resultCard").style.display = "block";

// Score
document.getElementById("score").innerHTML =
"Score: " + data.confidence + "%";

let statusBox = document.getElementById("statusBox");

let result = data.result.toLowerCase();

if(result.includes("supported") || result.includes("true")){

statusBox.className = "status-box supported";
statusBox.innerHTML = "✔ SUPPORTED";

}
else if(result.includes("refuted") || result.includes("false")){

statusBox.className = "status-box refuted";
statusBox.innerHTML = "✖ REFUTED";

}
else{

statusBox.className = "status-box uncertain";
statusBox.innerHTML = "? UNCERTAIN";

}

// Evidence details
document.getElementById("explanation").innerHTML =
"<strong>Simple Explanation:</strong> " + data.explanation;

document.getElementById("manipulation").innerHTML =
"<strong>Manipulation Detected:</strong> " + data.manipulation;

document.getElementById("sources").innerHTML =
"<strong>Evidence Sources:</strong> " + data.source;

document.getElementById("contradictions").innerHTML =
"<strong>Contradictions:</strong> " + data.contradictions;

}catch(error){

console.error(error);
alert("Error connecting to backend");

}

}


// Voice input
function startVoice(){

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

if(!SpeechRecognition){
alert("Speech recognition not supported in this browser");
return;
}

const recognition = new SpeechRecognition();

recognition.lang = "en-US";
recognition.start();

recognition.onresult = function(event){

let transcript = event.results[0][0].transcript;

document.getElementById("claimText").value = transcript;

}

recognition.onerror = function(){
alert("Voice recognition error");
}

}