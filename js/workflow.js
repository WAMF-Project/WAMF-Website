const birdImage = document.querySelector(".workflow-image-bird");
const detectionBox = document.querySelector(".detection-box");
const speciesCard = document.querySelector(".species-card");
const observationStatus = document.querySelector(".observation-status");

function resetWorkflow() {
  birdImage.classList.remove("is-visible");
  detectionBox.classList.remove("is-visible");
  speciesCard.classList.remove("is-visible");
  observationStatus.classList.remove("is-visible");
}

function runWorkflow() {
  resetWorkflow();

  setTimeout(() => {
    birdImage.classList.add("is-visible");
  }, 1500);

  setTimeout(() => {
    detectionBox.classList.add("is-visible");
  }, 1900);

  setTimeout(() => {
    speciesCard.classList.add("is-visible");
  }, 2700);

  setTimeout(() => {
    observationStatus.classList.add("is-visible");
  }, 4200);

  setTimeout(runWorkflow, 7500);
}

if (birdImage && detectionBox && speciesCard && observationStatus) {
  runWorkflow();
}
