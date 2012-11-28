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

      function split(val) {
        return val.split(/,\s*/);
      }

      function extractLast(term) {
        return split(term).pop();
      }

      this.$el.autocomplete({
        minLength: 0,
        source: function(request, response) {
          $.getJSON('/api/autocomplete/', {
            q: extractLast(request.term),
          }, function(data) {
            console.log('q', request.term)
            response(data.result);
          });
        },
        focus: function() {
          return false;
        },
        select: function(event, ui) {
          var terms = split(this.value);
          terms.pop();
          terms.push(ui.item.value);
          terms.push('');
          this.value = terms.join(', ');
          return false;
        }
      });

      return this;
    }

  });

  return SearchView;

});

