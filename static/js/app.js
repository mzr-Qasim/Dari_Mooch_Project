
        



var $owl = $('.owl-carousel5');
    
$owl.children().each( function( index ) {
  $(this).attr( 'data-position', index ); // NB: .attr() instead of .data()
});
$owl.owlCarousel({
  responsive:{
    0:{
        items:1,
        center:true,
        nav:true,
        loop:true,
        dots:false,
        autoplay:true,
    },
    600:{
        items:2,
        nav:true,
        loop:false,
        dots:true,
    },
    1000:{
        center:true,
        loop:true,
        items:3,
        nav:false,
        autoplay:true,
    },

}
  
});