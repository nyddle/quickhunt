define([
  'jquery',
  'underscore',
  'backbone',
  'collections/Jobs',
  'views/JobView',
  'views/AddView'
], function($, _, Backbone, Jobs, JobView, AddView) {

    var Router = Backbone.Router.extend({
      initialize: function() {
        //this.mainView = mainView;
        Backbone.history.start({pushState: true})
      },
      routes: {
        '':         'home',
        'edit/new': 'new'
      },
      home: function() {
        var jobs = new Jobs(),
            jobView = new JobView({ collection: jobs });
      },
      new: function() {
        var addView = new AddView();
      }

    });

    return Router;

});

