import {
  increamentCustomProperty,
  setCustomProperty,
  getCustomProperty,
} from "./updateCustomProperty.js";

const SPEED = 0.05;
const CACTUS_INTERVAL_MIN = 500;
const CACTUS_INTERVAL_MAX = 2000;
const worldElement = document.querySelector("[data-world]");

let nextCactusTime;

function setupCactus() {
  nextCactusTime = CACTUS_INTERVAL_MIN;
  document.querySelectorAll("[data-cactus]").forEach((cactus) => {
    cactus.remove();
  });
}

function updateCactus(delta, speedScale) {
  document.querySelectorAll("[data-cactus]").forEach((cactus) => {
    increamentCustomProperty(cactus, "--left", delta * speedScale * SPEED * -1);
    if (getCustomProperty(cactus, "--left") <= -100) {
      cactus.remove();
    }
  });

  if (nextCactusTime <= 0) {
    createCactus();
    nextCactusTime =
      randomNumberBetween(CACTUS_INTERVAL_MAX, CACTUS_INTERVAL_MAX) /
      speedScale;
  }

  nextCactusTime -= delta;
}

function getCactusRects() {
  return [...document.querySelectorAll("[data-cactus]")].map((cactus) => {
    return cactus.getBoundingClientRect();
  });
}

function createCactus() {
  const cactus = document.createElement("img");
  cactus.dataset.cactus = true;
  cactus.src = getRandomCactus();
  cactus.classList.add("cactus");
  setCustomProperty(cactus, "--left", 100);
  worldElement.append(cactus);
}

function getRandomCactus() {
  let cactusAddr = [
    "../img/colored-cactus.png",
    "../img/cactus.png",
    "../img/small-cactus.bmp",
  ];

  return cactusAddr[Math.floor(Math.random() * cactusAddr.length)];
}

function randomNumberBetween(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}

export { updateCactus, setupCactus, getCactusRects };
