define([
  'jquery',
  'underscore',
  'backbone',
  'handlebars',
  'modelBinder'
], function($, _, Backbone, Handlebars) {

  var EditView = Backbone.View.extend({

    modelBinder: undefined,

    el: $('form#add_job'),

    events: {
      'submit': 'submit'
    },

    initialize: function() {

      var oidinput = $('#oidinput').attr('value');
      this.modelBinder = new Backbone.ModelBinder();

      if ( oidinput === 'new' ) {
        this.model.url = '/api/jobs/new'
        this.modelBinder.bind(this.model, this.el);
      } else {
        // Устанавливаем id для модели
        this.model.set({ id: oidinput });
        var self = this;
        this.model.fetch({
          success: function() {
            self.modelBinder.bind(self.model, self.el);
          },
          error: function() {
            alert('Ошибка получения модели');
          }
        });
      }

      this.render();

    },

    submit: function(event) {

      event.preventDefault();

      if (this.model.isValid(true)) {
        this.model.save({}, {
          success: function(model, response) {
            console.log(response);
            document.location.href = '/';
          },
          error: function() {
            alert('Ошибка сохранения модели');
          }
        });
      } else {
        $('.alert').fadeIn();
      }

    },

    render: function() {

      var template = Handlebars.compile( $("#alert").html() );

      Backbone.Validation.bind(this, {
        valid: function(view, attr) {
          // do something
        },
        invalid: function(view, attr, error) {
          $(".alert").html(template({ label: 'Ooops!', message: error} ));
        }
      });

      /*this.model.on('validated:valid', this.valid, this);
      this.model.on('validated:invalid', this.invalid, this);*/

      return this;
    },

    valid: function() {
      //alert('валидно');
    },

    invalid: function() {
      //alert('не валидно');
    },

  });

  return EditView;

});

