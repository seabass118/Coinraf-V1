//Main.js

//Mobile Menu

const mobile_menu = document.getElementById('m_container');

const showMenu = () => {
    mobile_menu.className = 'm_open_ani';
}

const hideMenu = () => {
    mobile_menu.className = 'm_close_ani';
}

var acc = document.getElementsByClassName("m_dropdown");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
    } 
  });
}

//Color Mode

const btn_desktop = document.querySelector(".color_mode_desktop");
const btn_mobile = document.querySelector(".color_mode_mobile");
const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)");
const currentTheme = localStorage.getItem("theme");

if (currentTheme == "dark") {
    document.body.classList.toggle("dark-theme");
} else if (currentTheme == "light") {
    document.body.classList.toggle("light-theme");
}

btn_desktop.addEventListener("click", function () {
    if (prefersDarkScheme.matches) {
        document.body.classList.toggle("light-theme");
        var theme = document.body.classList.contains("light-theme")
            ? "light"
            : "dark";
    } else {
        document.body.classList.toggle("dark-theme");
        var theme = document.body.classList.contains("dark-theme")
            ? "dark"
            : "light";
    }
    localStorage.setItem("theme", theme);
});

btn_mobile.addEventListener("click", function () {
    if (prefersDarkScheme.matches) {
        document.body.classList.toggle("light-theme");
        var theme = document.body.classList.contains("light-theme")
            ? "light"
            : "dark";
    } else {
        document.body.classList.toggle("dark-theme");
        var theme = document.body.classList.contains("dark-theme")
            ? "dark"
            : "light";
    }
    localStorage.setItem("theme", theme);
});


//Image Slider

window.onload = function() {

    let slider = document.querySelector('#slider');
    let moveLi = Array.from(document.querySelectorAll('#slider #move li'));
    let counter = 1;
    let time = 5000;

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
    }

    slider.onmouseout = function() {
        autoPlay = setInterval(moveUP, time);
    }
  
}


//Search Function

function coinSearch(value) {
    value = value.trim(); 
    if(value != "") { 
    $.ajaxSetup({ cache: false });
    $.ajax({
        url: "ss_search",
        data: {searchText: value},
        dataType: "json",
        success: function(data){
            let res = ""
            $.each(data, function(key, value){
                res += '<a href="'+value.id.toLowerCase()+'">'+'<div class="ss_item flex-center-vertical" style="height: 40px;"><span class="ss_system_muted flex-center-vertical">'+
                '<div id="ss_item_active" style="color: var(--mint);">'+'</div>'+
                '<img src='+value.logo_url+' style="width: 20px; height: 20px; margin-right: 10px; border-radius: 10px;">'+'<div style="padding-right: 10px;">'+value.name+'</div>'+
                '</span>'+'<div id="search_id_cont" class="text_cont">'+value.id+'</div>'+'<div class="search_rank text_cont" style="margin-left: auto; margin-right: 10px;">'+'#'+value.rank+'</div>'+'</div>'+'</a>';
            });
            $('#ss_dropdown').html(res);
        }
    });
    } else {
        $("#ss_dropdown").html(""); 
    }
}

function fetchdata(){
    $.ajax({
        url: 'index_data',
        dataType: "json",
        success: function(response){
            let ap = ""
            console.log(response)
            $.each(response, function(key, value){
                ap += value.price+" "
            });
            $("#test_data").text(ap);
        }
    });
}

fetchdata()
