define([
  'underscore',
  'backbone'
], function(_, Backbone){

  var Job = Backbone.Model.extend({
    urlRoot: '/api/jobs'
  });

  return Job;

});
