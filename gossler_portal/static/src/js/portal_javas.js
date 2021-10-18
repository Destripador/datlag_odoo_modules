odoo.define('gossler_portal.portal_javas', function (require) {
  "use strict";

  var FormController = require('web.FormController');
FormController.include({
	_onButtonClicked: function (event) {
	if(event.data.attrs.id === "darkroom-save"){
	//your code
	}
	this._super(event);
	},
	});

});
