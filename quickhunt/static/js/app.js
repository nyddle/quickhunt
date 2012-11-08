define([
  'jquery',
  'underscore',
  'backbone',
  'collections/Jobs',
  'views/JobView',
  'views/AddView',
  'views/EditView',
  'models/Job'
], function($, _, Backbone, Jobs, JobView, AddView, EditView, Job) {

    var Router = Backbone.Router.extend({
      initialize: function() {
        //this.mainView = mainView;
        Backbone.history.start({pushState: true})
      },
      routes: {
        '':           'home',
        'edit/new':   'new',
        'edit/:job':  'edit'
      },
      home: function() {
        var jobs = new Jobs(),
            jobView = new JobView({ collection: jobs });
      },
      new: function() {

        var Job = Backbone.Model.extend({
          url: '/api/jobs/new'
        });

        var job = new Job(),
            addView = new AddView({ model: job });

      },
      edit: function() {
        var job = new Job({ id: $('#oidinput').attr('value') }),
            editView = new EditView({ model: job });
      }

    });

    return Router;

});

