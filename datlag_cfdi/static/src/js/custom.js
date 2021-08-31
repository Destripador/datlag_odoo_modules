odoo.define('hello_world.main', function (require) {
  "use strict";
  var rpc = require('web.rpc');
  var FormController = require('web.FormController');

  FormController.include({
  	_onButtonClicked: function (event) {
    	if(event.data.attrs.id === "validarlas"){
        this._rpc({
          model: 'datlag_cfdi.inicio',
          method: 'validar',
          args: [{'id': this.getSelectedIds()}],
        }).then(function(result){
         if (result == true){
           $('#validarlas').children('i').attr('class','fa fa-fw o_button_icon fa-check-circle')
         }
        });
    	}
      else if(event.data.attrs.id === "descargamasiva"){
           $('.descarga-masiva').attr('style','')
           $('.descarga-data').attr('style','display: none')
           $('#descarg-return').attr('style','')
           $('#descargamasiva').attr('style','display: none')
           return;
      }
      else if(event.data.attrs.id === "descarg-return"){
           $('.descarga-masiva').attr('style','display: none')
           $('.descarga-data').attr('style','')
           $('#descarg-return').attr('style','display: none')
           $('#descargamasiva').attr('style','')
           return;
      }
      else if(event.data.attrs.id === "descarga-inicio"){
            this._rpc({
              model: 'datlag_cfdi.inicio',
              method: 'descargamasiva',
              args: [{
                'id': this.getSelectedIds(),
                'start': $('#start').val(),
                'end': $('#final').val(),
              }],
            }).then(function(result){
             if (result == true){
               $('#validarlas').children('i').attr('class','fa fa-fw o_button_icon fa-check-circle')
             }
            });
      }
      this._super(event);
  	},
  });

});
