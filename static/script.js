function plusSlides(sliderId, n) {
    showSlides(sliderId, (slideIndex[sliderId] += n));
}

function currentSlide(sliderId, n) {
    showSlides(sliderId, (slideIndex[sliderId] = n));
}

function showSlides(sliderId, n) {
    let i;
    let slides = document.getElementById(sliderId).getElementsByClassName("shedule__myslide");
    let dots = document.getElementById(sliderId).getElementsByClassName("dot");

    if (n > slides.length) {
        slideIndex[sliderId] = 1;
    }
    if (n < 1) {
        slideIndex[sliderId] = slides.length;
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].classList.remove("active");
    }
    slides[slideIndex[sliderId] - 1].style.display = "block";
    dots[slideIndex[sliderId] - 1].classList.add("active");
}

// Инициализация slideIndex для каждого слайдера
let slideIndex = {};

// Вызов showSlides для каждого слайдера
document.addEventListener("DOMContentLoaded", function () {
    let sliders = document.getElementsByClassName("shedule__photo");
    for (let i = 0; i < sliders.length; i++) {
        slideIndex[sliders[i].id] = 1;
        showSlides(sliders[i].id, slideIndex[sliders[i].id]);
    }
});


let navMenu = document.getElementById('header__logo')
let cross = document.getElementById('navigation__cross')

function openNav() {
    console.log('hello')
}

function closeNav() {
    console.log('hello')
}

// navMenu.addEventListener('click', openNav)
// cross.addEventListener('click', closeNav)