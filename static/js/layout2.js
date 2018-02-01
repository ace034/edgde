$('.cloudinary-fileupload').bind('fileuploadprogress', function(e, data) {
  $('.progress_bar').css('width', Math.round((data.loaded * 100.0) / data.total) + '%');
});
