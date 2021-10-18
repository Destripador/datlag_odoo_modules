$(document).ready(function(){
  $('.sidebar-wrapper')
    .each(toggle_handler)
    .on('change', toggle_handler);
});

var toggle_handler = function(){
  if (localStorage.getItem("side_bar_portal") == null) {
      //hide or show menu by default
      $(".page-wrapper").addClass("toggled");
      localStorage.setItem("side_bar_portal", "True");
  }else{
     if(localStorage.getItem("side_bar_portal") == "True"){
       $(".page-wrapper").addClass("toggled");
     }else{
       $(".page-wrapper").removeClass("toggled");
     }
  }
};

function clears() {
      $(".page-wrapper").removeClass("toggled");
      localStorage.setItem("side_bar_portal", "False");
}

function adds() {
      $(".page-wrapper").addClass("toggled");
      localStorage.setItem("side_bar_portal", "True");
}


function exampleOnclick(name_a,comment_a,level_a,sender_a,date_a,description_a,photo_a) {
  var name = name_a;
  var comment = comment_a;
  var level = level_a;
  var sender = sender_a;
  var date = date_a;
  var photo = photo_a;
  var description = description_a;

  var exampleModal = getExampleModal();

  // Init the modal if it hasn't been already.
  if (!exampleModal) { exampleModal = initExampleModal(); }

  var html =
      '<div class="modal-header">' +
        '<h5 class="modal-title" id="exampleModalLabel">Logros</h5>' +
        '<button type="button" class="close" data-dismiss="modal" aria-label="Close">' +
          '<span aria-hidden="true">x</span>' +
        '</button>' +
      '</div>' +
      '<div class="modal-body">'+
        '<div class="d-flex justify-content-center">'+
          '<div class="card" style="width: 18rem;">' +
            '<img class="card-img-top" src="data:image/*;base64,' + photo + '"/>'+
            '<div class="card-body">' +
            '<h5 class="card-title">'+ name +'</h5>' +
            '<p class="card-text">'+ description +'</p>' +
            '<p class="card-text">'+comment+'</p>' +
            '<p class="card-text">Otorgada por '+sender+'</p>' +
            '<p class="card-text">Insignia de '+level+' Sigue asi!!</p>' +
            '<p class="card-text">'+date+'</p>' +
            '</div>' +
          '</div>' +
      '</div>' +
            '<br>'+
      '<div class="modal-footer">' +
      '</div>';

  setExampleModalContent(html);

  // Show the modal.
  jQuery(exampleModal).modal('show');

}

function getExampleModal() {
  return document.getElementById('exampleModal');
}

function setExampleModalContent(html) {
  getExampleModal().querySelector('.modal-content').innerHTML = html;
}

function initExampleModal() {
  var modal = document.createElement('div');
  modal.classList.add('modal', 'fade');
  modal.setAttribute('id', 'exampleModal');
  modal.setAttribute('tabindex', '-1');
  modal.setAttribute('role', 'dialog');
  modal.setAttribute('aria-labelledby', 'exampleModalLabel');
  modal.setAttribute('aria-hidden', 'true');
  modal.innerHTML =
        '<div class="modal-dialog" role="document">' +
          '<div class="modal-content"></div>' +
        '</div>';
  document.body.appendChild(modal);
  return modal;
}
