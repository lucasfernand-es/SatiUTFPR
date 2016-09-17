(function () {
    'use strict';

    var app = angular.module('sati', [ 'crud-factory', 'sati-factory', 'sati-directive',
                                        // public
                                        'event-controller', 'signup-controller',
                                        // Addon
                                        'ui.utils.masks',
                                        // essencials
                                        'ngSanitize'
                                        ]);

    app.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
    });


})(window.angular);