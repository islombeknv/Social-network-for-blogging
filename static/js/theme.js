;(function($) {
    "use strict"; 
    
    //* Navbar Fixed  
    function navbarFixed(){
        if ( $('.main_header_area').length ){ 
            $(window).on('scroll', function() {
                var scroll = $(window).scrollTop();   
                if (scroll >= 120 ) {
                    $("#header").addClass("navbar_fixed");
                } else {
                    $("#header").removeClass("navbar_fixed");
                }
            });
        };
    }; 
    
    // Scroll to top
    function scrollToTop() {
        if ($('.scroll-top').length) {  
            $(window).on('scroll', function () {
                if ($(this).scrollTop() > 200) {
                    $('.scroll-top').fadeIn();
                } else {
                    $('.scroll-top').fadeOut();
                }
            }); 
            //Click event to scroll to top
            $('.scroll-top').on('click', function () {
                $('html, body').animate({
                    scrollTop: 0
                }, 1000);
                return false;
            });
        }
    }
    
    // Product value
    function productValue() {
        var inputVal = $("#product-value");
        if (inputVal.length) {
            $('#value-decrease').on('click', function () {
                inputVal.html(function (i, val) {
                    return val * 1 - 1
                });
            });
            $('#value-increase').on('click', function () {
                inputVal.html(function (i, val) {
                    return val * 1 + 1
                });
            });
        }
    }
    
    //* Select js
    function nice_Select(){
        if ( $('.post_select').length ){ 
            $('select').niceSelect();
        };
    }; 
    
    // Preloader JS 
    function preloader(){
        if( $('.preloader').length ){
            $(window).on('load', function() {
                $('.preloader').fadeOut();
                $('.preloader').delay(50).fadeOut('slow');  
            })   
        }
    }
    
    /*Function Calls*/ 
    new WOW().init(); 
    navbarFixed ();
    scrollToTop ();
    nice_Select ();
    productValue (); 
    preloader ();
})(jQuery); 