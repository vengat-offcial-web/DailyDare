document.addEventListener("DOMContentLoaded", function () {
    const timerDisplay = document.getElementById("timer");
    const completeBtn = document.querySelector(".btn-accept");

    if (!timerDisplay) return;

    let totalSeconds = parseInt(timerDisplay.getAttribute("data-seconds")) || 0;
    let countdown = null; 

    // Initial state: Lock button
    if (completeBtn) {
        completeBtn.style.pointerEvents = "none";
        completeBtn.style.opacity = "0.5";
    }

    function updateCountdown() {
        let minutes = Math.floor(totalSeconds / 60);
        let seconds = totalSeconds % 60;

        if (seconds < 10) {
            seconds = "0" + seconds;
        }

        timerDisplay.innerText = (minutes < 10 ? "0" + minutes : minutes) + ":" + seconds;

        // Last 30 seconds - Warning & Unlock
        if (totalSeconds <= 30 && totalSeconds > 0) {
            timerDisplay.style.color = "#c0392b";
            if (completeBtn) {
                completeBtn.style.pointerEvents = "auto";
                completeBtn.style.opacity = "1";
            }
        }

        // Expired
        if (totalSeconds <= 0) {
            if (countdown) clearInterval(countdown);
            timerDisplay.innerText = "00:00 (EXPIRED)";
            timerDisplay.style.color = "#c0392b";
            
            if (completeBtn) {
                completeBtn.style.pointerEvents = "none";
                completeBtn.style.opacity = "0.5";
                completeBtn.innerText = "EXPIRED";
            }
        }
       
        totalSeconds--;
    }

    updateCountdown();
    countdown = setInterval(updateCountdown, 1000);
});