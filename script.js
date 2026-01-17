console.log("Welcome to Tic Tac Toe")
let music = new Audio("music.mp3")
let turn = new Audio("ting.mp3")
let gameover = new Audio("gameover.mp3")
let turn = "X"

// function to change the turn

const changeTurn = ()=>{
    return turn === "X"?"0": "X"
}

// function to check for a win

const checkWin = ()=>{

}

// Game logic
let boxes = document.getElementsByClassName("box");
Array.from(boxes).ForEach(Element =>{
    let bostext = Document.querySelector(".boxtext")
    boxtext.addEventListener("click", ()=>{
        if(e.innerText === ""){
            e.innerText = turn;
           turn = changeTurn();
            audioTurn.play();
            checkWin();
            document.getElemtsByClassName("info")[0].innerText = " turn for " + turn;
        }
    })
})
