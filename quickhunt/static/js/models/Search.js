// Deprecated
/*define([
  'underscore',
  'backbone'
], function(_, Backbone){

  var Search = Backbone.Model.extend({

    search: function(query) {

      var self = this;

      $.ajax({
        url: 'http://5ce5fkv:wghahjd5zp60b9as@beech-4930933.us-east-1.bonsai.io/quickhunt/jobs/_search',
        type: 'POST',
        crossDomain: true,
        dataType: 'jsonp',
        data: {
          'query': {
            'text': {
              '_all': 'scala'
            }
          }
        },
        success: function(result) {
          //var data = $.parseJSON( json );
          console.log('success', result);
          //t.trigger( 'search:end' );
        },
      });

    }

  });

  return Search;

});
*/