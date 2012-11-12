define([
  'jquery',
  'underscore',
  'backbone',
  'views/MapView'
], function($, _, Backbone, MapView) {

  var InsideView = Backbone.View.extend({

    el: $('.inside'),

    /*events: {
      'submit': 'submit'
    },*/

    initialize: function() {

      var mapView = new MapView();

    },

    render: function() {
      return this;
    }

  });

  return InsideView;

});

