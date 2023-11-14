// ============================================================================
//  Eco (2023) is a Piece of Charles K. Neimog
// ============================================================================
//
//    This program is free software. For information on usage
//    and redistribution, see the "LICENSE" file in this distribution.
//
//    This program is distributed in the hope that it will be useful,
//    but WITHOUT ANY WARRANTY; without even the implied warranty of
//    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
//
// ============================================================================
//  File author: Charles K. Neimog
// ============================================================================

var scoreNameOld = "no_gesture";
const fftSize = 2048;
var stream = navigator.mediaDevices.getUserMedia({audio: true, video: false});
var last_fft = new Date().getTime();
var lastYin = new Date().getTime();
var executingTune = false;
var ShowBangs = false;
var measureFinished = false;
var GlobalStart2Play = false;
var metronomeAttackStarted = false; 
var noBang = false;
var scoreImage;
var fastGestureAlreadyPlayed = false;
var fastGestureStart;
var randomGestureDuration;
var scoreName;
let pulse = {};
var measureDivWidth;
var metrointerval;

// =======================================
// =======================================
function send2pd(router, name) {
    var xhr = new XMLHttpRequest();
    var host = window.location.hostname;
    var port = window.location.port;
    var protocol = window.location.protocol;
    var url = protocol + '//' + host + ':' + port + '/send2pd'; // WARNING: This is an standard, all the requests must be sent to this url
    xhr.open('POST', url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    // router is the Json key, name is the Json value
    var data = JSON.stringify({[router]: name});
    xhr.send(data);
    // close the connection
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            xhr.abort();
        }
    }
}
// ============================================
function inputReals(size) {
    var result = new Float32Array(size);
    for (var i = 0; i < result.length; i++)
        result[i] = (i % 2) / 4.0;
    return result;
    }

// =======================================
// =======================================
function audioFftYin(target_frequency) {    
    var pitchesArray = [];
    var showResult = 0;
    var noPitchesDetected = 0;
    var Target_mc = (1200 * Math.log2(target_frequency / 440)) + 6900;
    var TargetMcModule = Target_mc % 1200 
    // document.getElementById("InstrumentTitle").innerHTML = "Tunning started | Target: " + target_frequency + " Hz";
    // document.getElementById("InstrumentTitle").style.backgroundColor =  "#3232ff";

    // =======================================
    function ckn_fft(dataArray, sampleRate){ // sorry, I do not know how to name this
        var now = new Date().getTime();
        if ((now - last_fft) < 150) {
            return;
        }
        last_fft = now;
        var fft = new pulse.fftReal(fftSize);
        var SOUND = dataArray
        var out = fft.forward(SOUND);
        var amplitude = new Float32Array(fftSize/2);
        for (var i = 0; i < fftSize / 2; i++) {
            var mag = Math.sqrt(out [i*2] * out[i*2] + out[i*2+1] * out[i*2+1]);
            var amp = mag / fftSize;
            var amp_log = 20 * Math.log10(amp);
            amplitude[i] = amp_log;
            // define ID saxTitle as amp_log

        }
        // save peaks in array
        var array_FrekAndAmp = [];
        for (var i = 0; i < fftSize/2 - 1; i++) {
            if (amplitude[i] > amplitude[i-1] && amplitude[i] > amplitude[i+1]) {
                p = (0.5 * ((amplitude[i-1] - amplitude[i+1]) / (amplitude[i-1] - 2 * amplitude[i] + amplitude[i+1]))) + i;
                freq = p * sampleRate / fftSize;
                // see if freq is within range
                if (freq > 100 && freq < 3000 && amplitude[i] > -95) {
                    array_FrekAndAmp.push(freq);
                    array_FrekAndAmp.push(amplitude[i]); // WARNING: I need to implement best amplitude equation!
                }
            }
        }
        send2pd("GuitarPeaks", array_FrekAndAmp);
    }
    // -----------------------------------------------
    function PitchDetection(data, sampleRate) {
        var now = new Date().getTime();
        if (now - lastYin > 25 && executingTune == true) {
            lastYin = now;

            // NOTE: Here is where the C code is called
            // =======================================
            var sound = yinModule._mallocMemory(fftSize * 4); // this is the pointer to the memory, _mallocMemory represent the mallocMemory in utilities.c
            yinModule.HEAPF32.set(data, sound / 4); // Here we convert the data to floats (32 bits) and set it to the memory
            var pitch = yinModule._C_getPitch(sound); // Here we call the C function getPitch, which is defined in index.c
            yinModule._freeMemory(sound); // Here we free the memory
            // ========================================

            if (pitch > 3520 || pitch < 65){ // if detented pitch is out of range
                noPitchesDetected += 1;
                if (noPitchesDetected > 15) {
                    pitchesArray = [];
                    document.getElementById("InstrumentTitle").innerHTML = "Not pitch was detected with 60% of confidence";
                    document.getElementById("InstrumentTitle").style.backgroundColor =  "red";
                    noPitchesDetected = 0;
                }
            } 
            else {
                var midicents = (1200 * Math.log2(pitch / 440)) + 6900;
                midicents = Math.round(midicents);
                midicents = midicents % 1200;
                pitchesArray.push(Math.round(midicents));

                if (pitchesArray.length > 10){
                    pitchesArray.shift(); // this make the array to have always 10 elements
                    var sum = pitchesArray.reduce(function(a, b) { return a + b; });
                    var avg = sum / pitchesArray.length;
                    avg =  Math.round(avg);
                    // calculate the difference between the target and the average
                    var diff =  avg - TargetMcModule; 
                    if (Math.abs(diff) > 100){
                        document.getElementById("InstrumentTitle").style.backgroundColor =  "red";
                        if (diff > 0){
                            document.getElementById("InstrumentTitle").innerHTML = "HIGH";
                        }
                        else{
                            document.getElementById("InstrumentTitle").innerHTML = "LOW";
                        }
                    } 
                    else{
                        var highorlow;
                        if (diff > 0){
                            highorlow = "HIGH";
                        }
                        else{
                            highorlow = "LOW";
                        }
                        document.getElementById("InstrumentTitle").innerHTML = Math.round(diff) + " cents." + highorlow;
                        if (Math.abs(diff) > 90){
                            document.getElementById("InstrumentTitle").style.backgroundColor = '#E80C00';
                        }
                        else if (Math.abs(diff) > 80){
                            document.getElementById("InstrumentTitle").style.backgroundColor = '#D11700';
                        }
                        else if (Math.abs(diff) > 70){
                            document.getElementById("InstrumentTitle").style.backgroundColor = '#B92300';
                        }
                        else if (Math.abs(diff) > 60){
                            document.getElementById("InstrumentTitle").style.backgroundColor = '#A22F00';
                        }
                        else if (Math.abs(diff) > 50){
                            document.getElementById("InstrumentTitle").style.backgroundColor = '#8C3A00';
                        }
                        else if (Math.abs(diff) > 40){
                            document.getElementById("InstrumentTitle").style.backgroundColor = '#744600';
                        }
                        else if (Math.abs(diff) > 30){
                            document.getElementById("InstrumentTitle").style.backgroundColor = '#5D5100';
                        }
                        else if (Math.abs(diff) > 20){
                            document.getElementById("InstrumentTitle").style.backgroundColor = '#2E6900';
                        }
                        else if (Math.abs(diff) > 15){
                            document.getElementById("InstrumentTitle").style.backgroundColor = '#177400';
                        } 
                        else if (Math.abs(diff) < 15){
                            document.getElementById("InstrumentTitle").style.backgroundColor = '#008000';
                            document.getElementById("InstrumentTitle").innerHTML = "TUNNED";
                        }
                    }
                }
                else{
                    return;
                }
            }
        }
    }
    // -----------------------------------------------
    function AudioStream() {
        var audioContext = new AudioContext();
        var analyser = audioContext.createAnalyser();
        analyser.fftSize = fftSize;
        var sampleRate = audioContext.sampleRate;
        var sampleRate = audioContext.sampleRate;
        var data = new Float32Array(analyser.fftSize);
        // -----------------------------------------------
        function step() {
            if (executingTune == true) {
                analyser.getFloatTimeDomainData(data);
                if (measureDivWidth > 95){
                    ckn_fft(data, sampleRate);
                }

                // PitchDetection(data, sampleRate);
                requestAnimationFrame(step);
            } 
            if (executingTune == false) {
                audioContext.close();
                document.getElementById("InstrumentTitle").innerHTML = "Ac. Guitar";
                document.getElementById("InstrumentTitle").style.backgroundColor =  "#d9d9d9";
            }
        }
        // -----------------------------------------------
        stream.then(function(stream) {
            var mediaStreamSource = audioContext.createMediaStreamSource(stream);
            mediaStreamSource.connect(analyser);
            step(); // this is a requestAnimationFrame???
        });
        // -----------------------------------------------
    }
    AudioStream();
}

// =======================================
function randomGestureScoreFile(randomGesture){
    var scoreImages = {1: "gestures/gesto1.png", 2: "gestures/gesto2.png"};
    return scoreImages[randomGesture];
}

// =======================================
function randomGestureDurationData(randomGesture){
    var scoreImages = {1: 4500, 2: 4500};
    return scoreImages[randomGesture];
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
function updateMeasureBarProgress(measureDuration, startPlay, tupletDuration, frequencyTarget, gestureNumber, scoreImage){
    var start = new Date().getTime();
    var interval = setInterval(function() {
        var now = new Date().getTime();
        var progress = now - start;
        if (executingTune == false && gestureNumber > 3){
            if (progress < startPlay){
                document.getElementById("InstrumentTitle").innerHTML = "Wait for the " + startPlay + " milliseconds";
                document.getElementById("InstrumentTitle").style.backgroundColor =  "orange";
            }
            if (progress > startPlay - tupletDuration){
                document.getElementById("InstrumentTitle").innerHTML = "Get Ready!";
                document.getElementById("InstrumentTitle").style.backgroundColor =  "yellow";
                if (metronomeAttackStarted == false){
                    noBang = true;
                    metronome4Attack(tupletDuration, startPlay, tupletDuration, frequencyTarget, gestureNumber);
                    metronomeAttackStarted = true;
                }
            }
            if (progress > startPlay){
                executingTune = true;
                audioFftYin(frequencyTarget); 
            }
        }
        var div = document.getElementById('DurationBar');
        var div_width = Math.min(progress / measureDuration * 100, 100);
        measureDivWidth = div_width;
        div.style.width =  div_width + '%';
        // if (div_width < 99){
        //     measureFinished = false;
        // }
        if (div_width == 100) {
            clearInterval(interval);
            div.style.width = 100;
            measureFinished = true;
            executingTune = false;
            fastGestureAlreadyPlayed = false;
            send2pd("guitar", "gesto" + gestureNumber + " " + gestureNumber); 
            clearInterval(metrointerval);
            if (gestureNumber != 0){
                scoreImage.src =  "emptyScore.png";
            }
            if (gestureNumber == 12){
                scoreImage.src =  "FIM.png";
            }
        }
    }, 30);
}

// =======================================
function metronome4Attack(span, startPlay, tupletDuration, frequencyTarget, gestureNumber, gestRepetition, gestProb){
    // random number between 0 and 1
    if (gestureNumber < 3){
        return;
    }
    if (Array.isArray(span)){
        var randomSpan = span[Math.floor(Math.random() * span.length)];
        span = randomSpan;
    }
    if (ShowBangs == false){
        ShowBangs = true;
        var barNoteDuration = document.getElementById("DurationNote");
        barNoteDuration.style.backgroundColor = "#000000";
        barNoteDuration.style.position = "fixed";
        barNoteDuration.style.top = "10%";
        barNoteDuration.style.left = "0%";
        barNoteDuration.style.width = "0%";
        barNoteDuration.style.height = "calc(2% - 0px)";

        var bangSVG = document.getElementById("InstrumentBang");
        bangSVG.style.top = "5%";
        bangSVG.style.left = "0%";
        bangSVG.style.display = "block";
        var svgText = document.getElementById("BangText");
        svgText.innerHTML = "Attack";
    } 
    else{
        var barNoteDuration = document.getElementById("DurationNote");
        var bangSVG = document.getElementById("InstrumentBang");
        var instrumentScore = document.getElementById("InstrumentScore");
    }
    var start = new Date().getTime();
    metrointerval = setInterval(function() {
        var now = new Date().getTime();
        var progress = now - start;
        var div_width = Math.min(progress / tupletDuration * 100, 100);
        var gestRepeatRandom = Math.random();
        if (gestRepeatRandom > (1 - gestProb) && fastGestureAlreadyPlayed == false){
            var randomGesture = Math.floor(Math.random() * 2) + 1;
            scoreImage.src = randomGestureScoreFile(randomGesture);
            randomGestureDuration = randomGestureDurationData(randomGesture);
            send2pd("fastGest", "fastGest in gesture" + gestureNumber + " for Guitar");
            fastGestureAlreadyPlayed = true;
            fastGestureStart = new Date().getTime();
        }
        // if gesture 
        if (fastGestureAlreadyPlayed == true){
            var fastGestureNow = new Date().getTime();
            var fastGestureProgress = fastGestureNow - fastGestureStart;
            if (fastGestureProgress > (randomGestureDuration * 1)){
                scoreImage.src = scoreName + '.png' + '?' + new Date().getTime();
            } 
        }
        barNoteDuration.style.width =  div_width + '%';
        if (div_width < 10 && noBang == false){
            var svgCircle = document.getElementById("BangCircle");
            svgCircle.style.fill = "#000000";
        }
        if (div_width > 20){
            var svgCircle = document.getElementById("BangCircle");
            svgCircle.style.fill = "#FFFFFF";
        }
        if (div_width == 100) {
            clearInterval(metrointerval);
            noBang = false;
            if (measureFinished === false){
                metronome4Attack(span, startPlay, tupletDuration, frequencyTarget, gestureNumber);
            } 
            else{
                console.log("Stop the metronome");
                metronomeAttackStarted = false;
                ShowBangs = false;
                bangSVG.style.display = "none";
                barNoteDuration.width = '0px';
            }
        }
    }, 30); 
}
            
// =======================================
function updateScore(i) {
    scoreImage = document.getElementById('InstrumentScore');
    readTextFile("guitar.json" + '?' + new Date().getTime(), function(text){
        var data = JSON.parse(text);
        var measureDuration = data.measureDuration;
        scoreName = data.Name;
        if (scoreName == scoreNameOld) {
            setTimeout(function() {updateScore(i)}, 30);
            return;
        } 
        else{
            var frequencyTarget = data.frequencyTarget;
            var tupletDuration = data.tupletDuration;
            var gestureNumber = data.gestureNumber;
            var startPlay = data.startPlay;
            var gestRepetition = data.gestRepetition; 
            var gestProb = data.gestProb;
            scoreImage.src = scoreName + '.png' + '?' + new Date().getTime();
            if (gestureNumber == 0){ // TODO: Refactor this
                executingTune = false;
                var bangSVG = document.getElementById("InstrumentBang");
                bangSVG.style.display = "none";
            }
            if (gestureNumber < 3 && executingTune == true){
                executingTune = false;
            }
            if (gestureNumber > 3){
                if (executingTune == false && startPlay == 0){
                    executingTune = true;
                    measureFinished = false;
                    audioFftYin(frequencyTarget);
                    metronome4Attack(measureDuration, startPlay, tupletDuration, frequencyTarget, gestureNumber, gestRepetition, gestProb); // TODO: update and remove unused variables
                }
                else {
                    executingTune = false;
                    // metronome4Attack(measureDuration, startPlay, tupletDuration, frequencyTarget, gestureNumber, gestRepetition, gestProb); // TODO: update and remove unused variables
                }
            }
            else {
                document.getElementById("InstrumentTitle").innerHTML = "Ac. Guitar";
                executingTune = false;
            }
            scoreNameOld = scoreName;
            updateMeasureBarProgress(measureDuration, startPlay, tupletDuration, frequencyTarget, gestureNumber, scoreImage);
            setTimeout(function() {updateScore(i)}, 30);
        }
    });
}

// =======================================
