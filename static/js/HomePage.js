$(document).ready(function() {

    

    $("#HomeTitle").animate({'opacity':'1'},1200)
    console.log("Ciao")
    
    $('.fading').delay(800).each( function(i){
          
      var bottom_of_object = $(this).offset().top + $(this).outerHeight();
      var bottom_of_window = $(window).scrollTop() + $(window).height();
      
      /* If the object is completely visible in the window, fade it it */
      if( bottom_of_window > bottom_of_object ){
          
          $(this).animate({'opacity':'1'},500);
              
      }
      
  }); 

    /* Every time the window is scrolled ... */
    $(window).scroll( function(){
    
      /* Check the location of each desired element */
      $('.fading').each( function(i){
          
          var bottom_of_object = $(this).offset().top + $(this).outerHeight();
          var bottom_of_window = $(window).scrollTop() + $(window).height();
          
       
          /* If the object is completely visible in the window, fade it it */
          if( bottom_of_window > bottom_of_object ){
              
              $(this).animate({'opacity':'1'},500);
                  
          }
          
      }); 
  
  });

  /*
  var $grid = $('.grid').masonry({
    itemSelector: '.grid-item',
    percentPosition: true,
    columnWidth: '.grid-sizer'
  });
  // layout Masonry after each image loads
  $grid.imagesLoaded().progress( function() {
    $grid.masonry("layout");
  }); 
  */

    //$(".fading").delay(1200).fadeInScroll()

    //$(".mouseHoverFade").on("mouseenter", function() {
    //    $(".mouseHoverFade").animate({backgroundColor: "#F0F8FF"}, "slow")
    //    console.log("CiaoCiaoCiao")
    //})
    
    /**
    var $grid = $('.grid').imagesLoaded( function() {
        // init Masonry after all images have loaded
        $grid.masonry({
            itemSelector: '.grid-item',
            // use element for option
            columnWidth: '.grid-sizer',
            percentPosition: true,
            isFitWidth: true
        });
        $grid.masonry('layout');
      });
     */

      
       
      

      /**
      // init Masonry
    var $grid = $('.grid').masonry({
        itemSelector: '.grid-item',
        // use element for option
        columnWidth: '.grid-sizer',
        percentPosition: true
    });
    // layout Masonry after each image loads
    $grid.imagesLoaded().progress( function() {
        $grid.masonry('layout');
    });
    */



});

