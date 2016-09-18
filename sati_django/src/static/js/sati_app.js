(function () {
    'use strict';

    var app = angular.module('sati', [ 'crud-factory', 'sati-factory', 'sati-directive',
                                        // public
                                        'event-controller', 'signup-controller',
                                        // Addon
                                        'ui.utils.masks',
                                        // essencials
                                        'ngSanitize', 'ngResource', 'ngRoute'
                                        ]);

    app.config(function($interpolateProvider, $httpProvider , $resourceProvider) {
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');

        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        //** django urls loves trailling slashes which angularjs removes by default.
        $resourceProvider.defaults.stripTrailingSlashes = false;

    });



})(window.angular);