var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
        content.style.display = "none";
    } else {
        content.style.display = "block";
    }
    });
}

function printSpecificArea() {
    document.querySelector('body *').style.display = 'none';
    document.querySelector('.form-container').style.display = 'none';
    document.querySelector('#output').style.display = 'block';
    document.querySelector('.printBtn').style.display = 'none';
    setInterval(function(){ window.print(); }, 1000);
    setInterval(function(){ window.location.reload(); }, 2000);
    
}

let main_buttons = document.querySelectorAll('.main_buttons');
let button = document.querySelector('#submit');
let tetrominos = document.querySelector('.container');
let form = document.querySelector('.form-container');

// button.addEventListener('click', () => {
//     for (let i = 0; i < main_buttons.length; i++) {
//         main_buttons[i].style.display = 'none';
//     }
//     form.style.display = 'none';
//     tetrominos.style.visibility = 'visible';
// });