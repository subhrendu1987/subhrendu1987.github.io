jQuery(document).ready( function($) {
    $('.update_profile').on('click', function() {
        var post_id = $(this).attr( 'id' );
        
        var designation = $('#designation').val();
        var phd_title = $('#designation').val();
        var phd_institute_location = $('#phd_institute_location').val();
        var phd_passing_year = $('#phd_passing_year').val();
        var phone = $('#phone').val();
        var web_profile = $('#web_profile').val();   
        var faculty_address = $('#faculty_address').val();
        var personal_web_page = $('#personal_web_page').val();       
        var degree = $('#degree').val();
        var recent_books = $('#recent_books').val();
        var summernote_profile =$('#summernote_profile').val();
        var upload_resume = $('#upload_resume').val();
        var awards_honours = $(this).attr( 'id' );
        var recent_publications = $(this).attr( 'id' );
        var research_interests = $(this).attr( 'id' );




        $.ajax({
            type: 'POST',
            url: ajax_object.ajaxurl,
            data: {
                action: 'custom_update_post',
                post_id: post_id,
                designation:designation,
                phd_title:phd_title,
                phd_institute_location:phd_institute_location,
                phd_passing_year:phd_passing_year,
                phone:phone,
                faculty_address:faculty_address,
                personal_web_page:personal_web_page,
                upload_resume:upload_resume,
                degree:degree,
                awards_honours:awards_honours,
                recent_publications:recent_publications,
                research_interests:research_interests,
                recent_books:recent_books,
                profile:summernote_profile
            }
        });
    });
});