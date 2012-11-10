define([
  'jquery',
  'underscore',
  'backbone',
  'collections/Jobs',
  'views/JobView',
  'views/EditView',
  'models/Job'
], function($, _, Backbone, Jobs, JobView, EditView, Job) {

    var Router = Backbone.Router.extend({
      initialize: function() {
        Backbone.history.start({pushState: true})
      },
      routes: {
        '':           'home',
        //'edit/new':   'new',
        'edit/:job':  'edit'
      },
      home: function() {
        var jobs = new Jobs(),
            jobView = new JobView({ collection: jobs });
      },
      edit: function(name) {
        var job = new Job(),
            editView = new EditView({ model: job });
      }

    });

    return Router;

});

