require.config({

  deps: ['init'],

  paths: {
    libs: 'libs',
    plugins: 'libs/plugins',

    jquery: 'libs/jquery',
    underscore: 'libs/underscore',
    backbone: 'libs/backbone',
    handlebars: 'libs/handlebars'
    modernizr: 'libs/modernizr'
  },

  shim: {
    backbone: {
      deps: ['jquery', 'underscore', 'handlebars'],
      exports: 'Backbone'
    }
  }

});
