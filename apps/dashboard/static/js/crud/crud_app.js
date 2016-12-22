(function () {
    'use strict';

    var app = angular.module('crud-app', [
        'Edition',
        'inputErrorsApp', 'inputIconDemo']);

    app.config(function ($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    });

})();