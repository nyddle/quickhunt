define([
  'jquery',
  'underscore',
  'backbone',
  'collections/Jobs',
  'views/JobView',
  'views/EditView',
  'views/InsideView',
  'models/Job'
], function($, _, Backbone, Jobs, JobView, EditView, InsideView, Job) {

    var Router = Backbone.Router.extend({
      initialize: function() {
        Backbone.history.start({pushState: true})
      },
      routes: {
        '':           'home',
        'edit/:job':  'edit',
        'jobs/:id':   'inside'
      },
      home: function() {
        var jobs = new Jobs(),
            jobView = new JobView({ collection: jobs });
      },
      edit: function(name) {
        var job = new Job(),
            editView = new EditView({ model: job });
      },
      inside: function() {
        var insideView = new InsideView();
      }

    });

    return Router;

});

