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

/*function showPopup(chapter) {
    $('#'+chapter).css('display','block');
}*/

function showPopup(chapter) {
console.log(chapter);
$('#sub-translation_'+chapter).css('display', 'block');
$('#overlay_'+chapter).css('display', 'block');

$('.close').click(function() {
    $('#sub-translation_'+chapter).css('display', 'none');
    $('#overlay_'+chapter).css('display', 'none');
});

$(document).keydown(function(e) {
    // ESCAPE key pressed
    if (e.keyCode == 27) {
        $('#sub-translation_'+chapter).css('display', 'none');
        $('#overlay_'+chapter).css('display', 'none');
    }
});

};

var all_trans = $("[id*=sub-translation");

function check_chapter(chapter) {
    var ok_sub = '';

    for (var i=0; i < all_trans.length; i++) {
        var array = all_trans[i].id.split('_');
        var sub = array[array.length - 1];
        var paar = sub.split('-');
        if (paar.length == 1 ){
            if (chapter == sub){
                console.log("SUB", chapter, sub, paar.length)
                ok_sub = all_trans[i];
            };
        } else {
            if (parseInt(chapter) >= parseInt(paar[0]) && parseInt(chapter) <= parseInt(paar[1])){
                console.log('inside: ', all_trans[i])
                ok_sub = all_trans[i];
                break;
            };
        };
    };
    return ok_sub.id;
};

$("[id*=subchapter]").click(function(){
    var my_array = this.id.split('_')
    var chapter = my_array[my_array.length - 1];
    var translate_sub = check_chapter(chapter);
    var ask_for = translate_sub.split('_')
    var my_chapter = ask_for[ask_for.length - 1]
    showPopup(my_chapter);
    });

});