define([
  'underscore',
  'backbone'
], function(_, Backbone){

  var Jobs = Backbone.Collection.extend({

    url: '/api/search',

    parse: function(data) {
      return data.result;
    },

    searchResult: function() {

    },

    search: function(query) {

      var self = this;

      $.ajax({
        url: 'http://5ce5fkv:wghahjd5zp60b9as@beech-4930933.us-east-1.bonsai.io/quickhunt/jobs/_search',
        type: 'POST',
        dataType: 'jsonp',
        data: {
          'query': {
            'text': {
              '_all': query
            }
          }
        },
        success: function(result) {
          var resultArr = [];
          for (var i = 0; i < result.hits.hits.length; i++) {
            resultArr.push(result.hits.hits[i]._source);
          };
          console.log(resultArr);
          self.reset(resultArr);
          //t.trigger( 'search:end' );
        },
      });

    }

  });

  return Jobs;

});
