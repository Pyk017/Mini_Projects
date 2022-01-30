let grid = document.getElementById("grid");
let list = document.getElementById("list");
let boxes = document.querySelectorAll(".box");
let images = document.querySelectorAll(".image");
let checkbox = document.getElementById("checkbox");
let gridIcon = document.getElementById("grid-image");
let listIcon = document.getElementById("list-image");
let flag = false;
let currentState;

let grid_images = Array(12)
  .fill(0)
  .map((img, idx) => {
    return `https://picsum.photos/500?random=${idx + 1}`;
  });

let list_images = Array(12)
  .fill(0)
  .map((img, idx) => {
    return `https://picsum.photos/600/300?random=${idx + 1}`;
  });

const grid_icons = [
  "./images/grid-gradient.png",
  "./images/grid-blue.png",
  "./images/grid-flatart.png",
  "./images/grid-pink.png",
  "./images/grid-cute.png",
];

const list_icons = [
  "./images/list-gradient.png",
  "./images/list-blue.png",
  "./images/list-flatart.png",
  "./images/list-pink.png",
  "./images/list-cute.png",
];

const TOTAL_ICONS = grid_icons.length;

let generateRandomIndex = () => {
  return Math.floor(Math.random() * 4);
};

let firstIconNum = generateRandomIndex();

gridIcon.src = grid_icons[firstIconNum];
gridIcon.dataset.iconNum = firstIconNum;

listIcon.src = list_icons[firstIconNum];
listIcon.dataset.iconNum = firstIconNum;

grid.addEventListener("click", userClicked);
list.addEventListener("click", userClicked);

checkbox.addEventListener("click", () => {
  let body = document.body;
  body.classList.toggle("dark-mode-body");
  toggleIcons();
});

function toggleIcons() {
  let presentIconNum = gridIcon.dataset.iconNum;
  let randomIconNum = generateRandomIndex();
  let correntIconNum =
    presentIconNum == randomIconNum
      ? (presentIconNum + 1) % TOTAL_ICONS
      : randomIconNum;

  gridIcon.src = grid_icons[correntIconNum];
  gridIcon.dataset.iconNum = correntIconNum;

  listIcon.src = list_icons[correntIconNum];
  listIcon.dataset.iconNum = correntIconNum;
}

function changeBoxes(dimention) {
  boxes.forEach((box) => {
    box.style.flexBasis = dimention + "%";
  });
}

function changeImages(type) {
  images.forEach((image, idx) => {
    image.src = type == "grid" ? grid_images[idx] : list_images[idx];
    image.style.aspectRatio = type == "grid" ? "1 / 1" : "auto";
  });
}

function userClicked() {
  if (this.getAttribute("id") == "grid") {
    changeBoxes("30");
    changeImages("grid");
  } else {
    changeBoxes("100");
    changeImages("list");
  }
}
