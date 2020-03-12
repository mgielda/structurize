$(document).ready(function() {
  $('.title').each(function() {
    wc = 0;
    $(this).nextUntil('li.title').each(function() {
      wc += $(this).text().split(' ').length;
    });
    $(this).html($(this).html()+" <span class='count'>("+wc+")</span>")
  });
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
    let parent = $(this).parent();
    if (!(parent.find('.text').is(':hidden'))) {
      parent.find('.text').hide();
      parent.find('.title').show();
    }
    else {
      parent.find('.title').hide();
      parent.find('.text').show();
    }
  });
});
