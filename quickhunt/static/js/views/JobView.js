console.log('ins', Handlebars);

define([
  'jquery',
  'underscore',
  'backbone',
  'handlebars'
], function($, _, Backbone, Handlebars) {

  console.log('Handlebars', Handlebars);

  var JobView = Backbone.View.extend({
    el: $('.jobs_list'),
    initialize: function() {
      var self = this;
      this.collection.fetch({
        success: function() {
          self.render();
        }
      });
    },
    render: function() {
      var collection = this.collection.toJSON();
      var template = Handlebars.compile( $("#job_template").html() );
      $(this.el).html(template({jobs: collection}));
    }
  });

  return JobView;

});
