

document.addEventListener("DOMContentLoaded", () => {
    const timerElement = document.getElementById("timer");
    if (!timerElement) return;
    let remainingSeconds = parseInt(timerElement.getAttribute("data-seconds")) || 60;

    function formatTime(seconds) {

        const mins = Math.floor(seconds / 60);
        const secs = seconds % 60;

        const formattedMins = String(mins).padStart(2, '0');
        const formattedSecs = String(secs).padStart(2, '0');

        return `${formattedMins}:${formattedSecs}`;
    }

    timerElement.innerText = formatTime(remainingSeconds);

    const timerInterval = setInterval(() => {

        remainingSeconds--;

    timerElement.innerText = formatTime(remainingSeconds);
    timerElement.innerText = formatTime(remainingSeconds);

if (remainingSeconds <= 0) {
            clearInterval(timerInterval); 
        }

    }, 1000); 
});