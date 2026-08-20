const form = document.getElementById("registration-form");
const submitButton = document.getElementById("submit-button");

form.addEventListener("submit", () => {
    submitButton.disabled = true;
    submitButton.querySelector("span:first-child").textContent = "Guardando inscripción...";
});
