$(function() {
    
    "use strict";

    //===== Subscribe modal

    $("#subscribeForm").on("submit", function(e) {
        e.preventDefault();
        var form = $(this);
        var data = new FormData(this);

        var xhr = new XMLHttpRequest();

        var success = function(event) {
            $("#subscribeFormWrapper").html('<p class="alert alert-success">Děkujeme, brzy se ozveme a uvaříme spolu to nejlepší pivo!</p>');
            dataLayer.push({'event': 'form', 'action': 'submit', 'label': 'subscribe'});
        };
        var fail = function(event) {
            if (xhr.status == 422) {
                $("#subscribeFormMessage").html('<p class="mt-20 alert alert-danger">Jejda, potřebujeme správnou e&#8209;mailovou adresu.</p>');
            } else {
                $("#subscribeFormMessage").html('<p class="mt-20 alert alert-danger">Omlouváme se, něco se pokazilo</p>');
            }
        };
        xhr.addEventListener('error', fail);
        xhr.addEventListener('load', function(event) {
            if (xhr.status != 200) {
                fail(event);
                return;
            }
            success(event);
        });
      
        xhr.open(form.attr("method"), form.attr("action"));
        xhr.send(data);
    });

    //===== CTA button tracking

    $("#ctaMain").on("click", function(e) {
        dataLayer.push({'event': 'cta', 'action': 'click', 'label': 'main'});
    });
    $("#ctaPartners").on("click", function(e) {
        dataLayer.push({'event': 'cta', 'action': 'click', 'label': 'partners'});
    });
    $("#ctaPrice").on("click", function(e) {
        dataLayer.push({'event': 'cta', 'action': 'click', 'label': 'price'});
    });


    //===== Contact form

    $("#contact-form").on("submit", function(e) {
        e.preventDefault();
        var form = $(this);
        var data = new FormData(this);

        var xhr = new XMLHttpRequest();

        var success = function(event) {
            $("#contact-form").html('<p class="alert alert-success">Děkujeme za zprávu, brzy se ti ozveme.</p>');
            dataLayer.push({'event': 'form', 'action': 'submit', 'label': 'contact'});
        };
        var fail = function(event) {
            if (xhr.status == 422) {
                $("#contact-form-message").html('<p class="alert alert-danger">Jejda, prosím vyplň všechna pole a zkontroluj e&#8209;mailovou adresu.</p>');
            } else {
                $("#contact-form-message").html('<p class="alert alert-danger">Omlouváme se, něco se pokazilo</p>');
            }
        };
        xhr.addEventListener('error', fail);
        xhr.addEventListener('load', function(event) {
            if (xhr.status != 200) {
                fail(event);
                return;
            }
            success(event);
        });
      
        xhr.open(form.attr("method"), form.attr("action"));
        xhr.send(data);
    });
    
    //===== Prealoder
    
    $(window).on('load', function(event) {
        $('.preloader').delay(200).fadeOut(500);
    });
    
     //===== close navbar-collapse when a  clicked
    
    $(".navbar-nav a").on('click', function () {
        $(".navbar-collapse").removeClass("show");
    });
    
    //===== Mobile Menu
    
    $(".navbar-toggler").on('click', function(){
        $(this).toggleClass("active");
    });
    
    $(".navbar-nav a").on('click', function() {
        $(".navbar-toggler").removeClass('active');
    });
    
    
    //===== Section Menu Active

    var scrollLink = $('.page-scroll');
        // Active link switching
        $(window).scroll(function() {
        var scrollbarLocation = $(this).scrollTop();

        scrollLink.each(function() {

          var sectionOffset = $(this.hash).offset().top - 73;

          if ( sectionOffset <= scrollbarLocation ) {
            $(this).parent().addClass('active');
            $(this).parent().siblings().removeClass('active');
          }
        });
    });    
    
        
    //===== Back to top
    
    // Show or hide the sticky footer button
    $(window).on('scroll', function(event) {
        if($(this).scrollTop() > 600){
            $('.back-to-top').fadeIn(200)
        } else{
            $('.back-to-top').fadeOut(200)
        }
    });
    
    
    //Animate the scroll to yop
    $('.back-to-top').on('click', function(event) {
        event.preventDefault();
        
        $('html, body').animate({
            scrollTop: 0,
        }, 1500);
    });
    
    
    //=====  AOS
    
    new WOW().init();
    
    
});