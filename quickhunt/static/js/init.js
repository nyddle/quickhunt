require.config({

  baseUrl: '/static/js/',

  paths: {
    jquery: 'libs/jquery',
    underscore: 'libs/underscore',
    backbone: 'libs/backbone',
    handlebars: 'libs/handlebars',
    modernizr: 'libs/modernizr',
    modelBinder: 'libs/backbone.modelBinder',
    validation: 'libs/backbone.validation',
    yandex: 'http://api-maps.yandex.ru/2.0-stable/?load=package.standard&lang=ru-RU'
  },

  shim: {
    backbone: {
      deps: ['jquery', 'underscore'],
      exports: 'Backbone'
    },
    underscore: {
      exports: '_'
    },
    handlebars: {
      exports: 'Handlebars'
    },
    modelBinder: {
      deps: ['backbone']
    },
    yandex: {
      exports: 'ymaps'
    }
  }

});

requirejs([
  'jquery',
  'underscore',
  'backbone',
  'app'
], function($, _, Backbone, App) {

  var app = new App();

});

