define([
  'jquery',
  'underscore',
  'backbone',
  'handlebars'
], function($, _, Backbone, Handlebars) {

  var JobView = Backbone.View.extend({

    el: $('.jobs_list'),

    initialize: function() {
      var self = this;
      this.collection.fetch({
        success: function() {
          self.template = Handlebars.compile( $("#job_template").html() );
          self.collection.bind('all', self.render, self);
          self.render();
        }
      });
    },

    render: function() {
      if (this.collection.length > 0) {
        var collection = this.collection.toJSON();
        $(this.el).html(this.template({jobs: collection}));
      } else {
        $(this.el).html('<p class="empty">empty</p>');
      }
      return this;
    }

  });

  return JobView;

});
