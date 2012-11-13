define([
  'jquery',
  'underscore',
  'backbone',
  'collections/Jobs',
  'views/JobView',
  'views/EditView',
  'views/InsideView',
  'views/SearchView',
  'models/Job',
  'models/Search'
], function($, _, Backbone, Jobs, JobView, EditView, InsideView, SearchView, Job, Search) {

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
            search = new Search(),
            jobView = new JobView({ collection: jobs }),
            searchView = new SearchView({ model: search });
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

