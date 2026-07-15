document.addEventListener("DOMContentLoaded", function () {

    if(document.querySelector(".heroSwiper")){

        new Swiper(".heroSwiper",{

            loop:true,

            speed:800,

            autoplay:{
                delay:5000,
                disableOnInteraction:false
            },

            pagination:{
                el:".swiper-pagination",
                clickable:true
            },

            navigation:{
                nextEl:".swiper-button-next",
                prevEl:".swiper-button-prev"
            }

        });

    }

});