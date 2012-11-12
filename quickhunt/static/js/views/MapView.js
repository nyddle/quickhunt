define([
  'jquery',
  'underscore',
  'backbone',
  'yandex'
], function($, _, Backbone, ymaps) {

  var MapView = Backbone.View.extend({

    el: document.getElementById('map'),

    /*events: {
      'submit': 'submit'
    },*/

    initialize: function() {

      console.log(ymaps);

      ymaps.ready(function() {

        var map = new ymaps.Map(document.getElementById('map'), {
          center: [55.76, 37.64],
          zoom: 2
        });

        //var myGeocoder = ymaps.geocode('Новый Арбат, 10');

      });

    },

    render: function() {
      return this;
    }

  });

  return MapView;

});

