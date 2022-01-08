import {
  increamentCustomProperty,
  setCustomProperty,
  getCustomProperty,
} from "./updateCustomProperty.js";

const groundElements = document.querySelectorAll("[data-ground]");
const SPEED = 0.05;

//? Initial setup of ground.
function setupGround() {
  setCustomProperty(groundElements[0], "--left", 0);
  setCustomProperty(groundElements[1], "--left", 300);
}

//? Update the ground length to infinite as it moves to the left.
function updateGround(delta, speedScale) {
  groundElements.forEach((ground) => {
    increamentCustomProperty(ground, "--left", delta * speedScale * SPEED * -1);
    if (getCustomProperty(ground, "--left") <= -300) {
      increamentCustomProperty(ground, "--left", 600);
    }
  });
}

export { setupGround, updateGround };
