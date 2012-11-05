define([
  'collections/Jobs',
  'views/JobView'
], function(Jobs, JobView) {

  var init = function() {
    var jobs = new Jobs();
    var jobView = new JobView({ collection: jobs });
  };

  return { init: init };

});
