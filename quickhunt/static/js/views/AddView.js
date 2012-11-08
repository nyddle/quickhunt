define([
  'jquery',
  'underscore',
  'backbone',
  'modelBinder'
], function($, _, Backbone) {

  var AddView = Backbone.View.extend({

    modelBinder: undefined,

    el: $('form#add_job'),

    events: {
      'submit': 'submit'
    },

    initialize: function() {
      this.modelBinder = new Backbone.ModelBinder();
      this.modelBinder.bind(this.model, this.el);
    },

    submit: function(event) {

      event.preventDefault();

      this.model.save({}, {
        success: function(model, response) {
          console.log(response);
          document.location.href = '/';
        },
        error: function() {
          alert('error');
        }
      });

    },

    render: function() {

    }

  });

  return AddView;

});
