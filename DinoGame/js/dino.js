import {
  getCustomProperty,
  increamentCustomProperty,
  setCustomProperty,
} from "./updateCustomProperty.js";

const dinoElement = document.querySelector("[data-dino]");
const JUMP_SPEED = 0.45;
const GRAVITY = 0.0015;
const DINO_FRAME_COUNT = 2;
const FRAME_TIME = 100;

let isJumping;
let currentFrameTime;
let dinoFrame;
let yVelocity;

function setupDino() {
  isJumping = false;
  currentFrameTime = 0;
  dinoFrame = 0;
  yVelocity = 0;
  setCustomProperty(dinoElement, "--bottom", 0);
  document.removeEventListener("keydown", onJump);
  document.addEventListener("keydown", onJump);
}

function updateDino(delta, speedScale) {
  handleRun(delta, speedScale);
  handleJump(delta);
}

function handleRun(delta, speedScale) {
  if (isJumping) {
    dinoElement.src = "../img/dino-stationary.png";
    return;
  }

  if (currentFrameTime >= FRAME_TIME) {
    dinoFrame = (dinoFrame + 1) % DINO_FRAME_COUNT;
    dinoElement.src = `../img/dino-run-${dinoFrame}.png`;
    currentFrameTime -= FRAME_TIME;
  }

  currentFrameTime += delta * speedScale;
}

function handleJump(delta) {
  if (!isJumping) return;

  increamentCustomProperty(dinoElement, "--bottom", yVelocity * delta);

  if (getCustomProperty(dinoElement, "--bottom") <= 0) {
    setCustomProperty(dinoElement, "--bottom", 0);
    isJumping = false;
  }

  yVelocity -= GRAVITY * delta;
}

function onJump(e) {
  if (e.code != "Space" || isJumping) return;

  yVelocity = JUMP_SPEED;
  isJumping = true;
}

function getDinoRects() {
  return dinoElement.getBoundingClientRect();
}

function setDinoLose() {
  dinoElement.src = "../img/dino-lose-red.png";
}

export { updateDino, setupDino, getDinoRects, setDinoLose };
