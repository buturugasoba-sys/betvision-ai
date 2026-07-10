
async function analyzeMatch() {

    const response = await fetch("http://localhost:8000/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            home_form: 80,
            goals_average: 3,
            defense_strength: 75
        })
    });

    const data = await response.json();

    document.getElementById("result").innerText =
        JSON.stringify(data);
}
