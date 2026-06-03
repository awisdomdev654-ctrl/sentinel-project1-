
async function getSecurityData() {
    try {
        // FETCH: Grabbing the data Python just exported
        const response = await fetch('security_data.json');
        const data = await response.json();

        // DOM SELECTION
        const statusText = document.getElementById('status');
        const timeText = document.getElementById('time');
        const card = document.getElementById('status-card');

        // UPDATING THE CONTENT
        statusText.innerText = data.status;
        timeText.innerText = data.last_scan;
        
        // LOGIC SMASH: CSS + DOM + PYTHON DATA
        if (data.status === "Warning") {
            card.className = "card warning"; // Triggers the red flashing animation
        } else {
            card.className = "card secure";  // Stays green
        }
    } catch (error) {
        console.log("Waiting for Python Sentinel to generate data...");
    }
}