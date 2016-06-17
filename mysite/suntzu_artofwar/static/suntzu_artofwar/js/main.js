/**
 * Created by alenush on 06.05.16.
 */
$(document).ready(function(){

$("[id*=translate_button]").click(function(){
    var my_array = this.id.split('_')
    var trans_num = my_array[my_array.length - 1];
    console.log(trans_num);
    $("#translation_"+trans_num).toggle('slow');
});

/* Page up button  */

var amountScrolled = 300;

$(window).scroll(function() {
	if ( $(window).scrollTop() > amountScrolled ) {
		$('a.back-to-top').fadeIn('slow');
	} else {
		$('a.back-to-top').fadeOut('slow');
	}
});
/* animation to up button */
$('a.back-to-top').click(function() {
	$('html, body').animate({
		scrollTop: 0
	}, 700);
	return false;
});

$('label').click(function() {

    var position = $('#left_menu').css('display');
    console.log(position);
    if (position == 'none'){
	    $('#left_menu').css('display','block');
    }
    else {
        $('#left_menu').css('display','none');
    }

    $("#site_wrap").toggleClass('col-md-12 col-md-9');

});

/* Translation of sub-chapters. Popup */

function showPopup(chapter) {
    $('#'+chapter).css('display','block');
}

var all_trans = $("[id*=sub-translation");

function check_chapter(chapter) {
    var ok_sub = '';

    for (var i=0; i < all_trans.length; i++) {
        var array = all_trans[i].id.split('_');
        var sub = array[array.length - 1];
        var paar = sub.split('-');
        if (paar[0] == chapter){
            ok_sub = all_trans[i];
        };
        if (paar[1] == chapter){
            ok_sub = all_trans[i];
        };
    };
    return ok_sub.id;
};

$("[id*=subchapter]").click(function(){
    var my_array = this.id.split('_')
    var chapter = my_array[my_array.length - 1];
    var translate_sub = check_chapter(chapter);
    showPopup(translate_sub);
    });



});