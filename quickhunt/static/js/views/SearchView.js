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

        this.render();

        var query = this.$el.val();
        this.collection.search(query);

      //}
    },

    render: function() {

      var self = this; //Small context issues

      this.$el.autocomplete({
        source: function(request, response) {
          $.getJSON('/api/autocomplete/', {
            q: request.term,
          }, function(data) {
            response(data.result);
          });
        }
      });

      return this;
    }

  });

  return SearchView;

});

