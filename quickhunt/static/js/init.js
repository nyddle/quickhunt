require.config({

  baseUrl: '/static/js/',

  paths: {
    jquery: 'libs/jquery',
    underscore: 'libs/underscore',
    backbone: 'libs/backbone',
    jqueryui: 'libs/jqueryui',
    handlebars: 'libs/handlebars',
    modernizr: 'libs/modernizr',
    modelBinder: 'libs/backbone.modelBinder',
    validation: 'libs/backbone.validation',
    yandex: 'http://api-maps.yandex.ru/2.0-stable/?load=package.standard&lang=ru-RU',
    visualSearch: 'libs/visualsearch'
  },

  shim: {
    backbone: {
      deps: ['jquery', 'underscore'],
      exports: 'Backbone'
    },
    underscore: {
      exports: '_'
    },
    jqueryui: {
      deps: ['jquery']
    },
    handlebars: {
      exports: 'Handlebars'
    },
    modelBinder: {
      deps: ['backbone']
    },
    yandex: {
      exports: 'ymaps'
    },
    visualSearch: {
      deps: ['jquery', 'jqueryui', 'underscore', 'backbone'],
      exports: 'VS'
    }
  }

});

requirejs([
  'jquery',
  'underscore',
  'backbone',
  'app',
  'visualSearch'
], function($, _, Backbone, App, VS) {

  console.log(VS);

  var app = new App();

  $(document).ready(function() {
    var visualSearch = VS.init({
      container  : $('.visual_search'),
      query      : '',
      minLength  : 0,
      showFacets : true,
      unquotable : [
        'текст',
        'город'
      ],
      callbacks  : {
        search : function(query, searchCollection) {
          console.log(["query", searchCollection.facets(), query]);
        },
        valueMatches : function(category, searchTerm, callback) {
          switch (category) {
          case 'блаа':
              callback([
                { value: '1-amanda', label: 'Amanda' },
                { value: '2-aron',   label: 'Aron' },
                { value: '3-eric',   label: 'Eric' },
                { value: '4-jeremy', label: 'Jeremy' },
                { value: '5-samuel', label: 'Samuel' },
                { value: '6-scott',  label: 'Scott' }
              ]);
              break;
            case 'filter':
              callback(['published', 'unpublished', 'draft']);
              break;
            case 'access':
              callback(['public', 'private', 'protected']);
              break;
            case 'title':
              callback([
                'Pentagon Papers',
                'CoffeeScript Manual',
                'Laboratory for Object Oriented Thinking',
                'A Repository Grows in Brooklyn'
              ]);
              break;
            case 'city':
              callback([
                'Cleveland',
                'New York City',
                'Brooklyn',
                'Manhattan',
                'Queens',
                'The Bronx',
                'Staten Island',
                'San Francisco',
                'Los Angeles',
                'Seattle',
                'London',
                'Portland',
                'Chicago',
                'Boston'
              ])
              break;
            case 'state':
              callback([
                "Alabama", "Alaska", "Arizona", "Arkansas", "California",
                "Colorado", "Connecticut", "Delaware", "District of Columbia", "Florida",
                "Georgia", "Guam", "Hawaii", "Idaho", "Illinois",
                "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
                "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
                "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
                "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina",
                "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
                "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee",
                "Texas", "Utah", "Vermont", "Virginia", "Virgin Islands",
                "Washington", "West Virginia", "Wisconsin", "Wyoming"
              ]);
              break
            case 'country':
              callback([
                "China", "India", "United States", "Indonesia", "Brazil",
                "Pakistan", "Bangladesh", "Nigeria", "Russia", "Japan",
                "Mexico", "Philippines", "Vietnam", "Ethiopia", "Egypt",
                "Germany", "Turkey", "Iran", "Thailand", "D. R. of Congo",
                "France", "United Kingdom", "Italy", "Myanmar", "South Africa",
                "South Korea", "Colombia", "Ukraine", "Spain", "Tanzania",
                "Sudan", "Kenya", "Argentina", "Poland", "Algeria",
                "Canada", "Uganda", "Morocco", "Iraq", "Nepal",
                "Peru", "Afghanistan", "Venezuela", "Malaysia", "Uzbekistan",
                "Saudi Arabia", "Ghana", "Yemen", "North Korea", "Mozambique",
                "Taiwan", "Syria", "Ivory Coast", "Australia", "Romania",
                "Sri Lanka", "Madagascar", "Cameroon", "Angola", "Chile",
                "Netherlands", "Burkina Faso", "Niger", "Kazakhstan", "Malawi",
                "Cambodia", "Guatemala", "Ecuador", "Mali", "Zambia",
                "Senegal", "Zimbabwe", "Chad", "Cuba", "Greece",
                "Portugal", "Belgium", "Czech Republic", "Tunisia", "Guinea",
                "Rwanda", "Dominican Republic", "Haiti", "Bolivia", "Hungary",
                "Belarus", "Somalia", "Sweden", "Benin", "Azerbaijan",
                "Burundi", "Austria", "Honduras", "Switzerland", "Bulgaria",
                "Serbia", "Israel", "Tajikistan", "Hong Kong", "Papua New Guinea",
                "Togo", "Libya", "Jordan", "Paraguay", "Laos",
                "El Salvador", "Sierra Leone", "Nicaragua", "Kyrgyzstan", "Denmark",
                "Slovakia", "Finland", "Eritrea", "Turkmenistan"
              ]);
              break;
          }
        },
        facetMatches : function(callback) {
          callback([
            'вакансия', 'зарплата', 'рабочий день', 'форма',
            { label: 'city',    category: 'location' },
            { label: 'address', category: 'location' },
            { label: 'country', category: 'location' },
            { label: 'state',   category: 'location' },
          ], {
              preserveOrder: true
          });
        }
      }
    });
  });

});

