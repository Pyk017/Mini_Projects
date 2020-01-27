var original_board;
var huplayer = 'O';
var opponent = 'X';
const win_combos = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [6, 4, 2], 
];

const cells = document.getElementsByClassName('cell');

function signing(){
    var original_value = document.getElementsByClassName("sign");
    if (original_value[0].checked){
        huplayer = original_value[0].value;
        opponent = original_value[1].value;
    }
    else{
        opponent = original_value[0].value;
        huplayer = original_value[1].value;
    }
    startGame();
}

function startGame(){
    document.getElementById("end").style.display = "none";
    original_board = Array.from(Array(9).keys());
    for (var i=0; i<cells.length; i++){
        cells[i].innerHTML = '';
        cells[i].style.removeProperty('background-color');
        cells[i].addEventListener('click', turnClick, false); 
    }
}

function turnClick(square){
    if (typeof original_board[square.target.id] == 'number'){
        turn(square.target.id, huplayer);
        if(!check_win(original_board, huplayer) && !check_tie()) turn(best_spot(), opponent);
    }
}

function turn(square_id, pl){
    original_board[square_id] = pl;
    console.log(square_id);
    document.getElementById(square_id).innerText = pl; 
    let game_won = check_win(original_board, pl);
    if(game_won) game_Over(game_won)
}

function check_win(board, player){
    let plays = board.reduce((a, e, i) =>
    (e == player) ? a.concat(i) : a, [])
    let game_won = null;
    for (let [index, win] of win_combos.entries()){
        if (win.every(elem => plays.indexOf(elem) > -1)){
            game_won = {index: index, player: player};
            break;
        }
    }
    return game_won;
}

function game_Over(game_won){
    for(let index of win_combos[game_won.index]){
        document.getElementById(index).style.backgroundColor = 
        (game_won.player) == huplayer ? "blue" : "red";
    }
    for (var i=0; i<cells.length; i++){
        cells[i].removeEventListener('click', turnClick, false);
    }
    declare_winner(game_won.player == huplayer ? "You Win!" : "You Lose!");
}

function declare_winner(string){
    document.getElementById("end").style.display = "block";
    document.getElementById("text").innerHTML = string;
}

function emptySquare(){
    return original_board.filter(s => typeof s == 'number');
}

function best_spot(){
    return minimax(original_board, opponent).index;
}

function check_tie(){
    if (emptySquare().length == 0){
        for (var i=0; i<cells.length; i++){
            cells[i].style.backgroundColor = "green"
            cells[i].removeEventListener("click", turnClick, false);
        }
        declare_winner("Tie Game");
        return true;
    }
    return false;
}

function minimax(newBoard, player) {
	var availSpots = emptySquare();

	if (check_win(newBoard, huplayer)) {
		return {score: -10};
	} else if (check_win(newBoard, opponent)) {
		return {score: 10};
	} else if (availSpots.length === 0) {
		return {score: 0};
	}
	var moves = [];
	for (var i = 0; i < availSpots.length; i++) {
		var move = {};
		move.index = newBoard[availSpots[i]];
		newBoard[availSpots[i]] = player;

		if (player == opponent) {
			var result = minimax(newBoard, huplayer);
			move.score = result.score;
		} else {
			var result = minimax(newBoard, opponent);
			move.score = result.score;
		}

		newBoard[availSpots[i]] = move.index;

		moves.push(move);
	}

	var bestMove;
	if(player === opponent) {
		var bestScore = -10000;
		for(var i = 0; i < moves.length; i++) {
			if (moves[i].score > bestScore) {
				bestScore = moves[i].score;
				bestMove = i;
			}
		}
	} else {
		var bestScore = 10000;
		for(var i = 0; i < moves.length; i++) {
			if (moves[i].score < bestScore) {
				bestScore = moves[i].score;
				bestMove = i;
			}
		}
	}
	return moves[bestMove];
}