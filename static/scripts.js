
$( document ).ready(function() {

    // Navbar click function
    $('li.menu').click(function(){
        $('li.menu').removeClass("active");
        $(this).addClass("active");
    });

    // Vocab difficulty click function
    $('a.vocab-level').click(function(){
        $('a.vocab-level').removeClass("active");
        $(this).addClass("active");

        // Make all elements visible first
        $('.english').show();

        // Hide easier vocab depending on the selected difficulty level
        if ($(this).attr("id") == "vocab2")
        {
            for (var i = 10; i < 100; i++)
            {
                $('#frequency'+i+'.english').hide()
                }
        }
        else if ($(this).attr("id") == "vocab3")
        {
            for (var j = 4; j < 100; j++)
            {
                $('#frequency'+j+'.english').hide();
            }
        }

        var id = $(this).attr("id").slice(-1);

        // Change the href attributes on the section numbers to reflect the new vocab level
        $('.section-link').each(function() {
            var href = $(this).attr("href")
            $(this).attr("href", href.slice(0, -1) + id);
        });
    });

    // When the book links are hovered over with mouse, diplay book number
    $('.book-link').hover(function() {
        $('.section-number').text("");
        var id = $(this).attr("id");
        $('.book-number').text(id);
    });

    // When the section links are hovered over with mouse, diplay section number
    $('.section-link').hover(function() {
        $('.book-number').text("");
        var href = $(this).attr("href").slice(-6, -2);
        $('.section-number').text(href);
    });

    console.log("hello")
    // Add 'active' class to links depending on the current page
    var pathname = window.location.pathname;
    if (pathname.length > 1)
    {
        if (pathname[1] == 'r')
        {
            $('#republic').trigger("click");
        }

        $('a.book-link').removeClass("active");
        console.log("hello");
        console.log(pathname.slice(-15, -14));
        $('.book-link[id="'+pathname.slice(-15, -14)+'"]').addClass("active");

        $('a.section-link').removeClass("active");
        $('.section-link[href="'+pathname+'"]').addClass("active");

        $('a.vocab-level').removeClass("active");
        $('#vocab'+pathname.slice(-1)).addClass("active");
    }
});

// Keep sidebar from overlapping with footer
// https://stackoverflow.com/questions/8653025/stop-fixed-position-at-footer
function checkOffset() {
    if($('.sidebar').offset().top + $('.sidebar').height()
                                          >= $('footer').offset().top - 10)
        $('.sidebar').css('position', 'absolute');
    else if($('.sidebar').offset().top + $('.sidebar').height()
                                          >= $('.passage-selection').offset().top - 10)
        $('.sidebar').css('position', 'absolute');
    if($(document).scrollTop() + window.innerHeight < $('footer').offset().top)
        $('.sidebar').css('position', 'fixed'); // restore when you scroll up
}

$(document).scroll(function() {
    checkOffset();
});
