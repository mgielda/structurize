$(document).ready(function() {
  $('li').on('click', function(event) {
    if ($(this).hasClass("text")) {
      $(this).hide();
      $(this).nextUntil('li.title').hide();
      $(this).prevUntil('li.title').hide();
      $(this).prevAll('li.title:first').show();
    }
    else if ($(this).hasClass("title")) {
      $(this).hide();
      $(this).nextUntil('li.title').show();
    }
    event.stopPropagation();
  });
  $('.header').on('click', function() {
    if (!($(this).find('.text').is(':hidden'))) {
      $(this).find('.text').hide();
      $(this).find('.title').show();
    }
    else {
      $(this).find('.title').hide();
      $(this).find('.text').show();
    }
  });
});
