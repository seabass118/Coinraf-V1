window.onload = function() {

    let slider = document.querySelector('#slider');
    let moveLi = Array.from(document.querySelectorAll('#slider #move li'));
    let counter = 1;
    let time = 5000;
    let line = document.querySelector('#line');

    line.style.animation = 'line ' + (time / 1000) + 's linear infinite';

    function moveUP() {

        if (counter == moveLi.length) {

            moveLi[0].style.marginLeft = '0%';
            counter = 1;

        } else if (counter >= 1) {

            moveLi[0].style.marginLeft = '-' + counter * 100 + '%';
            counter++;
        } 

    }

    let autoPlay = setInterval(moveUP, time);

    slider.onmouseover = function() {
        autoPlay = clearInterval(autoPlay);
        line.style.animation = '';
    }

    slider.onmouseout = function() {
        autoPlay = setInterval(moveUP, time);
        line.style.animation = 'line ' + (time / 1000) + 's linear infinite';
    }
  
}