// timing myself to see how quickly i can port the game to js

let coords = ['','','','','','','','','']
let computerWin = false;
let playerWin = false;
let playerAsk;
console.log('running')


function getRandomInt() {
    return (Math.floor(Math.random() * 8));
  } 

function drawBoard(){
    for(let i=0;i<9;i+=3){
    console.log(coords[i], "|", coords[i+1], "|", coords[i+2])
    console.log('-' * 10)
}}

async function OneRound(){
    while(true){
      playerMove = parseInt(await new Promise(resolve => {
        const playerAsk = prompt("What is the coordinate of your move: ");
        if(coords[playerAsk-1] == ''){
          resolve(playerAsk);
        }
        console.log('you cant move there dickhead')
      }));
      if(!isNaN(playerMove)){
        break;
      }
    }
    let computerMove;
    while(true){
      computerMove = getRandomInt();
      if(coords[computerMove] != '' && computerMove != playerMove-1){
        break;
      }
    }
  
    coords[playerMove-1] = 'x';
    coords[computerMove] = 'o';
    drawBoard();
  }

function wincheck(){
    for(let i=0;i<9;i+=3)
    {
        if(coords[i] == coords[i+1] && coords[i+1] == coords[i+2])
        {
            if(coords[i] == 'x')
            {
                playerWin = true;
            }
            else if(coords[i] == '0')
            {
                computerWin = true;
            }
        }}
    for(let i=0;i<3;i++){
        if(coords[i] == coords[i+3] && coords[i+3] == coords[i+6])
        {
            if(coords[i] == 'x'){
                playerWin = true;
            }
            else if(coords[i] == 'x'){
                computerWin = true;
            }
        }
    }
    if(coords[0] == coords[4] && coords[4] == coords[8])
        {
            if(coords[4] == 'x'){
                playerWin = true;
            }
            else if(coords[4] == 'x'){
                computerWin = true;
            }
        }
    if(coords[2] == coords[4] && coords[4] == coords[6])
    {
        if(coords[4] == 'x'){
            playerWin = true;
        }
        else if(coords[4] == 'x'){
            computerWin = true;
        }
    }
}

function playgame()
{
    console.log('running')
    while(true){
        console.log('cycle')
        OneRound();
        wincheck();
        if(playerWin){
            drawBoard();
            return console.log('you win!');
        }
        if(computerWin){
            drawBoard();
            return console.log('you lose');
        }
    }
}

playgame()