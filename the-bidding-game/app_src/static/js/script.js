// $(document).ready(function(){
//     var computerScore = 0;
//     var userScore = 0;

//     function getComputerChoice() {
//         var randomNum = Math.floor(Math.random() * 3) + 1;
//         var computerChoice;

//         if(randomNum === 1) {    
//             computerChoice = 'rock';
//         }
//         else if(randomNum === 2) {
//             computerChoice = 'paper';
//         }
//         else if(randomNum === 3) {
//             computerChoice = 'scissors';
//         }

//         return computerChoice;
//     }

//     function play(uc) {
//         var computerChoice = getComputerChoice();
//         console.log(uc)
//         if(computerChoice == 'rock') {
//             if(uc == 'paper') {
//                 winner = 'You win!';
//                 userScore++;
//             } 
//             else if(uc !== 'paper' && uc != computerChoice) {
//                 winner = 'Computer Wins!';
//                 computerScore++;
//             } else {
//                 winner = 'Draw, Better luck next time !';
//             }
//         } else if(computerChoice == 'paper') {
//             if(uc == 'scissors') {
//                 winner = 'You win!';
//                 userScore++;
//             } 
//             else if(uc !== 'scissors' && uc != computerChoice) {
//                 winner = 'Computer Wins!';
//                 computerScore++;
//             } else {
//                 winner = 'Draw, Better luck next time !';
//             }
//         } else if(computerChoice == 'scissors') {
//             if(uc == 'rock') {
//                 winner = 'You win!';
//                 userScore++;
//             } 
//             else if(uc !== 'rock' && uc != computerChoice) {
//                 winner = 'Computer Wins!';
//                 computerScore++;
//             } else {
//                 winner = 'Draw, Better luck next time !';
//             }
//         }

//         return [winner,computerChoice]
//     }

//     $('.game-board .col-4 div').click(function(){
//         var userChoice;

//         if($(this).hasClass('rock')) {
//             userChoice = 'rock';
//             var getResult = play(userChoice);
//             var winner = getResult[0];
//             var computerChoice = getResult[1];
//             $('.game-board').fadeOut().hide();
//             $('.decide-winner div').html('<h3>'+winner+'</h3><div class="'+computerChoice+'"></div><h2>'+computerChoice+'</h2>');
//             $('.decide-winner').fadeIn().removeClass('hidden');
//             $('.player-score').text(userScore);
//             $('.computer-score').text(computerScore);
//             setTimeout(function() {
//                 $('.decide-winner').fadeOut().addClass('hidden');
//                 $('.game-board').fadeIn().show();
//             }, 1500);
//         } 
//         else if($(this).hasClass('paper')) {
//             userChoice = 'paper';
//             var getResult = play(userChoice);
//             var winner = getResult[0];
//             var computerChoice = getResult[1];
//             $('.game-board').fadeOut().hide();
//             $('.decide-winner div').html('<h3>'+winner+'</h3><div class="'+computerChoice+'"></div><h2>'+computerChoice+'</h2>');
//             $('.decide-winner').fadeIn().removeClass('hidden');
//             $('.player-score').text(userScore);
//             $('.computer-score').text(computerScore);
//             setTimeout(function() {
//                 $('.decide-winner').fadeOut().addClass('hidden');
//                 $('.game-board').fadeIn().show();
//             }, 1500);
//         }
//         else if($(this).hasClass('scissors')) {
//             userChoice = 'scissors';
//             var getResult = play(userChoice);
//             var winner = getResult[0];
//             var computerChoice = getResult[1];
//             $('.game-board').fadeOut().hide();
//             $('.decide-winner div').html('<h3>'+winner+'</h3><div class="'+computerChoice+'"></div><h2>'+computerChoice+'</h2>');
//             $('.decide-winner').fadeIn().removeClass('hidden');
//             $('.player-score').text(userScore);
//             $('.computer-score').text(computerScore);
//             setTimeout(function() {
//                 $('.decide-winner').fadeOut().addClass('hidden');
//                 $('.game-board').fadeIn().show();
//             }, 1500);
//         }
//     });
// });