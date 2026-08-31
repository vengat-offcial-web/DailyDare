let totalSeconds = 5 * 60
const timerDisplay = document.getElementById("timer");
const completeBtn = document.querySelector("btn-accept");
const countdown = setInterval(function () {

    let minutes = Math.floor(totalSeconds / 60);

    let seconds = totalSeconds % 60;

    if (seconds < 10) {
        seconds = "0" + seconds;
    }

    timerDisplay.innerText = minutes + ":" + seconds

    if (totalSeconds <= 30 && totalSeconds > 0) {

        timerDisplay.style.color = "#ef4444";

        if (completeBtn) {
            completeBtn.style.pointerEvents = "auto";
            completeBtn.style.opacity = "1";
        }
    }

    if (totalSeconds <= 0) {

        clearInterval(countdown)

        timerDisplay.innerText = "00 : 00 (FAILED)";
        timerDisplay.style.color = "#ef4444";
    }

    if (completeBtn) {

        completeBtn.style.pointerEvents = "none";
        completeBtn.style.opacity = "0.5";
        completeBtn.innerText = "EXPIRED";
    }
    totalSeconds--

}, 1000)