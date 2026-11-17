// 1. HTML-la irukkura 3 mukkiyamaana items-ah edukurom
var timerText = document.getElementById("timer");
var completeBtn = document.getElementById("complete-btn");
var giveupBtn = document.querySelector(".btn-next");

// 2. HTML-la irundhu total seconds edukurom (eg: 60)
var seconds = parseInt(timerText.getAttribute("data-seconds"));

// 3. Page open aana udane time 30s-ku mela irundha button-ah lock pandrom
if (seconds > 30) {
    completeBtn.style.opacity = "0.4";
    completeBtn.style.pointerEvents = "none";
    completeBtn.innerText = "LOCKED";
}

// 4. Ovvoru 1 second-kum indha timer loop odum
var timer = setInterval(function() {

    // Minutes and Seconds calculation
    var mins = Math.floor(seconds / 60);
    var secs = seconds % 60;

    // 10-ku kulla irundha munnadi '0' serkurom (eg: 9 -> 09)
    if (mins < 10) { mins = "0" + mins; }
    if (secs < 10) { secs = "0" + secs; }

    // Screen-la time-ah kaaturom (eg: 01:30)
    timerText.innerText = mins + ":" + secs;

    // Kadaisi 30 seconds vandha: Timer RED color + Button UNLOCK!
    if (seconds <= 30) {
        timerText.style.color = "red";
        completeBtn.style.opacity = "1";
        completeBtn.style.pointerEvents = "auto";
        completeBtn.innerText = "COMPLETE";
    }

    // Time 0 aana udane: Timer stop + Automatic Give Up
    if (seconds <= 0) {
        clearInterval(timer);
        window.location.href = giveupBtn.href;
    }

    // Ovvoru second-um 1 kuraiyurom
    seconds = seconds - 1;

}, 1000);