/*global $, test, equal */
test("erros should be hidden on keypress", function(){
	$('input').trigger('keypress');
	equal($('.has-error').is(':visible'), false);
});