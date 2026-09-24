

const snakeHead = document.querySelector("snake-head");
const foodElement = document.querySelector("food");
const board = document.querySelector("board");
const scoreElement = document.querySelector("score");

let direction = {
    x: 1,
    y: 0,
};

const food = {
    x: 15,
    y: 10,
};

let snake = [
    { x: 5, y: 5 },
];

let score = 0;

