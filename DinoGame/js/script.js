import { updateGround, setupGround } from "./ground.js";
import { updateDino, setupDino, getDinoRects, setDinoLose } from "./dino.js";
import { updateCactus, setupCactus, getCactusRects } from "./cactus.js";

const WORLD_WIDTH = 100;
const WORLD_HEIGHT = 30;
const SPEED_SCALE_INCREAMENT = 0.00001;
const worldElement = $("[data-world]");
const scoreElement = document.querySelector("[data-score]");
const startScreenElement = document.querySelector("[data-start-screen]");

let lastTime;
let speedScale;
let score;

//? Call to setPixelToWorldScale() at the starting of the document for responsiveness.
setPixelToWorldScale();

//? Event listener calls setPixelToWorldScale() upon resizing the window.
window.addEventListener("resize", setPixelToWorldScale);

//? Event Listener calls handleStart() upon entering some keys once.
document.addEventListener("keydown", handleStart, { once: true });

//? this function update the time and animations on the object.
function update(time) {
  if (lastTime == null) {
    lastTime = time;
    window.requestAnimationFrame(update);
    return;
  }

  const delta = time - lastTime;

  updateGround(delta, speedScale);
  updateDino(delta, speedScale);
  updateCactus(delta, speedScale);
  updateSpeedScale(delta);
  updateScore(delta);

  if (checkLose()) return handleLose();

  lastTime = time;
  window.requestAnimationFrame(update);
}

//? function to update score.
function updateScore(delta) {
  score += delta * 0.01;
  scoreElement.textContent = Math.floor(score);
}

//? function to update the speed of the game as the game progresses based on delta.
function updateSpeedScale(delta) {
  speedScale += delta * SPEED_SCALE_INCREAMENT;
}

function checkLose() {
  const dinoRect = getDinoRects();
  console.log(dinoRect);
  console.log(getCactusRects());
  return getCactusRects().some((rect) => isCollision(rect, dinoRect));
}

function isCollision(rect1, rect2) {
  return (
    rect1.left < rect2.right &&
    rect1.top < rect2.bottom &&
    rect1.right > rect2.left &&
    rect1.bottom > rect2.top
  );
}

//? Whenever user clicks any button this function starts.
function handleStart() {
  lastTime = null;
  speedScale = 1;
  score = 0;
  setupGround();
  setupDino();
  setupCactus();
  startScreenElement.classList.add("hide");
  window.requestAnimationFrame(update);
}

function handleLose() {
  setDinoLose();
  setTimeout(() => {
    document.addEventListener("keydown", handleStart, { once: true });
    startScreenElement.classList.remove("hide");
  }, 1000);
}

//? function to change the dimentions of the game based on the screen size.
function setPixelToWorldScale() {
  let worldToPixelScale;

  if (window.innerWidth / window.innerHeight < WORLD_WIDTH / WORLD_HEIGHT) {
    worldToPixelScale = window.innerWidth / WORLD_WIDTH;
  } else {
    worldToPixelScale = window.innerHeight / WORLD_HEIGHT;
  }

  $("[data-world]").css("width", `${WORLD_WIDTH * worldToPixelScale}px`);

  $("[data-world]").css("height", `${WORLD_HEIGHT * worldToPixelScale}px`);
  console.log(WORLD_WIDTH * worldToPixelScale);
  console.log(WORLD_HEIGHT * worldToPixelScale);
}
