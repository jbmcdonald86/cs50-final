
$( document ).ready(function() {
    console.log( "ready!" );

    // Navbar click function
    $('li.menu').click(function(){
        console.log("hello")
        $('li.menu').removeClass("active");
        $(this).addClass("active");
    });

    $('a.vocab-level').click(function(){
        $('a.vocab-level').removeClass("active");
        $(this).addClass("active");

        // Make all elements visible first
        $('.english').show();

        // Hide easier vocab depending on the selected difficulty level
        if ($(this).attr("id") == "2")
        {
            for (var i = 1; i < 20; i++)
            {
                console.log(i.toString())
                $('.english li[frequency="1"]').toggle();
            }
        }
        else if ($(this).attr("id") == "3")
        {
            for (var j = 10; j < 20; j++)
            {
                $('.english [frequency="'+j+'"]').hide();
            }
        }
    });

    // When the book links are hovered over with mouse, diplay book number
    $('.book-link').hover(
    function() {
        $('.section-number').text("");
        var id = $(this).attr("id");
        $('.book-number').text(id);
    });

    // When the section links are hovered over with mouse, diplay section number
    $('.section-link').hover(
    function() {
        $('.book-number').text("");
        var href = $(this).attr("href").slice(-6, -2);
        $('.section-number').text(href);
    });

    // Add 'active' class to links depending on the current page
    var pathname = window.location.pathname
    if (pathname.length > 1)
    {
        if (pathname[1] == 'r')
        {
            console.log(pathname)
            $('#republic').trigger("click");
        }
        if (pathname[1] == 'o')
        {
            $('#odyssey').trigger("click");
        }

        $('a.book-link').removeClass("active");
        $('.book-link[href="'+pathname+'"]').addClass("active");

        $('a.section-link').removeClass("active");
        $('.section-link[href="'+pathname+'"]').addClass("active");

        $('a.vocab-level').removeClass("active");
        $('#'+pathname.slice(-1)).addClass("active");
    }
});

