/*$(document).ready(function(){

  $.fn.serializeJSON = function(){
    var json = {}
    var form = $(this);
    form.find('input, select').each(function(){
      var val
      if (!this.name) return;

      if ('radio' === this.type) {
        if (json[this.name]) { return; }

        json[this.name] = this.checked ? this.value : '';
      } else if ('checkbox' === this.type) {
        val = json[this.name];

        if (!this.checked) {
          if (!val) { json[this.name] = ''; }
        } else {
          json[this.name] =
            typeof val === 'string' ? [val, this.value] :
            $.isArray(val) ? $.merge(val, [this.value]) :
            this.value;
        }
      } else {
        json[this.name] = this.value;
      }
    })
    return json;
  }

   function addbutton() {
       $('#addjobbutton').click(function() {
            $.ajax({
              contentType: "application/json",
              type: "POST",
              url: "/api/jobs/" + $('#oidinput').attr('value'),
              data: JSON.stringify($('#addjobform').serializeJSON())
            }).done(function( msg ) {
              alert( "Server returned: " + msg );
              document.location.href = '/list';
            });
        });
    }

   addbutton();

});*/

require.config({

  baseUrl: '/static/js/',

  paths: {
    jquery: 'libs/jquery',
    underscore: 'libs/underscore',
    backbone: 'libs/backbone',
    handlebars: 'libs/handlebars',
    modernizr: 'libs/modernizr'
  },

  shim: {
    backbone: {
      deps: ['jquery', 'underscore'],
      exports: 'Backbone'
    },
    handlebars: {
      exports: 'Handlebars'
    }
  }

});

requirejs([
  'jquery',
  'underscore',
  'backbone',
  'handlebars',
  'app'
], function($, _, Backbone, Handlebars, app) {

  console.log(Handlebars);

  app.init();

});
