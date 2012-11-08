define([
  'jquery',
  'underscore',
  'backbone',
  'libs/backbone.syphon'
], function($, _, Backbone) {

  var AddView = Backbone.View.extend({

    el: $('#add_job'),

    events: {
      'submit': 'create'
    },

    initialize: function() {

    },

    create: function(event) {

      var data = Backbone.Syphon.serialize(this);

      Jobs = Backbone.Model.extend({
        url: '/api/jobs/new'
      });

      var job = new Jobs();

      job.save(data, {
        success: function(model, response) {
          console.log(response);
          document.location.href = '/';
        },
        error: function() {
          alert('error');
        }
      });

      event.preventDefault();
    },

    render: function() {

    }

  });

  return AddView;

});

