define([
  'jquery',
  'underscore',
  'backbone'
], function($, _, Backbone) {

  var SearchView = Backbone.View.extend({

    el: $('#search'),

    events: {
      'keypress': 'sendQuery'
    },

    initialize: function() {

    },

    sendQuery: function(event) {
      if (event.keyCode === 32) {
        console.log(this.$el.val().split(' '));
      }
    },

    render: function() {
      return this;
    }

  });

  return SearchView;

});

