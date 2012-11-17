define([
  'jquery',
  'underscore',
  'backbone'
], function($, _, Backbone) {

  var SearchView = Backbone.View.extend({

    el: $('#search'),

    events: {
      'keyup': 'sendQuery'
    },

    initialize: function() {

    },

    sendQuery: function(event) {
      //if ((event.keyCode || event.which) == 32) {
        var query = this.$el.val();
        this.collection.search(query);
      //}
    },

    render: function() {
      return this;
    }

  });

  return SearchView;

});

