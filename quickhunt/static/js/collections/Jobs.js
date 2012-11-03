define([
  'underscore',
  'backbone'
], function(_, Backbone){

  var Jobs = Backbone.Collection.extend({
    url: '/api/search',
    parse: function(data) {
      return data.result;
    }
  });

  return Jobs;

});
