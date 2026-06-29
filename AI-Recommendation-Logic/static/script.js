const button = document.getElementById("recommendBtn");

const recommendationList = document.getElementById("recommendationList");

button.addEventListener("click", async () => {

    const category = document.getElementById("category").value;

    const level = document.getElementById("level").value;

    if (category === "" || level === "") {

        alert("Please select both Category and Level.");

        return;

    }

    try {

        const response = await fetch("/recommend", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                category: category,
                level: level

            })

        });

        const data = await response.json();

        displayRecommendations(data.recommendations);

    }

    catch (error) {

        console.error(error);

        alert("Something went wrong!");

    }

});


function displayRecommendations(recommendations) {

    recommendationList.innerHTML = "";

    recommendations.forEach(item => {

        const li = document.createElement("li");

        li.innerHTML = "✅ " + item;

        recommendationList.appendChild(li);

    });

}
