define([
  'underscore',
  'backbone',
  'validation'
], function(_, Backbone){

  var Job = Backbone.Model.extend({
    //idAttribute: '_id',
    urlRoot: '/api/jobs',

    validation: {
      title: {
        required: true,
        msg: 'Please enter a title'
      },
      email: {
        pattern: 'email',
        msg: 'Please enter a valid email'
      },
      salary: {
        pattern: 'digits'
      }
    }

  });

  return Job;

});
