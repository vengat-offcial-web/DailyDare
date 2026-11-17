document.addEventListener("DOMContentLoaded", () => {
    // 1. HTML-la irundhu Timer text, Complete button, and Give Up button-ah pudikkurom
    const timerElement = document.getElementById("timer");
    const completeBtn = document.getElementById("complete-btn");
    const giveupBtn = document.querySelector(".btn-next"); // Auto-fail redirect-kaga Give Up link edukurom

    if (!timerElement) return;

    let remainingSeconds = parseInt(timerElement.getAttribute("data-seconds")) || 60;

    function formatTime(seconds) {
        const mins = Math.floor(seconds / 60);
        const secs = seconds % 60;
        return `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
    }

    // Helper Function A: Complete button-ah Lock & Blend panradhu
    function lockCompleteButton() {
        if (!completeBtn) return;
        completeBtn.style.opacity = "0.35";           // Dull-a background kooda blend aagum
        completeBtn.style.pointerEvents = "none";     // Mouse click panna mudiyadhu
        completeBtn.style.cursor = "not-allowed";     // Blocked icon kaattum
        completeBtn.innerText = "LOCKED";             // User-ku puriya text maathurom
    }

    // Helper Function B: Last 30 seconds-la Unlock panradhu
    function unlockCompleteButton() {
        if (!completeBtn) return;
        completeBtn.style.opacity = "1";              // Normal bright green color
        completeBtn.style.pointerEvents = "auto";     // Click panna mudiyum
        completeBtn.style.cursor = "pointer";
        completeBtn.innerText = "COMPLETE";
    }

    // Page load aana udane time 30 seconds-ku mela irundha button-ah lock pannidu
    if (remainingSeconds > 30) {
        lockCompleteButton();
    }

    timerElement.innerText = formatTime(remainingSeconds);

    const timerInterval = setInterval(() => {
        remainingSeconds--;
        timerElement.innerText = formatTime(remainingSeconds);

        // Kadaisi 30 seconds vandha udane Anti-Cheat lock open aagum
        if (remainingSeconds <= 30 && remainingSeconds > 0) {
            unlockCompleteButton();
        }

        // Time 00:00 aana udane Auto-Fail
        if (remainingSeconds <= 0) {
            clearInterval(timerInterval);
            if (giveupBtn) {
                window.location.href = giveupBtn.href; // Automatic-a Give Up URL-ku pogum
            }
        }
    }, 1000);
});