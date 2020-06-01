$(document).ready(function () {

    /* Hamburger menu */
    $('.btn-menu').click(function () {
        $('.ico-menu').toggleClass('open');
        $('.overlay').toggleClass('open-nav');

    });
    

    /* overlay menu on mobile */
    $('.overlay-content .overlay-link').click(function () {
        $('.overlay').removeClass('open-nav');
        $('.ico-menu').removeClass('open');
    });
    
    
    
    /* all links animation */
    $(document).on('click', 'a[href^="#"]', function (event) {
        event.preventDefault();
        $('html, body').animate({
            scrollTop: $($.attr(this, 'href')).offset().top - 68
        }, 500);
    });
    
    

    /* main nav li blue borders */
    $(function () {
        $('.main-nav li a').on('click', function () {
            $('.main-nav li a.active').removeClass('active');
            $(this).addClass('active');
        });
    });
    
    

    
    
    /* SLIDER */
    var slideIndex = 1;
    showSlides(slideIndex);

    function plusSlides(n) {
        showSlides(slideIndex += n);
    }

    function currentSlide(n) {
        showSlides(slideIndex = n);
    }

    function showSlides(n) {
        var i;
        var slides = document.getElementsByClassName("mySlides");

        if (n > slides.length) {
            slideIndex = 1
        }
        if (n < 1) {
            slideIndex = slides.length
        }
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }

        slides[slideIndex - 1].style.display = "block";

    }

    $('.prev').on('click', function () {
        plusSlides(-1)
    })

    $('.next').on('click', function () {
        plusSlides(1)
    })
    
    
    
    /* portfolio button color */ 
    $('.portfolio__toolbar button').on('click', function () {
        $('.portfolio-btn-active').removeClass('portfolio-btn-active');
        $(this).addClass('portfolio-btn-active');
    });
    
    
    /* portfolio masonry */
    var $grid = $('.grid').imagesLoaded(function () {
        // init Masonry after all images have loaded
        $grid.masonry({
            itemSelector: '.grid-item',
            transitionDuration: '0.6s'
        });
    });
    
    
    /* portfolio masonry filter */
    $(".portfolio__toolbar .btn").click(function () {
        var item = $(this).attr("data-filter");
        $('.grid').masonry('layout', {
            filter: item,
            shuffle: true
        });
    });

    

    /* back to top button */
    window.onscroll = function () {
        scrollFunction()
    };

    function scrollFunction() {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            document.getElementById("return-to-top-btn").style.display = "block";
        } else {
            document.getElementById("return-to-top-btn").style.display = "none";
        }
    };

    $('#return-to-top-btn').click(function () {
        $('body,html').animate({
            scrollTop: 0
        }, 800);
        return false;
    });


  
    

});


