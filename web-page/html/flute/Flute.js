var var_blick_ant = 0;
var score_name_old = "no_gesture";

// =======================================
function getLocalStream() {
    navigator.mediaDevices.getUserMedia({audio: true, video: false})
    // if audio is working then h1 text is "Audio is working"
    .then(function(stream) {
        var h1 = document.getElementsByTagName('h1')[0];
        h1.innerHTML = "Audio is working";
    })
    // if audio is not working then h1 text is "Audio is not working"
    .catch(function(err) {
        var h1 = document.getElementsByTagName('h1')[0];
        h1.innerHTML = "Audio is not working";
    });
}

// =======================================
function tune(){
    // uptade h1 text
    var h1 = document.getElementsByTagName('h1')[0];
    var random = Math.random();
    if (random < 0.5){
        h1.innerHTML = "↓ Tuning";
    }
    else{
        h1.innerHTML = "↑ Tuning";
    }
}

// =======================================
function readTextFile(file, callback) {
    var rawFile = new XMLHttpRequest();
    rawFile.overrideMimeType("application/json");
    rawFile.open("GET", file, true);
    rawFile.onreadystatechange = function() {
        if (rawFile.readyState === 4 && rawFile.status == "200") {
            callback(rawFile.responseText);
        }
    }
    rawFile.send(null);
}

// =======================================
function updateprogress(duration) {
    var start = new Date().getTime();
    var interval = setInterval(function() {
        var now = new Date().getTime();
        var progress = now - start;
        var div = document.getElementsByTagName('div')[0];
        var div_width = Math.min(progress / duration * 100, 100);
        div.style.width =  div_width + '%';
        // when the progress is 100%, clear the interval
        if (div_width == 100) {
            clearInterval(interval);
            div.style.width = 100;
        }              
    }, 10); 
}

// =======================================
function updateimage() {
    var var_blick_ant = 0;
    var i = 1;
    var image = document.getElementsByTagName('img')[0];
    image.src = 'score' + '.png' + '?' + new Date().getTime();
    // read json file inside flute/update_rate.json and get the update rate
    readTextFile("update_rate.json" + '?' + new Date().getTime(), function(text){
        var data = JSON.parse(text);
        var update_rate = data.update_rate;
        var score_name = data.name;
        if (score_name == 'FINAL_GESTURE'){
            getLocalStream();
            tune();
        }
        if (score_name == score_name_old) {
            console.log("Old Gesture"); 
            // sleep for 100 ms
            setTimeout(function() {updateimage()}, 100);
        } 
        else {
            score_name_old = score_name;
            var div = document.getElementsByTagName('div')[0];
            updateprogress(update_rate);
            setTimeout(function() {updateimage()}, 100);
        }
    });
}

// =======================================
// =======================================
// =======================================

updateimage();