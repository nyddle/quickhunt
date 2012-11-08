define([
  'jquery',
  'underscore',
  'backbone',
  'collections/Jobs',
  'views/JobView',
  'views/AddView',
  'models/Job'
], function($, _, Backbone, Jobs, JobView, AddView, Job) {

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
        var addView = new AddView();
      },
      edit: function() {
        var job = new Job({ id: $('#oidinput').attr('value') }),
            addView = new AddView({ model: job });
      }

    });

    return Router;

});

