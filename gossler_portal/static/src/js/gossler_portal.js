/**********************************************************************************
*
*    Copyright (c) 2017-today MuK IT GmbH.
*
*    This file is part of MuK Grid Snippets
*    (see https://mukit.at).
*
*    This program is free software: you can redistribute it and/or modify
*    it under the terms of the GNU Lesser General Public License as published by
*    the Free Software Foundation, either version 3 of the License, or
*    (at your option) any later version.
*
*    This program is distributed in the hope that it will be useful,
*    but WITHOUT ANY WARRANTY; without even the implied warranty of
*    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*    GNU Lesser General Public License for more details.
*
*    You should have received a copy of the GNU Lesser General Public License
*    along with this program. If not, see <http://www.gnu.org/licenses/>.
*
**********************************************************************************/
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

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
