$(document).ready(function(){

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
            });
        });
    }

    if ($('#oidinput').attr('value') == 'new') {
        addbutton();
    } else {
        $.ajax({
          contentType: "application/json",
          type: "GET",
          url: '/api/jobs/' + $('#oidinput').attr('value')
        }).done(function( msg ) {
          $('#addjobform').loadJSON(msg);
          addbutton();
        });
    }
});



require([
  'jquery',
  'underscore',
  'backbone'
], function($, _, Backbone) {



});
